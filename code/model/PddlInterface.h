#ifndef __PDDL_INTERFACE__
#define __PDDL_INTERFACE__

#include <math.h>
#include <nlp_string.h>
#include <nlp_string.h>
#include <hash_map>
#include "Pddl.h"
#include <antlr3.h>
using namespace std;

//														
class PddlInterface
{
	private:
		static const char* ToString (ANTLR3_BASE_TREE* _pTree)
		{
			ANTLR3_COMMON_TREE* pSuper = (ANTLR3_COMMON_TREE*)_pTree->super;
			/*
			if (NULL == pSuper)
				return "super is null";
			if (NULL == pSuper->token)
				return "super->token is null";
			if ((NULL == pSuper) ||
				(NULL == pSuper->token))
				return "";
				*/

			if (ANTLR3_TEXT_STRING == pSuper->token->textState)
			{
				// cout << "string type is ANTLR3_TEXT_STRING" << endl;
				return (const char*)pSuper->token->tokText.text;
			}
			else if (ANTLR3_TEXT_CHARP == pSuper->token->textState)
			{
				// cout << "string type is ANTLR3_TEXT_CHARP" << endl;
				// if (NULL == pSuper->token->tokText.chars)
					// return "super->token->toktext.chars is null";
				return (const char*) pSuper->token->tokText.chars;
			}
			else if (ANTLR3_TOKEN_EOF == pSuper->token->type)
			{
				// cout << "string type is EOF" << endl;
				return "";
			}
			else if (NULL != pSuper->token->input)
			{
				// cout << "string type is INPUT" << endl;
				ANTLR3_COMMON_TOKEN* pToken = pSuper->token;
				ANTLR3_STRING* pString = pToken->input->substr (pToken->input,
											  pToken->getStartIndex (pToken),
											  pToken->getStopIndex (pToken));
				return (const char*) pString->chars;
			}

			return "";

			// ANTLR3_STRING* pString = _pTree->toString (_pTree);
			// return (const char*) pString->chars;
		}
		static const char* ToTree (ANTLR3_BASE_TREE* _pTree)
		{
			ANTLR3_STRING* pString = _pTree->toStringTree (_pTree);
			return (const char*) pString->chars;
		}

		static void ParsePddlParameters (ANTLR3_BASE_TREE* _pTree,
										 PddlParameter_dq_t* _pdqParams,
										 int _iStartingIndex = 0);
		static void ParsePddlEffects (ANTLR3_BASE_TREE* _pTree,
									  PddlEffect_dq_t* _pdqEffects);
		static PddlPredicate* ParsePddlPredicate (ANTLR3_BASE_TREE* _pTree,
												  bool _bIsFunction);
		static PddlAction* ParsePddlAction (ANTLR3_BASE_TREE* _pTree);

		static PddlPredicate* ParsePddlInit (ANTLR3_BASE_TREE* _pTree);
		static PddlPredicate* ParsePddlGoal (ANTLR3_BASE_TREE* _pTree);

	public:
		static String ConstructProblemPddl (String& _rStartState,
											String& _rTargetState);

		//static PddlState* ComputeEndState (PddlDomain& _rDomain,
		//									PddlProblem& _rProblem,
		//									PddlPlan& _rPlan);
		static PddlState* ComputeEndStateFast (const PddlProblem& _rProblem,
											   const PddlPlan& _rPlan,
											   PddlPredicate_dq_t& _rdqPredicates);

		static PddlState* ComputeApproximateFutureInit (const PddlState& _rInit,
													   PddlPredicate_dq_t& _rdqPredicates);


		static PddlDomain* ParseDomainPddl (String& _rDomain);
		static PddlProblem* ParseProblemPddl (String& _rProblem);
		static PddlPlan* ParsePlan (PddlDomain& _rDomain, String& _rPlan);
};


#endif
