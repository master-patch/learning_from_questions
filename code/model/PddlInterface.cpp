#include "PddlParser.h"
#include "PddlLexer.h"
// [WARNING !!!]									
// PddlParser.h and PddlLexer.h have to be before	
// PddlInterface.h.  Otherwise we get weird errors.	
// [WARNING !!!]									
#include "PddlInterface.h"
#include <nlp_config.h>
#include <nlp_macros.h>
#include <assert.h>


//												
void PddlInterface::ParsePddlParameters (ANTLR3_BASE_TREE* _pTree,
										 PddlParameter_dq_t* _pdqParams,
										 int _iStartingIndex)
{
	long iParameters = _pTree->getChildCount (_pTree);
	for (int i = _iStartingIndex; i < iParameters; ++ i)
	{
		_pdqParams->push_back (PddlParameter ());
		PddlParameter& rParam = _pdqParams->back ();

		ANTLR3_BASE_TREE* pParam = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, i);	
		rParam.s_VariableName = ToString (pParam);
		// cout << "param variable name : " << rParam.s_VariableName << endl;
        if ('?' != rParam.s_VariableName.at (0))
            rParam.p_ResolvedValue = &rParam.s_VariableName;

		if (1 == pParam->getChildCount (pParam))
		{
			ANTLR3_BASE_TREE* pType = (ANTLR3_BASE_TREE*) pParam->getChild (pParam, 0);	
			rParam.s_Type = ToString (pType);
			// cout << "param variable type : " << rParam.s_Type << endl;
		}
	}
}


//												
void PddlInterface::ParsePddlEffects (ANTLR3_BASE_TREE* _pTree,
									  PddlEffect_dq_t* _pdqEffects)
{
	#ifndef NDEBUG
	int iBase = _pTree->getChildCount (_pTree);
	assert (1 == iBase);
	#endif

	ANTLR3_BASE_TREE* pEffectTree = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);
	int iEffects = pEffectTree->getChildCount (pEffectTree);

	for (int i = 0; i < iEffects; ++ i)
	{
		_pdqEffects->push_back (PddlEffect ());
		PddlEffect& rEffect = _pdqEffects->back ();

		ANTLR3_BASE_TREE* pEffect = (ANTLR3_BASE_TREE*) pEffectTree->getChild (pEffectTree, i);	
		String sToken (ToString (pEffect));
		// cout << "effect type : " << sToken << endl;
		if ("PRED_HEAD" == sToken)
		{
			// predicate being set true...
			int iEffectAttrs = pEffect->getChildCount (pEffect);
			assert (iEffectAttrs > 0);
			ANTLR3_BASE_TREE* pPredicateName
				= (ANTLR3_BASE_TREE*) pEffect->getChild (pEffect, 0);
			rEffect.s_Name = ToString (pPredicateName);
			// cout << "effect predicate : " << rEffect.s_Name << endl;
			rEffect.e_Effect = pe_predicate_set;

			if (iEffectAttrs > 1)
				ParsePddlParameters (pEffect, &rEffect.dq_Parameters, 1);
		}
		else if ("NOT_EFFECT" == sToken)
		{
			// predicate being set false ...
			assert (1 == pEffect->getChildCount (pEffect));
			ANTLR3_BASE_TREE* pChild
				= (ANTLR3_BASE_TREE*) pEffect->getChild (pEffect, 0);

			int iEffectAttrs = pChild->getChildCount (pChild);
			assert (iEffectAttrs > 0);
			ANTLR3_BASE_TREE* pPredicateName
				= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, 0);
			rEffect.s_Name = ToString (pPredicateName);
			// cout << "effect not predicate : " << rEffect.s_Name << endl;
			rEffect.e_Effect = pe_predicate_clear;

			if (iEffectAttrs > 1)
				ParsePddlParameters (pChild, &rEffect.dq_Parameters, 1);
		}
		else if ("ASSIGN_EFFECT" == sToken)
		{
			// function ...
			int iEffectAttrs = pEffect->getChildCount (pEffect);
			assert (3 == iEffectAttrs);

			// effect type ...
			ANTLR3_BASE_TREE* pEffectType
				= (ANTLR3_BASE_TREE*) pEffect->getChild (pEffect, 0);
			String sEffectType (ToString (pEffectType));
			// cout << "function effect type : " << sEffectType << endl;
			if ("assign" == sEffectType)
				rEffect.e_Effect = pe_assign;
			else if ("increase" == sEffectType)
				rEffect.e_Effect = pe_increase;
			else if ("decrease" == sEffectType)
				rEffect.e_Effect = pe_decrease;


			// function name + params
			ANTLR3_BASE_TREE* pFunction
				= (ANTLR3_BASE_TREE*) pEffect->getChild (pEffect, 1);
			// cout << "function effect head : " << ToString (pFunction) << endl;
			assert (0 == strcmp ("FUNC_HEAD", ToString (pFunction)));

			iEffectAttrs = pFunction->getChildCount (pFunction);
			ANTLR3_BASE_TREE* pFunctionName
				= (ANTLR3_BASE_TREE*) pFunction->getChild (pFunction, 0);
			rEffect.s_Name = ToString (pFunctionName);
			// cout << "function effect name : " << rEffect.s_Name << endl;

			if (iEffectAttrs > 1)
				ParsePddlParameters (pFunction, &rEffect.dq_Parameters, 1);


			// effect value ...
			ANTLR3_BASE_TREE* pEffectValue
				= (ANTLR3_BASE_TREE*) pEffect->getChild (pEffect, 2);
			String sEffectValue (ToString (pEffectValue));
			// cout << "function effect value : " << sEffectValue << endl;
			if (true == sEffectValue.IsDigit ())
				rEffect.f_FunctionEffectValue = (double) sEffectValue;
			else
			{
				assert ("FUNC_HEAD" == sEffectValue);
				rEffect.b_EffectValueIsPredicate = true;

				iEffectAttrs = pEffectValue->getChildCount (pEffectValue);
				ANTLR3_BASE_TREE* pFunctionName
					= (ANTLR3_BASE_TREE*) pEffectValue->getChild (pEffectValue, 0);
				rEffect.o_FunctionEffectValue.s_Name = ToString (pFunctionName);
				// cout << "func effect value name : " << rEffect.o_FunctionEffectValue.s_Name << endl;

				if (iEffectAttrs > 1)
					ParsePddlParameters (pEffectValue,
										 &rEffect.o_FunctionEffectValue.dq_Parameters,
										 1);
			}
		}
	}
}


//												
PddlPredicate* PddlInterface::ParsePddlPredicate (ANTLR3_BASE_TREE* _pTree,
												  bool _bIsFunction)
{
	PddlPredicate* pPredicate = NULL;
	if (true == _bIsFunction)
		pPredicate = new PddlFunctionValuePredicate;
	else
		pPredicate = new PddlPredicate;
	pPredicate->b_IsFunction = _bIsFunction;
	pPredicate->s_Name = ToString (_pTree);
	// cout << "predicate name : " << pPredicate->s_Name << endl;

	ParsePddlParameters (_pTree, &pPredicate->dq_Parameters);
	return pPredicate;
}


//												
PddlAction* PddlInterface::ParsePddlAction (ANTLR3_BASE_TREE* _pTree)
{
	PddlAction* pAction = new PddlAction;
	long iChildren = _pTree->getChildCount (_pTree);
	assert (iChildren > 1);

	{ // Name
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);	
		pAction->s_Name = ToString (pChild);
		// cout << "action name : " << pAction->s_Name << endl;
	}

	for (int i = 1; i < iChildren; ++ i)
	{
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, i);	
		String sToken (ToString (pChild));
		// cout << "action info : " << sToken << endl;
		if ("PARAMETERS" == sToken)
		{
			ParsePddlParameters (pChild, &pAction->dq_Parameters);
			continue;
		}

		if ("EFFECT" == sToken)
		{
			ParsePddlEffects (pChild, &pAction->dq_Effects);
			continue;
		}
	}

	return pAction;
}


//												
PddlDomain* PddlInterface::ParseDomainPddl (String& _rDomain)
{
	size_t iLength = _rDomain.length ();
	ANTLR3_UINT8* pText = ANTLR3_STRDUP (_rDomain);

	ANTLR3_INPUT_STREAM* paisDomain;
	paisDomain = antlr3NewAsciiStringInPlaceStream (pText, iLength, NULL);
	PddlLexer* pLexer = PddlLexerNew (paisDomain);

	ANTLR3_COMMON_TOKEN_STREAM* pTokenStream;
	pTokenStream = antlr3CommonTokenStreamSourceNew (ANTLR3_SIZE_HINT, TOKENSOURCE(pLexer));
	
	PddlParser* pParser = PddlParserNew (pTokenStream);
	PddlParser_getDomain_return oAST = pParser->getDomain (pParser);

	PddlDomain* pDomain = new PddlDomain;

	long iChildren = oAST.tree->getChildCount (oAST.tree);
	for (long c = 0; c < iChildren; ++ c)
	{
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) oAST.tree->getChild (oAST.tree, c);	
		String sToken (ToString (pChild));
		// cout << "domain info : " << sToken << endl;
		if ("TYPES" == sToken)
			continue;

		bool bIsPredicate = ("PREDICATES" == sToken);
		bool bIsFunction = ("FUNCTIONS" == sToken);
		bool bIsAction = ("ACTION" == sToken);

		if (bIsPredicate || bIsFunction)
		{
			long iGrandChildren = pChild->getChildCount (pChild);
			for (long t = 0; t < iGrandChildren; ++ t)
			{
				ANTLR3_BASE_TREE* pPredicateTree
					= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, t);	
				PddlPredicate* pPredicate
					= ParsePddlPredicate (pPredicateTree, bIsFunction);
				pDomain->dq_Predicates.push_back (pPredicate);
			}
		}

		if (bIsAction)
		{
			PddlAction* pAction = ParsePddlAction (pChild);
			pAction->LinkEffectsToParameters ();
			pDomain->hmp_NameToActions.insert (make_pair (pAction->s_Name, pAction));
		}
	}

	pParser->free (pParser);
	pLexer->free (pLexer);
	pTokenStream->free (pTokenStream);
	paisDomain->close (paisDomain);
	ANTLR3_FREE (pText);

	return pDomain;
}


//												
PddlPredicate* PddlInterface::ParsePddlInit (ANTLR3_BASE_TREE* _pTree)
{
	String sType = ToString (_pTree);
	PddlPredicate* pPredicate = NULL;
	if ("PRED_INST" == sType)
	{
		pPredicate = new PddlPredicate;
		int iPredicateAttr = _pTree->getChildCount (_pTree);
		assert (iPredicateAttr > 0);

		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);	
		pPredicate->s_Name = ToString (pChild);
		pPredicate->l_Value = 1;

		if (iPredicateAttr > 1)
			ParsePddlParameters (_pTree, &pPredicate->dq_Parameters, 1);
	}
	else if ("INIT_EQ" == sType)
	{
		pPredicate = new PddlFunctionValuePredicate;
		((PddlFunctionValuePredicate*)pPredicate)->c_Operator = '=';

		#ifndef NDEBUG
		int iFunctionAttr = _pTree->getChildCount (_pTree);
		assert (iFunctionAttr > 0);
		#endif

		// function ...			
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);	
		assert (0 == strcmp ("FUNC_HEAD", ToString (pChild)));

		int iFunctionParams = pChild->getChildCount (pChild);
		assert (iFunctionParams > 0);
		ANTLR3_BASE_TREE* pFunction = (ANTLR3_BASE_TREE*) pChild->getChild (pChild, 0);	
		pPredicate->s_Name = ToString (pFunction);
		pPredicate->b_IsFunction = true;

		if (iFunctionParams > 1)
			ParsePddlParameters (pChild, &pPredicate->dq_Parameters, 1);

		// value ...			
		ANTLR3_BASE_TREE* pValue = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 1);	
		String sValue = ToString (pValue);
		pPredicate->l_Value = (long)sValue;
        //cout << sValue << "::" << pPredicate->l_Value << endl;

	}

	return pPredicate;
}


//												
PddlPredicate* PddlInterface::ParsePddlGoal (ANTLR3_BASE_TREE* _pTree)
{
	String sType = ToString (_pTree);
	PddlPredicate* pPredicate = NULL;

	if ("PRED_HEAD" == sType)
	{
		// (PRED_HEAD connect m4_4 m4_3)
		pPredicate = new PddlPredicate;

		int iPredicateAttr = _pTree->getChildCount (_pTree);
		assert (iPredicateAttr > 1);

		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);	
		pPredicate->s_Name = ToString (pChild);
		pPredicate->l_Value = 1;

		if (iPredicateAttr > 1)
			ParsePddlParameters (_pTree, &pPredicate->dq_Parameters, 1);
	}

	else if ("COMPARISON_GD" == sType)
	{
		// (COMPARISON_GD > (FUNC_HEAD thing-available wood-pickaxe) 0)
		pPredicate = new PddlFunctionValuePredicate;

		#ifndef NDEBUG
		int iFunctionAttr = _pTree->getChildCount (_pTree);
		assert (iFunctionAttr > 0);
		#endif

		// function ...			
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 0);	
		String sOperator = ToString (pChild);
		if (1 != sOperator.length ())
			abort ();
		((PddlFunctionValuePredicate*)pPredicate)->c_Operator = sOperator [0];

		ANTLR3_BASE_TREE* pFunction = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 1);	
		int iFunctionParams = pFunction->getChildCount (pFunction);
		// assert (iFunctionParams > 1);
		assert (0 == strcmp ("FUNC_HEAD", ToString (pFunction)));
		
		ANTLR3_BASE_TREE* pFunctionName = (ANTLR3_BASE_TREE*) pFunction->getChild (pFunction, 0);
		pPredicate->s_Name = ToString (pFunctionName);
		pPredicate->b_IsFunction = true;

		if (iFunctionParams > 1)
			ParsePddlParameters (pFunction, &pPredicate->dq_Parameters, 1);

		// value ...			
		ANTLR3_BASE_TREE* pValue = (ANTLR3_BASE_TREE*) _pTree->getChild (_pTree, 2);
		String sValue = ToString (pValue);
		pPredicate->l_Value = (long)sValue;
	}

	return pPredicate;
}


//												
PddlProblem* PddlInterface::ParseProblemPddl (String& _rProblem)
{
	size_t iLength = _rProblem.length ();
	ANTLR3_UINT8* pText = ANTLR3_STRDUP (_rProblem);

	ANTLR3_INPUT_STREAM* paisDomain;
	paisDomain = antlr3NewAsciiStringInPlaceStream (pText, iLength, NULL);
	PddlLexer* pLexer = PddlLexerNew (paisDomain);

	ANTLR3_COMMON_TOKEN_STREAM* pTokenStream;
	pTokenStream = antlr3CommonTokenStreamSourceNew (ANTLR3_SIZE_HINT, TOKENSOURCE(pLexer));
	
	PddlParser* pParser = PddlParserNew (pTokenStream);
	PddlParser_getProblem_return oAST = pParser->getProblem (pParser);

	PddlProblem* pProblem = new PddlProblem;
	long iChildren = oAST.tree->getChildCount (oAST.tree);
	for (long c = 0; c < iChildren; ++ c)
	{
		ANTLR3_BASE_TREE* pChild = (ANTLR3_BASE_TREE*) oAST.tree->getChild (oAST.tree, c);
		// cout << ToTree (pChild) << endl;
		String sToken (ToString (pChild));

		if ("PROBLEM_NAME" == sToken)
		{
			assert (1 == pChild->getChildCount (pChild));
			ANTLR3_BASE_TREE* pGrandChild
				= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, 0);

			pProblem->o_StartState.s_Preamble << "(problem "
											  << ToString (pGrandChild)
											  << ")\n";
		}

		else if ("PROBLEM_DOMAIN" == sToken)
		{
			assert (1 == pChild->getChildCount (pChild));
			ANTLR3_BASE_TREE* pGrandChild
				= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, 0);

			pProblem->o_StartState.s_Preamble << "(:domain "
											  << ToString (pGrandChild)
											  << ")\n";
		}

		else if ("OBJECTS" == sToken)
		{
			pProblem->o_StartState.s_Preamble << "(:objects\n";

			long iObjects = pChild->getChildCount (pChild);
			for (long o = 0; o < iObjects; ++ o)
			{
				ANTLR3_BASE_TREE* pObject
					= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, o);	
				assert (1 == pObject->getChildCount (pObject));
				ANTLR3_BASE_TREE* pObjectType
					= (ANTLR3_BASE_TREE*) pObject->getChild (pObject, 0);	

				pProblem->o_StartState.s_Preamble << ToString (pObject)
												  << " - "
												  << ToString (pObjectType)
												  << '\n';
			}

			pProblem->o_StartState.s_Preamble << ")\n";
		}

		else if ("INIT" == sToken)
		{
			long iPredicates = pChild->getChildCount (pChild);
			for (long t = 0; t < iPredicates; ++ t)
			{
				ANTLR3_BASE_TREE* pPredicateTree
					= (ANTLR3_BASE_TREE*) pChild->getChild (pChild, t);	
				PddlPredicate* pPredicate = ParsePddlInit (pPredicateTree);
				pProblem->o_StartState.dq_Predicates.push_back (pPredicate);
			}
		}
		
		else if ("GOAL" == sToken)
		{
			assert (1 == pChild->getChildCount (pChild));
			ANTLR3_BASE_TREE* pGoalTree = (ANTLR3_BASE_TREE*) pChild->getChild (pChild, 0);
			String sToken (ToString (pGoalTree));
			if ("AND_GD" != sToken)
				pGoalTree = pChild;

			long iPredicates = pGoalTree->getChildCount (pGoalTree);
			for (long t = 0; t < iPredicates; ++ t)
			{
				ANTLR3_BASE_TREE* pPredicateTree
					= (ANTLR3_BASE_TREE*) pChild->getChild (pGoalTree, t);	
				PddlPredicate* pPredicate = ParsePddlGoal (pPredicateTree);
				pProblem->o_PartialGoalState.dq_Predicates.push_back (pPredicate);
			}
		}
	}

	pParser->free (pParser);
	pLexer->free (pLexer);
	pTokenStream->free (pTokenStream);
	paisDomain->close (paisDomain);
	ANTLR3_FREE (pText);


	return pProblem;
}


//												
PddlPlan* PddlInterface::ParsePlan (PddlDomain& _rDomain, String& _rPlan)
{
    PddlPlan* pPlan = new PddlPlan();
    String_dq_t dqActionStrs;
	
	String sPlan (_rPlan);
	sPlan.LowerCase ();
    sPlan.Split (dqActionStrs, '\n');
    
    ITERATE (String_dq_t, dqActionStrs, iter)
    {
        if (0 == iter->length())
			continue;
        String_dq_t dqTokens;
        iter->Split(dqTokens, ' ');
        String& sName = dqTokens[0];
         
        if (_rDomain.hmp_NameToActions.find (sName) == _rDomain.hmp_NameToActions.end())
        {
            cerr << "Could not find action \"" << sName << "\" in domain." << endl;
            
            assert(false);
        }
        else
        {
            PddlAction* pAction = _rDomain.hmp_NameToActions[sName];
            PddlAction* pBindAction = new PddlAction (*pAction);
            if (dqTokens.size() != pBindAction->dq_Parameters.size() + 1)
            {
                cerr << "Number of parameters doesn't match: " << *iter;
                assert(false);
            }
            for (size_t i = 1; i < dqTokens.size(); ++i)
                pBindAction->dq_Parameters[i-1].SetValue (dqTokens[i]);

            pPlan->dq_Actions.push_back(pBindAction);
        }
    }
    return pPlan;
}


//												
/*
PddlState* PddlInterface::ComputeEndState (PddlDomain& _rDomain,
                                            PddlProblem& _rProblem,
                                            PddlPlan& _rPlan)
{
    PddlState* pState = &_rProblem.o_StartState;
	PddlState* pDeleteState = NULL;
    ITERATE (PddlAction_dq_t, _rPlan.dq_Actions, iter) 
    {
        PddlState* pNextState = pState->ComputeNextState (**iter);
        pState = pNextState;
		if (NULL != pDeleteState)
			delete pDeleteState;
		pDeleteState = pNextState;
    }

	#ifndef NDEBUG
	PddlState* pTest = ComputeEndStateFast (_rDomain, _rProblem, _rPlan);
	assert (*pTest == *pState);
	#endif

    return pState;
}
*/


//												
PddlState* PddlInterface::ComputeEndStateFast (const PddlProblem& _rProblem,
                                               const PddlPlan& _rPlan,
											   PddlPredicate_dq_t& _rdqPredicates)
{
	PddlState* pNewState = new PddlState (_rProblem.o_StartState);
    CONST_ITERATE (PddlAction_dq_t, _rPlan.dq_Actions, iter) 
    {
		PddlAction* pAction = *iter;
        pNewState->UpdateToNextState (*pAction, _rdqPredicates);
    }

    return pNewState;
}


//												
PddlState* PddlInterface::ComputeApproximateFutureInit (const PddlState& _rInit,
														PddlPredicate_dq_t& _rdqPredicates)
{
    PddlState* pNewState = new PddlState (_rInit);
    HashToPddlPredicate_hmp_t hmpPredicate (2 * pNewState->dq_Predicates.size ());
    
    ITERATE (PddlPredicate_dq_t, pNewState->dq_Predicates, ite)
    {
        PddlPredicate* pPredicate = *ite;
        String& hash = pPredicate->BoundIdentityHash ();
        hmpPredicate.insert (make_pair (hash, pPredicate));
    }

    ITERATE (PddlPredicate_dq_t, _rdqPredicates, ite)
    {
        PddlPredicate* pPredicate = *ite;
        String& hash = pPredicate->BoundIdentityHash ();
        
        HashToPddlPredicate_hmp_t::iterator itFind = hmpPredicate.find (hash);
        if (hmpPredicate.end () == itFind)
        {
            // Not sure if creating new instance is needed.
            PddlPredicate * pNewPred = new PddlPredicate (*pPredicate);
            pNewPred->s_BoundIdentityHash = "";

            hmpPredicate.insert (make_pair (hash, pNewPred)); 
            pNewState->dq_Predicates.push_back (pNewPred);
        }
        else
        {
            PddlPredicate *pStatePred = itFind->second;
            // for boolean predicate, just change the value (True / False)
            if (false == pStatePred->b_IsFunction)
                pStatePred->l_Value = pPredicate->l_Value;

            // for function predicate (e.g. thing-available), change value
			// if it is increased.
            else
            {
                if (pPredicate->l_Value > pStatePred->l_Value)
                    pStatePred->l_Value = pPredicate->l_Value;
            }
        }
    }

    return pNewState;
}




