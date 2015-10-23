#include "FFInterface.h"
#include "CompressedBuffer.h"
#include <nlp_config.h>
#include <nlp_macros.h>
#include <nlp_filesystem.h>
#include <assert.h>

#define RECEIVE_BUFFER	2048

bool FFInterface::b_Active = false;
FFInterface* FFInterface::p_FFInterface = NULL;


//												
FFInterface::FFInterface (void)
{
	p_Callback = NULL;
	pthread_mutex_init (&mtx_TaskList, NULL);
}


//												
FFInterface::~FFInterface (void)
{
	Disconnect ();
	ClearTasks ();
	pthread_mutex_destroy (&mtx_TaskList);

	ITERATE (GoalToPrerequisites_hmp_t, hmp_GoalToPrerequisites, ite)
		delete ite->second;
	ITERATE (GoalToPlan_hmp_t, hmp_GoalToPlan, ite)
		delete ite->second;
}


//												
bool FFInterface::SendMessage (const String& _rMessage)
{
	size_t iLength = _rMessage.length () + sizeof (size_t) + 1;

	Buffer bufMsg;
	bufMsg.Append (&iLength, sizeof (size_t));
	bufMsg.Append ((const char*)_rMessage, _rMessage.length () + 1);

	assert (iLength == bufMsg.Length ());
	return ClientSocket::SendBlocking (bufMsg.GetData (), bufMsg.Length ());
}


//												
bool FFInterface::SendMessage (const Buffer& _rMessage)
{
	size_t iLength = _rMessage.Length () + sizeof (size_t);

	Buffer bufMsg;
	bufMsg.Append (&iLength, sizeof (size_t));
	bufMsg.Append (_rMessage);

	assert (iLength == bufMsg.Length ());
	return ClientSocket::SendNonBlocking (bufMsg.GetData (), bufMsg.Length ());
}


//												
bool FFInterface::Connect (void)
{
	b_UseLocalHeuristicEvaluator = (1 == (int)(config)"use_local_heuristic_evaluator");
	if (true == b_UseLocalHeuristicEvaluator)
	{
		if (false == InitHeuristicEvaluator ())
			return false;

		b_Active = true;
		p_FFInterface = this;
		pthread_create (&thr_SocketLoop, NULL, RunThread, this);
		pthread_detach (thr_SocketLoop);
		return true;
	}

	String sServer = (config)"cache_host";
	String sPort = (config)"cache_service";

	if (false == ClientSocket::ConnectBlocking (sServer, sPort))
	{
		cout << "   [EE] Failed to connect to cache server at "
			 << sServer << ':' << sPort << endl;
		return false;
	}

	b_KnownWorldOnly = (1 == (int)(config)"known_world_only");
	if (true == b_KnownWorldOnly)
	{
		cout << "Activating known-world-only mode." << endl;
		SendMessage (String (":[known world only]"));

		SetStandalone (true);

		Buffer bufTemp;
		size_t iMessageSize = 0;
		while (true)
		{
			char zData [RECEIVE_BUFFER + 1];
			long lBytes = ReceiveBlocking (zData, RECEIVE_BUFFER, 100);
			if (lBytes > 0)
				bufTemp.Append (zData, lBytes);

			if (false == bufTemp.ReadFromIndex (0, &iMessageSize, sizeof (size_t)))
				continue;
			if (iMessageSize > bufTemp.Length ())
				continue;
			break;
		}

		Buffer bufResponse = bufTemp.PopFirstMessageAsBuffer (iMessageSize);
		bufResponse.DropFront (sizeof (size_t));
		String sMessage = bufResponse;
		if (":Known-world-only mode active" == sMessage)
			cout << "   Known world only mode active." << endl;
		else
		{
			cout << "   [WARNING] Failed to activate known-world-only mode.\n"
					"   Got following response from cache: ["
				 << sMessage << ']' << endl;
		}
		SetStandalone (false);
	}

	ClearConnection ();

	b_Active = true;
	pthread_create (&thr_SocketLoop, NULL, RunThread, this);
	pthread_detach (thr_SocketLoop);

	return true;
}


//												
void FFInterface::Disconnect (void)
{
	b_Active = false;
	if (true == b_UseLocalHeuristicEvaluator)
		return;
	sleep (1);
	Socket::Close ();
}


//												
long FFInterface::RegisterDomain (String& _rDomain)
{
	if (true == b_UseLocalHeuristicEvaluator)
		return 0;

	SetStandalone (true);

	// send request ...	
	String sRequest;
	sRequest << "+" << _rDomain;
	if (false == SendMessage (sRequest))
	{
		cerr << "[ERROR] Request failed on RegisterDomain." << endl;
		SetStandalone (false);
		return -1;
	}

	// get response ...	
	Buffer bufTemp;
	size_t iMessageSize = 0;
	while (true)
	{
		char zData [RECEIVE_BUFFER + 1];
		long lBytes = ReceiveBlocking (zData, RECEIVE_BUFFER, 100);
		if (lBytes > 0)
			bufTemp.Append (zData, lBytes);

		if (false == bufTemp.ReadFromIndex (0, &iMessageSize, sizeof (size_t)))
			continue;
		if (iMessageSize > bufTemp.Length ())
			continue;
		break;
	}
	SetStandalone (false);

	Buffer bufResponse = bufTemp.PopFirstMessageAsBuffer (iMessageSize);
	char cType = bufResponse [sizeof (size_t)];
	if ('d' != cType)
	{
		cerr << "[ERROR] Bad line format in response to domain registration."
			 << " expected 'd', got '" << cType << "'." << endl;
		return -1;
	}
	long lDomainId;
	if (false == bufResponse.ReadFromIndex (1 + sizeof (size_t),
											&lDomainId,
											sizeof (size_t)))
	{
		cerr << "[ERROR] Failed to read domain id from domain registration reponse."
			 << endl;
		return -1;
	}

	return lDomainId;
}


//												
bool FFInterface::SendTask (size_t _iId,
							size_t _iDomain,
							String& _rProblem,
							size_t _iTimelimit)
{
	if (NULL == p_Callback)
	{
		cerr << "   [EE] Callback not set for FFInterface. Will not be able to relay FF responses back. Not sending task to FF." << endl;
		return false;
	}

	pthread_mutex_lock (&mtx_TaskList);
	pair <TaskIdToFFResponse_hmp_t::iterator, bool> pairInsert;
	FFResponse* pResponse = new FFResponse;
	pairInsert = hmp_TaskIdToFFResponse.insert (make_pair (_iId, pResponse));

	_rProblem.Strip ();
	pResponse->i_Domain = _iDomain;
	pResponse->s_Problem = _rProblem;
	pthread_mutex_unlock (&mtx_TaskList);

	if (true == b_UseLocalHeuristicEvaluator)
		return true;

	// send request to cache...			
	CompressedBuffer bufProblem (_rProblem);
	size_t iCompressedSize = bufProblem.CompressedSize ();
	size_t iUncompressedSize = bufProblem.UncompressedSize ();

	Buffer bufRequest;
	bufRequest.Append ("?", 1);
	bufRequest.Append (&_iId, sizeof (size_t));
	bufRequest.Append (&_iTimelimit, sizeof (size_t));
	bufRequest.Append (&_iDomain, sizeof (size_t));
	bufRequest.Append (&iCompressedSize, sizeof (size_t));
	bufRequest.Append (&iUncompressedSize, sizeof (size_t));
	bufRequest.Append (bufProblem);

	if (false == SendMessage (bufRequest))
		return false;

	return true;
}


//												
void FFInterface::ClearTasks (void)
{
	pthread_mutex_lock (&mtx_TaskList);
	ITERATE (TaskIdToFFResponse_hmp_t, hmp_TaskIdToFFResponse, ite)
		delete ite->second;
	hmp_TaskIdToFFResponse.clear ();
	pthread_mutex_unlock (&mtx_TaskList);
}


//												
bool FFInterface::TestTasksClear (void)
{
	pthread_mutex_lock (&mtx_TaskList);
	if (false == hmp_TaskIdToFFResponse.empty ())
	{
		pthread_mutex_unlock (&mtx_TaskList);
		return false;
	}
	pthread_mutex_unlock (&mtx_TaskList);
	return true;
}


//												
void FFInterface::OnReceive (const void* _zData, long _lBytes)
{
	o_Data.Append (_zData, _lBytes);
	
	while (true)
	{
		size_t iMessageSize;
		if (false == o_Data.ReadFromIndex (0, &iMessageSize, sizeof (size_t)))
			return;
		if (iMessageSize > o_Data.Length ())
			return;

		// process reply...					
		Buffer bufResponse = o_Data.PopFirstMessageAsBuffer (iMessageSize);
		char cType = bufResponse [sizeof (size_t)];

		// cout << "OnReceive " << iMessageSize  << " " << cType << endl;

		if (('c' == cType) || ('f' == cType))
		{
			// Cache hit. This message has plan.
			size_t iOffset = sizeof (size_t) + 1;

			size_t iTaskId;
			if (false == bufResponse.ReadFromIndex (iOffset, &iTaskId, sizeof (size_t)))
			{
				cerr << "[ERROR] Failed to read task id from cache response." << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iCompressedSize;
			if (false == bufResponse.ReadFromIndex (iOffset,
													&iCompressedSize,
													sizeof (size_t)))
			{
				cerr << "[ERROR] Failed to read compressed size from cache response."
					 << endl;
				break;
			}
			iOffset += sizeof (size_t);

			size_t iUncompressedSize;
			if (false == bufResponse.ReadFromIndex (iOffset,
													&iUncompressedSize,
													sizeof (size_t)))
			{
				cerr << "[ERROR] Failed to read uncompressed size from cache response."
					 << endl;
				break;
			}
			iOffset += sizeof (size_t);

			// cout << "compressed data : " << iCompressedSize << " "
			//	 << iUncompressedSize << endl;
			void* pCompressedFFResponse = (char*) bufResponse.GetData () + iOffset;
			CompressedBuffer bufCompressedFFResponse;
			bufCompressedFFResponse.SetData (pCompressedFFResponse,
											 iCompressedSize,
											 iUncompressedSize);


			// find task in sent-task map...	
			pthread_mutex_lock (&mtx_TaskList);
			TaskIdToFFResponse_hmp_t::iterator	iteTask;
			iteTask = hmp_TaskIdToFFResponse.find (iTaskId);
			if (hmp_TaskIdToFFResponse.end () == iteTask)
			{
				cerr << "   [WW] task id not found ["
					 << iTaskId << ']' << endl;
				pthread_mutex_unlock (&mtx_TaskList);
				return;
			}

			// update task attributes...		
			FFResponse* pResponse = iteTask->second;
			if (false == bufCompressedFFResponse.Uncompress (&pResponse->s_FFOutput))
			{
				cerr << "[ERROR] Failed to uncompress FF response." << endl;
				pthread_mutex_unlock (&mtx_TaskList);
				break;
			}
			pResponse->e_PlanningOutcome
				= FFInterface::FFExtractOutcome (pResponse->s_FFOutput);
			if (po_plan_found == pResponse->e_PlanningOutcome)
			{
				pResponse->s_Plan = FFInterface::ExtractPlan (pResponse->s_FFOutput);
				pResponse->l_States = FFInterface::StatesEvaluated (pResponse->s_FFOutput);
			}

			// clear local information about task
			hmp_TaskIdToFFResponse.erase (iteTask);
			pthread_mutex_unlock (&mtx_TaskList);

			// callback with received response...
			p_Callback->OnFFResponse (iTaskId, *pResponse);
			delete pResponse;
		}

		else if ('u' == cType)
		{
			// used for restricted world runs.	
			size_t iOffset = sizeof (size_t) + 1;
			size_t iTaskId;
			if (false == bufResponse.ReadFromIndex (iOffset, &iTaskId, sizeof (size_t)))
			{
				cerr << "[ERROR] Failed to read task id from cache response." << endl;
				break;
			}

			// find task from id ...			
			pthread_mutex_lock (&mtx_TaskList);
			TaskIdToFFResponse_hmp_t::iterator	iteTask;
			iteTask = hmp_TaskIdToFFResponse.find (iTaskId);
			if (hmp_TaskIdToFFResponse.end () == iteTask)
			{
				cerr << "   [WW] task id not found ["
					 << iTaskId << ']' << endl;
				pthread_mutex_unlock (&mtx_TaskList);
				return;
			}

			// update task attributes ...		
			FFResponse* pResponse = iteTask->second;
			pResponse->e_PlanningOutcome = po_outside_known_world;
			if (false == b_KnownWorldOnly)
			{
				cerr << "   [WW] 'Outside-known-world' respose received from "
						"cache, but learner is not in 'known-world-only' mode."
					 << endl;
			}

			// clear local information about task
			hmp_TaskIdToFFResponse.erase (iteTask);
			pthread_mutex_unlock (&mtx_TaskList);

			// callback with received response...
			p_Callback->OnFFResponse (iTaskId, *pResponse);
			delete pResponse;
		}

		else 
		{
			// This shouldn't happen!			
			cerr << "[EE]  Unknown response from cache "
				 << cType << endl;
		}
	}
}


//												
void FFInterface::OnDisconnect (void)
{
	cout << "[EE] Socket connection to cache server lost, attempting to reconnect."
		 << endl;

	exit (1);
}


//												
void FFInterface::ClearConnection (void)
{
	SetStandalone (true);
	char zData [RECEIVE_BUFFER + 1];
	long lBytes = ReceiveBlocking (zData, RECEIVE_BUFFER, 100);
	long lTotalBytes = lBytes;

	while (lBytes > 0)
	{
		long lBytes = ReceiveBlocking (zData, RECEIVE_BUFFER, 100);
		if (lBytes > 0)
			lTotalBytes += lBytes;
	}
	SetStandalone (false);

	if (lTotalBytes > 0)
		cout << "[INFO] Discarding " << lTotalBytes << " of unexpected data." << endl;
}



//												
void* FFInterface::RunThread (void* _pArg)
{
	if (NULL != p_FFInterface)
	{
		while (true == b_Active)
		{
			usleep (100);
			p_FFInterface->RunLocalHeuristicEvaluator ();
		}
	}
	else
	{
		while (true == b_Active)
			AllSockets::ProcessEvents (1000);
	}

	pthread_exit (&((FFInterface*)_pArg)->thr_SocketLoop);
	return NULL;
}


//												
FFPlaningOutcome_e FFInterface::FFExtractOutcome (String& _rFFResponse)
{
	if (true == _rFFResponse.Has ("ff: found legal plan as follows"))
	{
		if (false == _rFFResponse.HasPattern ("step *0:"))
			return po_goal_already_satisfied;
		return po_plan_found;
	}

	else if (true == _rFFResponse.Has ("ff: goal can be simplified to true. the empty plan solves it"))
		return po_goal_already_satisfied;

	else if ((true == _rFFResponse.Has ("ff: goal can be simplified to false. no plan will solve it")) ||
			(true == _rFFResponse.Has ("problem unsolvable.")) ||
			(true == _rFFResponse.Has ("problem proven unsolvable.")))
		return po_unsolvable;

	else if (true == _rFFResponse.Has ("[killed planner on timeout]"))
		return po_timeout;

	else if ((true == _rFFResponse.Has ("syntax error in line")) ||
			 (true == _rFFResponse.Has ("undeclared predicate ")) ||
			 (true == _rFFResponse.Has ("undeclared predicate ")))
		return po_syntax_error;
	else if (true == _rFFResponse.Has (" increase max_"))
	{
		cerr << "[WARNING] FF requests code change. -------------------\n"
			 << _rFFResponse << '\n'
			 << "------------------------------------------------------\n"
			 << endl;
		return po_ff_code_change_required;
	}

	cerr << "[WARNING] Unknown planning outcome. ------------------\n"
		 << _rFFResponse << '\n'
		 << "------------------------------------------------------\n"
		 << endl;
	return po_unknown;
};


//												
String FFInterface::ExtractPlan (String& _rFFResponse)
{
	if (po_plan_found != FFInterface::FFExtractOutcome (_rFFResponse))
		return "";

	String_dq_t dqLines;
	_rFFResponse.SplitLines (dqLines);

	String sPlan;
	bool bInPlan = false;
	ITERATE (String_dq_t, dqLines, ite)
	{
		if ((true == ite->StartsWith ("step "))
			&& (true == ite->Has (":")))
			bInPlan = true;
		if (false == ite->Has (":"))
		{
			bInPlan = false;
			continue;
		}

		if (true == bInPlan)
		{
			String_dq_t dqValues;
			ite->Split (dqValues, ':');
			dqValues [1].Strip ();

			sPlan << dqValues [1] << '\n';
		}
	}

	sPlan.Strip ();
	return sPlan;
}


//												
long FFInterface::StatesEvaluated (String& _rFFResponse)
{
	String_dq_t dqLines;
	_rFFResponse.SplitLines (dqLines);

	long lStates = -1;
	ITERATE (String_dq_t, dqLines, ite)
	{
		if (false == ite->Has (" searching, evaluating "))
			continue;
		if (false == ite->Has (" states, to a max depth of"))
			continue;

		String_dq_t dqValues;
		ite->SplitByString (dqValues, ", evaluating ");

		lStates = dqValues [1];
	}

	return lStates;
}


//												
bool FFInterface::InitHeuristicEvaluator (void)
{
	String_dq_t dqLines;
	if (false == File::ReadLines ((config)"heuristic_evaluator_rules", dqLines))
		return false;

	b_IgnoreNumericValues = (1 == (int)(config)"ignore_predicate_numerics");

	String_set_t* psetCurrentPrerequisites = NULL;
	String* pCurrentPlan = NULL;
	ITERATE (String_dq_t, dqLines, ite)
	{
		ite->Strip ();
		if ("" == *ite)
			continue;
		if (true == ite->StartsWith ("#"))
			continue;

		if (true == ite->StartsWith (":"))
		{
			String_dq_t dqTokens;
			ite->Split (dqTokens);

			PddlFunctionValuePredicate oPredicate;
			oPredicate.c_Operator = '>';
			oPredicate.b_IsFunction = true;
			oPredicate.s_Name = "thing-available";
			oPredicate.dq_Parameters.push_back (PddlParameter ());
			oPredicate.dq_Parameters [0].SetValue (dqTokens [1]);
			oPredicate.l_Value = (true == b_IgnoreNumericValues)? 0 : (int)dqTokens [2];

			psetCurrentPrerequisites->insert (oPredicate.GetPddlString ());
			continue;
		}

		if (true == ite->StartsWith (">>"))
		{
			String_dq_t dqTokens;
			ite->Split (dqTokens);

			PddlFunctionValuePredicate oPredicate;
			oPredicate.c_Operator = '>';
			oPredicate.b_IsFunction = true;
			oPredicate.s_Name = "thing-available";
			oPredicate.dq_Parameters.push_back (PddlParameter ());
			oPredicate.dq_Parameters [0].SetValue (dqTokens [1]);
			oPredicate.l_Value = (true == b_IgnoreNumericValues)? 0 : (int)dqTokens [2];

			// cout << "  [" << oPredicate.GetPddlString () << "]" << endl;
			psetCurrentPrerequisites = new String_set_t;
			hmp_GoalToPrerequisites.insert (make_pair (oPredicate.GetPddlString (),
													   psetCurrentPrerequisites));
			pCurrentPlan = new String;
			hmp_GoalToPlan.insert (make_pair (oPredicate.GetPddlString (), pCurrentPlan));
			continue;
		}

		*pCurrentPlan << *ite << "\n";
	}

	return true;
}


//												
void FFInterface::RunLocalHeuristicEvaluator (void)
{
	TaskIdToFFResponse_hmp_t hmpLocal;

	pthread_mutex_lock (&mtx_TaskList);
	ITERATE (TaskIdToFFResponse_hmp_t, hmp_TaskIdToFFResponse, ite)
	{
		FFResponse* pResponse = ite->second;
		PddlProblem* pPddlProblem = PddlInterface::ParseProblemPddl (pResponse->s_Problem);
		pResponse->e_PlanningOutcome = HasPrerequisites (*pPddlProblem, 
														 pResponse->s_Problem,
														 pResponse->s_Plan);
		delete pPddlProblem;

		if (po_plan_found == pResponse->e_PlanningOutcome)
			pResponse->l_States = 1;

		hmpLocal.insert (make_pair (ite->first, pResponse));
	}
	hmp_TaskIdToFFResponse.clear ();
	pthread_mutex_unlock (&mtx_TaskList);


	ITERATE (TaskIdToFFResponse_hmp_t, hmpLocal, ite)
	{
		FFResponse* pResponse = ite->second;
		p_Callback->OnFFResponse (ite->first, *pResponse);
		delete pResponse;
	}
	hmpLocal.clear ();
}


//												
FFPlaningOutcome_e FFInterface::HasPrerequisites (PddlProblem& _rPddlProblem, 
												  String& _rProblem,
												  String& _rPlan)
{
	// first find prerequisites...	
	if (true == _rPddlProblem.o_PartialGoalState.dq_Predicates.empty ())
	{
		cerr << "[ERROR] Problem goal empty in FFInterface::HasPrerequisites." << endl;
		return po_goal_already_satisfied;
	}
	if (_rPddlProblem.o_PartialGoalState.dq_Predicates.size () > 1)
	{
		cerr << "[ERROR] Problem goal has multiple predicates." << endl;
		cout << _rPddlProblem.o_PartialGoalState.dq_Predicates.size () << endl;
		return po_syntax_error;
	}

	PddlPredicate* pGoalPredicate = _rPddlProblem.o_PartialGoalState.dq_Predicates [0];
	if (true == b_IgnoreNumericValues)
		pGoalPredicate->l_Value = 0;
	String sGoalPddl (pGoalPredicate->GetPddlString ());

	GoalToPrerequisites_hmp_t::iterator	iteGoal;
	iteGoal = hmp_GoalToPrerequisites.find (sGoalPddl);
	if (hmp_GoalToPrerequisites.end () == iteGoal)
	{
		// cerr << "[ERROR] Unknown goal predicate in FFInterface::HasPrerequisites : "
		//	 << pGoalPredicate->GetPddlString () << endl;
		// return po_unsolvable;
		return po_plan_found;
	}

	String_set_t* psetPrerequisites = iteGoal->second;

	// cout << "[goal] " << sGoalPddl << " " << psetPrerequisites->size () << endl;

	// check if prerequisites are satisfied...	
	String_set_t setSatisfiedPrerequisites;
	ITERATE (PddlPredicate_dq_t, _rPddlProblem.o_StartState.dq_Predicates, ite)
	{
		PddlPredicate* pInitPredicate = *ite;
		if ((true == b_IgnoreNumericValues) &&
			(true == pInitPredicate->b_IsFunction))
		{
			if (pInitPredicate->l_Value > 0)
			{
				((PddlFunctionValuePredicate*)pInitPredicate)->c_Operator = '>';
				pInitPredicate->l_Value = 0;
			}
		}

		String sInitPredicate (pInitPredicate->GetPddlString ());
		if (psetPrerequisites->end () != psetPrerequisites->find (sInitPredicate))
		{
			// cout << "      " << sInitPredicate << endl;
			setSatisfiedPrerequisites.insert (sInitPredicate);
		}
	}

	if (psetPrerequisites->size () == setSatisfiedPrerequisites.size ())
	{
		GoalToPlan_hmp_t::iterator	itePlan;
		itePlan = hmp_GoalToPlan.find (sGoalPddl);
		if (hmp_GoalToPlan.end () == itePlan)
		{
			cerr << "[ERROR] plan not found for solvable goal in FFInterface::HasPrerequisites."
				 << endl;
			return po_ff_code_change_required;
		}

		_rPlan = *itePlan->second;
		return po_plan_found;
	}
	return po_unsolvable;
}





