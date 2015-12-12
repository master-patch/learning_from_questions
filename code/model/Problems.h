#ifndef __PLANNING_PROBLEM__
#define __PLANNING_PROBLEM__

#include "SubgoalPolicy.h"
#include <nlp_string.h>
#include <nlp_filesystem.h>
#include <nlp_config.h>
#include <nlp_macros.h>
#include "Pddl.h"


class Problem;
typedef deque <Problem>		Problem_dq_t;
typedef map <String, int>	SolutionsToCount_map_t;

class Problem
{
	private:
		static Problem_dq_t	dq_Problems;

	public:
		String				s_FileName;
		String				s_Problem;
		String				s_PddlPreamble;
		PddlProblem*		p_PddlProblem;
		SubgoalSequence*	p_SolutionSequence;
		double				d_SolutionReward;
		int					i_SolutionIteration;
		bool				b_SubgoalsNotNeeded;
		SolutionsToCount_map_t	map_SolutionsToCount;

		int_Vec_t			vec_InitPredicateIdentityFI;
		int_Vec_t			vec_InitPredicateNameFI;
		int_Vec_t			vec_InitParameterValueFI;
		int_Vec_t			vec_TargetPredicateIdentityFI;
		int_Vec_t			vec_TargetPredicateNameFI;
		int_Vec_t			vec_TargetParameterValueFI;

		int_Vec_t			vec_QuestionInitPredicateIdentityFI;
		int_Vec_t			vec_QuestionInitPredicateNameFI;
		int_Vec_t			vec_QuestionInitParameterValueFI;
		int_Vec_t			vec_QuestionTargetPredicateIdentityFI;
		int_Vec_t			vec_QuestionTargetPredicateNameFI;
		int_Vec_t			vec_QuestionTargetParameterValueFI;

		//									
		Problem (String& _rProblem, String& _rFileName);
		~Problem (void);
        
		PddlProblem& GetPddlProblem (void);
		bool AddSolution (SubgoalSequence* _pSequence,
						  double _dReward,
						  int _iIteration);
		SubgoalSequence* GetCurrentSolution (void)
		{ return p_SolutionSequence; };
		double GetCurrentSolutionReward (void)
		{ return d_SolutionReward; };
		int GetCurrentSolutionIteration (void)
		{ return i_SolutionIteration; };


		static bool Load (void);

		static void Clear (void)
		{ dq_Problems.clear (); }
		
		static long GetProblemCount (void)
		{ return dq_Problems.size (); };
		
		static Problem* GetProblem (int _iProblem)
		{ return &dq_Problems [_iProblem]; };

		static long TotalSolvedProblems (void);
		static bool LogSolutions (const char* _zPath);
		static void PrintSolvedProblems (void);
};



#endif
