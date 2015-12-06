#include "Learner.h"
#include "Problems.h"
#include <stdio.h>
#include <limits.h>
#include <iomanip>
#include <omp.h>
using namespace std;


//										
ostream& operator<< (ostream& _rStream, const SubgoalSequence& _rSequence)
{
	bool bFirst = true;
	CONST_ITERATE (Subgoal_dq_t, _rSequence.dq_Subgoals, ite)
	{
		const Subgoal& rSubgoal = *ite;
		if (SEQUENCE_END == rSubgoal.i_SequenceEnd)
			continue;
		if (false == bFirst)
			_rStream << " | ";
		bFirst = false;
		_rStream << rSubgoal.p_PddlSubgoalPredicate->GetPddlString ();
		switch (rSubgoal.e_PlanningOutcome)
		{
			case po_plan_found:
				_rStream << "|plan-found";
				break;
			case po_goal_already_satisfied:
				_rStream << "|trivial-goal";
				break;
			case po_unsolvable:
				_rStream << "|unsolvable";
				break;
			case po_timeout:
				_rStream << "|timeout";
				break;
			case po_syntax_error:
				_rStream << "|pdd-syntax-error";
				break;
			case po_ff_code_change_required:
				_rStream << "|ff-code-change";
				break;
			case po_outside_known_world:
				_rStream << "|outside-known-world";
				break;
			default:
				_rStream << "|<??>";
		}
	}
	return _rStream;
}


//										
SubgoalLearner::SubgoalLearner (void)
{
	pthread_mutex_init (&mtx_WaitForSequences, NULL);
	pthread_cond_init (&cv_WaitForSequences, NULL);
	p_PddlDomain = NULL;
}

SubgoalLearner::~SubgoalLearner (void)
{
	pthread_mutex_destroy (&mtx_WaitForSequences);
	pthread_cond_destroy (&cv_WaitForSequences);
	delete p_PddlDomain;
}


//										
bool SubgoalLearner::Init (void)
{
	d_TaskCompletionReward = (config)"task_completion_reward";
	d_PlanFailureReward = (config)"plan_failure_penalty";
	d_SuccessfulStepRewardBase = (config)"successful_step_reward_base";
	d_UnnecessarySubgoalPenalty = (config)"unnecessary_subgoal_penalty";
	d_RewardForHittingCachePeriphery = (config)"reward_for_hitting_cache_periphery";
	i_SequencesOnFirstIteration = (config)"sequences_on_first_iteration";
	i_SequencesPerIteration = (config)"sequences_per_iteration";

	i_TrainingTimeFFTimelimit = (config)"training_time_ff_time_limit";
	i_TestTimeFFTimelimit = (config)"test_time_ff_time_limit";

	b_LearnFromAlternateSequences = (1 == (int)(config)"learn_from_alternate_sequences");
	b_LearnOnSubgoalFreeProblems = (1 == (int)(config)"learn_on_subgoal_free_problems");
	b_RememberSolutions = (1 == (int)(config)"remember_solutions");
	b_DisplayFFProgress = (1 == (int)(config)"display_ff_progress");
	b_LogPredictions = (1 == (int)(config)"log_predictions");
	b_UseLocalHeuristicEvaluator = (1 == (int)(config)"use_local_heuristic_evaluator");

	assert (Problem::GetProblemCount () > 0);
	vec_TargetGoalCompletions.Create (Problem::GetProblemCount ());

	if (false == o_SubgoalPolicy.Init ())
		return false;
	o_FFInterface.SetCallback (this);
	if (false == o_FFInterface.Connect ())
		return false;

	String_dq_t dqLines;
	if (false == File::ReadLines ((config)"domain_pddl_file", dqLines))
		return false;

	String sDomainPddl;
	sDomainPddl.Join (dqLines, '\n');
	p_PddlDomain = PddlInterface::ParseDomainPddl (sDomainPddl);

	i_DomainPddlId = o_FFInterface.RegisterDomain (sDomainPddl);
	return (-1 != i_DomainPddlId);
}


//										
void SubgoalLearner::OnFFResponse (int _iIndex, FFResponse& _rResponse)
{
	pthread_mutex_lock (&mtx_WaitForSequences);
	if (true == b_DisplayFFProgress)
		cout << "\x08 \x08" << flush;

	// keep count of the types of responses...				
	switch (_rResponse.e_PlanningOutcome)
	{
		case po_plan_found:
			++ i_OutcomePlansFound;
			break;
		case po_goal_already_satisfied:
			++ i_OutcomeGoalsAlreadySatisfied;
			break;
		case po_unsolvable:
			++ i_OutcomeUnsolvable;
			break;
		case po_timeout:
			++ i_OutcomeTimeouts;
			break;
		case po_syntax_error:
			++ i_OutcomeSyntaxError;
			break;
		case po_outside_known_world:
			++ i_OutcomeOutsideKnownWorld;
			break;
		case po_unknown:
			++ i_OutcomeUnknown;
			break;
		default:
			;
	}


	// find the sequence for this response...				
	IndexToSubgoalSequenceState_hmp_t::iterator	ite;
	ite = hmp_IndexToSequenceState.find (_iIndex);
	if (hmp_IndexToSequenceState.end () == ite)
	{
		cerr << "   [EE] Sequence state index [" << _iIndex
			 << "] not found in Callback." << endl;
		return;
	}
	SubgoalSequenceState& rState = ite->second;
	Subgoal* pLastSubgoal = rState.p_Sequence->GetSubgoal (rState.i_CurrentStep);

  assert(false == pLastSubgoal->b_isQuestion);

  pLastSubgoal->e_PlanningOutcome = _rResponse.e_PlanningOutcome;


	// check for syntax error responses ...					
	if (po_syntax_error == _rResponse.e_PlanningOutcome)
	{
		Subgoal* pSubgoal = rState.p_Sequence->GetSubgoal (rState.i_CurrentStep);
		cout << "\n[WARNING] Syntax error ---------------------------\n"
			 << _rResponse.s_FFOutput << '\n'
			 << "----------------------------------------------------\n"
			 << pSubgoal->s_ProblemPddl << '\n'
			 << "----------------------------------------------------\n"
			 << endl;
	}


	// stop this sequence we couldn't find a plan ...		
	if ((po_plan_found != _rResponse.e_PlanningOutcome) &&
		(po_goal_already_satisfied != _rResponse.e_PlanningOutcome))
	{
		f_TotalPlanDepthReached += rState.i_CurrentStep
									/ (float) rState.p_Sequence->Length ();

		set_PendingSequences.erase (_iIndex);

		if (true == set_PendingSequences.empty ())
			pthread_cond_signal (&cv_WaitForSequences);
		pthread_mutex_unlock (&mtx_WaitForSequences);
		return;
	}

	// Compute the end state of the plan for this subgoal.	
	// We need this to test the next subgoal...				
	{
		if (true == b_UseLocalHeuristicEvaluator)
		{
			PddlState& rInitState
				= pLastSubgoal->p_PddlProblem->o_StartState;
			PddlPredicate_dq_t& rdqPredicatesToSet
				= pLastSubgoal->p_PddlProblem->o_PartialGoalState.dq_Predicates;

			// most of our subgoal predicates are of the form	
			// (> (thing-available x) n).  In this case, l_Value
			// is actually n, and we need to increment it to	
			// n+1 to make sure the end-state computation is	
			// correct...										
			ITERATE (PddlPredicate_dq_t, rdqPredicatesToSet, ite)
			{
				PddlPredicate* pToSet = *ite;
				if (false == pToSet->b_IsFunction)
					continue;
				if ('>' != ((PddlFunctionValuePredicate*)pToSet)->c_Operator)
					continue;
				++ pToSet->l_Value;
			}

			// cout << "=========================================" << endl;
			// cout << _iIndex << endl;
			// cout << pLastSubgoal->p_PddlProblem->o_PartialGoalState << endl;

			PddlState* pEndState
				= PddlInterface::ComputeApproximateFutureInit (rInitState,
															   rdqPredicatesToSet);
			_rResponse.s_EndStatePredicates = pEndState->GetPredicatePddlString ();


			//cout << pLastSubgoal->p_PddlProblem->o_PartialGoalState << endl;
			//cout << "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" << endl;
			//cout << rInitState << endl;
			//cout << "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" << endl;
			//cout << *pEndState << endl;
			//cout << "=========================================" << endl;
			delete pEndState;
		}

		else if (po_goal_already_satisfied != _rResponse.e_PlanningOutcome)
		{
			PddlPlan* pPddlPlan = PddlInterface::ParsePlan (*p_PddlDomain,
															_rResponse.s_Plan);

			PddlPredicate_dq_t* pdqPredicates = new PddlPredicate_dq_t;
			rState.dq_PlanSubgoalSequences.push_back (pdqPredicates);
			PddlState* pEndState
				= PddlInterface::ComputeEndStateFast (*pLastSubgoal->p_PddlProblem,
													  *pPddlPlan,
													  *pdqPredicates);

			_rResponse.s_EndStatePredicates = pEndState->GetPredicatePddlString ();

			delete pEndState;
			delete pPddlPlan;
		}

		else
		{
			_rResponse.s_EndStatePredicates
				= pLastSubgoal->p_PddlProblem->o_StartState.GetPredicatePddlString ();

			PddlPredicate_dq_t* pdqPredicates = new PddlPredicate_dq_t;
			rState.dq_PlanSubgoalSequences.push_back (pdqPredicates);
		}
	}
	delete pLastSubgoal->p_PddlProblem;
	pLastSubgoal->p_PddlProblem = NULL;
	rState.p_Sequence->SetSubtaskFFResponse (rState.i_CurrentStep, _rResponse);


	// check for task completion ...						
	if (true == pLastSubgoal->b_IsLastSubgoalToTarget)
	{
		// this sequence is gets us to the target goal !!
		f_TotalPlanDepthReached += 1;
		vec_TargetGoalCompletions [rState.i_ProblemId] = 1;

		rState.b_TaskComplete = true;
		Problem* pProblem = Problem::GetProblem (rState.i_ProblemId);
		if (true == rState.b_FullTask)
			pProblem->b_SubgoalsNotNeeded = true;

		set_PendingSequences.erase (_iIndex);

		if (true == set_PendingSequences.empty ())
			pthread_cond_signal (&cv_WaitForSequences);
		pthread_mutex_unlock (&mtx_WaitForSequences);
		return;
	}


	// Get the next subtask....								
	String sProblemPddl;
  //Use function to determine next subgoal to ensure we get a real subtask
  if (false == rState.p_Sequence->GetSubtask (rState.nextSubgoal(),
											    &sProblemPddl))
	{
		// we have already checked for task completion,	
		// so we should never get to this code point...	
		assert (false);
	}
  //Note, i_CurrentState is now updated
  
	sProblemPddl.Strip ();
	if ("" == sProblemPddl)
	{
		cout << "[ERROR] problem pddl is empty in OnFFResponse ()!" << endl;
		if (po_goal_already_satisfied == _rResponse.e_PlanningOutcome)
			cout << "        previous problem had 0 length plan." << endl;
	}


	// send out the subtask to FF...						
	PddlProblem* pPddlProblem = PddlInterface::ParseProblemPddl (sProblemPddl);
	rState.p_Sequence->SetSubtask (rState.i_CurrentStep,
								   sProblemPddl,
								   pPddlProblem);

	pthread_mutex_unlock (&mtx_WaitForSequences);

	++ i_TotalPlanJobs;
	o_FFInterface.SendTask (_iIndex,
							i_DomainPddlId,
							sProblemPddl,
							i_CurrentFFTimelimit);
	if (true == b_DisplayFFProgress)
		cout << '.' << flush;
}


//										
double SubgoalLearner::ComputeReward (SubgoalSequenceState& _rState)
{
	assert (false == _rState.p_Sequence->dq_Subgoals.empty ());

	double dReward = 0;
	bool bTaskComplete = true;

	ITERATE (Subgoal_dq_t, _rState.p_Sequence->dq_Subgoals, ite)
	{
		Subgoal& rSubgoal = *ite;
		if (SEQUENCE_END == rSubgoal.i_SequenceEnd)
			continue;

		if (po_ff_code_change_required == rSubgoal.e_PlanningOutcome)
		{
			// if FF asked for a code change, we don't know 	
			// the correct outcome, so don't learn on this...	
			_rState.d_Reward = 0;
			return 0;
		}
    
		if ((po_plan_found != rSubgoal.e_PlanningOutcome) &&
			(po_goal_already_satisfied != rSubgoal.e_PlanningOutcome))
		{
			bTaskComplete = false;
			break;
		}
    if (rSubgoal.b_isQuestion)
      dReward += double((config) "ir:reward");
		else if (po_goal_already_satisfied  == rSubgoal.e_PlanningOutcome)
			dReward -= d_UnnecessarySubgoalPenalty;
		else if (po_plan_found == rSubgoal.e_PlanningOutcome)
			dReward += d_SuccessfulStepRewardBase;
		else if (po_outside_known_world == rSubgoal.e_PlanningOutcome)
			dReward += d_RewardForHittingCachePeriphery;
	}

	_rState.d_Reward = dReward;
	if (true == bTaskComplete)
		_rState.d_Reward += d_TaskCompletionReward;
	else
		_rState.d_Reward -= d_PlanFailureReward;

	return _rState.d_Reward;
}


//										
void SubgoalLearner::TrimPlanSubgoalSequences (PlanSubgoalSequences_dq_t& _rdqPlanSubgoals)
{
	ITERATE (PlanSubgoalSequences_dq_t, _rdqPlanSubgoals, iteSequence)
	{
		PddlPredicate_dq_t* pdqOld = *iteSequence;
		PddlPredicate_dq_t* pdqNew = new PddlPredicate_dq_t;
		*iteSequence = pdqNew;

		PddlPredicate* pLastPred = NULL;
		ITERATE (PddlPredicate_dq_t, (*pdqOld), ite)
		{
			PddlPredicate* pPred = *ite;
			bool bSkipThisPredicate
				= (NULL == o_SubgoalPolicy.FindEquivalentPredicateCandidate (*pPred));
			if ((NULL != pLastPred) &&
				(true == pPred->b_IsFunction) &&
				(true == pLastPred->b_IsFunction))
			{
				// check if the current predicate is the		
				// same as the last one (with different value)	
				if (*pPred == *pLastPred)
					bSkipThisPredicate = true;
			}

			if (true == bSkipThisPredicate)
				delete pPred;
			else
			{
				pdqNew->push_back (pPred);
				pLastPred = pPred;
			}
		}

		delete pdqOld;
	}
}


//										
void SubgoalLearner::ProposeAlternateSequences (SubgoalSequenceState& _rState,
										SubgoalSequence_dq_t& _rdqAlternateSequences)
{
	if (true == _rState.dq_PlanSubgoalSequences.empty ())
		return;
	assert (_rState.p_Sequence->dq_Subgoals.size () - 1
			>= _rState.dq_PlanSubgoalSequences.size ());

	TrimPlanSubgoalSequences (_rState.dq_PlanSubgoalSequences);

	SubgoalSequence* pNewSequence = new SubgoalSequence;
	_rdqAlternateSequences.push_back (pNewSequence);
	pNewSequence->s_ProblemPddlPreamble = _rState.p_Sequence->s_ProblemPddlPreamble;
	pNewSequence->p_TargetProblem = _rState.p_Sequence->p_TargetProblem;

	Subgoal& rObservedLastSubgoal = _rState.p_Sequence->dq_Subgoals.back ();
	#ifndef NDEBUG
	bool bPlanFound = ((po_plan_found == rObservedLastSubgoal.e_PlanningOutcome) ||
					   (po_goal_already_satisfied == rObservedLastSubgoal.e_PlanningOutcome));
	assert (false == (bPlanFound ^ _rState.b_TaskComplete));
	#endif

	// SEQUENCE_END subgoal...	
	{
		Subgoal* pSubgoal = pNewSequence->AddSubgoalToBack ();
		pSubgoal->i_SequenceEnd = SEQUENCE_END;
	}

	// subgoals ...				
	Subgoal* pSubgoal = NULL;
	{
		ITERATE (PlanSubgoalSequences_dq_t, _rState.dq_PlanSubgoalSequences, ite)
		{
			PddlPredicate_dq_t* pdqPlanSubgoals = *ite;
			ITERATE (PddlPredicate_dq_t, (*pdqPlanSubgoals), iteSubgoal)
			{
				PddlPredicate* pEquivalentCandidate
					= o_SubgoalPolicy.FindEquivalentPredicateCandidate (**iteSubgoal);
				if (NULL == pEquivalentCandidate)
					continue;

				pSubgoal = pNewSequence->AddSubgoalToBack ();
				pSubgoal->i_SequenceEnd = 0;
				pSubgoal->b_IsLastSubgoalToTarget = false;
				pSubgoal->i_SubgoalSelection = pEquivalentCandidate->i_PredicateCandidateIndex;
				pSubgoal->p_PddlSubgoalPredicate = pEquivalentCandidate;
				pSubgoal->e_PlanningOutcome = po_plan_found;
			}
		}
	}

	// target subgoal...		
	if ((po_plan_found == rObservedLastSubgoal.e_PlanningOutcome) ||
		(po_goal_already_satisfied == rObservedLastSubgoal.e_PlanningOutcome))
	{
		if ((NULL != pSubgoal) &&
			(pSubgoal->i_SubgoalSelection == rObservedLastSubgoal.i_SubgoalSelection))
		{
			pSubgoal->b_IsLastSubgoalToTarget = true;
			pSubgoal->p_PddlSubgoalPredicate = rObservedLastSubgoal.p_PddlSubgoalPredicate;
			pSubgoal->p_PddlTargetProblem = rObservedLastSubgoal.p_PddlTargetProblem;
			pSubgoal->e_PlanningOutcome = rObservedLastSubgoal.e_PlanningOutcome;
		}
		else
		{
			Subgoal* pSubgoal = pNewSequence->AddSubgoalToBack ();
			pSubgoal->i_SequenceEnd = 0;
			pSubgoal->b_IsLastSubgoalToTarget = true;
			pSubgoal->i_SubgoalSelection = rObservedLastSubgoal.i_SubgoalSelection;
			pSubgoal->p_PddlSubgoalPredicate = rObservedLastSubgoal.p_PddlSubgoalPredicate;
			pSubgoal->p_PddlTargetProblem = rObservedLastSubgoal.p_PddlTargetProblem;
			pSubgoal->e_PlanningOutcome = rObservedLastSubgoal.e_PlanningOutcome;
		}
	}
}

void SubgoalLearner::TryLinkingSubgoals(void) {
	o_SubgoalPolicy.clearAnswers();
  vec_TargetGoalCompletions.Memset (0);
	i_TotalPlanJobs = 0;
	i_OutcomePlansFound = 0;
	i_OutcomeGoalsAlreadySatisfied = 0;
	i_OutcomeUnsolvable = 0;
	i_OutcomeSyntaxError = 0;
	i_OutcomeTimeouts = 0;
	i_OutcomeOutsideKnownWorld = 0;
	i_OutcomeUnknown = 0;
	f_TotalPlanDepthReached = 0;

	i_CurrentFFTimelimit = i_TrainingTimeFFTimelimit;

	// These flags are supposed to be randomly	
	// sampled. But on the first iteration we	
	// set them to true to force some learning.	
	o_SubgoalPolicy.ForceConnectionUseFlags ();

  o_SubgoalPolicy.SampleConnections (false);
  int d = 0; // d is the index of the problem

  Problem* pProblem = Problem::GetProblem (d);
  SubgoalSequence* pSequence = new SubgoalSequence;
  pSequence->s_ProblemPddlPreamble = pProblem->s_PddlPreamble;

  pSequence->p_TargetProblem = pProblem;
  o_SubgoalPolicy.SampleSubgoalTestSequence (*pProblem,  pSequence);

  // The PddlProblem we pass into SetSubtask is deleted	
  // when the pSequence is deleted at the end of this		
  // learning iteration.  So we need to make a copy of the
  // PddlProblem here...									
  PddlProblem* pPddlProblem = new PddlProblem (pProblem->GetPddlProblem ());
  pSequence->SetSubtask (1, pProblem->s_Problem, pPddlProblem);

  ++ i_TotalPlanJobs;
  int iIndex = d;

  pthread_mutex_lock (&mtx_WaitForSequences);
  pair <IndexToSubgoalSequenceState_hmp_t::iterator, bool> pairInsert;
  pairInsert = hmp_IndexToSequenceState.insert (make_pair (iIndex, 
                                                           SubgoalSequenceState (pSequence, 1, d)));
  SubgoalSequenceState& rState = pairInsert.first->second;
  rState.b_FullTask = true;
  rState.p_TargetProblem = pProblem;
  set_PendingSequences.insert (iIndex);
  pthread_mutex_unlock (&mtx_WaitForSequences);

  if (rState.p_Sequence->GetSubgoal( rState.i_CurrentStep)->b_isQuestion) {
    rState.nextSubgoal();
  }

  o_FFInterface.SendTask (iIndex,
                          i_DomainPddlId,
                          pProblem->s_Problem,
                          i_CurrentFFTimelimit);
  if (true == b_DisplayFFProgress)
    cout << '.' << flush;

	// condition wait for sequences to complete...	
	pthread_mutex_lock (&mtx_WaitForSequences);
	pthread_cond_wait (&cv_WaitForSequences, &mtx_WaitForSequences);
	pthread_mutex_unlock (&mtx_WaitForSequences);

	// update parameters ...	
	double dTotalReward = 0;
	long lTotalLength = 0;
	int iCount = 0;
	
	o_SubgoalPolicy.InitUpdate ();
	ITERATE (IndexToSubgoalSequenceState_hmp_t, hmp_IndexToSequenceState, ite)
	{
		SubgoalSequenceState& rState = ite->second;
		double dReward = ComputeReward (rState);
		dTotalReward += dReward;
		++ iCount;

		lTotalLength += rState.p_Sequence->dq_Subgoals.size () - 1;
		if ((true == b_LearnOnSubgoalFreeProblems) ||
			(false == rState.p_TargetProblem->b_SubgoalsNotNeeded))
		{
			o_SubgoalPolicy.UpdateParameters (*rState.p_Sequence,
											  dReward,
											  rState.b_TaskComplete,
											  true);

		}

    delete rState.p_Sequence;

  }
		// cleanup...				
		ITERATE (PlanSubgoalSequences_dq_t, rState.dq_PlanSubgoalSequences, ite)
		{
			PddlPredicate_dq_t* pdqPredicates = *ite;
			ITERATE (PddlPredicate_dq_t, (*pdqPredicates), itePred)
				delete *itePred;
			delete pdqPredicates;
		}
		rState.dq_PlanSubgoalSequences.clear ();

	o_SubgoalPolicy.CompleteUpdate ();

	cout << "Done running through sequence link!"
		 << endl;
	hmp_IndexToSequenceState.clear ();

}
//										
void SubgoalLearner::TryPlanningOnFullTasks (void)
{
	vec_TargetGoalCompletions.Memset (0);
	i_TotalPlanJobs = 0;
	i_OutcomePlansFound = 0;
	i_OutcomeGoalsAlreadySatisfied = 0;
	i_OutcomeUnsolvable = 0;
	i_OutcomeSyntaxError = 0;
	i_OutcomeTimeouts = 0;
	i_OutcomeOutsideKnownWorld = 0;
	i_OutcomeUnknown = 0;
	f_TotalPlanDepthReached = 0;

	i_CurrentFFTimelimit = i_TrainingTimeFFTimelimit;

	// These flags are supposed to be randomly	
	// sampled. But on the first iteration we	
	// set them to true to force some learning.	
	o_SubgoalPolicy.ForceConnectionUseFlags ();

	o_SubgoalPolicy.SampleConnections (false);
	for (int d = 0; d < Problem::GetProblemCount (); ++ d)
	{
		Problem* pProblem = Problem::GetProblem (d);
		SubgoalSequence* pSequence = new SubgoalSequence;
		pSequence->s_ProblemPddlPreamble = pProblem->s_PddlPreamble;

		pSequence->p_TargetProblem = pProblem;
		o_SubgoalPolicy.SampleZeroSubgoalSequence (*pProblem, pSequence);

		// The PddlProblem we pass into SetSubtask is deleted	
		// when the pSequence is deleted at the end of this		
		// learning iteration.  So we need to make a copy of the
		// PddlProblem here...									
		PddlProblem* pPddlProblem = new PddlProblem (pProblem->GetPddlProblem ());
		pSequence->SetSubtask (1, pProblem->s_Problem, pPddlProblem);

		++ i_TotalPlanJobs;
		int iIndex = d;

		pthread_mutex_lock (&mtx_WaitForSequences);
		pair <IndexToSubgoalSequenceState_hmp_t::iterator, bool> pairInsert;
		pairInsert = hmp_IndexToSequenceState.insert (make_pair (iIndex, 
										 SubgoalSequenceState (pSequence, 1, d)));
		SubgoalSequenceState& rState = pairInsert.first->second;
		rState.b_FullTask = true;
		rState.p_TargetProblem = pProblem;
		set_PendingSequences.insert (iIndex);
		pthread_mutex_unlock (&mtx_WaitForSequences);


		o_FFInterface.SendTask (iIndex,
								i_DomainPddlId,
								pProblem->s_Problem,
								i_CurrentFFTimelimit);
		if (true == b_DisplayFFProgress)
			cout << '.' << flush;
	}

	// condition wait for sequences to complete...	
	pthread_mutex_lock (&mtx_WaitForSequences);
	pthread_cond_wait (&cv_WaitForSequences, &mtx_WaitForSequences);
	pthread_mutex_unlock (&mtx_WaitForSequences);

	// update parameters ...	
	double dTotalReward = 0;
	long lTotalLength = 0;
	int iCount = 0;
	long lTotalAltenateLength = 0;
	int iAlternateCount = 0;

	o_SubgoalPolicy.InitUpdate ();
	ITERATE (IndexToSubgoalSequenceState_hmp_t, hmp_IndexToSequenceState, ite)
	{
		SubgoalSequenceState& rState = ite->second;
		double dReward = ComputeReward (rState);
		dTotalReward += dReward;
		++ iCount;

		lTotalLength += rState.p_Sequence->dq_Subgoals.size () - 1;
		if ((true == b_LearnOnSubgoalFreeProblems) ||
			(false == rState.p_TargetProblem->b_SubgoalsNotNeeded))
		{
			o_SubgoalPolicy.UpdateParameters (*rState.p_Sequence,
											  dReward,
											  rState.b_TaskComplete,
											  true);
			//o_SubgoalPolicy.UpdateParameters (*rState.p_Sequence,
			//								  dReward,
			//								  rState.b_TaskComplete,
			//								  false);

			if ((true == b_LearnFromAlternateSequences) &&
				(true == rState.b_TaskComplete))
			{
				SubgoalSequence_dq_t dqAlternates;
				ProposeAlternateSequences (rState, dqAlternates);
				ITERATE (SubgoalSequence_dq_t, dqAlternates, iteAlternate)
				{
					SubgoalSequence* pAlternate = *iteAlternate;
					lTotalAltenateLength += pAlternate->dq_Subgoals.size ();
					++ iAlternateCount;
					o_SubgoalPolicy.UpdateParameters (*pAlternate,
													  dReward,
													  rState.b_TaskComplete,
													  true);
					//o_SubgoalPolicy.UpdateParameters (*pAlternate,
					//								  dReward,
					//								  rState.b_TaskComplete,
					//								  false);
					delete *iteAlternate;
				}
			}
		}

		if (true == rState.b_TaskComplete)
			// (true == b_RememberSolutions))
		{
			assert (true == rState.p_TargetProblem->b_SubgoalsNotNeeded);
			if (false == rState.p_TargetProblem->AddSolution (rState.p_Sequence,
															  dReward, -1))
				delete rState.p_Sequence;
		}
		else
			delete rState.p_Sequence;


		// cleanup...				
		ITERATE (PlanSubgoalSequences_dq_t, rState.dq_PlanSubgoalSequences, ite)
		{
			PddlPredicate_dq_t* pdqPredicates = *ite;
			ITERATE (PddlPredicate_dq_t, (*pdqPredicates), itePred)
				delete *itePred;
			delete pdqPredicates;
		}
		rState.dq_PlanSubgoalSequences.clear ();
	}

	o_SubgoalPolicy.CompleteUpdate ();

	cout << "pf:" << i_OutcomePlansFound
		 << " gs:" << i_OutcomeGoalsAlreadySatisfied
		 << " us:" << i_OutcomeUnsolvable
		 << " to:" << i_OutcomeTimeouts
		 << " uw:" << i_OutcomeOutsideKnownWorld
		 << " uk:" << i_OutcomeUnknown
		 << " / " << i_TotalPlanJobs
		 << ", tc:" << vec_TargetGoalCompletions.Sum ()
		 << ", ts:" << Problem::TotalSolvedProblems ()
		 << setprecision (2)
		 << ", al:" << lTotalLength / (float)iCount
		 << ", aal:" << lTotalAltenateLength / (float)iAlternateCount
		 << ", dpth:" << f_TotalPlanDepthReached / (float)i_TotalPlanJobs
		 << ", tcr:" << o_SubgoalPolicy.ConnectionPredictionRatio ()
		 << ", rwd:" << dTotalReward / (double)iCount
		 << ", wvn:" << o_SubgoalPolicy.WeightVectorNorm ()
		 << setprecision (5)
		 << endl;


	hmp_IndexToSequenceState.clear ();
}

/**
 **Given the i_CurrentStep, sets the step to the next non-question subgoal
 **Note this cannot overflow in regular use as last subgoal is
 ** ensured to be a real subgoal
**/
int SubgoalSequenceState::nextSubgoal(){
  unsigned int currentStep = this->i_CurrentStep;
  size_t max_step =  this->p_Sequence->dq_Subgoals.size();

  assert(currentStep < max_step);
  ++ (this->i_CurrentStep);
  while(true == this->p_Sequence->GetSubgoal(currentStep)->b_isQuestion) {
    assert(currentStep < max_step);
    ++(currentStep);
  }
  this->i_CurrentStep = currentStep;
  return this->i_CurrentStep;
}



//										
void SubgoalLearner::Iterate (int _iIteration, bool _bTestMode)
{
	o_SubgoalPolicy.clearAnswers();

	vec_TargetGoalCompletions.Memset (0);
	i_TotalPlanJobs = 0;
	i_OutcomePlansFound = 0;
	i_OutcomeGoalsAlreadySatisfied = 0;
	i_OutcomeUnsolvable = 0;
	i_OutcomeSyntaxError = 0;
	i_OutcomeTimeouts = 0;
	i_OutcomeOutsideKnownWorld = 0;
	i_OutcomeUnknown = 0;
	f_TotalPlanDepthReached = 0;

	if (true == _bTestMode)
		i_CurrentFFTimelimit = i_TestTimeFFTimelimit;
	else
		i_CurrentFFTimelimit = i_TrainingTimeFFTimelimit;

	o_SubgoalPolicy.SampleExplorationParameters ();
	o_SubgoalPolicy.SampleConnections (_bTestMode);

	// generate subgoal sequences ...	
	int iSequencesPerIteration = (_iIteration <= 1)?
									i_SequencesOnFirstIteration :
									i_SequencesPerIteration;
	iSequencesPerIteration = (true == _bTestMode)? 1 : iSequencesPerIteration;
	for (int i = 0; i < iSequencesPerIteration; ++ i)
	{
		for (int d = 0; d < Problem::GetProblemCount (); ++ d)
		{
			o_SubgoalPolicy.SampleConnectionUseFlags ();

			Problem* pProblem = Problem::GetProblem (d);
			SubgoalSequence* pSequence = new SubgoalSequence;
			pSequence->s_ProblemPddlPreamble = pProblem->s_PddlPreamble;

			pSequence->p_TargetProblem = pProblem;
			if (true == pProblem->b_SubgoalsNotNeeded)
				o_SubgoalPolicy.SampleZeroSubgoalSequence (*pProblem, pSequence);

			else
				o_SubgoalPolicy.SampleSubgoalSequence (*pProblem,
													   _bTestMode,
													   pSequence);


			Subgoal* pSubgoal = pSequence->GetSubgoal (1);
			pSubgoal->s_StartStatePredicates
				= pProblem->p_PddlProblem->o_StartState.GetPredicatePddlString ();


			String sProblemPddl;
			pSequence->GetSubtask (1, &sProblemPddl);

			sProblemPddl.Strip ();
			if ("" == sProblemPddl)
			{
				cout << "[ERROR] problem pddl is empty in Learn ()!" << endl;
				cout << "start state predicates ----------------------\n"
					 << pSubgoal->s_StartStatePredicates << '\n'
					 << "pddl subgoal predicates ---------------------\n"
					 << *pSubgoal->p_PddlSubgoalPredicate << '\n'
					 << "---------------------------------------------\n"
					 << endl;
			}

			PddlProblem* pPddlProblem = PddlInterface::ParseProblemPddl (sProblemPddl);
			pSequence->SetSubtask (1, sProblemPddl, pPddlProblem);

			++ i_TotalPlanJobs;

			int iIndex = 1000 * i + d;

			//										
			pair <IndexToSubgoalSequenceState_hmp_t::iterator, bool> pairInsert;
			pairInsert = hmp_IndexToSequenceState.insert (make_pair (iIndex, 
											 SubgoalSequenceState (pSequence, 1, d)));
			SubgoalSequenceState& rState = pairInsert.first->second;
			rState.b_FullTask = false;
			rState.p_TargetProblem = pProblem;
			set_PendingSequences.insert (iIndex);
		}
	}


	pthread_mutex_lock (&mtx_WaitForSequences);
	ITERATE (IndexToSubgoalSequenceState_hmp_t, hmp_IndexToSequenceState, ite)
	{
		int iIndex = ite->first;
		SubgoalSequenceState& rState = ite->second;

    unsigned int subgoalIndex = 1;

    //Ensure first subgoal we send to MetricFF is a subgoal
		Subgoal* pSubgoal = rState.p_Sequence->GetSubgoal (subgoalIndex);
    while(true == pSubgoal->b_isQuestion) {
      pSubgoal = rState.p_Sequence->GetSubgoal (++ subgoalIndex);
    }

		if (false == pSubgoal->b_isQuestion) {
			o_FFInterface.SendTask (iIndex,
				i_DomainPddlId,
				pSubgoal->s_ProblemPddl,
				i_CurrentFFTimelimit);
		} else {
			// Do not send the question
			set_PendingSequences.erase (iIndex);
		}

		if (true == b_DisplayFFProgress)
			cout << '.' << flush;
	}
	pthread_mutex_unlock (&mtx_WaitForSequences);



	// condition wait for sequences to complete...	
	pthread_mutex_lock (&mtx_WaitForSequences);
	pthread_cond_wait (&cv_WaitForSequences, &mtx_WaitForSequences);
	pthread_mutex_unlock (&mtx_WaitForSequences);


	if (true == b_LogPredictions)
		LogPredictions (_iIteration);


	// update parameters ...	
	double dTotalReward = 0;
	long lTotalLength = 0;
	int iCount = 0;
	long lTotalAltenateLength = 0;
	int iAlternateCount = 0;
	int_set_t setSolvedSubgoals;

	o_SubgoalPolicy.InitUpdate ();
	ITERATE (IndexToSubgoalSequenceState_hmp_t, hmp_IndexToSequenceState, ite)
	{
		SubgoalSequenceState& rState = ite->second;
		Problem* pTargetProblem = rState.p_TargetProblem;

		if (true == rState.b_TaskComplete)
		{
			ITERATE (Subgoal_dq_t, rState.p_Sequence->dq_Subgoals, iteSubgoal)
			{
				Subgoal& rSubgoal = *iteSubgoal;
				if (SEQUENCE_END == rSubgoal.i_SequenceEnd)
					continue;
				assert (rSubgoal.i_SubgoalSelection >= 0);
				setSolvedSubgoals.insert (rSubgoal.i_SubgoalSelection);
			}
		}

		double dReward = ComputeReward (rState);
		dTotalReward += dReward;
		++ iCount;

		lTotalLength += rState.p_Sequence->dq_Subgoals.size () - 1;
		if (false == _bTestMode)
		{
			if ((true == b_LearnOnSubgoalFreeProblems) ||
				(false == pTargetProblem->b_SubgoalsNotNeeded))
			{
				o_SubgoalPolicy.UpdateParameters (*rState.p_Sequence,
												  dReward,
												  rState.b_TaskComplete,
												  true);
				//o_SubgoalPolicy.UpdateParameters (*rState.p_Sequence,
				//								  dReward,
				//								  rState.b_TaskComplete,
				//								  false);

				if (true == b_RememberSolutions)
				{
					SubgoalSequence* pBestObserved = pTargetProblem->GetCurrentSolution ();
					int iBestIteration = pTargetProblem->GetCurrentSolutionIteration ();
					if ((NULL != pBestObserved) && (_iIteration != iBestIteration))
					{
						double dBestReward = pTargetProblem->GetCurrentSolutionReward ();
						o_SubgoalPolicy.UpdateParameters (*pBestObserved,
														  dBestReward,
														  rState.b_TaskComplete,
														  true);
						//o_SubgoalPolicy.UpdateParameters (*pBestObserved,
						//								  dBestReward,
						//								  rState.b_TaskComplete,
						//								  false);
					}
				}

				if ((true == b_LearnFromAlternateSequences) &&
					(true == rState.b_TaskComplete))
				{
					SubgoalSequence_dq_t dqAlternates;
					ProposeAlternateSequences (rState, dqAlternates);
					ITERATE (SubgoalSequence_dq_t, dqAlternates, iteAlternate)
					{
						SubgoalSequence* pAlternate = *iteAlternate;
						// cout << "      " << pAlternate->ToLogString () << endl;
						lTotalAltenateLength += pAlternate->dq_Subgoals.size ();
						++ iAlternateCount;
						o_SubgoalPolicy.UpdateParameters (*pAlternate,
														  dReward,
														  rState.b_TaskComplete,
														  true);
						//o_SubgoalPolicy.UpdateParameters (*pAlternate,
						//								  dReward,
						//								  rState.b_TaskComplete,
						//								  false);
						delete *iteAlternate;
					}
				}
			}
		}

		if ((true == rState.b_TaskComplete) &&
			// (true == b_RememberSolutions) &&
			(false == pTargetProblem->b_SubgoalsNotNeeded))
		{
			if (false == pTargetProblem->AddSolution (rState.p_Sequence,
													  dReward,
													  _iIteration))
				delete rState.p_Sequence;
		}
		else
			delete rState.p_Sequence;


		// cleanup...				
		ITERATE (PlanSubgoalSequences_dq_t, rState.dq_PlanSubgoalSequences, ite)
		{
			PddlPredicate_dq_t* pdqPredicates = *ite;
			ITERATE (PddlPredicate_dq_t, (*pdqPredicates), itePred)
				delete *itePred;
			delete pdqPredicates;
		}
		rState.dq_PlanSubgoalSequences.clear ();
	}
	o_SubgoalPolicy.CompleteUpdate ();

	// add solved subgoals to policy for feature computation...	
	o_SubgoalPolicy.AddReachableSubgoals (setSolvedSubgoals);


	float fAvgAlternateLength = 0;
	if (iAlternateCount > 0)
		fAvgAlternateLength = lTotalAltenateLength / (float)iAlternateCount;

	cout << "pf:" << i_OutcomePlansFound
		 << " gs:" << i_OutcomeGoalsAlreadySatisfied
		 << " us:" << i_OutcomeUnsolvable
		 << " to:" << i_OutcomeTimeouts
		 << " uw:" << i_OutcomeOutsideKnownWorld
		 << " uk:" << i_OutcomeUnknown
		 << " / " << i_TotalPlanJobs
		 << ", tc:" << vec_TargetGoalCompletions.Sum ()
		 << ", ts:" << Problem::TotalSolvedProblems ()
		 << setprecision (2)
		 << ", al:" << lTotalLength / (float)iCount
		 << ", aal:" << fAvgAlternateLength
		 << ", dpth:" << f_TotalPlanDepthReached / (float)i_TotalPlanJobs
		 << ", tcr:" << o_SubgoalPolicy.ConnectionPredictionRatio ()
		 << ", rwd:" << dTotalReward / (double)iCount
		 << ", wvn:" << o_SubgoalPolicy.WeightVectorNorm ()
		 << setprecision (5)
		 << endl;

	hmp_IndexToSequenceState.clear ();
}


//										
void SubgoalLearner::LogPredictions (int _iIteration)
{
	String sLogFile;
	sLogFile << ((config)"prediction_log_path") << _iIteration;
	File file;
	if (false == file.Open (sLogFile, ios_base::out))
		return;

	ITERATE (IndexToSubgoalSequenceState_hmp_t, hmp_IndexToSequenceState, ite)
	{
		SubgoalSequenceState& rState = ite->second;

		PddlProblem* pPddlProblem = rState.p_TargetProblem->p_PddlProblem;
		String sTarget;
		sTarget << ((true == rState.b_TaskComplete)? "1 : " : "0 : ");
		sTarget << pPddlProblem->o_PartialGoalState.GetPredicatePddlString ();
		sTarget.Strip ();

		file << sTarget << " : PRED :";
		if (true == rState.p_TargetProblem->b_SubgoalsNotNeeded)
			file << " [SUBGOALS NOT NEEDED]" << endl;
		else
			file << *rState.p_Sequence << endl;

		SubgoalSequence_dq_t dqAlternates;
		ProposeAlternateSequences (rState, dqAlternates);
		ITERATE (SubgoalSequence_dq_t, dqAlternates, iteAlternate)
		{
			SubgoalSequence* pAlternate = *iteAlternate;
			file << sTarget << " : FF :" << *pAlternate << endl;
		}
		if (true == dqAlternates.empty ())
			file << sTarget << " : FF :" << endl;

	}

	file.flush ();
	file.Close ();
}




