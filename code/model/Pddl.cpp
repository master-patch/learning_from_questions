#include "Pddl.h"
#include <nlp_macros.h>
#include <map>
#include <assert.h>
using namespace std;


//																
PddlParameter::PddlParameter (void)
{
	p_ResolvedValue = &s_Value;
	// p_ResolvedValue = &s_VariableName;
};

PddlParameter::PddlParameter (const PddlParameter& _rParam)
{
	s_Type = _rParam.s_Type;
	s_VariableName = _rParam.s_VariableName;

	s_Value = _rParam.s_Value;
    if (&_rParam.s_Value == _rParam.p_ResolvedValue)
        p_ResolvedValue = &s_Value;
    else
        p_ResolvedValue = _rParam.p_ResolvedValue;
	// p_ResolvedValue = &s_VariableName;
}

void PddlParameter::SetValue (String& _rValue)
{
	s_Value = _rValue;
};


//																
String PddlParameter::GetPddlString (void) const
{
	return *p_ResolvedValue;
}



//																
PddlPredicate::PddlPredicate (void)
{
	l_Value = 0;
	b_IsFunction = false;
	i_PredicateCandidateIndex = -1;
	i_PredicateIdentityFeatureIndex = -1;
	i_PredicateNameFeatureIndex = -1;
	i_PredicateCandidateWithoutNumber = -1;
}

PddlPredicate::PddlPredicate (const PddlPredicate& _rPredicate)
{
	s_Name = ((PddlPredicate&)_rPredicate).s_Name;
	l_Value = ((PddlPredicate&)_rPredicate).l_Value;
	b_IsFunction = ((PddlPredicate&)_rPredicate).b_IsFunction;
	dq_Parameters = ((PddlPredicate&)_rPredicate).dq_Parameters;
	s_BoundIdentityHash = ((PddlPredicate&)_rPredicate).s_BoundIdentityHash;

	i_PredicateCandidateIndex = _rPredicate.i_PredicateCandidateIndex;
	i_PredicateIdentityFeatureIndex = _rPredicate.i_PredicateIdentityFeatureIndex;
	i_PredicateNameFeatureIndex = _rPredicate.i_PredicateNameFeatureIndex;
	i_PredicateCandidateWithoutNumber = _rPredicate.i_PredicateCandidateWithoutNumber;
	vec_ParameterValueFeatureIndex.Copy (_rPredicate.vec_ParameterValueFeatureIndex);

	// fix parameter bindings ...
	ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
	{
		PddlParameter& rParam = *ite;
		if (&rParam.s_Value == rParam.p_ResolvedValue)
			continue;
		rParam.s_Value = *rParam.p_ResolvedValue;
		rParam.p_ResolvedValue = &rParam.s_Value;
	}
}
    


String PddlPredicate::InstanceHash(void) const
{
    // NK: I added this where I dereference the p_ResolvedValue
    // because I wasn't sure if other code was relying on different hashing
    // also removed the type because it seemed unecessary and I didn't have it
	String sHash;
	sHash << s_Name << '\x01'; //<< b_IsFunction << '\x03';
	CONST_ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
	{
		const PddlParameter& rParam = *ite;
		sHash << *rParam.p_ResolvedValue << '\x02';
	}
	return sHash;
}



//																
String PddlPredicate::GetPddlString (void) const
{
	assert (false == b_IsFunction);

	String sPddl;
	if (true == b_IsFunction)
		sPddl << "(= (";
	else
		sPddl << "(";

	sPddl << s_Name;
	CONST_ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
		sPddl << ' ' << ite->GetPddlString ();

	if (true == b_IsFunction)
		sPddl << ") " << (int)l_Value;

	sPddl << ')';
	return sPddl;
}


//																
String& PddlPredicate::BoundIdentityHash (void)
{
	assert (false == b_IsFunction);

	if ("" == s_BoundIdentityHash)
	{
		s_BoundIdentityHash << s_Name << '\x01'; //<< b_IsFunction << '\x03';
		ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
		{
			PddlParameter& rParam = *ite;
			s_BoundIdentityHash << rParam.s_Type << '\x01'
								<< *rParam.p_ResolvedValue << '\x02';
		}
	}
	return s_BoundIdentityHash;
}


//																
String PddlPredicate::UnBoundIdentityHash (void)
{
	String sHash;
	sHash << s_Name << '\x01' << b_IsFunction << '\x03';
	ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
	{
		PddlParameter& rParam = *ite;
		sHash << rParam.s_Type << '\x02';
	}
	return sHash;
}


//																
bool PddlPredicate::operator== (const PddlPredicate& _rRight) const
{
	if (b_IsFunction != _rRight.b_IsFunction)
		return false;
	if (s_Name != _rRight.s_Name)
		return false;

	if (dq_Parameters.size () != _rRight.dq_Parameters.size ())
		return false;
	for (size_t i = 0; i < dq_Parameters.size (); ++i)
	{
		const PddlParameter& rLeftParam = dq_Parameters [i];
		const PddlParameter& rRightParam = _rRight.dq_Parameters [i];

		if ((NULL == rLeftParam.p_ResolvedValue) &&
			(NULL == rRightParam.p_ResolvedValue))
			continue;
		if ((NULL == rLeftParam.p_ResolvedValue) ^
			(NULL == rRightParam.p_ResolvedValue))
			return false;
		if (*rLeftParam.p_ResolvedValue != *rRightParam.p_ResolvedValue)
			return false;

		// if (dq_Parameters [i].s_Type != _rRight.dq_Parameters [i].s_Type)
		//	return false;
		//if (dq_Parameters [i].s_VariableName != _rRight.dq_Parameters [i].s_VariableName)
		//	return false;
	}
	return true;
}


//																
PddlFunctionValuePredicate::PddlFunctionValuePredicate (const PddlFunctionValuePredicate& _rPredicate)
	: PddlPredicate (_rPredicate)
{
	c_Operator = ((PddlFunctionValuePredicate&)_rPredicate).c_Operator;
}


//																
String PddlFunctionValuePredicate::InstanceHash(void) const
{
	String sHash;
	sHash << c_Operator << '\x01' << s_Name << '\x01';
	CONST_ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
	{
		const PddlParameter& rParam = *ite;
		sHash << *rParam.p_ResolvedValue << '\x02';
	}
	return sHash;
}



//																
String PddlFunctionValuePredicate::GetPddlString (void) const
{
	String sPddl;
	sPddl << "(" << c_Operator << " (" << s_Name;
	CONST_ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
		sPddl << ' ' << ite->GetPddlString ();

	sPddl << ") " << (int)l_Value << ')';
	return sPddl;
}


//																
String& PddlFunctionValuePredicate::BoundIdentityHash (void)
{
	if ("" == s_BoundIdentityHash)
	{
		s_BoundIdentityHash << s_Name << '\x01';
		ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
		{
			PddlParameter& rParam = *ite;
			s_BoundIdentityHash << rParam.s_Type << '\x01'
								<< *rParam.p_ResolvedValue << '\x02';
		}
	}
	return s_BoundIdentityHash;
}


String PddlFunctionValuePredicate::UnBoundIdentityHash (void)
{
	String sHash;
	sHash << c_Operator << '\x01' << s_Name << '\x01' << b_IsFunction << '\x03';
	ITERATE (PddlParameter_dq_t, dq_Parameters, ite)
	{
		PddlParameter& rParam = *ite;
		sHash << rParam.s_Type << '\x02';
	}
	return sHash;
}


//																
bool PddlFunctionValuePredicate::operator== (const PddlFunctionValuePredicate& _rRight) const
{
	if (c_Operator != _rRight.c_Operator)
		return false;
	return ((PddlPredicate&)*this == (PddlPredicate&)_rRight);
}


//																
PddlEffect::PddlEffect (const PddlEffect& _rEffect)
 : PddlPredicate (_rEffect)
{
	e_Effect = ((PddlEffect&)_rEffect).e_Effect;
	f_FunctionEffectValue = ((PddlEffect&)_rEffect).f_FunctionEffectValue;
	o_FunctionEffectValue = ((PddlEffect&)_rEffect).o_FunctionEffectValue;
	b_EffectValueIsPredicate = ((PddlEffect&)_rEffect).b_EffectValueIsPredicate;
}


//																
PddlAction::PddlAction (const PddlAction& _rAction)
{
    s_Name = ((PddlAction&)_rAction).s_Name;
    dq_Parameters = ((PddlAction&)_rAction).dq_Parameters;
    dq_Effects = ((PddlAction&)_rAction).dq_Effects;
    LinkEffectsToParameters ();
}


//																
void PddlAction::LinkEffectsToParameters (void)
{
	map<String,int>	mapVariableToIndex;
	for (size_t i = 0; i < dq_Parameters.size (); ++ i)
		mapVariableToIndex [dq_Parameters [i].s_VariableName] = i;
	
	ITERATE (PddlEffect_dq_t, dq_Effects, iteEffect)
	{
		PddlEffect& rEffect = *iteEffect;
		ITERATE (PddlParameter_dq_t, rEffect.dq_Parameters, iteParam)
		{
			PddlParameter& rVariable = *iteParam;
			if ('?' != rVariable.s_VariableName.at (0))
				// this is a literal value ...
				rVariable.p_ResolvedValue = &rVariable.s_VariableName;
			else
			{
				// this is a variable value...
				map<String,int>::iterator	ite;
				ite = mapVariableToIndex.find (rVariable.s_VariableName);
				if (mapVariableToIndex.end () == ite)
				{
					cerr << "   [EE] Variable in effect clause not found "
							"in action parameters." << endl;
					cout << rVariable.s_VariableName << endl;
					cout << *this << endl;
					assert (false);
				}
				int iParamIndex = mapVariableToIndex [rVariable.s_VariableName];
				PddlParameter& rParam = dq_Parameters [iParamIndex];
				rVariable.p_ResolvedValue = rParam.p_ResolvedValue;
			}
		}

        if (rEffect.b_EffectValueIsPredicate)
        {
            ITERATE (PddlParameter_dq_t, rEffect.o_FunctionEffectValue.dq_Parameters, iteParam)
            {
                PddlParameter& rVariable = *iteParam;
                if ('?' != rVariable.s_VariableName.at (0))
                    // this is a literal value ...
                    rVariable.p_ResolvedValue = &rVariable.s_VariableName;
                else
                {
                    // this is a variable value...
                    map<String,int>::iterator	ite;
                    ite = mapVariableToIndex.find (rVariable.s_VariableName);
                    if (mapVariableToIndex.end () == ite)
                    {
                        cerr << "   [EE] Variable in effect clause not found "
                                "in action parameters." << endl;
                        cout << rVariable.s_VariableName << endl;
                        cout << *this << endl;
                        assert (false);
                    }
                    int iParamIndex = mapVariableToIndex [rVariable.s_VariableName];
                    PddlParameter& rParam = dq_Parameters [iParamIndex];
                    rVariable.p_ResolvedValue = rParam.p_ResolvedValue;
                }
            }
        }
	}
}


//														
PddlDomain::~PddlDomain (void)
{
	ITERATE (NameToPddlAction_hmp_t, hmp_NameToActions, ite)
		delete ite->second;
	hmp_NameToActions.clear ();

	ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
		delete *ite;
	dq_Predicates.clear ();
}


//														
PddlState::PddlState (const PddlState& _rState)
{
    s_Preamble = _rState.s_Preamble;
    
    PddlPredicate_dq_t::const_iterator iter;
    for (iter = _rState.dq_Predicates.begin(); iter != _rState.dq_Predicates.end(); ++iter)
    {
		const PddlPredicate* pFrom = *iter;
		if (true == pFrom->b_IsFunction)
			dq_Predicates.push_back (new PddlFunctionValuePredicate (*(PddlFunctionValuePredicate*)pFrom));
		else
			dq_Predicates.push_back (new PddlPredicate (*pFrom));
    }
}


//														
PddlState::~PddlState (void)
{
	ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
		delete *ite;
	dq_Predicates.clear ();
}


//														
long PddlState::calcEffectValue(const PddlEffect& _rEffect,
                         const HashToPddlPredicate_hmp_t& _hmpPredicate)
{
    if (false == _rEffect.b_EffectValueIsPredicate)
        return _rEffect.f_FunctionEffectValue;

    else
    {
        String& hash = ((PddlPredicate&)_rEffect.o_FunctionEffectValue).BoundIdentityHash();
        // PddlPredicate* pPred = ((HashToPddlPredicate_hmp_t&)_hmpPredicate)[hash];
		HashToPddlPredicate_hmp_t::const_iterator	ite;
		ite = _hmpPredicate.find (hash);
		assert (_hmpPredicate.end () != ite);
		const PddlPredicate* pPred = ite->second;

        return pPred->l_Value;
    }
}


//														
void PddlState::UpdateToNextState (const PddlAction& _rAction,
								   PddlPredicate_dq_t& _rdqPredicates)
{
    // cout << _rAction << endl;
    HashToPddlPredicate_hmp_t hmpOldPredicate (2 * dq_Predicates.size ());

	CONST_ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
    {
		PddlPredicate* pPredicate = *ite;
        String& hash = pPredicate->BoundIdentityHash();
        // cout << hash << endl;
        hmpOldPredicate.insert (make_pair (hash, pPredicate));
    }


    // cout << "applying effects : " << _rAction.dq_Effects.size () << endl;
	CONST_ITERATE (PddlEffect_dq_t, _rAction.dq_Effects, ite)
    {
		PddlPredicate& rPredicate = (PddlPredicate&) *ite;
        String& hash = rPredicate.BoundIdentityHash();
        // cout << *ite << endl;
        // cout << hash << endl;
        if (pe_assign == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpOldPredicate [hash];
            long value = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value = value;
			pPred->s_BoundIdentityHash = "";

			PddlFunctionValuePredicate* pNewPred
				= new PddlFunctionValuePredicate (*(PddlFunctionValuePredicate*)pPred);
			_rdqPredicates.push_back (pNewPred);
        }
        else if (pe_increase == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpOldPredicate [hash];
            long inc = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value += inc;
			pPred->s_BoundIdentityHash = "";
    		// cout << inc << " " << (pPred->l_Value) << endl;

			PddlFunctionValuePredicate* pNewPred
				= new PddlFunctionValuePredicate (*(PddlFunctionValuePredicate*)pPred);
			_rdqPredicates.push_back (pNewPred);
        }
        else if (pe_decrease == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpOldPredicate[hash];
            long dec = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value -= dec;
			pPred->s_BoundIdentityHash = "";
     		// cout << dec << " " << (pPred->l_Value) << endl;
        }
        else if (pe_predicate_set == ite->e_Effect)
        {
            if (hmpOldPredicate.end() == hmpOldPredicate.find(hash))
            {
                PddlPredicate& ref = (PddlPredicate&)*ite;
                PddlPredicate *pPred = new PddlPredicate(ref);
                hmpOldPredicate.insert (make_pair (hash, pPred));
                pPred->l_Value = 1;
				pPred->s_BoundIdentityHash = "";

				dq_Predicates.push_back (pPred);
				_rdqPredicates.push_back (new PddlPredicate (*pPred));
            }
            else
            {
                PddlPredicate *pPred = hmpOldPredicate[hash];
                pPred->l_Value = 1;
				pPred->s_BoundIdentityHash = "";
				_rdqPredicates.push_back (new PddlPredicate (*pPred));
            }
        }
        else if (pe_predicate_clear == ite->e_Effect)
        {
            if (hmpOldPredicate.end() == hmpOldPredicate.find(hash))
            {
                PddlPredicate& ref = (PddlPredicate&)*ite;
                PddlPredicate *pPred = new PddlPredicate(ref);
                hmpOldPredicate.insert (make_pair (hash, pPred));
                pPred->l_Value = 0;
				pPred->s_BoundIdentityHash = "";

				dq_Predicates.push_back (pPred);
            }
            else
            {
                PddlPredicate *pPred = hmpOldPredicate [hash];
                pPred->l_Value = 0;
				pPred->s_BoundIdentityHash = "";
            }
        }
        else
        {
            cerr << "Unknown action effect type:" << endl;
            cerr << *ite << endl;
            assert(false);
        }
    }
}


//														
PddlState* PddlState::ComputeNextState(const PddlAction& _rAction)
{
    // cout << _rAction << endl;
    HashToPddlPredicate_hmp_t hmpOldPredicate (2 * dq_Predicates.size ());
    HashToPddlPredicate_hmp_t hmpNewPredicate (2 * dq_Predicates.size ());


	CONST_ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
    {
		PddlPredicate* pPredicate = *ite;

        String& hash = pPredicate->BoundIdentityHash();
        // cout << hash << endl;
        hmpOldPredicate.insert (make_pair (hash, pPredicate));
		if (true == pPredicate->b_IsFunction)
			hmpNewPredicate.insert (make_pair (hash, new PddlFunctionValuePredicate (*(PddlFunctionValuePredicate*)pPredicate)));
		else
			hmpNewPredicate.insert (make_pair (hash, new PddlPredicate (*pPredicate)));
    }


    // cout << "applying effects : " << _rAction.dq_Effects.size () << endl;
	CONST_ITERATE (PddlEffect_dq_t, _rAction.dq_Effects, ite)
    {
		PddlPredicate& rPredicate = (PddlPredicate&) *ite;
        String& hash = rPredicate.BoundIdentityHash();
        // cout << *ite << endl;
        // cout << hash << endl;
        if (pe_assign == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpNewPredicate[hash];
            long value = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value = value;
			pPred->s_BoundIdentityHash = "";
        }
        else if (pe_increase == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpNewPredicate[hash];
            long inc = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value += inc;
			pPred->s_BoundIdentityHash = "";
    		// cout << inc << " " << (pPred->l_Value) << endl;
        }
        else if (pe_decrease == ite->e_Effect)
        {
            PddlPredicate *pPred = hmpNewPredicate[hash];
            long dec = long (calcEffectValue(*ite, hmpOldPredicate));
            pPred->l_Value -= dec;
			pPred->s_BoundIdentityHash = "";
     		// cout << dec << " " << (pPred->l_Value) << endl;
        }
        else if (pe_predicate_set == ite->e_Effect)
        {
            if (hmpNewPredicate.end() == hmpNewPredicate.find(hash))
            {
                PddlPredicate& ref = (PddlPredicate&)*ite;
                PddlPredicate *pPred = new PddlPredicate(ref);
                hmpNewPredicate.insert(make_pair(hash, pPred));
                pPred->l_Value = 1;
				pPred->s_BoundIdentityHash = "";
            }
            else
            {
                PddlPredicate *pPred = hmpNewPredicate[hash];
                pPred->l_Value = 1;
				pPred->s_BoundIdentityHash = "";
            }
        }
        else if (pe_predicate_clear == ite->e_Effect)
        {
            if (hmpNewPredicate.end() == hmpNewPredicate.find(hash))
            {
                PddlPredicate& ref = (PddlPredicate&)*ite;
                PddlPredicate *pPred = new PddlPredicate(ref);
                hmpNewPredicate.insert(make_pair(hash, pPred));
                pPred->l_Value = 0;
				pPred->s_BoundIdentityHash = "";
            }
            else
            {
                PddlPredicate *pPred = hmpNewPredicate[hash];
                pPred->l_Value = 0;
				pPred->s_BoundIdentityHash = "";
            }
        }
        else
        {
            cerr << "Unknown action effect type:" << endl;
            cerr << *ite << endl;
            assert(false);
        }
    }


    PddlState* state = new PddlState();
    state->s_Preamble = s_Preamble;
    ITERATE (HashToPddlPredicate_hmp_t, hmpNewPredicate, it)
        state->dq_Predicates.push_back(it->second);


    return state;
}


//																
String PddlState::GetPddlString (void)
{
	String sPddl;
	sPddl << "(define \n"
		  << s_Preamble
		  << "\n\n"
		  << "(:init\n"
		  << PddlState::GetPredicatePddlString ()
		  << "\n)\n)";

	return sPddl;
}


//																
String PddlState::GetPredicatePddlString (void)
{
	String_set_t setPredicates;
	ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
	{
		PddlPredicate* pPredicate = *ite;
		if (true == pPredicate->b_IsFunction)
			setPredicates.insert (pPredicate->GetPddlString ());
		else if (0 != pPredicate->l_Value)
			setPredicates.insert (pPredicate->GetPddlString ());
	}

	String sPddl;
	ITERATE (String_set_t, setPredicates, ite)
		sPddl << *ite << '\n';
	return sPddl;
}


//																
bool PddlState::operator== (const PddlState& _rRight) const
{
	if (s_Preamble != _rRight.s_Preamble)
		return false;
	size_t iPredicates = dq_Predicates.size ();
	if (_rRight.dq_Predicates.size () != iPredicates)
		return false;

	String_set_t setLeft;
	CONST_ITERATE (PddlPredicate_dq_t, dq_Predicates, ite)
		setLeft.insert ((*ite)->GetPddlString ());

	String_set_t setRight;
	CONST_ITERATE (PddlPredicate_dq_t, _rRight.dq_Predicates, ite)
		setRight.insert ((*ite)->GetPddlString ());

	String_set_t::const_iterator	iteLeft = setLeft.begin ();
	String_set_t::const_iterator	iteRight = setRight.begin ();
	for (; iteLeft != setLeft.end (), iteRight != setRight.end ();
		 ++ iteLeft, ++ iteRight)
	{
		if (*iteLeft != *iteRight)
			return false;
	}

	return true;
}


//																
String PddlProblem::GetPddlString (void)
{
	String sPddl;
	sPddl << "(define \n"
		  << o_StartState.s_Preamble
		  << "\n\n"
		  << "(:init\n"
		  << o_StartState.GetPredicatePddlString ()
		  << "\n)"
		  << "(:goal\n"
		  << o_PartialGoalState.GetPredicatePddlString ()
		  << "\n)\n)";

	return sPddl;
}


//																
PddlPlan::~PddlPlan (void)
{
	ITERATE (PddlAction_dq_t, dq_Actions, ite)
		delete *ite;
	dq_Actions.clear ();
}


//																
ostream& operator<< (ostream& _rStream, const PddlParameter& _rParam)
{
	if ("" != _rParam.s_Type)
		_rStream << _rParam.s_Type << ' ';
	_rStream << _rParam.s_VariableName;
	if ((NULL != _rParam.p_ResolvedValue) &&
		("" != *_rParam.p_ResolvedValue))
		_rStream << " = " << *_rParam.p_ResolvedValue;
	return _rStream;
}


//																
ostream& operator<< (ostream& _rStream, const PddlParameter_dq_t& _rdqParam)
{
	for (size_t i = 0; i < _rdqParam.size (); ++ i)
	{
		if (i > 0)
			_rStream << ',';
		const PddlParameter& rParam = _rdqParam [i];
		_rStream << rParam;
	}
	return _rStream;
}


//																
ostream& operator<< (ostream& _rStream, const PddlPredicate& _rPredicate)
{
	_rStream << _rPredicate.s_Name;
	if (true == _rPredicate.b_IsFunction)
		_rStream << "(";
	else
		_rStream << "<";
	_rStream << _rPredicate.dq_Parameters;
	if (true == _rPredicate.b_IsFunction)
		_rStream << ") = " << _rPredicate.l_Value;
	else
		_rStream << ">" << _rPredicate.l_Value;
	return _rStream;
}

//																
ostream& operator<< (ostream& _rStream, const PddlFunctionValuePredicate& _rPredicate)
{
	_rStream << _rPredicate.s_Name << "(" << _rPredicate.dq_Parameters;
	_rStream << ") " << _rPredicate.c_Operator << ' ' << _rPredicate.l_Value;
	return _rStream;
}

//																
ostream& operator<< (ostream& _rStream, const PddlEffect& _rEffect)
{
	if (pe_assign == _rEffect.e_Effect)
		_rStream << "[= ";
	else if (pe_increase == _rEffect.e_Effect)
		_rStream << "[+ ";
	else if (pe_decrease == _rEffect.e_Effect)
		_rStream << "[- ";

	if ((pe_assign == _rEffect.e_Effect) ||
		(pe_increase == _rEffect.e_Effect) ||
		(pe_decrease == _rEffect.e_Effect))
	{
		if (true == _rEffect.b_EffectValueIsPredicate)
			_rStream << _rEffect.o_FunctionEffectValue << "] ";
		else
			_rStream << _rEffect.f_FunctionEffectValue << "] ";
	}

	else if (pe_predicate_set == _rEffect.e_Effect)
		_rStream << "[1] ";
	else if (pe_predicate_clear == _rEffect.e_Effect)
		_rStream << "[0] ";

	_rStream << _rEffect.s_Name;
	_rStream << '(' << _rEffect.dq_Parameters << ')';
	return _rStream;
}


//																
ostream& operator<< (ostream& _rStream, const PddlAction& _rAction)
{
	_rStream << _rAction.s_Name << endl;
	_rStream << "[PARAMS]:" << endl;
	ITERATE (PddlParameter_dq_t, ((PddlAction&)_rAction).dq_Parameters, ite)
		_rStream << "   " << *ite << endl;
	_rStream << "[EFFECTS]:" << endl;
	ITERATE (PddlEffect_dq_t, ((PddlAction&)_rAction).dq_Effects, ite)
		_rStream << "   " << *ite << endl;

	return _rStream;
}


//																
ostream& operator<< (ostream& _rStream, const PddlDomain& _rDomain)
{
	ITERATE (PddlPredicate_dq_t, ((PddlDomain&)_rDomain).dq_Predicates, ite)
		_rStream << **ite << endl;
	_rStream << endl;
	ITERATE (NameToPddlAction_hmp_t, ((PddlDomain&)_rDomain).hmp_NameToActions, ite)
		_rStream << *ite->second << endl;

	return _rStream;
}

//																
ostream& operator<< (ostream& _rStream, const PddlState& _rProblem)
{
	_rStream << _rProblem.s_Preamble << endl << endl;
	ITERATE (PddlPredicate_dq_t, ((PddlState&)_rProblem).dq_Predicates, ite)
		_rStream << **ite << endl;

	return _rStream;
}

//																
ostream& operator<< (ostream& _rStream, const PddlProblem& _rProblem)
{
	_rStream << _rProblem.o_StartState.s_Preamble << endl << endl;
	_rStream << "(:init " << endl;
	ITERATE (PddlPredicate_dq_t, ((PddlState&)_rProblem.o_StartState).dq_Predicates, ite)
		_rStream << **ite << endl;
	_rStream << ")\n(:goal " << endl;
	ITERATE (PddlPredicate_dq_t, ((PddlState&)_rProblem.o_PartialGoalState).dq_Predicates, ite)
		_rStream << **ite << endl;
	_rStream << ')';

	return _rStream;
}



