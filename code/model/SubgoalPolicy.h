#ifndef __SUBGOAL_POLCY__
#define __SUBGOAL_POLCY__

#include "LogLinearPolicy.h"
#include "FFInterface.h"
#include <nlp_distr.h>
#include <nlp_time.h>
#include <nlp_filesystem.h>
#include <nlp_matrix.h>
#include <deque>
using namespace std;

#define	SEQUENCE_END	(int)1
#define FEEDBACK_NEG_PLAN_FAIL			0
#define FEEDBACK_NEG_NOT_IN_PREFIX		1
#define FEEDBACK_POS_PLAN_OK			2


class Problem;
class Subgoal;
class SubgoalSequence;
class SentenceConnection;
typedef deque <int>							int_dq_t;
typedef deque <Subgoal>						Subgoal_dq_t;
typedef deque <SubgoalSequence*>			SubgoalSequence_dq_t;
typedef hash_map<int, PddlPredicate*>		int_PddlPredicate_map_t;
typedef hash_map<String, PddlPredicate*>	PddlStringToPredicate_map_t;
typedef vector<vector<int> >				int_vec_vec_t;
typedef vector<int>							int_vec_t;
typedef vector<int_vec_t>					ReachabilityEquivalent_vec_t;
typedef vector<char>						char_vec_t;
typedef hash_map<String, int>				String_int_map_t;
typedef hash_map<int, String>				int_String_map_t;
typedef hash_map<String, set<int> >			String_intset_map_t;
typedef set<String>							String_set_t;
typedef hash_map<int, hash_map<int, int> >	int_int_int_map_map_t;
typedef hash_map<int,int>					int_int_map_t;
typedef hash_map<int,float>					FeatureToValue_map_t;
typedef hash_map<String,int>				FeatureToIndex_hmp_t;
typedef vector <PddlPredicate*>				PddlPredicate_vec_t;
typedef vector <SentenceConnection*>		SentenceConnection_vec_t;
typedef map <String, FeatureToValue_map_t*> ConnectionHashToFeatures_map_t;



enum enum_subgoal_t{START, SUBGOAL, GOAL};


//										
class SentenceConnection
{
	public:
		Features*	p_PositiveFeatures;
		Features*	p_NegativeFeatures;
		int			i_Sentence;
		int			i_From;
		int			i_To;

		SentenceConnection (void)
		{
			p_PositiveFeatures = NULL;
			p_NegativeFeatures = NULL;
		};
};

	
//										
class Subgoal
{
	public:
		LogProbability	lprb_SequenceEnd;
		LogProbability	lprb_Subgoal;
		Features_vec_t	vec_SequenceEndFeatureVectors; 
		Features_vec_t	vec_SubgoalFeatureVectors; 

		String			s_StartStatePredicates;
		String			s_ProblemPddl;
		String			s_FFOutput;
		String			s_Plan;

		Features*       p_SelectedPredicateFeatures;
		PddlPredicate*	p_PddlSubgoalPredicate;
		PddlProblem*	p_PddlProblem;
		PddlProblem*	p_PddlTargetProblem;

		long			l_States;
		long			i_SubgoalSelection;
		int				i_SequenceEnd;
		FFPlaningOutcome_e	e_PlanningOutcome;
		bool			b_IsLastSubgoalToTarget;
		bool			b_ForcedSequenceEnd;

		Subgoal (void);
		~Subgoal (void);
};


//										
class SubgoalSequence
{
	friend class SubgoalPolicy;
	public:
		Subgoal_dq_t	dq_Subgoals;
		char_vec_t		vec_PredicatesInSequence;
		String			s_ProblemPddlPreamble;
		Problem*		p_TargetProblem;

		bool			b_UseSimpleConnectionFeatures;
		bool			b_UseTextConnectionFeatures;
		bool			b_UseComplexNonConnectionFeatures;


		SubgoalSequence (void);
		~SubgoalSequence (void);

		int Length (void)
		{ return dq_Subgoals.size (); };

		Subgoal* AddSubgoalToFront (void)
		{
			dq_Subgoals.push_front (Subgoal ());
			return &dq_Subgoals.front ();
		}
		Subgoal* AddSubgoalToBack (void)
		{
			dq_Subgoals.push_back (Subgoal ());
			return &dq_Subgoals.back ();
		}

		Subgoal* GetSubgoal (unsigned int _iIndex)
		{
			assert (_iIndex < dq_Subgoals.size ());
			return &dq_Subgoals [_iIndex];
		};

		void SetSubtaskFFResponse (unsigned int _iIndex, FFResponse& _rResponse);
		bool GetSubtask (unsigned int _iIndex, String* _pProblemPddl);
		void SetSubtask (unsigned int _iIndex,
						 String _rProblemPddl,
						 PddlProblem* _pPddlProblem);

		String ToLogString (void);
};


//										
enum ExplorationType_e
{
	et_epsilon_greedy,
	et_softmax,
	et_epsilon_softmax,
	et_unknown
};


//										
class ExplorationParameters
{
	public:
		ExplorationType_e	e_ExplorationType;
		float				f_Epsilon;
		float				f_EpsilonMin;
		float				f_EpsilonRange;
		float				f_Beta;
		float				f_BetaMin;
		float				f_BetaRange;

		ExplorationParameters (void)
		{
			e_ExplorationType = et_unknown;
			f_Epsilon = 0;
			f_EpsilonMin = 0;
			f_EpsilonRange = 0;
			f_Beta = 0;
			f_BetaMin = 0;
			f_BetaRange = 0;
		}

		ExplorationType_e ToEnum (String _sType);
		const char* ToString (ExplorationType_e _eType);

		void SetParamsFromConfig (String _rPrefix);
		String SampleParameters (Sample& _rSample);
		void PrintConfiguration (const char* _zPrefix);
};


//										
enum ConnectionRewardType_e
{
	crt_linear,
	crt_single_success,
	crt_unknown
};


//										
class SubgoalPolicy
{
	friend class SubgoalLearner;

	private:
		LogLinearModel	o_SequenceEndModel;
		LogLinearModel	o_SubgoalSelectionModel;
		LogLinearModel	o_TextConnectionModel;

		FeatureSpace	o_SequenceEndFeatureSpace;
		FeatureSpace	o_SubgoalFeatureSpace;
		FeatureSpace	o_TextConnectionFeatureSpace;
		Sample			o_Sample;

		LogProbability	lprb_SentenceConnection;

		double_Vec_t	vec_ConnectionFE;
		double_Vec_t	vec_SequenceEndFE;
		double_Vec_t	vec_SubgoalFE;

		FeatureToIndex_hmp_t	hmp_ParameterValueToIndex;
		FeatureToIndex_hmp_t	hmp_PredicateNameToIndex;
		FeatureToIndex_hmp_t	hmp_PredicateWithoutNumberToIndex;
		FeatureToIndex_hmp_t	hmp_PredicateIdToIndex;
		String_int_map_t        map_ProblemToGoldLength;
		int_String_map_t        map_FeatureIndexToFeatureString;
		int_dq_t                dq_FeaturesToDebugPrint;


		PddlStringToPredicate_map_t	map_PddlStringToCandidatePredicate;
		PddlPredicate_vec_t			vec_CandidatePredicates;
		char_vec_t					vec_CanReachCandidatePredicate;

		Matrix <char,2>	mtx_PredicateConnectionsFromTo;
		Matrix <char,2>	mtx_PredicateConnectionsToFrom;
		Matrix <int_dq_t*,2>	mtx_SentencesPositiveFromTo;
		Matrix <int_dq_t*,2>	mtx_SentencesNegativeFromTo;
		Matrix <int, 3>	mtx_FeedbackOnSentenceConnections;

		SentenceConnection_vec_t	vec_SentenceConnections;
		ReachabilityEquivalent_vec_t	vec_ReachabilityPredicateEqulivalents;

		size_t			i_OffsetToConnectionFeatures;
		size_t			i_OffsetToPredicateNameFeatures;
		size_t			i_OffsetToParameterValueFeatures;
		size_t			i_OffsetToPredicateIdentityFeatures;
		size_t			i_PredicateNames;
		size_t			i_ParameterValues;
		size_t			i_PredicateIdentities;
		int				i_MaxConnectionDepth;
		int				i_MaxPredicateValue;
		int				i_MaxSequenceLength;

		ExplorationParameters	o_SequenceEndExploration;
		ExplorationParameters	o_SubgoalExploration;
		ExplorationParameters	o_ConnectionExploration;
		ConnectionRewardType_e	e_ConnectionRewardType;

		long			i_CandidatePredicates;
		long			i_CandidatePredicateNumbersMerged;
		float			f_UseSimpleConnectionFeatures;
		bool			b_UseSimpleConnectionFeatures;
		float			f_UseTextConnectionFeatures;
		bool			b_UseTextConnectionFeatures;
		float			f_UseComplexNonConnectionFeatures;
		bool			b_UseComplexNonConnectionFeatures;
		float			f_NonConnectionFeatureImportance;
		bool			b_DisallowNeighboringDuplicateSubgoals;
		bool			b_DisallowAnyDuplicateSubgoals;
		bool			b_UseLogarithmicDistanceScore;
		bool			b_ForceConnectionWeights;
		double			d_ForcedConnectionWeightToInit;
		double			d_ForcedConnectionWeightToTarget;
		bool			b_UsePredicateValueFeature;
		bool			b_UseReachableSubgoalFeature;
		bool			b_UseReachabilityEquivalents;
		float			f_PredicateIdentityPairFeatureWeight;
		float			f_ConnectionSuccessReward;
		float			f_ConnectionFailurePenalty;

		bool			b_UseOnlyPreviousSubgoal;
		bool			b_IncludeInit;
		bool            b_UseGoldLength;
		bool			b_PrintTextConnectionFeatures;
		bool			b_LogConnectionPredictions;
		bool			b_LogConnectionFeedback;
		bool			b_RetainPredicateConnectionFeedback;
		bool			b_UseSuccessFailureCountsInFeedback;
		int				i_UpdatesPerIteration;


		float DistanceScore (float _fDistance)
		{
			if (true == b_UseLogarithmicDistanceScore)
				return 1 / (float)(1 + log (_fDistance));
			else
				return 1 / (float)_fDistance;
		};
		int GetPredicateIdentityFeatureIndex (const String& _rPredicate);
		int GetPredicateNameFeatureIndex (const String& _rName);
		int GetPredicateWithoutNumberIndex (const PddlPredicate& _rPredicate);
		int GetParameterValueFeatureIndex (const String& _rValue);

		void ComputeSubgoalFeatures (int _iIndex,
									 const Problem& _rProblem,
									 SubgoalSequence* _pSequence);
		void ComputeSequenceEndFeatures (int _iIndex,
										 const Problem& _rProblem,
										 SubgoalSequence* _pSequence);
		
		bool LoadSimpleConnectionFile (void);
		bool LoadFeatureConnectionFile (void);
		bool LoadPredDictFile (void);
		void LoadGoldLengthFile (void);
		void LoadFeaturesToDebugPrintFile(void);
		void LogDebugFeatureWeights(File *file);

		PddlPredicate* FindEquivalentPredicateCandidate (PddlPredicate& _rPredicate);
		int FindPredicateCandidateIndex (PddlPredicate& _rPredicate);
		int FindInitPredicateCandidateIndex (PddlPredicate& _rPredicate);
		void AssignIndicesToTargetProblemPredicates (void);

		void AddLastSubgoal (const Problem& _rProblem,
							 SubgoalSequence* _pSequence);
		void AddForcedSequenceEnd (const Problem& _rProblem,
								   SubgoalSequence* _pSequence);
		inline size_t SampleDecision (LogProbability& _rLogProb,
									  ExplorationParameters& _rExploration,
									  bool _bTestMode);
		inline size_t SampleSequenceEnd (int _iSubgoalIndex,
										 const Problem& _rProblem, 
										 LogProbability& _rLogProb,
										 bool _bTestMode);
		void UpdateConnectionParameters (void);
		void DebugPrintFeatureVectors (const Subgoal& subgoal,
									   ostream* osOut,
									   const String& sPrefix) const;

		void SetFeatures (const int_Vec_t& _rvecFI,
						  size_t _iOffset,
						  Features* _pFV,
						  float _fValue = 1,
						  bool _bCheckDuplicates = true)
		{
			for (size_t i = 0; i < _rvecFI.Size (); ++ i)
				_pFV->Set (_iOffset + _rvecFI [i], _fValue, _bCheckDuplicates);
		}

	public:
		SubgoalPolicy (void);
		~SubgoalPolicy (void);

		bool Init (void);

		void SampleExplorationParameters (void);
		void ForceConnectionUseFlags (void);
		void SampleConnectionUseFlags (void);

		void SampleConnections (bool _bTestMode);
		void SampleSubgoalSequence (const Problem& _rProblem,
									bool _bTestMode,
									SubgoalSequence* _pSequence);
		void SampleZeroSubgoalSequence (const Problem& _rProblem,
										SubgoalSequence* _pSequence);

		void InitUpdate (void);
		void UpdateParameters (SubgoalSequence& _rSequence,
							   double _dReward,
							   bool _bTaskComplete,
							   bool _bWithConnections);
		void CompleteUpdate (void);

		void AddReachableSubgoals (const int_set_t& _rsetReachableSubgoals);
		bool SaveWeights (int _iIteration);
		void Test(void);
		double WeightVectorNorm (void);
		String GetFeatureString (int _iIndex) const;
		void WriteConnectionFeedback (void);
		void WriteConnectionPredictionHeader (void);
		void WriteConnectionPredictions (void);
		String ConnectionPredictionRatio (void);
};


#endif
