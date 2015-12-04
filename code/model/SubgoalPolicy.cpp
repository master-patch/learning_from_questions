#include "SubgoalPolicy.h"
#include <nlp_config.h>
#include <nlp_filesystem.h>
#include <nlp_macros.h>
#include <assert.h>
#include "Problems.h"


//													
Subgoal::Subgoal (void)
{
	l_States = -1;
	i_SubgoalSelection = -1;
	i_SequenceEnd = -1;
	e_PlanningOutcome = po_unknown;
	p_PddlProblem = NULL;
	p_PddlTargetProblem = NULL;
	p_PddlSubgoalPredicate = NULL;
	b_IsLastSubgoalToTarget = false;
	b_ForcedSequenceEnd = false;
	b_isQuestion = false;
	p_SelectedPredicateFeatures = NULL;
}

Subgoal::~Subgoal (void)
{
	l_States = -2;
	e_PlanningOutcome = po_unknown;
	delete p_PddlProblem;

	ITERATE (Features_vec_t, vec_SequenceEndFeatureVectors, ite)
		delete *ite;
	vec_SequenceEndFeatureVectors.clear ();
	delete p_SelectedPredicateFeatures;

	ITERATE (Features_vec_t, vec_SubgoalFeatureVectors, ite)
		delete *ite;
	vec_SubgoalFeatureVectors.clear ();
}


//													
SubgoalSequence::SubgoalSequence (void)
{
}

SubgoalSequence::~SubgoalSequence (void)
{
}


//													
void SubgoalSequence::SetSubtaskFFResponse (unsigned int _iIndex,
										   FFResponse& _rResponse)
{
	// current subgoal ...	
	#ifndef NDEBUG
	if (_iIndex > dq_Subgoals.size ())
	{
		cerr << "[ERROR] subgoal index in SetSubtaskFFResponse ["
			 << _iIndex << "] out-of-bounds of sequence (length "
			 << dq_Subgoals.size () << ")." << endl;
		assert (false);
	}
	#endif

	Subgoal& rCurrentSubgoal = dq_Subgoals [_iIndex];
	rCurrentSubgoal.s_FFOutput = _rResponse.s_FFOutput;
	rCurrentSubgoal.s_Plan = _rResponse.s_Plan;
	rCurrentSubgoal.l_States = _rResponse.l_States;
	rCurrentSubgoal.e_PlanningOutcome = _rResponse.e_PlanningOutcome;

	
	// next subgoal ...		
	unsigned int iSubgoalIndex = _iIndex + 1;
	if (iSubgoalIndex == dq_Subgoals.size ())
	{
		assert (true == dq_Subgoals [_iIndex].b_IsLastSubgoalToTarget);
		// This is the last subgoal, so no need to 	
		// the init state of next subgoal.			
		return;
	}

	#ifndef NDEBUG
	if (iSubgoalIndex > dq_Subgoals.size ())
	{
		cerr << "[ERROR] next subgoal index in SetSubtaskFFResponse ["
			 << iSubgoalIndex << "] out-of-bounds of sequence (length "
			 << dq_Subgoals.size () << ")." << endl;
		assert (false);
	}
	#endif

	Subgoal& rNextSubgoal = dq_Subgoals [iSubgoalIndex];
	assert ("" == rNextSubgoal.s_StartStatePredicates);
	rNextSubgoal.s_StartStatePredicates = _rResponse.s_EndStatePredicates;
}


//													
bool SubgoalSequence::GetSubtask (unsigned int _iIndex,
								  String* _pProblemPddl)
{
	if (_iIndex >= dq_Subgoals.size ())
		return false;
	Subgoal& rSubgoal = dq_Subgoals [_iIndex];
	assert (SEQUENCE_END != rSubgoal.i_SequenceEnd);

	assert ("" != s_ProblemPddlPreamble);
	assert ("" != rSubgoal.s_StartStatePredicates);

	String sGoal;
	if (_iIndex + 1 == dq_Subgoals.size ())
	{
		if (false == rSubgoal.b_IsLastSubgoalToTarget)
			return false;

		assert (true == rSubgoal.b_IsLastSubgoalToTarget);
		sGoal = rSubgoal.p_PddlTargetProblem->o_PartialGoalState.GetPredicatePddlString ();
	}
	else
	{
		assert (false == rSubgoal.b_IsLastSubgoalToTarget);
		sGoal = rSubgoal.p_PddlSubgoalPredicate->GetPddlString ();
	}

	sGoal.Strip ();
	if ("" == sGoal)
	{
		cerr << "[ERROR] empty goal";
		if (true == rSubgoal.b_IsLastSubgoalToTarget)
		{
			cerr << ", last subgoal to target" << endl;
			cerr << "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
			cerr << rSubgoal.p_PddlTargetProblem->o_PartialGoalState << '\n';
			cerr << "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" << endl;
		}
		else
		{
			cerr << ", NOT last subgoal to target" << endl;
			cerr << "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
			cerr << *rSubgoal.p_PddlSubgoalPredicate << '\n';
			cerr << "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" << endl;
		}
	}

	assert ("" != sGoal);

	*_pProblemPddl = "";
	*_pProblemPddl << "(define\n"
				   << s_ProblemPddlPreamble << "\n\n"
				   << "(:init \n"
				   << rSubgoal.s_StartStatePredicates
				   << ")\n"
				   // << "(:goal\ (and \n"
				   << "(:goal \n"
				   << sGoal
				   << "\n)\n)";
				   //<< "\n)\n)\n)";
	return true;
}


//													
void SubgoalSequence::SetSubtask (unsigned int _iIndex,
								  String _rProblemPddl,
								  PddlProblem* _pPddlProblem)
{
	assert (_iIndex < dq_Subgoals.size ());
	dq_Subgoals [_iIndex].s_ProblemPddl = _rProblemPddl;
	dq_Subgoals [_iIndex].p_PddlProblem = _pPddlProblem;
}


//													
String SubgoalSequence::ToLogString (void)
{
	String sReturn;
	ITERATE (Subgoal_dq_t, dq_Subgoals, ite)
	{
		Subgoal& rSubgoal = *ite;
		if (SEQUENCE_END == rSubgoal.i_SequenceEnd)
			continue;
		if (true == rSubgoal.b_IsLastSubgoalToTarget)
			continue;

		if ("" != sReturn)
			sReturn << '\n';
		sReturn << rSubgoal.p_PddlSubgoalPredicate->GetPddlString ();
	}
	return sReturn;
}


//													
void ExplorationParameters::SetParamsFromConfig (String _rPrefix)
{
	f_EpsilonMin		= (config)(_rPrefix + ":epsilon-min");
	f_EpsilonRange		= ((float)(config)(_rPrefix + ":epsilon-max")) - f_EpsilonMin;
	f_BetaMin			= log2 ((config)(_rPrefix + ":beta-min"));
	f_BetaRange			= log2 ((config)(_rPrefix + ":beta-max")) - f_BetaMin;
	e_ExplorationType	= ToEnum ((config)(_rPrefix + ":exploration_type"));
}


//													
String ExplorationParameters::SampleParameters (Sample& _rSample)
{
	String sExploration;

	if ((et_epsilon_greedy == e_ExplorationType) ||
		(et_epsilon_softmax == e_ExplorationType))
	{
		f_Epsilon = f_EpsilonMin + f_EpsilonRange * _rSample.SampleUniform ();
		sExploration << "e:" << f_Epsilon << ' ';
	}

	if ((et_softmax == e_ExplorationType) ||
		(et_epsilon_softmax == e_ExplorationType))
	{
		f_Beta = pow (2, f_BetaMin + f_BetaRange * _rSample.SampleUniform ());
		sExploration << "b:" << f_Beta << ' ';
	}

	return sExploration;
}


//													
void ExplorationParameters::PrintConfiguration (const char* _zPrefix)
{
	cout << "   " << _zPrefix << " exploration : "
		 << ToString (e_ExplorationType)
		 << endl;
	if ((et_epsilon_greedy == e_ExplorationType) ||
		(et_epsilon_softmax == e_ExplorationType))
	{
		cout << "   " << _zPrefix << " epsilon     : "
			 << f_EpsilonMin << " < "
			 << f_EpsilonMin + f_EpsilonRange
			 << endl;
	}
	if ((et_softmax == e_ExplorationType) ||
		(et_epsilon_softmax == e_ExplorationType))
	{
		cout << "   " << _zPrefix << " beta        : "
			 << f_BetaMin << " < "
			 << f_BetaMin + f_BetaRange 
			 << endl;
	}
}


//													
SubgoalPolicy::SubgoalPolicy (void)
{
	Random::Init ();

	b_UseSimpleConnectionFeatures = false;
	b_UseTextConnectionFeatures = false;
	b_UseComplexNonConnectionFeatures = false;
}

SubgoalPolicy::~SubgoalPolicy (void)
{
	Random::Destroy ();

	ITERATE (PddlPredicate_vec_t, vec_CandidatePredicates, ite)
		delete *ite;
	vec_CandidatePredicates.clear ();

	ITERATE (SentenceConnection_vec_t, vec_SentenceConnections, iteConn)
	{
		SentenceConnection* pConnection = *iteConn;
		delete pConnection->p_PositiveFeatures;
		delete pConnection->p_NegativeFeatures;
		delete pConnection;
	}
	vec_SentenceConnections.clear ();

	if (true == mtx_SentencesPositiveFromTo.IsInitialized ())
	{
		for (int f = 0; f < i_CandidatePredicateNumbersMerged; ++ f)
		{
			for (int t = 0; t < i_CandidatePredicateNumbersMerged; ++ t)
			{
				if (NULL != mtx_SentencesPositiveFromTo (f, t))
					delete mtx_SentencesPositiveFromTo (f, t);
				if (NULL != mtx_SentencesNegativeFromTo (f, t))
					delete mtx_SentencesNegativeFromTo (f, t);
			}
		}
	}
}


//													
ExplorationType_e ExplorationParameters::ToEnum (String _sType)
{
	if ("epsilon-greedy" == _sType)
		return et_epsilon_greedy;
	else if ("softmax" == _sType)
		return et_softmax;
	else if ("epsilon-softmax" == _sType)
		return et_epsilon_softmax;
	return et_unknown;
}

const char* ExplorationParameters::ToString (ExplorationType_e _eType)
{
	if (et_epsilon_greedy == _eType)
		return "epsilon-greedy";
	else if (et_softmax == _eType)
		return "softmax";
	else if (et_epsilon_softmax == _eType)
		return "epsilon-softmax";
	return "unknown";
}


//													
bool SubgoalPolicy::Init (void)
{
	o_SequenceEndModel.Init ("end");
	o_SubgoalSelectionModel.Init ("subgoal");
	o_TextConnectionModel.Init ("connection");

	o_SequenceEndExploration.SetParamsFromConfig ("end");
	o_SubgoalExploration.SetParamsFromConfig ("subgoal");
	o_ConnectionExploration.SetParamsFromConfig ("connection");

	i_MaxSequenceLength = (config)"max_subgoal_sequence_length";
	b_DisallowNeighboringDuplicateSubgoals = (1 == (int)(config)"disallow_neighboring_duplicate_subgoals");
	b_DisallowAnyDuplicateSubgoals = (1 == (int)(config)"disallow_any_duplicate_subgoals");
	b_UseLogarithmicDistanceScore = (1 == (int)(config)"use_logarithmic_distance_score");

	b_ForceConnectionWeights = (1 == (int)(config)"force_connection_weights");
	d_ForcedConnectionWeightToInit = (config)"forced_connection_weight_to_init";
	d_ForcedConnectionWeightToTarget = (config)"forced_connection_weight_to_target";
	b_UsePredicateValueFeature = (1 == (int)(config)"use_predicate_value_feature");
	b_UseReachableSubgoalFeature = (1 == (int)(config)"use_reachable_subgoal_feature");
	b_UseReachabilityEquivalents = (1 == (int)(config)"use_reachability_equivalents");

	b_UseOnlyPreviousSubgoal = (1 == (int)(config)"features:use_only_previous_subgoal");
	b_IncludeInit = (0 != (int)(config)"features:include_init");
	f_PredicateIdentityPairFeatureWeight = (config)"predicate_identity_pair_feature_weight";
	String sConnectionRewardType ((config)"connection:reward_type");
	if ("linear" == sConnectionRewardType)
		e_ConnectionRewardType = crt_linear;
	else if ("single_success" == sConnectionRewardType)
		e_ConnectionRewardType = crt_single_success;
	else
	{
		cout << "[ERROR] Unknown connection reward type '"
			 << sConnectionRewardType << "'." << endl;
		e_ConnectionRewardType = crt_unknown;
	}
	f_ConnectionSuccessReward = (config)"connection:success_reward";
	f_ConnectionFailurePenalty = (config)"connection:failure_penalty";
	b_RetainPredicateConnectionFeedback
		= (1 == (int)(config)"connection:retain_connection_feedback");
	b_UseSuccessFailureCountsInFeedback
		= (1 == (int)(config)"use_success_failure_counts_in_feedback");
	i_UpdatesPerIteration = (config)"text_updates_per_iteration";

	cout << "Initializing subgoal policy" << endl;
	cout << "   Max sequence length : " << i_MaxSequenceLength << endl;
	if (true == b_DisallowAnyDuplicateSubgoals)
		cout << "   Disallowing any duplicate subgoals." << endl;
	else if (true == b_DisallowNeighboringDuplicateSubgoals)
		cout << "   Disallowing neighboring duplicate subgoals." << endl;
	else
		cout << "   Allowing duplicate subgoals." << endl;
	if (true == b_UseLogarithmicDistanceScore)
		cout << "   Using logarithmic distance score." << endl;
	else
		cout << "   Using normal distance score." << endl;
	if (true == b_UsePredicateValueFeature)
		cout << "   Using predicate value feature." << endl;
	if (true == b_UseReachableSubgoalFeature)
		cout << "   Using reachable-subgoal feature." << endl;
	if (true == b_UseReachabilityEquivalents)
		cout << "   Using reachability equivalents." << endl;
	cout << "   predicate identity pair feature weight : "
		 << f_PredicateIdentityPairFeatureWeight << endl;

	o_SequenceEndExploration.PrintConfiguration ("Seq end");
	o_SubgoalExploration.PrintConfiguration ("Subgoal");
	o_ConnectionExploration.PrintConfiguration ("Connect");


	f_NonConnectionFeatureImportance = (double)(config)"non_connection_feature_importance";

	if (false == LoadPredDictFile ())
		return false;
	AssignIndicesToTargetProblemPredicates ();

	i_PredicateNames = hmp_PredicateNameToIndex.size ();
	i_ParameterValues = hmp_ParameterValueToIndex.size ();
	i_PredicateIdentities = hmp_PredicateIdToIndex.size ();


	o_SequenceEndFeatureSpace.SetBagOfWordsOffset (2 * pow (i_PredicateIdentities, 2));

	size_t iFeatureSet = i_MaxPredicateValue + 1 + 6
						 + 2 * pow (i_PredicateNames, 2)
						 + 2 * pow (i_ParameterValues, 2)
						 + 2 * pow (i_PredicateIdentities, 2);
	o_SubgoalFeatureSpace.SetBagOfWordsOffset (iFeatureSet);

	i_OffsetToConnectionFeatures = i_MaxPredicateValue + 1;
	i_OffsetToPredicateNameFeatures = 14 + i_OffsetToConnectionFeatures;
	i_OffsetToParameterValueFeatures = i_OffsetToPredicateNameFeatures
										+ 2 * pow (i_PredicateNames, 2);
	i_OffsetToPredicateIdentityFeatures = i_OffsetToParameterValueFeatures
										+ 2 * pow (i_ParameterValues, 2);

	b_PrintTextConnectionFeatures
		= (1 == (int)(config)"features:print_text_connection_features");
	if (true == b_PrintTextConnectionFeatures)
	{
		//first three features
		for (int i = 0; i < i_MaxPredicateValue; ++ i)
		{
			String sFeature;
			sFeature << "PredVal:" << i;
			map_FeatureIndexToFeatureString[i] = sFeature;
		}

		map_FeatureIndexToFeatureString [i_MaxPredicateValue] = "<unused>";
		map_FeatureIndexToFeatureString [i_OffsetToConnectionFeatures] = "<unused>";
		map_FeatureIndexToFeatureString [1 + i_OffsetToConnectionFeatures] = "ReachableSubgoal";
		map_FeatureIndexToFeatureString [2 + i_OffsetToConnectionFeatures] = "ConnInit";
		map_FeatureIndexToFeatureString [3 + i_OffsetToConnectionFeatures] = "ConnInit+Reachable";
		map_FeatureIndexToFeatureString [4 + i_OffsetToConnectionFeatures] = "NoConnInit";

		for (int d = 1; d < 5; ++ d)
		{
			map_FeatureIndexToFeatureString [5 + 2*(d-1) + i_OffsetToConnectionFeatures]
									= "ConnFuture";
			map_FeatureIndexToFeatureString [6 + 2*(d-1) + i_OffsetToConnectionFeatures]
									= "ConnFuture+Reachable";
		}
		map_FeatureIndexToFeatureString [13 + i_OffsetToConnectionFeatures] = "NoConnFuture";


		// populate Feature Strings -- names
		ITERATE(FeatureToIndex_hmp_t, hmp_PredicateNameToIndex, itrFrom)
		{
			ITERATE(FeatureToIndex_hmp_t, hmp_PredicateNameToIndex, itrTo)
			{
				int iIndexInit = i_OffsetToPredicateNameFeatures
								 + (2 * i_PredicateNames * itrFrom->second
										+ itrTo->second);
				int iIndexFuture = i_OffsetToPredicateNameFeatures
								   + (2 * i_PredicateNames * itrFrom->second
										  + itrTo->second 
										  + i_PredicateNames);
				map_FeatureIndexToFeatureString [iIndexInit]
					= "NameInit::" + itrFrom->first + "::" + itrTo->first;
				map_FeatureIndexToFeatureString [iIndexFuture]
					= "NameFuture::" + itrFrom->first + "::" + itrTo->first;
			}
		}

		// populate Feature Strings -- values
		ITERATE(FeatureToIndex_hmp_t, hmp_ParameterValueToIndex, itrFrom)
		{
			ITERATE(FeatureToIndex_hmp_t, hmp_ParameterValueToIndex, itrTo)
			{
				int iIndexInit = i_OffsetToParameterValueFeatures
								 + (2 * i_ParameterValues * itrFrom->second
										+ itrTo->second);
				int iIndexFuture = i_OffsetToParameterValueFeatures
								   + (2 * i_ParameterValues * itrFrom->second
										  + itrTo->second
										  + i_ParameterValues);
				map_FeatureIndexToFeatureString [iIndexInit]
					= "ValueInit::" + itrFrom->first + "::" + itrTo->first;
				map_FeatureIndexToFeatureString [iIndexFuture]
					= "ValueFuture::" + itrFrom->first + "::" + itrTo->first;
			}
		}

		// populate Feature Strings -- identity
		ITERATE(FeatureToIndex_hmp_t, hmp_PredicateIdToIndex, itrFrom)
		{
			ITERATE(FeatureToIndex_hmp_t, hmp_PredicateIdToIndex, itrTo)
			{
				int iIndexInit = i_OffsetToPredicateIdentityFeatures 
								 + (2 * i_PredicateIdentities*itrFrom->second
										+ itrTo->second);
				int iIndexFuture = i_OffsetToPredicateIdentityFeatures
								   + (2 * i_PredicateIdentities * itrFrom->second
										  + itrTo->second
										  + i_PredicateIdentities);
				map_FeatureIndexToFeatureString [iIndexInit]
					= "PredIdInit::" + itrFrom->first + "::" + itrTo->first;
				map_FeatureIndexToFeatureString [iIndexFuture]
					= "PredIdFuture::" + itrFrom->first + "::" + itrTo->first;
			}
		}

		#ifndef NDEBUG
		// make sure all the values are there
		for(unsigned int i = 0; i < map_FeatureIndexToFeatureString.size(); i++)
		{
			assert (map_FeatureIndexToFeatureString.find(i)
					!= map_FeatureIndexToFeatureString.end());
		}
		#endif
	}


	f_UseSimpleConnectionFeatures = (config)"use_pddl_connection_features";
	f_UseTextConnectionFeatures = (config)"use_text_connection_features";
	f_UseComplexNonConnectionFeatures = (config)"use_complex_non_connection_features";

	b_LogConnectionPredictions = false;
	b_LogConnectionFeedback = false;
	if (f_UseTextConnectionFeatures > 0)
	{
		b_LogConnectionPredictions = (1 == (int)(config)"log_connection_predictions");
		b_LogConnectionFeedback = (1 == (int)(config)"log_connection_feedback");
	}

	if ((f_UseSimpleConnectionFeatures > 0) && 
		(f_UseTextConnectionFeatures > 0))
	{
		cerr << "[ERROR] Conflicting configuration options set:\n"
				"Both 'use_pddl_connection_features' and 'use_text_connection_features'\n"
				"options have been set to true. Only one can be active at one time."
			 << endl;
		return false;
	}

	if (f_UseSimpleConnectionFeatures > 0)
	{
		if (false == LoadSimpleConnectionFile ())
			return false;
	}
	else if (f_UseTextConnectionFeatures > 0)
	{
		if (false == LoadFeatureConnectionFile ())
			return false;
		if (true == b_PrintTextConnectionFeatures)
			LoadFeaturesToDebugPrintFile();
	}

	if (true == b_LogConnectionPredictions)
		WriteConnectionPredictionHeader ();

	//NK: my debug stuff
	b_UseGoldLength = (1 == (int)(config)"use_gold_length");
	if (true == b_UseGoldLength)
		LoadGoldLengthFile();

	return true;
}


//													
void SubgoalPolicy::LoadFeaturesToDebugPrintFile(void)
{
	String sGoldLengthFile = (config)"features:debug_features_to_print_file";
	// read in the dict file
	String_dq_t dqLines;
	File::ReadLines (sGoldLengthFile, dqLines);

	ITERATE (String_dq_t, dqLines, iterLine)
	{
		String sFeature = *iterLine;
		int iIndex = o_SubgoalFeatureSpace.GetFeatureIndex (sFeature, true);
		if(iIndex == 0)
		{
			cout << "Couldn't find feature:" << sFeature << endl;
			continue;
		}


		dq_FeaturesToDebugPrint.push_back(iIndex);
	}

	cout << "   loaded " << this->dq_FeaturesToDebugPrint.size()
		 << " features to debug print " << endl;
}


//													
void SubgoalPolicy::LogDebugFeatureWeights (File* _pFile)
{
	if (false == b_PrintTextConnectionFeatures)
		return;

	*_pFile << "Text Features:" << endl;
	ITERATE(int_dq_t, dq_FeaturesToDebugPrint, iter)
	{
		int iFeature = *iter;
		*_pFile << "Feature: "
				<< o_SubgoalSelectionModel.GetWeight(iFeature)
				<< ":" << GetFeatureString(iFeature)
				<< ":" <<  iFeature << endl;
	}
}


//													
String SubgoalPolicy::GetFeatureString(int _iIndex) const
{
	if (_iIndex >= o_SubgoalFeatureSpace.BagOfWordsOffset())
	{
		return o_SubgoalFeatureSpace.GetFeatureString(_iIndex);
	}

	int_String_map_t::const_iterator iter =  map_FeatureIndexToFeatureString.find(_iIndex);
	assert(iter != map_FeatureIndexToFeatureString.end());
	return iter->second;
}




//													
int SubgoalPolicy::GetPredicateIdentityFeatureIndex (const String& _rPredicate)
{
	FeatureToIndex_hmp_t::iterator	ite;
	ite = hmp_PredicateIdToIndex.find (_rPredicate);
	if (hmp_PredicateIdToIndex.end () == ite)
	{
		int iIndex = hmp_PredicateIdToIndex.size ();
		hmp_PredicateIdToIndex.insert (make_pair (_rPredicate, iIndex));
		return iIndex;
	}
	return ite->second;
}


//													
int SubgoalPolicy::GetPredicateNameFeatureIndex (const String& _rName)
{
	FeatureToIndex_hmp_t::iterator	ite;
	ite = hmp_PredicateNameToIndex.find (_rName);
	if (hmp_PredicateNameToIndex.end () == ite)
	{
		int iIndex = hmp_PredicateNameToIndex.size ();
		hmp_PredicateNameToIndex.insert (make_pair (_rName, iIndex));
		return iIndex;
	}
	return ite->second;
}


//													
int SubgoalPolicy::GetPredicateWithoutNumberIndex (const PddlPredicate& _rPredicate)
{
	String sPddlWithoutNumber;
	if (true == _rPredicate.b_IsFunction)
	{
		PddlFunctionValuePredicate* pClone
			= (PddlFunctionValuePredicate*)((PddlPredicate&)_rPredicate).Clone ();
		pClone->l_Value = 0;
		sPddlWithoutNumber = pClone->GetPddlString ();
		delete pClone;
	}
	else
		sPddlWithoutNumber = _rPredicate.GetPddlString ();


	FeatureToIndex_hmp_t::iterator	ite;
	ite = hmp_PredicateWithoutNumberToIndex.find (sPddlWithoutNumber);
	if (hmp_PredicateWithoutNumberToIndex.end () == ite)
	{
		int iIndex = hmp_PredicateWithoutNumberToIndex.size ();
		hmp_PredicateWithoutNumberToIndex.insert (make_pair (sPddlWithoutNumber, iIndex));
		return iIndex;
	}
	return ite->second;
}


//													
int SubgoalPolicy::GetParameterValueFeatureIndex (const String& _rValue)
{
	FeatureToIndex_hmp_t::iterator	ite;
	ite = hmp_ParameterValueToIndex.find (_rValue);
	if (hmp_ParameterValueToIndex.end () == ite)
	{
		int iIndex = hmp_ParameterValueToIndex.size ();
		hmp_ParameterValueToIndex.insert (make_pair (_rValue, iIndex));
		return iIndex;
	}
	return ite->second;
}


//													
void SubgoalPolicy::AssignIndicesToTargetProblemPredicates (void)
{
	cout << "Assigning indices to problem predicates." << endl;
	String_set_t setMissingInitPredicates;
	String_set_t setMissingTargetPredicates;
	for (long i = 0; i < Problem::GetProblemCount (); ++ i)
	{
		Problem* pProblem = Problem::GetProblem (i);
		PddlProblem& rPddlProblem = pProblem->GetPddlProblem ();

		int_set_t	setPredicateIdentityFI;
		int_set_t	setPredicateNameFI;
		int_set_t	setParameterValueFI;

		// init state ...		
		ITERATE (PddlPredicate_dq_t, rPddlProblem.o_StartState.dq_Predicates, ite)
		{
			PddlPredicate* pPredicate = *ite;

			// assign predicate candidate index ...	
			pPredicate->i_PredicateCandidateIndex = FindInitPredicateCandidateIndex (*pPredicate);
			if (-1 == pPredicate->i_PredicateCandidateIndex)
				setMissingInitPredicates.insert (pPredicate->GetPddlString ());

			// assign feature indices to predicate	
			pPredicate->i_PredicateIdentityFeatureIndex
				= GetPredicateIdentityFeatureIndex (pPredicate->GetPddlString ());
			pPredicate->i_PredicateNameFeatureIndex
				= GetPredicateNameFeatureIndex (pPredicate->s_Name);
			pPredicate->i_PredicateCandidateWithoutNumber
				= GetPredicateWithoutNumberIndex (*pPredicate);

			int_set_t setValueFI;
			CONST_ITERATE (PddlParameter_dq_t, pPredicate->dq_Parameters, iteParam)
				setValueFI.insert (GetParameterValueFeatureIndex (*iteParam->p_ResolvedValue));

			pPredicate->vec_ParameterValueFeatureIndex.Create (setValueFI.size ());
			int x = 0;
			ITERATE (int_set_t, setValueFI, iteFI)
				pPredicate->vec_ParameterValueFeatureIndex [x++] = *iteFI;

			// collect feature indicies for problem	
			setPredicateIdentityFI.insert (pPredicate->i_PredicateIdentityFeatureIndex);
			setPredicateNameFI.insert (pPredicate->i_PredicateNameFeatureIndex);
			setParameterValueFI.insert (setValueFI.begin (), setValueFI.end ());
		}

		// assign init feature indices to problem	
		pProblem->vec_InitPredicateIdentityFI.Create (setPredicateIdentityFI.size ());
		int x = 0;
		ITERATE (int_set_t, setPredicateIdentityFI, ite)
			pProblem->vec_InitPredicateIdentityFI [x++] = *ite;

		pProblem->vec_InitPredicateNameFI.Create (setPredicateNameFI.size ());
		x = 0;
		ITERATE (int_set_t, setPredicateNameFI, ite)
			pProblem->vec_InitPredicateNameFI [x++] = *ite;

		pProblem->vec_InitParameterValueFI.Create (setParameterValueFI.size ());
		x = 0;
		ITERATE (int_set_t, setParameterValueFI, ite)
			pProblem->vec_InitParameterValueFI [x++] = *ite;


		// goal state ...		
		setPredicateIdentityFI.clear ();
		setPredicateNameFI.clear ();
		setParameterValueFI.clear ();
		
		ITERATE (PddlPredicate_dq_t, rPddlProblem.o_PartialGoalState.dq_Predicates, ite)
		{
			PddlPredicate* pPredicate = *ite;

			// assign predicate candidate index ...	
			pPredicate->i_PredicateCandidateIndex = FindPredicateCandidateIndex (*pPredicate);
			if (-1 == pPredicate->i_PredicateCandidateIndex)
				setMissingTargetPredicates.insert (pPredicate->GetPddlString ());

			// assign feature indices to predicate	
			pPredicate->i_PredicateIdentityFeatureIndex
				= GetPredicateIdentityFeatureIndex (pPredicate->GetPddlString ());
			pPredicate->i_PredicateNameFeatureIndex
				= GetPredicateNameFeatureIndex (pPredicate->s_Name);
			pPredicate->i_PredicateCandidateWithoutNumber
				= GetPredicateWithoutNumberIndex (*pPredicate);

			int_set_t setValueFI;
			CONST_ITERATE (PddlParameter_dq_t, pPredicate->dq_Parameters, iteParam)
				setValueFI.insert (GetParameterValueFeatureIndex (*iteParam->p_ResolvedValue));

			pPredicate->vec_ParameterValueFeatureIndex.Create (setValueFI.size ());
			int x = 0;
			ITERATE (int_set_t, setValueFI, iteFI)
				pPredicate->vec_ParameterValueFeatureIndex [x++] = *iteFI;

			// collect feature indicies for problem	
			setPredicateIdentityFI.insert (pPredicate->i_PredicateIdentityFeatureIndex);
			setPredicateNameFI.insert (pPredicate->i_PredicateNameFeatureIndex);
			setParameterValueFI.insert (setValueFI.begin (), setValueFI.end ());
		}

		// assign target feature indices to problem	
		pProblem->vec_TargetPredicateIdentityFI.Create (setPredicateIdentityFI.size ());
		x = 0;
		ITERATE (int_set_t, setPredicateIdentityFI, ite)
			pProblem->vec_TargetPredicateIdentityFI [x++] = *ite;

		pProblem->vec_TargetPredicateNameFI.Create (setPredicateNameFI.size ());
		x = 0;
		ITERATE (int_set_t, setPredicateNameFI, ite)
			pProblem->vec_TargetPredicateNameFI [x++] = *ite;

		pProblem->vec_TargetParameterValueFI.Create (setParameterValueFI.size ());
		x = 0;
		ITERATE (int_set_t, setParameterValueFI, ite)
			pProblem->vec_TargetParameterValueFI [x++] = *ite;
	}

	cout << "   " << setMissingInitPredicates.size ()
		 << " init predicates not present in candidate list." << endl;
	cout << "   " << setMissingTargetPredicates.size ()
		 << " target predicates not present in candidate list." << endl;
}


//													
void SubgoalPolicy::LoadGoldLengthFile(void)
{
	String sGoldLengthFile = (config)"gold_length_file";
	// read in the dict file
	String_dq_t dqLines;
	File::ReadLines (sGoldLengthFile, dqLines);

	ITERATE (String_dq_t, dqLines, iterLine)
	{
		// Problem | length
    		String_dq_t dqSplit;
    		// read in the dict file
		iterLine->Split (dqSplit, '|');
		assert (dqSplit.size () == 2);
		String sProblem = dqSplit[0];
		int iLength = dqSplit[1];
		this->map_ProblemToGoldLength[sProblem] = iLength;
	}

	cout << "   loaded " << this->map_ProblemToGoldLength.size()
		 << " gold lengths " << endl;
}


//													
bool SubgoalPolicy::LoadPredDictFile (void)
{
  String sPddlDictFile;
  int object_questions = (config) "ir:object-questions";
  int action_questions = (config) "ir:action-questions";

  // Read the config to find which question-predicates to include
	if(object_questions == 1 && action_questions == 1)
	{
		sPddlDictFile = (config)"pddl_dict_question_objectsActions_file";
	}
	else if (object_questions == 1 && action_questions != 1)
	{
	 	sPddlDictFile = (config)"pddl_dict_question_objects_file";
	}
	else if (object_questions != 1 && action_questions == 1)
	{
		sPddlDictFile = (config)"pddl_dict_question_actions_file";
	}
	else
	{
		sPddlDictFile = (config)"pddl_dict_file";
	}

  cout << "    loading dict: " << sPddlDictFile << endl;

	String_dq_t dqLines;
	if (false == File::ReadLines (sPddlDictFile, dqLines))
	{
		cerr << "[ERROR] Failed to read predicate dictionary file." << endl;
		return false;
	}

	i_MaxPredicateValue = 0;
	vec_CandidatePredicates.reserve (dqLines.size ());
	ITERATE (String_dq_t, dqLines, iterLine)
	{
		// id | 0/1 predicate/function | name	
		String_dq_t dqSplit;
		iterLine->Split (dqSplit, '|');
		assert (dqSplit.size () == 3);
		int iIndex = dqSplit [0];
		int iValue = (int)dqSplit [1];
		bool bIsFunction = (iValue > 0);
		String sPredicate = dqSplit[2];
		sPredicate.Strip ();

		String_dq_t dqPred;
		sPredicate.Split (dqPred, ' ');

		PddlPredicate* pPred;
		if (true == bIsFunction)
			pPred = new PddlFunctionValuePredicate;
		else
			pPred = new PddlPredicate;

		pPred->i_PredicateCandidateIndex = iIndex;
		pPred->s_Name = dqPred [0];
		pPred->b_IsFunction = bIsFunction;
		pPred->l_Value = iValue;

		if (true == bIsFunction)
		{
			pPred->l_Value --;
			((PddlFunctionValuePredicate*)pPred)->c_Operator = '>';
			if (i_MaxPredicateValue < pPred->l_Value)
				i_MaxPredicateValue = pPred->l_Value;
		}

		int_set_t setValueFI;
		for (unsigned int i = 1; i < dqPred.size (); i++)
		{
			pPred->dq_Parameters.push_back (PddlParameter());
			pPred->dq_Parameters [i-1].SetValue (dqPred [i]);
			setValueFI.insert (GetParameterValueFeatureIndex (dqPred [i]));
		}
		pPred->vec_ParameterValueFeatureIndex.Create (setValueFI.size ());
		int x = 0;
		ITERATE (int_set_t, setValueFI, iteFI)
			pPred->vec_ParameterValueFeatureIndex [x++] = *iteFI;

		assert ((long) vec_CandidatePredicates.size () == iIndex);
		vec_CandidatePredicates.push_back (pPred);

		String sPddlString (pPred->GetPddlString ());
		pair <PddlStringToPredicate_map_t::iterator, bool> pairInsert;
		pairInsert = map_PddlStringToCandidatePredicate.insert (make_pair (sPddlString, pPred));
		if (false == pairInsert.second)
		{
			cerr << "[ERROR] Duplicate predicate in candidate dictionary?\n"
				 << sPddlString << endl;
		}

		pPred->i_PredicateIdentityFeatureIndex
			= GetPredicateIdentityFeatureIndex (pPred->GetPddlString ());
		pPred->i_PredicateNameFeatureIndex
			= GetPredicateNameFeatureIndex (pPred->s_Name);
		pPred->i_PredicateCandidateWithoutNumber
			= GetPredicateWithoutNumberIndex (*pPred);


		if (true == pPred->b_IsFunction)
		{
			PddlFunctionValuePredicate* pClone = (PddlFunctionValuePredicate*)pPred->Clone ();
			pClone->c_Operator = '=';
			++ pClone->l_Value;

			map_PddlStringToCandidatePredicate [pClone->GetPddlString ()] = pPred;
			delete pClone;
		}
	}

	// '0' is a valid predicate value, so we need to add 1 here...	
	++ i_MaxPredicateValue;

	i_CandidatePredicates = vec_CandidatePredicates.size ();
	vec_CanReachCandidatePredicate.resize (i_CandidatePredicates, 0);

	i_CandidatePredicateNumbersMerged = hmp_PredicateWithoutNumberToIndex.size ();

	// compute reachability predicate equivalents...				
	vector <int_set_t>	vecReachabilityEquivalents;
	vecReachabilityEquivalents.resize (i_CandidatePredicates);
	for (int i = 0; i < i_CandidatePredicates; ++ i)
	{
		PddlPredicate* pPred = vec_CandidatePredicates [i];
		if (false == pPred->b_IsFunction)
			continue;

		PddlFunctionValuePredicate* pClone = (PddlFunctionValuePredicate*)pPred->Clone ();
		pClone->l_Value = 0;

		PddlPredicate* pEquivalent = FindEquivalentPredicateCandidate (*pClone);
		delete pClone;
		if (NULL == pEquivalent)
		{
			cerr << "[ERROR] Predicate candidate with numeric value 0 not found: "
				 << pClone->GetPddlString () << endl;
			abort ();
		}

		vecReachabilityEquivalents [pEquivalent->i_PredicateCandidateIndex].insert (pPred->i_PredicateCandidateIndex);
	}


	for (int i = 0; i < i_CandidatePredicates; ++ i)
	{
		ITERATE (int_set_t, vecReachabilityEquivalents [i], ite)
		{
			vecReachabilityEquivalents [*ite].insert (i);
			ITERATE (int_set_t, vecReachabilityEquivalents [i], iteOther)
				vecReachabilityEquivalents [*ite].insert (*iteOther);
		}
	}

	vec_ReachabilityPredicateEqulivalents.resize (i_CandidatePredicates);
	for (int i = 0; i < i_CandidatePredicates; ++ i)
	{
		ITERATE (int_set_t, vecReachabilityEquivalents [i], ite)
			vec_ReachabilityPredicateEqulivalents [i].push_back (*ite);
	}

	mtx_PredicateConnectionsFromTo.Create (i_CandidatePredicates,
										   i_CandidatePredicates);
	mtx_PredicateConnectionsFromTo.Memset (0);
	mtx_PredicateConnectionsToFrom.Create (i_CandidatePredicates,
										   i_CandidatePredicates);
	mtx_PredicateConnectionsToFrom.Memset (0);


	cout << "   loaded " << i_CandidatePredicates
		 << " candidate predicates.  Max value of "
		 << i_MaxPredicateValue << endl;

	return true;
}


//													
bool SubgoalPolicy::LoadSimpleConnectionFile (void)
{
	i_MaxConnectionDepth = 0;
	cout << "   loading simple connection file: "
		 << (config)"pddl_connection_file" << endl;

	String_dq_t dqLines;
	if (false == File::ReadLines ((config)"pddl_connection_file", dqLines))
	{
		cerr << "[ERROR] Failed to open connection file." << endl;
		return false;
	}
	ITERATE(String_dq_t, dqLines, ite)
	{
		String_dq_t dqSplit;
		ite->Split(dqSplit, '|');

		assert(dqSplit.size() >= 3);
		int iDepth = dqSplit[0];
		int iFrom = dqSplit[1];
		int iTo = dqSplit[2];
		mtx_PredicateConnectionsFromTo (iFrom, iTo) = iDepth;
		mtx_PredicateConnectionsToFrom (iTo, iFrom) = iDepth;

		if (i_MaxConnectionDepth < iDepth)
			i_MaxConnectionDepth = iDepth;
	}
	cout << "   loaded " << dqLines.size ()
		 << " pddl relationships, with max depth "
		 << i_MaxConnectionDepth << endl;

	return true;
}


//													
bool SubgoalPolicy::LoadFeatureConnectionFile (void)
{
	i_MaxConnectionDepth = 0;
	cout << "   loading feature connection file : "
		 << (config)"text_connection_file" << endl;

	ConnectionHashToFeatures_map_t	mapConnectionHashToFeatures;

	//													
	File file;
	if (false == file.Open ((config)"text_connection_file"))
	{
		cerr << "[ERROR] Failed open connection file." << endl;
		return false;
	}

	size_t iLines = 0;
	String sLine;
	while (true == file.ReadLine (sLine))
	{
		++ iLines;
		String_dq_t dqSplit;
		sLine.Split(dqSplit, '|');

		assert(dqSplit.size() >= 5);
		String sFeature = dqSplit [0];
		float fFeatureValue = (double) dqSplit [1];
		int iFrom = dqSplit [2];
		int iTo = dqSplit [3];
		int iSentenceId = dqSplit [4];

		String sHash;
		sHash << iFrom << '|' << iTo << '|' << iSentenceId;
		FeatureToValue_map_t* pmapFeatureToValuePos;
		// FeatureToValue_map_t* pmapFeatureToValueNeg;
		ConnectionHashToFeatures_map_t::iterator	iteFeatures;
		iteFeatures = mapConnectionHashToFeatures.find (sHash);
		if (mapConnectionHashToFeatures.end () == iteFeatures)
		{
			SentenceConnection* pConnection = new SentenceConnection;
			vec_SentenceConnections.push_back (pConnection);
			pConnection->i_Sentence = iSentenceId;
			pConnection->i_From = iFrom;
			pConnection->i_To = iTo;

			pmapFeatureToValuePos = new FeatureToValue_map_t;
			// pmapFeatureToValueNeg = new FeatureToValue_map_t;
			mapConnectionHashToFeatures.insert (make_pair (sHash, pmapFeatureToValuePos));
		}
		else
		{
			pmapFeatureToValuePos = iteFeatures->second;
			// pmapFeatureToValuePos = iteFeatures->second.first;
			// pmapFeatureToValueNeg = iteFeatures->second.second;
		}

		// String sPositiveFeature;
		// sPositiveFeature << "pos\x01" << sFeature;
		int iFeature = o_TextConnectionFeatureSpace.GetFeatureIndex (sFeature);
		pmapFeatureToValuePos->insert (make_pair (iFeature, fFeatureValue));

		// String sNegativeFeature;
		// sNegativeFeature << "neg\x01" << sFeature;
		// int iNegativeFeature = o_TextConnectionFeatureSpace.GetFeatureIndex (sNegativeFeature);
		// pmapFeatureToValueNeg->insert (make_pair (iNegativeFeature, fFeatureValue));
	}


	//													
	mtx_SentencesPositiveFromTo.Create (i_CandidatePredicateNumbersMerged, i_CandidatePredicateNumbersMerged);
	mtx_SentencesPositiveFromTo.Memset (0);
	mtx_SentencesNegativeFromTo.Create (i_CandidatePredicateNumbersMerged, i_CandidatePredicateNumbersMerged);
	mtx_SentencesNegativeFromTo.Memset (0);

	ITERATE (SentenceConnection_vec_t, vec_SentenceConnections, iteConn)
	{
		SentenceConnection* pConnection = *iteConn;
		pConnection->p_PositiveFeatures = new Features;
		pConnection->p_NegativeFeatures = new Features;

		String sHash;
		sHash << pConnection->i_From << '|'
			  << pConnection->i_To << '|'
			  << pConnection->i_Sentence;

		ConnectionHashToFeatures_map_t::iterator	iteFeatures;
		iteFeatures = mapConnectionHashToFeatures.find (sHash);
		assert (mapConnectionHashToFeatures.end () != iteFeatures);

		FeatureToValue_map_t* pmapFeatureToValuePos = iteFeatures->second;
		pConnection->p_PositiveFeatures->SetSize (pmapFeatureToValuePos->size ());
		pConnection->p_NegativeFeatures->SetSize (pmapFeatureToValuePos->size ());
		ITERATE (FeatureToValue_map_t, (*pmapFeatureToValuePos), ite)
		{
			pConnection->p_PositiveFeatures->Set (ite->first, ite->second);
			pConnection->p_NegativeFeatures->Set (ite->first, - ite->second);
		}

		// FeatureToValue_map_t* pmapFeatureToValueNeg = iteFeatures->second.second;
		// pConnection->p_NegativeFeatures->SetSize (pmapFeatureToValueNeg->size ());
		// ITERATE (FeatureToValue_map_t, (*pmapFeatureToValueNeg), ite)
		//	pConnection->p_NegativeFeatures->Set (ite->first, ite->second);

		delete pmapFeatureToValuePos;
		// delete pmapFeatureToValueNeg;

		PddlPredicate* pFrom = vec_CandidatePredicates [pConnection->i_From];
		int iFrom = pFrom->i_PredicateCandidateWithoutNumber;
		PddlPredicate* pTo = vec_CandidatePredicates [pConnection->i_To];
		int iTo = pTo->i_PredicateCandidateWithoutNumber;

		if (NULL == mtx_SentencesPositiveFromTo (iFrom, iTo))
			mtx_SentencesPositiveFromTo (iFrom, iTo) = new int_dq_t;
		if (NULL == mtx_SentencesNegativeFromTo (iFrom, iTo))
			mtx_SentencesNegativeFromTo (iFrom, iTo) = new int_dq_t;
	}
	mapConnectionHashToFeatures.clear ();

	lprb_SentenceConnection.Create (2);
	mtx_FeedbackOnSentenceConnections.Create (i_CandidatePredicateNumbersMerged,
											  i_CandidatePredicateNumbersMerged,
											  3);
	mtx_FeedbackOnSentenceConnections.Memset (0);


	cout << "   loaded " << vec_SentenceConnections.size ()
		 << " text relationships, and " << iLines
		 << " features for an average feature size of "
		 << iLines / (float)vec_SentenceConnections.size () << endl;

	return true;
}


//													
void SubgoalPolicy::ComputeSequenceEndFeatures (int _iIndex,
												const Problem& _rProblem,
												SubgoalSequence* _pSequence)
{
	// features look at last subgoal & init state.
	// [predicate identity]^2	
	// [connections]
	Subgoal* pSubgoal = _pSequence->GetSubgoal (_iIndex);
	pSubgoal->vec_SequenceEndFeatureVectors.resize (2);

	// all features are computed by comparing the 
	// next subgoal in the sequence with the init 
	// state...									  
	Subgoal* pNextSubgoal = _pSequence->GetSubgoal (_iIndex + 1);
	assert (NULL != pNextSubgoal);


	for (int e = 0; e < 2; ++ e)
	{
		Features* pFeatures = new Features;
		pSubgoal->vec_SequenceEndFeatureVectors [e] = pFeatures;

		size_t iFeatureCount = _rProblem.vec_InitPredicateIdentityFI.Size ();
		pFeatures->SetSize (iFeatureCount);
		// pFeatures->SetSize (1);

		// predicate identity...	
		size_t iOffset = pNextSubgoal->p_PddlSubgoalPredicate->i_PredicateIdentityFeatureIndex
						 * 2 * i_PredicateIdentities
						 + e * i_PredicateIdentities;
		SetFeatures (_rProblem.vec_InitPredicateIdentityFI,
					 iOffset,
					 pFeatures);
		/*
		size_t iOffset = pNextSubgoal->p_PddlSubgoalPredicate->i_PredicateIdentityFeatureIndex
						 + e * i_PredicateIdentities;
		pFeatures->Set (iOffset, 1);
		*/

		// connections ...			
		// [SB] I'm not sure connection features	
		// are good to have here.  We're assuming	
		// that connection features will encode		
		// long distance relationships, whereas		
		// predicting sequence-end requires short	
		// distance relationships...				
	}
}


//													
void SubgoalPolicy::ComputeSubgoalFeatures (int _iIndex,
											const Problem& _rProblem,
											SubgoalSequence* _pSequence)
{
	PddlProblem& rPddlProblem = ((Problem&)_rProblem).GetPddlProblem ();
	Subgoal* pSubgoal = _pSequence->GetSubgoal (_iIndex);
	pSubgoal->vec_SubgoalFeatureVectors.resize (i_CandidatePredicates);

	int iSubgoals = (int)_pSequence->dq_Subgoals.size ();
	// include the target 
	bool bIncludeTarget = (!b_UseOnlyPreviousSubgoal || (_iIndex == iSubgoals-1));
	size_t iEndSubgoal = b_UseOnlyPreviousSubgoal ? min(iSubgoals,_iIndex+2) : iSubgoals;


	float fDistanceFactorToTarget = DistanceScore (_pSequence->Length () - _iIndex);
	for (int c = 0; c < i_CandidatePredicates; ++ c)
	{
		const PddlPredicate* pCandidatePredicate = vec_CandidatePredicates [c];
		int iReachableSubgoal = 0;
		if ((true == b_UseReachableSubgoalFeature) &&
			(true == b_UseComplexNonConnectionFeatures))
			iReachableSubgoal = (int) vec_CanReachCandidatePredicate [c];
		Features* pFeatures = new Features;
		pSubgoal->vec_SubgoalFeatureVectors [c] = pFeatures;

		int iCandidatePredicateParameters
			= pCandidatePredicate->vec_ParameterValueFeatureIndex.Size ();


		// set feature vector size ...		
		size_t iFeatureCount = 2;
		if (0 != f_NonConnectionFeatureImportance)
		{
			iFeatureCount += _rProblem.vec_InitPredicateNameFI.Size ()
							 + _rProblem.vec_TargetPredicateNameFI.Size ()
							 + _rProblem.vec_InitPredicateIdentityFI.Size ()
							 + _rProblem.vec_TargetPredicateIdentityFI.Size ()
							 + iCandidatePredicateParameters
								* (_rProblem.vec_InitParameterValueFI.Size ()
									+ _rProblem.vec_TargetParameterValueFI.Size ());

			for (size_t i = _iIndex + 1; i < _pSequence->dq_Subgoals.size (); ++ i)
			{
				Subgoal& rSubgoal = _pSequence->dq_Subgoals [i];
				PddlPredicate* pSubgoalPredicate = rSubgoal.p_PddlSubgoalPredicate;
				iFeatureCount += 2 + pSubgoalPredicate->vec_ParameterValueFeatureIndex.Size ();
			}
		}


		//									
		iFeatureCount += 4;
		pFeatures->SetSize (iFeatureCount);



		// predicate numerics feature...
		if ((true == b_UsePredicateValueFeature) &&
			(true == b_UseComplexNonConnectionFeatures))
		{
			assert (pCandidatePredicate->l_Value >= 0);
			// pFeatures->Set (0, 0.1 * pCandidatePredicate->l_Value);
			// pFeatures->Set (pCandidatePredicate->l_Value, 0.01);
		}
		// pFeatures->Set (1 + i_OffsetToConnectionFeatures, iReachableSubgoal);


		// features to init & target ...	
		if (0 != f_NonConnectionFeatureImportance)
		{
			// predicate name...	
			size_t iOffset = i_OffsetToPredicateNameFeatures
							 + pCandidatePredicate->i_PredicateNameFeatureIndex
							 * 2 * i_PredicateNames;
			if(true == b_IncludeInit)
			{
				SetFeatures (_rProblem.vec_InitPredicateNameFI,
							 iOffset,
							 pFeatures,
							 f_NonConnectionFeatureImportance);
			}
			if (true == bIncludeTarget)
			{
				SetFeatures (_rProblem.vec_TargetPredicateNameFI,
							 iOffset + i_PredicateNames,
							 pFeatures,
							 fDistanceFactorToTarget * f_NonConnectionFeatureImportance);
			}

			// predicate identity...
			iOffset = i_OffsetToPredicateIdentityFeatures
					  + pCandidatePredicate->i_PredicateIdentityFeatureIndex
					  * 2 * i_PredicateIdentities;
			if(true == b_IncludeInit)
			{
				SetFeatures (_rProblem.vec_InitPredicateIdentityFI,
							 iOffset,
							 pFeatures,
							 f_PredicateIdentityPairFeatureWeight
							 * f_NonConnectionFeatureImportance);
			}
			if (true == bIncludeTarget)
			{
				SetFeatures (_rProblem.vec_TargetPredicateIdentityFI,
							 iOffset + i_PredicateIdentities,
							 pFeatures,
							 f_PredicateIdentityPairFeatureWeight
							 	 * fDistanceFactorToTarget
							 	 * f_NonConnectionFeatureImportance);
			}

			// parameter values...	
			for (int v = 0; v < iCandidatePredicateParameters; ++ v)
			{
				iOffset = i_OffsetToParameterValueFeatures
						  + pCandidatePredicate->vec_ParameterValueFeatureIndex [v]
						  * 2 * i_ParameterValues;
				if(true == b_IncludeInit)
				{
					SetFeatures (_rProblem.vec_InitParameterValueFI,
								 iOffset,
								 pFeatures,
								 f_NonConnectionFeatureImportance);
				}

				if (true == bIncludeTarget)
				{
					SetFeatures (_rProblem.vec_TargetParameterValueFI,
								 iOffset + i_ParameterValues,
								 pFeatures,
								 fDistanceFactorToTarget * f_NonConnectionFeatureImportance);
				}
			}


			// features to other subgoals ...	
			for (size_t i = _iIndex + 1; i < iEndSubgoal; ++ i)
			{
				Subgoal& rSubgoal = _pSequence->dq_Subgoals [i];
				PddlPredicate* pSubgoalPredicate = rSubgoal.p_PddlSubgoalPredicate;
				float fDistanceFactor = f_NonConnectionFeatureImportance * DistanceScore (i - _iIndex);

				// predicate name...	
				iOffset = i_OffsetToPredicateNameFeatures
						  + pCandidatePredicate->i_PredicateNameFeatureIndex
						  * 2 * i_PredicateNames + i_PredicateNames;
				pFeatures->Set (iOffset + pSubgoalPredicate->i_PredicateNameFeatureIndex, 
								fDistanceFactor,
								false);

				// predicate identity...
				iOffset = i_OffsetToPredicateIdentityFeatures
						  + pCandidatePredicate->i_PredicateIdentityFeatureIndex
						  * 2 * i_PredicateIdentities + i_PredicateIdentities;
				pFeatures->Set (iOffset + pSubgoalPredicate->i_PredicateIdentityFeatureIndex,
								f_PredicateIdentityPairFeatureWeight * fDistanceFactor,
								false);

				// parameter values...	
				for (int v = 0; v < iCandidatePredicateParameters; ++ v)
				{
					iOffset = i_OffsetToParameterValueFeatures
							  + pCandidatePredicate->vec_ParameterValueFeatureIndex [v]
							  * 2 * i_ParameterValues + i_ParameterValues;

					SetFeatures (pSubgoalPredicate->vec_ParameterValueFeatureIndex,
								 iOffset,
								 pFeatures,
								 fDistanceFactor,
								 false);
				}
			}
		}

		// connection features ...			
		if ((true == b_UseSimpleConnectionFeatures) ||
			(true == b_UseTextConnectionFeatures))
		{
			if(true == b_IncludeInit)
			{
				bool bHaveConnToInit = false;
				// connection distance to init state.
				Matrix <char,1> mtxSliceFrom;
				mtxSliceFrom.GetSlice (mtx_PredicateConnectionsToFrom,
									   pCandidatePredicate->i_PredicateCandidateIndex);

				CONST_ITERATE (PddlPredicate_dq_t, rPddlProblem.o_StartState.dq_Predicates, ite)
				{
					PddlPredicate* pInitPredicate = *ite;
					if (-1 == pInitPredicate->i_PredicateCandidateIndex)
						continue;
					if (0 == mtxSliceFrom (pInitPredicate->i_PredicateCandidateIndex))
						continue;
					
					pFeatures->Set (2 + i_OffsetToConnectionFeatures, 1);
					pFeatures->Set (3 + i_OffsetToConnectionFeatures, iReachableSubgoal);
					bHaveConnToInit = true;
					break;
				}

				if (false == bHaveConnToInit)
					pFeatures->Set (4 + i_OffsetToConnectionFeatures, 1);
			}


			// connection distance to target state.
			Matrix <char,1> mtxSliceTo;
			mtxSliceTo.GetSlice (mtx_PredicateConnectionsFromTo,
								 pCandidatePredicate->i_PredicateCandidateIndex);

			if (true == bIncludeTarget)
			{
				CONST_ITERATE (PddlPredicate_dq_t, rPddlProblem.o_PartialGoalState.dq_Predicates, ite)
				{
					PddlPredicate* pGoalPredicate = *ite;
					if (-1 == pGoalPredicate->i_PredicateCandidateIndex)
						continue;
					if (0 == mtxSliceTo (pGoalPredicate->i_PredicateCandidateIndex))
						continue;
					// The -1 below is to account for the fact that 	
					// iSubgoals is the length of the list, and _iIndex	
					// is zero indexed...								
					int iDistance = iSubgoals - _iIndex - 1;
					if (iDistance < 3)
					{
						size_t iOffset = 2 * (iDistance - 1) + i_OffsetToConnectionFeatures;
						pFeatures->Set (5 + iOffset, 1);
						pFeatures->Set (6 + iOffset, iReachableSubgoal);
					}
					break;
				}
			}


			// connection distance to future subgoals.
			bool bHaveConnToFuture = false;
			for (size_t s = _iIndex + 1; s < iEndSubgoal; ++ s)
			{
				Subgoal* pNextSubgoal = _pSequence->GetSubgoal (s);
				int iNextPredicate = pNextSubgoal->p_PddlSubgoalPredicate->i_PredicateCandidateIndex;
				if (0 == mtxSliceTo (iNextPredicate))
					continue;
				int iDistance = s - _iIndex;
				if (iDistance > 2)
					break;

				size_t iOffset = 2 * (iDistance - 1) + i_OffsetToConnectionFeatures;
				pFeatures->Set (5 + iOffset, 1, false);
				pFeatures->Set (6 + iOffset, iReachableSubgoal, false);
				bHaveConnToFuture = true;
			}

			if (false == bHaveConnToFuture)
				pFeatures->Set (13 + i_OffsetToConnectionFeatures, 1);
		}
	}
}



//													
void SubgoalPolicy::SampleExplorationParameters (void)
{
	cout << "   se ["
		 << o_SequenceEndExploration.SampleParameters (o_Sample)
		 << "]  ";
	cout << "sg ["
		 << o_SubgoalExploration.SampleParameters (o_Sample)
		 << "]  ";
	cout << "cn ["
		 << o_ConnectionExploration.SampleParameters (o_Sample)
		 << "]";
	cout << endl;
}


//													
void SubgoalPolicy::ForceConnectionUseFlags (void)
{
	if (f_UseSimpleConnectionFeatures > 0)
		b_UseSimpleConnectionFeatures = true;
	if (f_UseTextConnectionFeatures > 0)
		b_UseTextConnectionFeatures = true;
	if (f_UseComplexNonConnectionFeatures > 0)
		b_UseComplexNonConnectionFeatures = true;
}


//													
void SubgoalPolicy::SampleConnectionUseFlags (void)
{
	b_UseSimpleConnectionFeatures = false;
	if (f_UseSimpleConnectionFeatures > 0)
		b_UseSimpleConnectionFeatures
			= (o_Sample.SampleUniform () < f_UseSimpleConnectionFeatures);

	b_UseTextConnectionFeatures = false;
	if (f_UseTextConnectionFeatures > 0)
		b_UseTextConnectionFeatures
			= (o_Sample.SampleUniform () < f_UseTextConnectionFeatures);

	b_UseComplexNonConnectionFeatures = false;
	if (f_UseComplexNonConnectionFeatures > 0)
		b_UseComplexNonConnectionFeatures
			= (o_Sample.SampleUniform () < f_UseComplexNonConnectionFeatures);
}


//													
size_t SubgoalPolicy::SampleDecision (LogProbability& _rLogProb,
									  ExplorationParameters& _rExploration,
									  bool _bTestMode)
{
	if (true == _bTestMode)
		return o_Sample.Argmax (_rLogProb.GetData (), _rLogProb.Size ());


	// epsilon-softmax 	
	if (et_epsilon_softmax == _rExploration.e_ExplorationType)
	{
		if (o_Sample.SampleUniform () < _rExploration.f_Epsilon)
			return o_Sample.SampleFromLogPDF (_rLogProb.GetData (),
											  _rLogProb.Size (),
											  _rExploration.f_Beta);
		return o_Sample.Argmax (_rLogProb.GetData (), _rLogProb.Size ());
	}
	// epsilon-greedy	
	if (et_epsilon_greedy == _rExploration.e_ExplorationType)
	{
		if (o_Sample.SampleUniform () < _rExploration.f_Epsilon)
			return o_Sample.SampleUniformCategorical (_rLogProb.Size ());
		return o_Sample.Argmax (_rLogProb.GetData (), _rLogProb.Size ());
	}
	// softmax			
	return o_Sample.SampleFromLogPDF (_rLogProb.GetData (),
									  _rLogProb.Size (),
									  _rExploration.f_Beta);
}


//													
size_t SubgoalPolicy::SampleSequenceEnd (int _iSubgoalIndex,
										 const Problem& _rProblem,
										 LogProbability& _rLogProb,
										 bool _bTestMode)
{
	if (true == b_UseGoldLength)
	{
		String_int_map_t::iterator	iteLen;
		iteLen = map_ProblemToGoldLength.find (_rProblem.s_FileName);
		if (map_ProblemToGoldLength.end () == iteLen)
		{
			cerr << "[ERROR] Was told to use gold solution lengths, "
					"but length not known for problem '"
				 << _rProblem.s_FileName << "'." << endl;
		}

		return (_iSubgoalIndex >= iteLen->second)? SEQUENCE_END : 0;      
	}

	return SampleDecision (_rLogProb, o_SequenceEndExploration, _bTestMode);
}


//													
void SubgoalPolicy::SampleZeroSubgoalSequence (const Problem& _rProblem,
											   SubgoalSequence* _pSequence)
{
	// this vector is an intermediate structure used for feature	
	// computation, and needs to be cleared for each sequence...	
	_pSequence->vec_PredicatesInSequence.resize (i_CandidatePredicates, 0);

	_pSequence->b_UseSimpleConnectionFeatures = b_UseSimpleConnectionFeatures;
	_pSequence->b_UseTextConnectionFeatures = b_UseTextConnectionFeatures;
	_pSequence->b_UseComplexNonConnectionFeatures = b_UseComplexNonConnectionFeatures;

	AddLastSubgoal (_rProblem, _pSequence);
	AddForcedSequenceEnd (_rProblem, _pSequence);
}


//													
void SubgoalPolicy::SampleConnections (bool _bTestMode)
{
	if (f_UseTextConnectionFeatures <= 0)
		return;

	for (int f = 0; f < i_CandidatePredicateNumbersMerged; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicateNumbersMerged; ++ t)
		{
			int_dq_t* pdqConnectionHit = mtx_SentencesPositiveFromTo (f, t);
			if (NULL != pdqConnectionHit)
				pdqConnectionHit->clear ();
			pdqConnectionHit = mtx_SentencesNegativeFromTo (f, t);
			if (NULL != pdqConnectionHit)
				pdqConnectionHit->clear ();
		}
	}

	mtx_PredicateConnectionsFromTo.Memset (0);
	mtx_PredicateConnectionsToFrom.Memset (0);

	int iPositives = 0;
	int iNegatives = 0;
	for (size_t i = 0; i < vec_SentenceConnections.size (); ++ i)
	{
		SentenceConnection* pConnection = vec_SentenceConnections [i];
		lprb_SentenceConnection [0]
			= o_TextConnectionModel.ComputeLogProb (*pConnection->p_NegativeFeatures);
		lprb_SentenceConnection [1]
			= o_TextConnectionModel.ComputeLogProb (*pConnection->p_PositiveFeatures);

		PddlPredicate* pPddlFrom = vec_CandidatePredicates [pConnection->i_From];
		PddlPredicate* pPddlTo = vec_CandidatePredicates [pConnection->i_To];
		int iPddlFrom = pPddlFrom->i_PredicateCandidateWithoutNumber;
		int iPddlTo = pPddlTo->i_PredicateCandidateWithoutNumber;

		if (0 == SampleDecision (lprb_SentenceConnection,
								 o_ConnectionExploration,
								 _bTestMode))
		{
			++ iNegatives;
			int_dq_t* pdqConnectionHit
				= mtx_SentencesNegativeFromTo (iPddlFrom, iPddlTo);
			if (NULL != pdqConnectionHit)
				pdqConnectionHit->push_back (i);
			continue;
		}
		++ iPositives;

		// remember which connections are sampled,	
		// and also from which sentences...			

		mtx_PredicateConnectionsFromTo (pConnection->i_From, pConnection->i_To) = 1;
		mtx_PredicateConnectionsToFrom (pConnection->i_To, pConnection->i_From) = 1;

		int_dq_t* pdqConnectionHit
			= mtx_SentencesPositiveFromTo (iPddlFrom, iPddlTo);
		if (NULL != pdqConnectionHit)
			pdqConnectionHit->push_back (i);
	}

	cout << "   +" << iPositives << "  -" << iNegatives << endl;
	if (true == b_LogConnectionPredictions)
		WriteConnectionPredictions ();
}


void SubgoalPolicy::SampleSubgoalSequence (const Problem& _rProblem,
										   bool _bTestMode,
										   SubgoalSequence* _pSequence)
{
	// Sample sequence length...	
	assert (0 != i_CandidatePredicates);
	_pSequence->vec_PredicatesInSequence.resize (i_CandidatePredicates, 0);

	_pSequence->b_UseSimpleConnectionFeatures = b_UseSimpleConnectionFeatures;
	_pSequence->b_UseTextConnectionFeatures = b_UseTextConnectionFeatures;
	_pSequence->b_UseComplexNonConnectionFeatures = b_UseComplexNonConnectionFeatures;


	// we first need the last subgoal to reach the actual target goal...
	AddLastSubgoal (_rProblem, _pSequence);

	// Sample subgoals...			
	bool bAlreadyAddedSequenceEnd = false;
	Subgoal* pNextSubgoal = _pSequence->GetSubgoal (0);
	for (int i = 0; i < i_MaxSequenceLength; ++ i)
	{
		Subgoal* pSubgoal = _pSequence->AddSubgoalToFront ();

		// sample END-SEQUENCE symbol...	
		assert (true == pSubgoal->vec_SequenceEndFeatureVectors.empty ());
		ComputeSequenceEndFeatures (0, _rProblem, _pSequence);
		pSubgoal->lprb_SequenceEnd.Create (2);
		for (int e = 0; e < 2; ++ e)
		{
			Features* pFV = pSubgoal->vec_SequenceEndFeatureVectors [e];
			pSubgoal->lprb_SequenceEnd [e] = o_SequenceEndModel.ComputeLogProb (*pFV);
			delete pFV;
		}
		pSubgoal->vec_SequenceEndFeatureVectors.clear ();
		pSubgoal->i_SequenceEnd = SampleSequenceEnd (i,
													 _rProblem,
													 pSubgoal->lprb_SequenceEnd,
													 _bTestMode);
		if (SEQUENCE_END == pSubgoal->i_SequenceEnd)
		{
			bAlreadyAddedSequenceEnd = true;
			break;
		}


		assert (true == pSubgoal->vec_SubgoalFeatureVectors.empty ());
		ComputeSubgoalFeatures (0, _rProblem, _pSequence);

		// compute log probs	
		pSubgoal->lprb_Subgoal.Create (i_CandidatePredicates);
		for (long g = 0; g < i_CandidatePredicates; ++ g)
		{
			Features* pFV = pSubgoal->vec_SubgoalFeatureVectors [g];

			// check if this is identical to the next subgoal...
			if ((NULL != pNextSubgoal) &&
				(g == pNextSubgoal->i_SubgoalSelection))
				pSubgoal->lprb_Subgoal [g] = -1000;

			// check if this is identical to any future subgoal	
			else if ((true == b_DisallowAnyDuplicateSubgoals) &&
					 (1 == _pSequence->vec_PredicatesInSequence [g]))
				pSubgoal->lprb_Subgoal [g] = -1000;

			else
				pSubgoal->lprb_Subgoal [g] = o_SubgoalSelectionModel.ComputeLogProb (*pFV);

			if (false == b_PrintTextConnectionFeatures)
				delete pFV;
		}


		// sample	
		pSubgoal->i_SubgoalSelection
			= SampleDecision (pSubgoal->lprb_Subgoal, o_SubgoalExploration, _bTestMode);
		pSubgoal->p_PddlSubgoalPredicate
			= vec_CandidatePredicates [pSubgoal->i_SubgoalSelection];

    	//TODO: Add Config Check to make sure this is valid. Else if question found and
    	// config, throw an error
    	if (0 == pSubgoal->p_PddlSubgoalPredicate->s_Name.compare("question")) {
		pSubgoal->b_isQuestion = true;
      		String_dq_t dq_QuestionArgs;
      		//Parse Question from PddlString
      		String s_PredicateString = pSubgoal->p_PddlSubgoalPredicate->GetPddlString();
      		size_t i_Start = s_PredicateString.rfind("(") + 1;
      		size_t i_End = s_PredicateString.find(")");
      		String s_QuestionString = s_PredicateString.substr(i_Start, i_End - i_Start);
      		s_QuestionString.Split(dq_QuestionArgs, ' ');
      		//Parse Question type and query from question
      		String s_QuestionType = dq_QuestionArgs[1];
      		size_t i_QueryIndex = s_QuestionString.find(dq_QuestionArgs[2]);
      		String s_QuestionQuery = s_QuestionString.substr(i_QueryIndex);
          if(false == AskQuestion(s_QuestionType, s_QuestionQuery)) {
            //TODO cout error, throw error type behavior
          }
          LoadConnections();
    }

		_pSequence->vec_PredicatesInSequence [pSubgoal->i_SubgoalSelection] = 1;

		// delete the old one
		if (true == b_PrintTextConnectionFeatures)
		{
			if (pSubgoal->p_SelectedPredicateFeatures != NULL)
				delete pSubgoal->p_SelectedPredicateFeatures;

			for (long g = 0; g < i_CandidatePredicates; ++ g)
			{
				Features* pFV = pSubgoal->vec_SubgoalFeatureVectors [g];
				if(g == pSubgoal->i_SubgoalSelection)
					pSubgoal->p_SelectedPredicateFeatures = pFV;
				else 
					delete pFV;
			}
		}

		pSubgoal->vec_SubgoalFeatureVectors.clear ();

		if (true == b_DisallowNeighboringDuplicateSubgoals)
			pNextSubgoal = pSubgoal;
	}

	if (false == bAlreadyAddedSequenceEnd)
		AddForcedSequenceEnd (_rProblem, _pSequence);
}

//Query IR system with question and update Connection set as a result.
// TODO: Add Answer Type param
bool SubgoalPolicy::AskQuestion(String s_QuestionType, String s_QuestionQuery) {
  String key = s_QuestionType + s_QuestionQuery;
  String answer;
  if (map_QuestionAnswerPairs[key]) {
    answer = map_QuestionAnswerPairs[key];
    return true;
  } else {
    // TODO: Do RPC to Nicolas code
    if (false == o_IR.SendQuestion(s_QuestionType, s_QuestionQuery)) {
    	return false;
    }
    char sResponse[256];
    o_IR.ReceiveMessage(sResponse, 255);
  }
  return true;
}

//
void SubgoalPolicy::AddLastSubgoal (const Problem& _rProblem,
									SubgoalSequence* _pSequence)
{
	assert (0 == _pSequence->Length ());
	Subgoal* pSubgoal = _pSequence->AddSubgoalToFront ();

	assert (true == pSubgoal->vec_SubgoalFeatureVectors.empty ());
	ComputeSubgoalFeatures (0, _rProblem, _pSequence);
	assert (false == pSubgoal->vec_SubgoalFeatureVectors.empty ());

	pSubgoal->lprb_Subgoal.Create (i_CandidatePredicates);
	for (long g = 0; g < i_CandidatePredicates; ++ g)
	{
		Features* pFV = pSubgoal->vec_SubgoalFeatureVectors [g];
		pSubgoal->lprb_Subgoal [g] = o_SubgoalSelectionModel.ComputeLogProb (*pFV);
		delete pFV;
	}
	pSubgoal->vec_SubgoalFeatureVectors.clear ();


	// Identify target goal's predicate indices...	
	PddlProblem& rPddlProblem = ((Problem&)_rProblem).GetPddlProblem ();
	if (1 != rPddlProblem.o_PartialGoalState.dq_Predicates.size ())
	{
		cerr << "[ERROR] Target goal has multiple predicates set.\n"
			 << "        This code cannot handle this scenario :-/"
			 << endl;
		assert (false);
	}

	PddlPredicate* pTargetGoalPredicate
		= rPddlProblem.o_PartialGoalState.dq_Predicates [0];
	pSubgoal->i_SubgoalSelection = pTargetGoalPredicate->i_PredicateCandidateIndex;
	pSubgoal->p_PddlSubgoalPredicate = vec_CandidatePredicates [pSubgoal->i_SubgoalSelection];
	if (-1 == pSubgoal->i_SubgoalSelection)
	{
		cerr << "[ERROR] Failed to find target goal predicate in candidate predicate list:"
			 << *pTargetGoalPredicate << endl;
		abort ();
	}

	_pSequence->vec_PredicatesInSequence [pSubgoal->i_SubgoalSelection] = 1;

	// set other variables in subgoal...			
	pSubgoal->b_IsLastSubgoalToTarget = true;
	pSubgoal->i_SequenceEnd = 0;
	pSubgoal->p_PddlTargetProblem = &rPddlProblem;
}


//													
void SubgoalPolicy::AddForcedSequenceEnd (const Problem& _rProblem,
										  SubgoalSequence* _pSequence)
{
	Subgoal* pSubgoal = _pSequence->AddSubgoalToFront ();

	assert (true == pSubgoal->vec_SequenceEndFeatureVectors.empty ());
	ComputeSequenceEndFeatures (0, _rProblem, _pSequence);

	pSubgoal->lprb_SequenceEnd.Create (2);
	for (int e = 0; e < 2; ++ e)
	{
		Features* pFV = pSubgoal->vec_SequenceEndFeatureVectors [e];
		pSubgoal->lprb_SequenceEnd [e] = o_SequenceEndModel.ComputeLogProb (*pFV);
		delete pFV;
	}
	pSubgoal->vec_SequenceEndFeatureVectors.clear ();
	pSubgoal->i_SequenceEnd = SEQUENCE_END;
	pSubgoal->b_ForcedSequenceEnd = true;
}


//													
void SubgoalPolicy::InitUpdate (void)
{
	o_SequenceEndModel.InitializeFeatureExpectationVector (vec_SequenceEndFE,
										o_SequenceEndFeatureSpace.MaxIndex () + 1);

	o_SubgoalSelectionModel.InitializeFeatureExpectationVector (vec_SubgoalFE,
										o_SubgoalFeatureSpace.MaxIndex () + 1);
}


//													
void SubgoalPolicy::UpdateParameters (SubgoalSequence& _rSequence,
									  double _dReward,
									  bool _bTaskComplete,
									  bool _bWithConnections)
{
	/*
	if (true == _bWithConnections)
	{
		b_UseSimpleConnectionFeatures = (f_UseSimpleConnectionFeatures > 0);
		b_UseTextConnectionFeatures = (f_UseTextConnectionFeatures > 0);
		b_UseComplexNonConnectionFeatures = (f_UseComplexNonConnectionFeatures > 0);
	}
	else
	{
		b_UseSimpleConnectionFeatures = false;
		b_UseTextConnectionFeatures = false;
	}
	*/

	b_UseSimpleConnectionFeatures = _rSequence.b_UseSimpleConnectionFeatures;
	b_UseTextConnectionFeatures = _rSequence.b_UseTextConnectionFeatures;
	b_UseComplexNonConnectionFeatures = _rSequence.b_UseComplexNonConnectionFeatures;


	// connection prediction model...	
	if ((f_UseTextConnectionFeatures > 0) && (true == _bWithConnections))
	{
		int_set_t setPreviousSubgoals;
		size_t iSequenceLength = _rSequence.dq_Subgoals.size ();
		for (size_t f = 0; f < iSequenceLength; ++ f)
		{
			Subgoal* pFrom = _rSequence.GetSubgoal (f);
			if (true == pFrom->b_ForcedSequenceEnd)
				continue;
			if (SEQUENCE_END == pFrom->i_SequenceEnd)
				continue;
			if (po_goal_already_satisfied == pFrom->e_PlanningOutcome)
				continue;
			if (po_plan_found != pFrom->e_PlanningOutcome)
				break;
			int iFrom = pFrom->p_PddlSubgoalPredicate->i_PredicateCandidateWithoutNumber;
			setPreviousSubgoals.insert (iFrom);

			size_t t = f + 1;
			if (t >= iSequenceLength)
				break;
			Subgoal* pTo = _rSequence.GetSubgoal (t);
			if (true == pTo->b_ForcedSequenceEnd)
				continue;
			if (SEQUENCE_END == pTo->i_SequenceEnd)
				continue;
			if ((po_outside_known_world == pTo->e_PlanningOutcome) ||
				(po_goal_already_satisfied == pTo->e_PlanningOutcome))
				continue;

			// find sentences that contributed to this connection.	
			int iTo = pTo->p_PddlSubgoalPredicate->i_PredicateCandidateWithoutNumber;
			if (po_plan_found == pTo->e_PlanningOutcome)
				mtx_FeedbackOnSentenceConnections (iFrom, iTo, FEEDBACK_POS_PLAN_OK) += 1;
			else
				mtx_FeedbackOnSentenceConnections (iFrom, iTo, FEEDBACK_NEG_PLAN_FAIL) += 1;


			// negative reward for any subgoal that didn't occur before iTo...
			if (po_plan_found == pTo->e_PlanningOutcome)
			{
				for (int n = 0; n < i_CandidatePredicateNumbersMerged; ++ n)
				{
					if (setPreviousSubgoals.end () != setPreviousSubgoals.find (n))
						continue;
					mtx_FeedbackOnSentenceConnections (n, iTo, FEEDBACK_NEG_NOT_IN_PREFIX)
						+= 1;
				}
			}
		}
	}


	// sequence prediction models ...	
	for (int i = _rSequence.dq_Subgoals.size () - 1; i >= 0; -- i)
	{
		Subgoal* pSubgoal = _rSequence.GetSubgoal (i);
		if (true == pSubgoal->b_ForcedSequenceEnd)
			continue;

		if (false == pSubgoal->b_IsLastSubgoalToTarget)
		{
			assert (-1 != pSubgoal->i_SequenceEnd);
			// sequence end model ...			
			{
				// recompute features ...		
				assert (true == pSubgoal->vec_SequenceEndFeatureVectors.empty ());
				ComputeSequenceEndFeatures (i, *_rSequence.p_TargetProblem, &_rSequence);

				// It's possible to have subgoals that don't	
				// the policy distribution already computed.	
				// I.e. in the case where we propose additional	
				// sequences based on the predicted sequence.	
				if (0 == pSubgoal->lprb_SequenceEnd.Size ())
				{
					pSubgoal->lprb_SequenceEnd.Create (2);
					for (int e = 0; e < 2; ++ e)
					{
						Features* pFV = pSubgoal->vec_SequenceEndFeatureVectors [e];
						pSubgoal->lprb_SequenceEnd [e]
							= o_SequenceEndModel.ComputeLogProb (*pFV);
					}
				}

				// compute negative expectation	
				o_SequenceEndModel.ComputeNegativeFeatureExpectation (pSubgoal->lprb_SequenceEnd,
												pSubgoal->vec_SequenceEndFeatureVectors,
												_dReward,
												vec_SequenceEndFE);

				// add selected action features	
				Features* pSelectedFeatures
					= pSubgoal->vec_SequenceEndFeatureVectors [pSubgoal->i_SequenceEnd];
				for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
					vec_SequenceEndFE [pSelectedFeatures->Index (f)]
						+= _dReward * pSelectedFeatures->Feature (f);

				// clear up memory ...			
				ITERATE (Features_vec_t, pSubgoal->vec_SequenceEndFeatureVectors, ite)
					delete *ite;
				pSubgoal->vec_SequenceEndFeatureVectors.clear ();

				if (SEQUENCE_END == pSubgoal->i_SequenceEnd)
					continue;
			}
		}


		// subgoal model ...				
		{
			assert (-1 != pSubgoal->i_SubgoalSelection);

			// recompute features ...		
			assert (true == pSubgoal->vec_SubgoalFeatureVectors.empty ());
			ComputeSubgoalFeatures (i, *_rSequence.p_TargetProblem, &_rSequence);

			// It's possible to have subgoals that don't	
			// the policy distribution already computed.	
			// I.e. in the case where we propose additional	
			// sequences based on the predicted sequence.	
			if (0 == pSubgoal->lprb_Subgoal.Size ())
			{
				pSubgoal->lprb_Subgoal.Create (i_CandidatePredicates);
				for (long g = 0; g < i_CandidatePredicates; ++ g)
				{
					Features* pFV = pSubgoal->vec_SubgoalFeatureVectors [g];
					pSubgoal->lprb_Subgoal [g]
						= o_SubgoalSelectionModel.ComputeLogProb (*pFV);
				}
			}

			// compute negative expectation	
			o_SubgoalSelectionModel.ComputeNegativeFeatureExpectation (pSubgoal->lprb_Subgoal,
											pSubgoal->vec_SubgoalFeatureVectors,
											_dReward,
											vec_SubgoalFE);

			// add selected action features	
			Features* pSelectedFeatures
				= pSubgoal->vec_SubgoalFeatureVectors [pSubgoal->i_SubgoalSelection];
			for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
				vec_SubgoalFE [pSelectedFeatures->Index (f)]
					+= _dReward * pSelectedFeatures->Feature (f);

			// clear up memory ...			
			ITERATE (Features_vec_t, pSubgoal->vec_SubgoalFeatureVectors, ite)
				delete *ite;
			pSubgoal->vec_SubgoalFeatureVectors.clear ();
		}
	}
}


//													
void SubgoalPolicy::UpdateConnectionParameters (void)
{
	if (f_UseTextConnectionFeatures <= 0)
		return;

	// collate feedback ...					
	Matrix <int, 2>	mtxCollatedFeedback;
	mtxCollatedFeedback.Create (i_CandidatePredicateNumbersMerged,
								i_CandidatePredicateNumbersMerged);
	mtxCollatedFeedback.Memset (0);

	unsigned long iPositives = 0;
	unsigned long iNegatives = 0;
	for (int f = 0; f < i_CandidatePredicateNumbersMerged; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicateNumbersMerged; ++ t)
		{
			int iPos = mtx_FeedbackOnSentenceConnections (f, t, FEEDBACK_POS_PLAN_OK);
			int iNegPlanFail
				= mtx_FeedbackOnSentenceConnections (f, t, FEEDBACK_NEG_PLAN_FAIL);
			int iNegNotInPrefix
				= mtx_FeedbackOnSentenceConnections (f, t, FEEDBACK_NEG_NOT_IN_PREFIX);

			int iFeedback = 0;
			if (true == b_UseSuccessFailureCountsInFeedback)
			{
				if (iNegPlanFail > 0)
					iFeedback = - iNegPlanFail;
				if (iPos > 0)
					iFeedback = iPos;
				if (iNegNotInPrefix > 0)
					iFeedback = - iNegNotInPrefix;
			}
			else
			{
				if (iNegPlanFail > 0)
					iFeedback = -1;
				if (iPos > 0)
					iFeedback = 1;
				if (iNegNotInPrefix > 0)
					iFeedback = -1;
			}

			mtxCollatedFeedback (f, t) = iFeedback;
			if (iFeedback > 0)
				iPositives += iFeedback;
			else if (iFeedback < 0)
				iNegatives -= iFeedback;
		}
	}

	if ((0 == iPositives) && (0 == iNegatives))
	{
		if (true == b_LogConnectionFeedback)
			WriteConnectionFeedback ();
		if (false == b_RetainPredicateConnectionFeedback)
			mtx_FeedbackOnSentenceConnections.Memset (0);
		return;
	}

	// compute normalization factors ...	
	// double dMidpoint = iPositives; //(iPositives + iNegatives) / (double) 2;
	double dMidpoint = 1;
	double dPositiveReweighting = 0;
	if (iPositives > 0)
		dPositiveReweighting = dMidpoint / (double) iPositives;
	double dNegativeReweighting = 0;
	if (iNegatives > 0)
		dNegativeReweighting = dMidpoint / (double) iNegatives;
	cout << iPositives << " " << iNegatives << " "
		<< dPositiveReweighting << " " << dNegativeReweighting << endl;


	// update params...						
	for (int i = 0; i < i_UpdatesPerIteration; ++ i)
	{
		for (int f = 0; f < i_CandidatePredicateNumbersMerged; ++ f)
		{
			for (int t = 0; t < i_CandidatePredicateNumbersMerged; ++ t)
			{
				double dReward = mtxCollatedFeedback (f, t);
				if (0 == dReward)
					continue;
				if (dReward > 0)
					dReward *= dPositiveReweighting * f_ConnectionSuccessReward;
				else
					dReward *= dNegativeReweighting * f_ConnectionFailurePenalty;


				// positive predictions ...		
				{
					int_dq_t* pdqSentence = mtx_SentencesPositiveFromTo (f, t);
					if (NULL != pdqSentence)
					{
						ITERATE (int_dq_t, (*pdqSentence), ite)
						{
							SentenceConnection* pConnection = vec_SentenceConnections [*ite];
							lprb_SentenceConnection [0]
								= o_TextConnectionModel.ComputeLogProb (*pConnection->p_NegativeFeatures);
							lprb_SentenceConnection [1]
								= o_TextConnectionModel.ComputeLogProb (*pConnection->p_PositiveFeatures);

							Features_vec_t vecFeatures;
							vecFeatures.reserve (2);
							vecFeatures.push_back (pConnection->p_NegativeFeatures);
							vecFeatures.push_back (pConnection->p_PositiveFeatures);

							o_TextConnectionModel.ComputeNegativeFeatureExpectation (lprb_SentenceConnection,
																					 vecFeatures,
																					 dReward,
																					 vec_ConnectionFE);

							// add selected action features	
							Features* pSelectedFeatures = pConnection->p_PositiveFeatures;
							for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
								vec_ConnectionFE [pSelectedFeatures->Index (f)]
									+= dReward * pSelectedFeatures->Feature (f);

							/*
							pSelectedFeatures = pConnection->p_NegativeFeatures;
							for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
								vec_ConnectionFE [pSelectedFeatures->Index (f)]
									-= lprb_SentenceConnection [0] * dReward * pSelectedFeatures->Feature (f);
							*/
						}
					}
				}


				// negative predictions ...		
				{
					dReward *= -1.0;

					int_dq_t* pdqSentence = mtx_SentencesNegativeFromTo (f, t);
					if (NULL != pdqSentence)
					{
						ITERATE (int_dq_t, (*pdqSentence), ite)
						{
							SentenceConnection* pConnection = vec_SentenceConnections [*ite];
							lprb_SentenceConnection [0]
								= o_TextConnectionModel.ComputeLogProb (*pConnection->p_NegativeFeatures);
							lprb_SentenceConnection [1]
								= o_TextConnectionModel.ComputeLogProb (*pConnection->p_PositiveFeatures);

							Features_vec_t vecFeatures;
							vecFeatures.reserve (2);
							vecFeatures.push_back (pConnection->p_NegativeFeatures);
							vecFeatures.push_back (pConnection->p_PositiveFeatures);

							o_TextConnectionModel.ComputeNegativeFeatureExpectation (lprb_SentenceConnection,
																					 vecFeatures,
																					 dReward,
																					 vec_ConnectionFE);

							// add selected action features	
							Features* pSelectedFeatures = pConnection->p_NegativeFeatures;
							for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
								vec_ConnectionFE [pSelectedFeatures->Index (f)]
									+= dReward * pSelectedFeatures->Feature (f);

							/*
							pSelectedFeatures = pConnection->p_PositiveFeatures;
							for (int f = 0; f < pSelectedFeatures->Size (); ++ f)
								vec_ConnectionFE [pSelectedFeatures->Index (f)]
									-= lprb_SentenceConnection [1] * dReward * pSelectedFeatures->Feature (f);
							*/
						}
					}
				}
			}
		}
	}

	if (true == b_LogConnectionFeedback)
		WriteConnectionFeedback ();
	if (false == b_RetainPredicateConnectionFeedback)
		mtx_FeedbackOnSentenceConnections.Memset (0);
}


//													
void SubgoalPolicy::CompleteUpdate (void)
{
	o_SequenceEndModel.UpdateWeights (1, vec_SequenceEndFE);
	o_SubgoalSelectionModel.UpdateWeights (1, vec_SubgoalFE);

	o_TextConnectionModel.InitializeFeatureExpectationVector (vec_ConnectionFE,
										o_TextConnectionFeatureSpace.MaxIndex () + 1);
	UpdateConnectionParameters ();
	o_TextConnectionModel.UpdateWeights (1, vec_ConnectionFE);

	if (true == b_ForceConnectionWeights)
	{
		size_t f = 2 + i_OffsetToConnectionFeatures;
		if (o_SubgoalSelectionModel.GetWeight (f) < d_ForcedConnectionWeightToInit)
			o_SubgoalSelectionModel.SetWeight (f, d_ForcedConnectionWeightToInit);
		f = 3 + i_OffsetToConnectionFeatures;
		if (o_SubgoalSelectionModel.GetWeight (f) < d_ForcedConnectionWeightToInit)
			o_SubgoalSelectionModel.SetWeight (f, d_ForcedConnectionWeightToInit);

		for (int d = 1; d < 5; ++ d)
		{
			f = 5 + 2*(d-1) + i_OffsetToConnectionFeatures;
			if (o_SubgoalSelectionModel.GetWeight (f) < d_ForcedConnectionWeightToTarget)
				o_SubgoalSelectionModel.SetWeight (f, d_ForcedConnectionWeightToTarget);
			f = 6 + 2*(d-1) + i_OffsetToConnectionFeatures;
			if (o_SubgoalSelectionModel.GetWeight (f) < d_ForcedConnectionWeightToTarget)
				o_SubgoalSelectionModel.SetWeight (f, d_ForcedConnectionWeightToTarget);
		}
	}
}


//													
void SubgoalPolicy::AddReachableSubgoals (const int_set_t& _rsetReachableSubgoals)
{
	ITERATE (int_set_t, _rsetReachableSubgoals, ite)
	{
		assert (*ite < i_CandidatePredicates);
		assert (*ite < (long)vec_CanReachCandidatePredicate.size ());
		assert (i_CandidatePredicates == (long)vec_CanReachCandidatePredicate.size ());

		vec_CanReachCandidatePredicate [*ite] = 1;

		if (true == b_UseReachabilityEquivalents)
		{
			ITERATE (int_vec_t, vec_ReachabilityPredicateEqulivalents [*ite], iteEquiv)
				vec_CanReachCandidatePredicate [*iteEquiv] = 1;
		}
	}
}


//													
int SubgoalPolicy::FindInitPredicateCandidateIndex (PddlPredicate& _rPredicate)
{
	int i = -1;
	CONST_ITERATE (PddlPredicate_vec_t, vec_CandidatePredicates, ite)
	{
		++ i;
		PddlPredicate* pCandidate = *ite;
		if (*(PddlPredicate*)pCandidate != (PddlPredicate&)_rPredicate)
			continue;
		return i;
	}
	return -1;
}


//													
int SubgoalPolicy::FindPredicateCandidateIndex (PddlPredicate& _rPredicate)
{
	int i = -1;
	CONST_ITERATE (PddlPredicate_vec_t, vec_CandidatePredicates, ite)
	{
		++ i;
		PddlPredicate* pCandidate = *ite;
		if (*pCandidate != _rPredicate)
			continue;
		return i;
	}
	return -1;
}


//													
PddlPredicate* SubgoalPolicy::FindEquivalentPredicateCandidate (PddlPredicate& _rPredicate)
{
	PddlStringToPredicate_map_t::iterator	ite;
	ite = map_PddlStringToCandidatePredicate.find (_rPredicate.GetPddlString ());
	if (map_PddlStringToCandidatePredicate.end () == ite)
		return NULL;
	return ite->second;
}


//													
bool SubgoalPolicy::SaveWeights (int _iIteration)
{
	if (1 == (int)(config)"save_global_feature_map")
	{
		File file ((config)"global_feature_mapping_file", ios_base::out);
		ITERATE (int_String_map_t, map_FeatureIndexToFeatureString, ite)
			file << ite->first << '\x01' << ite->second << endl;
		file.Close ();
	}
	
	int iPeriod = (config)"end:param_save_period";
	if ((iPeriod > 0) && (0 == (_iIteration % iPeriod)))
	{
		if (false == o_SequenceEndFeatureSpace.SaveFeatureMapping ("end"))
			return false;
		if (false == o_SequenceEndModel.SaveWeights ("end"))
			return false;
	}

	iPeriod = (config)"subgoal:param_save_period";
	if ((iPeriod > 0) && (0 == (_iIteration % iPeriod)))
	{
		if (false == o_SubgoalFeatureSpace.SaveFeatureMapping ("subgoal"))
			return false;
		if (false == o_SubgoalSelectionModel.SaveWeights ("subgoal"))
			return false;
	}

	iPeriod = (config)"connection:param_save_period";
	if ((iPeriod > 0) && (0 == (_iIteration % iPeriod)))
	{
		if (false == o_TextConnectionFeatureSpace.SaveFeatureMapping ("connection"))
			return false;
		if (false == o_TextConnectionModel.SaveWeights ("connection"))
			return false;
	}

	return true;
}


//													
double SubgoalPolicy::WeightVectorNorm (void)
{
	return o_SequenceEndModel.WeightVectorNorm ()
			+ o_SubgoalSelectionModel.WeightVectorNorm ()
			+ o_TextConnectionModel.WeightVectorNorm ();
}


//													
void SubgoalPolicy::DebugPrintFeatureVectors (const Subgoal& subgoal,
											  ostream* osOut,
											  const String& sPrefix) const
{
	// iterate over possible
	for(unsigned int iPred = 0; iPred < subgoal.vec_SubgoalFeatureVectors.size(); iPred++){
		const Features& featuresCur = *subgoal.vec_SubgoalFeatureVectors[iPred];
		const PddlPredicate& predCur = *vec_CandidatePredicates [iPred];
		*osOut << sPrefix << ":" << iPred << ":" << predCur.GetPddlString() << "\n";
		for (int iFeatureListIndex = 0; iFeatureListIndex < featuresCur.Size(); iFeatureListIndex++){
			int iFeature = featuresCur.Index(iFeatureListIndex);
			const String& sFeature = o_SubgoalFeatureSpace.GetFeatureString(iFeature);
			*osOut << "\t" << iFeature << "-->" << sFeature << "\n";
		}
	}
}


//													
void SubgoalPolicy::WriteConnectionPredictionHeader (void)
{
	File file;
	if (false == file.Open ((config)"connection_prediction_log_file",
						    ios_base::out))
		return;

	for (int f = 0; f < i_CandidatePredicates; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicates; ++ t)
		{
			PddlPredicate* pPddlFrom = vec_CandidatePredicates [f];
			int iPddlFrom = pPddlFrom->i_PredicateCandidateWithoutNumber;
			PddlPredicate* pPddlTo = vec_CandidatePredicates [t];
			int iPddlTo = pPddlTo->i_PredicateCandidateWithoutNumber;
			if (NULL == mtx_SentencesPositiveFromTo (iPddlFrom, iPddlTo))
				continue;
			file << f << ':' << t << ' ';
		}
	}
	file << endl;
	file.flush ();
	file.Close ();
}


//													
void SubgoalPolicy::WriteConnectionPredictions (void)
{
	File file;
	if (false == file.Open ((config)"connection_prediction_log_file",
						    ios_base::out|ios_base::app))
		return;

	for (int f = 0; f < i_CandidatePredicates; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicates; ++ t)
		{
			PddlPredicate* pPddlFrom = vec_CandidatePredicates [f];
			int iPddlFrom = pPddlFrom->i_PredicateCandidateWithoutNumber;
			PddlPredicate* pPddlTo = vec_CandidatePredicates [t];
			int iPddlTo = pPddlTo->i_PredicateCandidateWithoutNumber;
			if (NULL == mtx_SentencesPositiveFromTo (iPddlFrom, iPddlTo))
				continue;
			file << ((0 == mtx_PredicateConnectionsFromTo (f, t))? '0' : '1') << ' ';
		}
	}
	file << endl;
	file.flush ();
	file.Close ();
}


//													
String SubgoalPolicy::ConnectionPredictionRatio (void)
{
	// if (f_UseTextConnectionFeatures <= 0)
		return String ("0/0");

	/*
	long lTotal = 0;
	long lPredictedConnections = 0;
	for (int f = 0; f < i_CandidatePredicateNumbersMerged; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicateNumbersMerged; ++ t)
		{
			if (NULL == mtx_SentencesPositiveFromTo (f, t))
				continue;
			++ lTotal;
			lPredictedConnections +=  mtx_PredicateConnectionsFromTo (f, t);
		}
	}

	String sRet;
	sRet << lPredictedConnections << '/' << lTotal;
	return sRet;
	*/
}


//													
void SubgoalPolicy::WriteConnectionFeedback (void)
{
	/*
	File file;
	if (false == file.Open ((config)"connection_feedback_log_file",
						    ios_base::out|ios_base::app))
		return;

	for (int f = 0; f < i_CandidatePredicates; ++ f)
	{
		for (int t = 0; t < i_CandidatePredicates; ++ t)
		{
			int iSuccesses = mtx_FeedbackOnSentenceConnections (f, t, 1);
			int iFailures = mtx_FeedbackOnSentenceConnections (f, t, 0);
			if ((0 == iSuccesses) && (0 == iFailures))
				continue;

			file << f << ':' << t << ':' << iSuccesses << ':' << iFailures << ' ';
		}
	}
	file << endl;
	file.flush ();
	file.Close ();
	*/
}

void SubgoalPolicy::TestQA ()
{
	String type;
	String query;
	type << "action";
	query << "wood";
	if (AskQuestion(type, query)) {
		cout << "QA1: success" << endl;
	} else {
		cout << "QA1: fail" << endl;
	}
	if (AskQuestion(type, query)) {
		cout << "QA2: success" << endl;
	} else {
		cout << "QA2: fail" << endl;
	}
	cout << "QA: Done questioning" << endl;
}





