#ifndef __SUBGOAL_LEARNER__
#define __SUBGOAL_LEARNER__

#include "SubgoalPolicy.h"
#include "Problems.h"
#include "FFInterface.h"
#include <set>
using namespace std;

class SubgoalSequenceState;
typedef hash_map <int, SubgoalSequenceState>	IndexToSubgoalSequenceState_hmp_t;
typedef set <int>								int_set_t;
typedef deque <PddlPredicate_dq_t*>				PlanSubgoalSequences_dq_t;


//										
class SubgoalSequenceState
{
	public:
		SubgoalSequence*			p_Sequence;
		Problem*					p_TargetProblem;
		PlanSubgoalSequences_dq_t	dq_PlanSubgoalSequences;
		double						d_Reward;
		int							i_CurrentStep;
		int							i_ProblemId;
		bool						b_TaskComplete;
		bool						b_FullTask;
    int             nextSubgoal();

		SubgoalSequenceState (SubgoalSequence* _pSequence, int _iStep, int _iId)
		{
			p_Sequence = _pSequence;
			p_TargetProblem = NULL;
			i_CurrentStep = _iStep;
			i_ProblemId = _iId;
			d_Reward = 0;
			b_TaskComplete = false;
			b_FullTask = false;
		};

};

ostream& operator<< (ostream& _rStream, const SubgoalSequence& _rSequence);


//										
class SubgoalLearner : public FFCallback
{
	private:
		SubgoalPolicy	o_SubgoalPolicy;
		FFInterface		o_FFInterface;
		double			d_PlanFailureReward;
		double			d_TaskCompletionReward;
		double			d_SuccessfulStepRewardBase;
		double			d_UnnecessarySubgoalPenalty;
		double			d_RewardForHittingCachePeriphery;
		int				i_SequencesOnFirstIteration;
		int				i_SequencesPerIteration;

		int_Vec_t		vec_TargetGoalCompletions;
		int				i_TotalPlanJobs;
		int				i_OutcomePlansFound;
		int				i_OutcomeGoalsAlreadySatisfied;
		int				i_OutcomeUnsolvable;
		int				i_OutcomeSyntaxError;
		int				i_OutcomeTimeouts;
		int				i_OutcomeOutsideKnownWorld;
		int				i_OutcomeUnknown;
		float			f_TotalPlanDepthReached;

		int				i_CurrentFFTimelimit;
		int				i_TestTimeFFTimelimit;
		int				i_TrainingTimeFFTimelimit;

		bool			b_LearnFromAlternateSequences;
		bool			b_LearnOnSubgoalFreeProblems;
		bool			b_RememberSolutions;
		bool			b_UseLocalHeuristicEvaluator;
		bool			b_LogPredictions;
		bool			b_DisplayFFProgress;

		long			i_DomainPddlId;
		PddlDomain*		p_PddlDomain;
		IndexToSubgoalSequenceState_hmp_t	hmp_IndexToSequenceState;
		int_set_t							set_PendingSequences;

		pthread_mutex_t	mtx_WaitForSequences;
		pthread_cond_t	cv_WaitForSequences;


		void OnFFResponse (int _iIndex, FFResponse& _rResponse);
		double ComputeReward (SubgoalSequenceState& _rState);
		void LogPredictions (int _iIteration);
		void TrimPlanSubgoalSequences (PlanSubgoalSequences_dq_t& _rdqPlanSubgoals);
		void ProposeAlternateSequences (SubgoalSequenceState& _rState,
										SubgoalSequence_dq_t& _rdqAlternateSequences);

	public:
		SubgoalLearner (void);
		~SubgoalLearner (void);

		bool Init (void);

    void TryLinkingSubgoals(void);
		void TryPlanningOnFullTasks (void);
		void Iterate (int _iIteration, bool _bTestMode);
		void SaveWeights (int _iIteration)
		{ o_SubgoalPolicy.SaveWeights (_iIteration); };
};


#endif
