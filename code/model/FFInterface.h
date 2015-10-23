#ifndef __FF_INTERFACE__
#define __FF_INTERFACE__

#include <nlp_string.h>
#include <nlp_string.h>
#include <nlp_socket.h>
#include <hash_map>
#include "PddlInterface.h"
using namespace std;

class FFResponse;
typedef hash_map <int, FFResponse*>			TaskIdToFFResponse_hmp_t;
typedef hash_map <String, int>				CacheIdToTaskId_hmp_t;	
typedef hash_map <String, String_set_t*>	GoalToPrerequisites_hmp_t;
typedef hash_map <String, String*>			GoalToPlan_hmp_t;


//														
enum FFPlaningOutcome_e
{
	po_plan_found,
	po_goal_already_satisfied,
	po_unsolvable,
	po_timeout,
	po_syntax_error,
	po_ff_code_change_required,
	po_outside_known_world,
	po_unknown
};


//														
class FFResponse
{
	public:
		size_t				i_Domain;
		String				s_Problem;

		String				s_FFOutput;
		String				s_EndStatePredicates;
		String				s_Plan;
		long				l_States;
		FFPlaningOutcome_e	e_PlanningOutcome;

		FFResponse (void)
		{
			l_States = -1;
			e_PlanningOutcome = po_unknown;
		};
};


//														
class FFCallback
{
	public:
		virtual void OnFFResponse (int _iIndex, FFResponse& _rResponse) = 0;
};


//														
class FFInterface : public ClientSocket, private PddlInterface
{
	private:
		static bool					b_Active;
		static FFInterface*			p_FFInterface;

		TaskIdToFFResponse_hmp_t	hmp_TaskIdToFFResponse;
		Buffer						o_Data;
		bool						b_KnownWorldOnly;

		pthread_t					thr_SocketLoop;
		pthread_mutex_t				mtx_TaskList;

		FFCallback*					p_Callback;

		GoalToPrerequisites_hmp_t	hmp_GoalToPrerequisites;
		GoalToPlan_hmp_t			hmp_GoalToPlan;
		bool						b_UseLocalHeuristicEvaluator;
		bool						b_IgnoreNumericValues;

		bool InitHeuristicEvaluator (void);
		void RunLocalHeuristicEvaluator (void);
		FFPlaningOutcome_e HasPrerequisites (PddlProblem& _rPddlProblem,
											 String& _rProblem,
											 String& _rPlan);
		bool SendMessage (const String& _rMessage);
		bool SendMessage (const Buffer& _rMessage);

	public:
		FFInterface (void);
		~FFInterface (void);

		bool Connect (void);
		void Disconnect (void);
		void SetCallback (FFCallback* _pCallback)
		{ p_Callback = _pCallback; };

		long RegisterDomain (String& _rDomain);
		bool SendTask (size_t _iId,
					   size_t _iDomain,
					   String& _rProblem,
					   size_t _iTimelimit);
		void ClearTasks (void);
		bool TestTasksClear (void);

		//								
		void OnReceive (const void* _zData, long _lBytes);
		void OnDisconnect (void);
		void ClearConnection (void);

		//								
		static FFPlaningOutcome_e FFExtractOutcome (String& _rFFResponse);
		static String ExtractPlan (String& _rFFResponse);
		static long StatesEvaluated (String& _rFFResponse);

		//								
		static void* RunThread (void* _pArg);
};


#endif
