#include "IR.h"
#include "CompressedBuffer.h"
#include <nlp_config.h>
#include <nlp_macros.h>
#include <nlp_filesystem.h>
#include <assert.h>

#define RECEIVE_BUFFER	2048

// Book-keeping
bool IR::b_Active = false;
IR* IR::p_IR = NULL;
										
IR::IR (void)
{
	p_Callback = NULL;
	pthread_mutex_init (&mtx_QuestionList, NULL);
}
											
IR::~IR (void)
{
	Disconnect ();
	pthread_mutex_destroy (&mtx_QuestionList);
}

void IR::Disconnect (void)
{
	b_Active = false;
	sleep (1);
	Socket::Close ();
}

void IR::OnDisconnect (void)
{
	cout << "[EE] Socket connection to cache server lost, attempting to reconnect."
		 << endl;

	exit (1);
}

bool IR::Connect (void)
{
	String sServer = (config)"ir_host";
	String sPort = (config)"ir_service";

	if (false == ClientSocket::ConnectBlocking (sServer, sPort))
	{
		cout << "   [EE] Failed to connect to IR server at "
			 << sServer << ':' << sPort << endl;
		return false;
	}
	// ClearConnection ();

	b_Active = true;
	pthread_create (&thr_SocketLoop, NULL, RunThread, this);
	pthread_detach (thr_SocketLoop);

	return true;
}

void IR::ClearConnection (void)
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
										
bool IR::SendMessage (const String& _rMessage)
{
	// TODO: what is the +1 for?
	int iLength = _rMessage.length ();

	// TODO: make sure that instead of sending the length, we send EOM
	Buffer bufMsg;
	bufMsg.Append (&iLength, sizeof (int));
	bufMsg.Append ((const char*)_rMessage, _rMessage.length ());

	// assert (iLength == bufMsg.Length ());
	return ClientSocket::SendBlocking (bufMsg.GetData (), bufMsg.Length ());
}

void* IR::RunThread (void* _pArg)
{
	if (NULL != p_IR)
	{
		while (true == b_Active)
		{
			usleep (100);
			// TODO: not exactly sure what but something should happen here and when done, return a value
			// p_IR->RunLocalHeuristicEvaluator ();
		}
	}
	else
	{
		while (true == b_Active)
			AllSockets::ProcessEvents (1000);
	}

	pthread_exit (&((IR*)_pArg)->thr_SocketLoop);
	return NULL;
}
										
bool IR::SendQuestion (String _sType,
							String& _sQuestion)
{
	if (NULL == p_Callback)
	{
		cerr << "   [EE] Callback not set for IR. Will not be able to relay IR system responses back. Not sending Question to IR system." << endl;
		return false;
	}

	// TODO: check if we really need to lock the thread
	// pthread_mutex_lock (&mtx_QuestionList);
	// pthread_mutex_unlock (&mtx_QuestionList);

	String question;
	question << _sType << " " << _sQuestion;
	if (false == SendMessage (question))
		return false;

	return true;
}
											
void IR::OnReceive (const void* _zData, long _lBytes)
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

		cout << "OnReceive " << iMessageSize  << " " << cType << endl;

		IRAnswer* aAnswer;
		// TODO: here we should process the data, the comment below can be useful
		// Otherwise have a look at IR.cpp
		p_Callback->OnIRAnswer (*aAnswer);
		delete aAnswer;

		// if ('u' == cType)
		// {
		// 	// used for restricted world runs.	
		// 	size_t iOffset = sizeof (size_t) + 1;
		// 	size_t iQuestionId;
		// 	if (false == bufResponse.ReadFromIndex (iOffset, &iQuestionId, sizeof (size_t)))
		// 	{
		// 		cerr << "[ERROR] Failed to read Question id from cache response." << endl;
		// 		break;
		// 	}

		// 	// find Question from id ...			
		// 	pthread_mutex_lock (&mtx_QuestionList);
		// 	QuestionIdToIRAnswer_hmp_t::iterator	iteQuestion;
		// 	iteQuestion = hmp_QuestionIdToIRAnswer.find (iQuestionId);
		// 	if (hmp_QuestionIdToIRAnswer.end () == iteQuestion)
		// 	{
		// 		cerr << "   [WW] Question id not found ["
		// 			 << iQuestionId << ']' << endl;
		// 		pthread_mutex_unlock (&mtx_QuestionList);
		// 		return;
		// 	}

		// 	// update Question attributes ...		
		// 	IRAnswer* aAnswer = iteQuestion->second;
		// 	aAnswer->e_PlanningOutcome = po_outside_known_world;
		// 	if (false == b_KnownWorldOnly)
		// 	{
		// 		cerr << "   [WW] 'Outside-known-world' respose received from "
		// 				"cache, but learner is not in 'known-world-only' mode."
		// 			 << endl;
		// 	}

		// 	// clear local information about Question
		// 	hmp_QuestionIdToIRAnswer.erase (iteQuestion);
		// 	pthread_mutex_unlock (&mtx_QuestionList);

		// 	// callback with received response...
		// 	p_Callback->OnIRAnswer (iQuestionId, *aAnswer);
		// 	delete aAnswer;
		// }

		// else 
		// {
		// 	// This shouldn't happen!			
		// 	cerr << "[EE]  Unknown response from cache "
		// 		 << cType << endl;
		// }
	}
}