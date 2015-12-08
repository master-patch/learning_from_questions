#ifndef __PDDL__
#define __PDDL__

#include <nlp_string.h>
#include <nlp_vector.h>
#include <nlp_time.h>
#include <deque>
#include <hash_map>
using namespace std;


class PddlParameter;
class PddlPredicate;
class PddlEffect;
class PddlAction;
typedef deque <PddlParameter>			PddlParameter_dq_t;
typedef deque <PddlPredicate*>			PddlPredicate_dq_t;
typedef deque <PddlEffect>				PddlEffect_dq_t;
typedef deque <PddlAction*>				PddlAction_dq_t;
typedef hash_map <String, PddlAction*>	NameToPddlAction_hmp_t;
typedef hash_map <String, PddlPredicate*> HashToPddlPredicate_hmp_t;
typedef Vector <int>					int_Vec_t;

//										
class PddlParameter
{
	friend class PddlPredicate;

	private:
		String	s_Value;

	public:
		String	s_Type;
		String	s_VariableName;
		String*	p_ResolvedValue;
	
		PddlParameter (void);
		PddlParameter (const PddlParameter& _rParam);
		void SetValue (String& _rValue);
		String GetPddlString (void) const;
};

ostream& operator<< (ostream& _rStream, const PddlParameter& _rParam);
ostream& operator<< (ostream& _rStream, const PddlParameter_dq_t& _rdqParam);


//										
class PddlPredicate
{
	public:
		int_Vec_t			vec_ParameterValueFeatureIndex;
		PddlParameter_dq_t	dq_Parameters;
		String				s_Name;
		String				s_BoundIdentityHash;
		long             	l_Value;
    String        s_Suffix;

		// index of predicate in subgoal candidate list	
		int					i_PredicateCandidateIndex;
		// feature indices ...							
		int					i_PredicateIdentityFeatureIndex;
		int					i_PredicateNameFeatureIndex;
		int					i_PredicateCandidateWithoutNumber;
    int         i_SuffixObjectFeatureIndex;

		bool				b_IsFunction;

        virtual String InstanceHash (void) const;
		virtual String& BoundIdentityHash (void);
		virtual String UnBoundIdentityHash (void);

		PddlPredicate (void);
		PddlPredicate (const PddlPredicate& _rPredicate);
		virtual ~PddlPredicate (void) {}
		virtual String GetPddlString (void) const;

		virtual bool operator== (const PddlPredicate& _rRight) const;
		virtual bool operator!= (const PddlPredicate& _rRight) const
		{ return (false == operator==(_rRight)); };

		virtual PddlPredicate* Clone (void)
		{ return new PddlPredicate (*this); };
};

ostream& operator<< (ostream& _rStream, const PddlPredicate& _rPredicate);


//										
class PddlFunctionValuePredicate : public PddlPredicate
{
	public:
		char	c_Operator;

        virtual String InstanceHash (void) const;
		virtual String& BoundIdentityHash (void);
		virtual String UnBoundIdentityHash (void);

		PddlFunctionValuePredicate (void) : PddlPredicate ()
		{
			b_IsFunction = true;
			c_Operator = '*';
		};

		PddlFunctionValuePredicate (const PddlFunctionValuePredicate& _rPredicate);
		virtual ~PddlFunctionValuePredicate (void) {}
		virtual String GetPddlString (void) const;

		virtual bool operator== (const PddlFunctionValuePredicate& _rRight) const;
		virtual bool operator!= (const PddlFunctionValuePredicate& _rRight) const
		{ return (false == operator==(_rRight)); };

		virtual PddlPredicate* Clone (void)
		{ return new PddlFunctionValuePredicate (*this); };
};

ostream& operator<< (ostream& _rStream, const PddlFunctionValuePredicate& _rPredicate);


//										
enum PddlEffect_e
{
	pe_unknown,
	pe_assign,
	pe_increase,
	pe_decrease,
	pe_predicate_set,
	pe_predicate_clear
};


//										
class PddlEffect : public PddlPredicate
{
	public:
		PddlPredicate	o_FunctionEffectValue;
		PddlEffect_e	e_Effect;
		long			f_FunctionEffectValue;
		bool			b_EffectValueIsPredicate;

		PddlEffect (void) : PddlPredicate ()
		{
			e_Effect = pe_unknown;
			f_FunctionEffectValue = 0;
			b_EffectValueIsPredicate = false;
		};

		PddlEffect (const PddlEffect& _rEffect);
};

ostream& operator<< (ostream& _rStream, const PddlEffect& _rEffect);


//										
class PddlAction
{
	public:
		PddlParameter_dq_t	dq_Parameters;
		PddlEffect_dq_t		dq_Effects;
		String				s_Name;

        PddlAction (void) {};
        PddlAction (const PddlAction& _rAction);
		void LinkEffectsToParameters (void);

};

ostream& operator<< (ostream& _rStream, const PddlAction& _rAction);


//										
class PddlDomain
{
	public:
		PddlPredicate_dq_t		dq_Predicates;
		NameToPddlAction_hmp_t	hmp_NameToActions;

		PddlDomain (void) {};
		~PddlDomain (void);
};

ostream& operator<< (ostream& _rStream, const PddlDomain& _rDomain);


//										
class PddlState
{
    private:
        long calcEffectValue (const PddlEffect& _rEffect,
                        	   const HashToPddlPredicate_hmp_t& _hmpPredicate);

	public:
		PddlPredicate_dq_t	dq_Predicates;
		String				s_Preamble;

		PddlState (void) {};
        PddlState (const PddlState& _rState);
		~PddlState (void);

        PddlState* ComputeNextState (const PddlAction& _rAction);
        void UpdateToNextState (const PddlAction& _rAction,
								PddlPredicate_dq_t& _rdqPredicates);
		String GetPddlString (void);
		String GetPredicatePddlString (void);

		bool operator== (const PddlState& _rRight) const;
};

ostream& operator << (ostream& _rStream, const PddlState& _rState);

//										
class PddlProblem
{
	public:
		PddlState	o_StartState;
		PddlState	o_PartialGoalState;

		PddlProblem (void) {};
		~PddlProblem (void) {};
		String GetPddlString (void);
};

ostream& operator<< (ostream& _rStream, const PddlProblem& _rProblem);


//										
class PddlPlan
{
	public:
		PddlAction_dq_t	dq_Actions;

		PddlPlan (void) {};
		~PddlPlan (void);
};


#endif
