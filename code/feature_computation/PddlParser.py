# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 Pddl.g 2011-11-28 11:16:31

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
REQUIRE_KEY=46
FUNCTIONS=10
LETTER=49
PRED_INST=42
TYPES=7
EXISTS_GD=27
EOF=-1
COMPARISON_GD=29
ACTION=13
T__93=93
ANY_CHAR=50
T__94=94
NOT_EFFECT=34
T__91=91
NAME=45
T__92=92
T__90=90
PROBLEM_DOMAIN=17
OBJECTS=18
ASSIGN_EFFECT=33
T__99=99
T__98=98
T__97=97
T__96=96
T__95=95
T__80=80
T__81=81
T__82=82
T__83=83
LINE_COMMENT=52
PROBLEM=15
NUMBER=48
WHITESPACE=53
UNARY_MINUS=38
OR_GD=24
T__85=85
T__84=84
T__87=87
T__86=86
T__89=89
T__88=88
DOMAIN_NAME=5
PRED_HEAD=35
T__71=71
T__72=72
PREDICATES=11
VARIABLE=47
T__70=70
INIT_AT=40
T__76=76
T__75=75
T__74=74
INIT=19
T__73=73
T__79=79
T__78=78
T__77=77
AND_GD=23
T__68=68
T__69=69
T__66=66
T__67=67
T__64=64
FUNC_HEAD=20
T__65=65
T__62=62
T__63=63
PARAMETERS=12
NOT_GD=25
PROBLEM_NAME=16
T__118=118
DURATIVE_ACTION=14
T__119=119
T__116=116
T__117=117
T__114=114
T__115=115
PROBLEM_METRIC=44
T__120=120
CONSTANTS=9
T__61=61
T__60=60
T__55=55
T__56=56
T__57=57
T__58=58
T__54=54
IMPLY_GD=26
T__107=107
T__108=108
T__109=109
T__59=59
T__103=103
T__104=104
T__105=105
T__106=106
T__111=111
T__110=110
T__113=113
T__112=112
INIT_EQ=39
DIGIT=51
NOT_PRED_INIT=41
BINARY_OP=37
GOAL=36
FORALL_GD=28
T__102=102
T__101=101
T__100=100
DOMAIN=4
WHEN_EFFECT=32
PRECONDITION=21
EFFECT=22
PROBLEM_CONSTRAINT=43
AND_EFFECT=30
EITHER_TYPE=8
FORALL_EFFECT=31
REQUIREMENTS=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "DOMAIN", "DOMAIN_NAME", "REQUIREMENTS", "TYPES", "EITHER_TYPE", "CONSTANTS", 
    "FUNCTIONS", "PREDICATES", "PARAMETERS", "ACTION", "DURATIVE_ACTION", 
    "PROBLEM", "PROBLEM_NAME", "PROBLEM_DOMAIN", "OBJECTS", "INIT", "FUNC_HEAD", 
    "PRECONDITION", "EFFECT", "AND_GD", "OR_GD", "NOT_GD", "IMPLY_GD", "EXISTS_GD", 
    "FORALL_GD", "COMPARISON_GD", "AND_EFFECT", "FORALL_EFFECT", "WHEN_EFFECT", 
    "ASSIGN_EFFECT", "NOT_EFFECT", "PRED_HEAD", "GOAL", "BINARY_OP", "UNARY_MINUS", 
    "INIT_EQ", "INIT_AT", "NOT_PRED_INIT", "PRED_INST", "PROBLEM_CONSTRAINT", 
    "PROBLEM_METRIC", "NAME", "REQUIRE_KEY", "VARIABLE", "NUMBER", "LETTER", 
    "ANY_CHAR", "DIGIT", "LINE_COMMENT", "WHITESPACE", "'('", "'define'", 
    "')'", "'domain'", "':requirements'", "':types'", "'-'", "'either'", 
    "':functions'", "'number'", "':constants'", "':predicates'", "':constraints'", 
    "':action'", "':parameters'", "':precondition'", "':effect'", "'and'", 
    "'or'", "'not'", "'imply'", "'exists'", "'forall'", "':durative-action'", 
    "':duration'", "':condition'", "'preference'", "'at'", "'over'", "'start'", 
    "'end'", "'all'", "':derived'", "'when'", "'*'", "'+'", "'/'", "'>'", 
    "'<'", "'='", "'>='", "'<='", "'assign'", "'scale-up'", "'scale-down'", 
    "'increase'", "'decrease'", "'?duration'", "'problem'", "':domain'", 
    "':objects'", "':init'", "':goal'", "':metric'", "'minimize'", "'maximize'", 
    "'total-time'", "'is-violated'", "'always'", "'sometime'", "'within'", 
    "'at-most-once'", "'sometime-after'", "'sometime-before'", "'always-within'", 
    "'hold-during'", "'hold-after'"
]




class PddlParser(Parser):
    grammarFileName = "Pddl.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(PddlParser, self).__init__(input, state, *args, **kwargs)

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )

        self.dfa25 = self.DFA25(
            self, 25,
            eot = self.DFA25_eot,
            eof = self.DFA25_eof,
            min = self.DFA25_min,
            max = self.DFA25_max,
            accept = self.DFA25_accept,
            special = self.DFA25_special,
            transition = self.DFA25_transition
            )

        self.dfa37 = self.DFA37(
            self, 37,
            eot = self.DFA37_eot,
            eof = self.DFA37_eof,
            min = self.DFA37_min,
            max = self.DFA37_max,
            accept = self.DFA37_accept,
            special = self.DFA37_special,
            transition = self.DFA37_transition
            )

        self.dfa78 = self.DFA78(
            self, 78,
            eot = self.DFA78_eot,
            eof = self.DFA78_eof,
            min = self.DFA78_min,
            max = self.DFA78_max,
            accept = self.DFA78_accept,
            special = self.DFA78_special,
            transition = self.DFA78_transition
            )

        self.dfa80 = self.DFA80(
            self, 80,
            eot = self.DFA80_eot,
            eof = self.DFA80_eof,
            min = self.DFA80_min,
            max = self.DFA80_max,
            accept = self.DFA80_accept,
            special = self.DFA80_special,
            transition = self.DFA80_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.prog_return, self).__init__()

            self.tree = None




    # $ANTLR start "prog"
    # Pddl.g:61:1: prog : ( domain )+ ;
    def prog(self, ):

        retval = self.prog_return()
        retval.start = self.input.LT(1)

        root_0 = None

        domain1 = None



        try:
            try:
                # Pddl.g:61:5: ( ( domain )+ )
                # Pddl.g:61:7: ( domain )+
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:61:7: ( domain )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 54) :
                        alt1 = 1


                    if alt1 == 1:
                        # Pddl.g:61:9: domain
                        pass 
                        self._state.following.append(self.FOLLOW_domain_in_prog281)
                        domain1 = self.domain()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, domain1.tree)
                        if self._state.backtracking == 0:
                            print domain1.tree.toStringTree();



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prog"

    class getdomain_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.getdomain_return, self).__init__()

            self.tree = None




    # $ANTLR start "getdomain"
    # Pddl.g:64:1: getdomain : ( domain )+ ;
    def getdomain(self, ):

        retval = self.getdomain_return()
        retval.start = self.input.LT(1)

        root_0 = None

        domain2 = None



        try:
            try:
                # Pddl.g:64:10: ( ( domain )+ )
                # Pddl.g:64:12: ( domain )+
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:64:12: ( domain )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 54) :
                        alt2 = 1


                    if alt2 == 1:
                        # Pddl.g:64:14: domain
                        pass 
                        self._state.following.append(self.FOLLOW_domain_in_getdomain297)
                        domain2 = self.domain()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, domain2.tree)
                        if self._state.backtracking == 0:
                            return domain2.tree;



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "getdomain"

    class getproblem_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.getproblem_return, self).__init__()

            self.tree = None




    # $ANTLR start "getproblem"
    # Pddl.g:65:1: getproblem : ( problem )+ ;
    def getproblem(self, ):

        retval = self.getproblem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        problem3 = None



        try:
            try:
                # Pddl.g:65:11: ( ( problem )+ )
                # Pddl.g:65:13: ( problem )+
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:65:13: ( problem )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 54) :
                        alt3 = 1


                    if alt3 == 1:
                        # Pddl.g:65:15: problem
                        pass 
                        self._state.following.append(self.FOLLOW_problem_in_getproblem311)
                        problem3 = self.problem()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, problem3.tree)
                        if self._state.backtracking == 0:
                            return problem3.tree;



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "getproblem"

    class pddlDoc_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.pddlDoc_return, self).__init__()

            self.tree = None




    # $ANTLR start "pddlDoc"
    # Pddl.g:95:1: pddlDoc : ( domain | problem );
    def pddlDoc(self, ):

        retval = self.pddlDoc_return()
        retval.start = self.input.LT(1)

        root_0 = None

        domain4 = None

        problem5 = None



        try:
            try:
                # Pddl.g:97:9: ( domain | problem )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 54) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 55) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == 54) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == 57) :
                                alt4 = 1
                            elif (LA4_3 == 102) :
                                alt4 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # Pddl.g:97:11: domain
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_domain_in_pddlDoc356)
                    domain4 = self.domain()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, domain4.tree)


                elif alt4 == 2:
                    # Pddl.g:97:20: problem
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_problem_in_pddlDoc360)
                    problem5 = self.problem()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, problem5.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pddlDoc"

    class domain_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.domain_return, self).__init__()

            self.tree = None




    # $ANTLR start "domain"
    # Pddl.g:99:1: domain : '(' 'define' domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* ')' -> ^( DOMAIN domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* ) ;
    def domain(self, ):

        retval = self.domain_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal6 = None
        string_literal7 = None
        char_literal16 = None
        domainName8 = None

        requireDef9 = None

        typesDef10 = None

        constantsDef11 = None

        predicatesDef12 = None

        functionsDef13 = None

        constraints14 = None

        structureDef15 = None


        char_literal6_tree = None
        string_literal7_tree = None
        char_literal16_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_constantsDef = RewriteRuleSubtreeStream(self._adaptor, "rule constantsDef")
        stream_requireDef = RewriteRuleSubtreeStream(self._adaptor, "rule requireDef")
        stream_predicatesDef = RewriteRuleSubtreeStream(self._adaptor, "rule predicatesDef")
        stream_constraints = RewriteRuleSubtreeStream(self._adaptor, "rule constraints")
        stream_structureDef = RewriteRuleSubtreeStream(self._adaptor, "rule structureDef")
        stream_domainName = RewriteRuleSubtreeStream(self._adaptor, "rule domainName")
        stream_functionsDef = RewriteRuleSubtreeStream(self._adaptor, "rule functionsDef")
        stream_typesDef = RewriteRuleSubtreeStream(self._adaptor, "rule typesDef")
        try:
            try:
                # Pddl.g:102:5: ( '(' 'define' domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* ')' -> ^( DOMAIN domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* ) )
                # Pddl.g:102:7: '(' 'define' domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* ')'
                pass 
                char_literal6=self.match(self.input, 54, self.FOLLOW_54_in_domain375) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal6)
                string_literal7=self.match(self.input, 55, self.FOLLOW_55_in_domain377) 
                if self._state.backtracking == 0:
                    stream_55.add(string_literal7)
                self._state.following.append(self.FOLLOW_domainName_in_domain379)
                domainName8 = self.domainName()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_domainName.add(domainName8.tree)
                # Pddl.g:103:7: ( requireDef )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 54) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == 58) :
                        alt5 = 1
                if alt5 == 1:
                    # Pddl.g:0:0: requireDef
                    pass 
                    self._state.following.append(self.FOLLOW_requireDef_in_domain387)
                    requireDef9 = self.requireDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_requireDef.add(requireDef9.tree)



                # Pddl.g:104:7: ( typesDef )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == 54) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 59) :
                        alt6 = 1
                if alt6 == 1:
                    # Pddl.g:0:0: typesDef
                    pass 
                    self._state.following.append(self.FOLLOW_typesDef_in_domain396)
                    typesDef10 = self.typesDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typesDef.add(typesDef10.tree)



                # Pddl.g:105:7: ( constantsDef )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 54) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 64) :
                        alt7 = 1
                if alt7 == 1:
                    # Pddl.g:0:0: constantsDef
                    pass 
                    self._state.following.append(self.FOLLOW_constantsDef_in_domain405)
                    constantsDef11 = self.constantsDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_constantsDef.add(constantsDef11.tree)



                # Pddl.g:106:7: ( predicatesDef )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 54) :
                    LA8_1 = self.input.LA(2)

                    if (LA8_1 == 65) :
                        alt8 = 1
                if alt8 == 1:
                    # Pddl.g:0:0: predicatesDef
                    pass 
                    self._state.following.append(self.FOLLOW_predicatesDef_in_domain414)
                    predicatesDef12 = self.predicatesDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_predicatesDef.add(predicatesDef12.tree)



                # Pddl.g:107:7: ( functionsDef )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == 54) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == 62) :
                        alt9 = 1
                if alt9 == 1:
                    # Pddl.g:0:0: functionsDef
                    pass 
                    self._state.following.append(self.FOLLOW_functionsDef_in_domain423)
                    functionsDef13 = self.functionsDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_functionsDef.add(functionsDef13.tree)



                # Pddl.g:108:7: ( constraints )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 54) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == 66) :
                        alt10 = 1
                if alt10 == 1:
                    # Pddl.g:0:0: constraints
                    pass 
                    self._state.following.append(self.FOLLOW_constraints_in_domain432)
                    constraints14 = self.constraints()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_constraints.add(constraints14.tree)



                # Pddl.g:109:7: ( structureDef )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 54) :
                        alt11 = 1


                    if alt11 == 1:
                        # Pddl.g:0:0: structureDef
                        pass 
                        self._state.following.append(self.FOLLOW_structureDef_in_domain441)
                        structureDef15 = self.structureDef()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_structureDef.add(structureDef15.tree)


                    else:
                        break #loop11
                char_literal16=self.match(self.input, 56, self.FOLLOW_56_in_domain450) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal16)

                # AST Rewrite
                # elements: typesDef, functionsDef, constantsDef, domainName, predicatesDef, constraints, structureDef, requireDef
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 111:7: -> ^( DOMAIN domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* )
                    # Pddl.g:111:10: ^( DOMAIN domainName ( requireDef )? ( typesDef )? ( constantsDef )? ( predicatesDef )? ( functionsDef )? ( constraints )? ( structureDef )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DOMAIN, "DOMAIN"), root_1)

                    self._adaptor.addChild(root_1, stream_domainName.nextTree())
                    # Pddl.g:111:30: ( requireDef )?
                    if stream_requireDef.hasNext():
                        self._adaptor.addChild(root_1, stream_requireDef.nextTree())


                    stream_requireDef.reset();
                    # Pddl.g:111:42: ( typesDef )?
                    if stream_typesDef.hasNext():
                        self._adaptor.addChild(root_1, stream_typesDef.nextTree())


                    stream_typesDef.reset();
                    # Pddl.g:112:17: ( constantsDef )?
                    if stream_constantsDef.hasNext():
                        self._adaptor.addChild(root_1, stream_constantsDef.nextTree())


                    stream_constantsDef.reset();
                    # Pddl.g:112:31: ( predicatesDef )?
                    if stream_predicatesDef.hasNext():
                        self._adaptor.addChild(root_1, stream_predicatesDef.nextTree())


                    stream_predicatesDef.reset();
                    # Pddl.g:112:46: ( functionsDef )?
                    if stream_functionsDef.hasNext():
                        self._adaptor.addChild(root_1, stream_functionsDef.nextTree())


                    stream_functionsDef.reset();
                    # Pddl.g:113:17: ( constraints )?
                    if stream_constraints.hasNext():
                        self._adaptor.addChild(root_1, stream_constraints.nextTree())


                    stream_constraints.reset();
                    # Pddl.g:113:30: ( structureDef )*
                    while stream_structureDef.hasNext():
                        self._adaptor.addChild(root_1, stream_structureDef.nextTree())


                    stream_structureDef.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "domain"

    class domainName_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.domainName_return, self).__init__()

            self.tree = None




    # $ANTLR start "domainName"
    # Pddl.g:116:1: domainName : '(' 'domain' NAME ')' -> ^( DOMAIN_NAME NAME ) ;
    def domainName(self, ):

        retval = self.domainName_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal17 = None
        string_literal18 = None
        NAME19 = None
        char_literal20 = None

        char_literal17_tree = None
        string_literal18_tree = None
        NAME19_tree = None
        char_literal20_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_57 = RewriteRuleTokenStream(self._adaptor, "token 57")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")

        try:
            try:
                # Pddl.g:117:5: ( '(' 'domain' NAME ')' -> ^( DOMAIN_NAME NAME ) )
                # Pddl.g:117:7: '(' 'domain' NAME ')'
                pass 
                char_literal17=self.match(self.input, 54, self.FOLLOW_54_in_domainName534) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal17)
                string_literal18=self.match(self.input, 57, self.FOLLOW_57_in_domainName536) 
                if self._state.backtracking == 0:
                    stream_57.add(string_literal18)
                NAME19=self.match(self.input, NAME, self.FOLLOW_NAME_in_domainName538) 
                if self._state.backtracking == 0:
                    stream_NAME.add(NAME19)
                char_literal20=self.match(self.input, 56, self.FOLLOW_56_in_domainName540) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal20)

                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 118:6: -> ^( DOMAIN_NAME NAME )
                    # Pddl.g:118:9: ^( DOMAIN_NAME NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DOMAIN_NAME, "DOMAIN_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "domainName"

    class requireDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.requireDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "requireDef"
    # Pddl.g:121:1: requireDef : '(' ':requirements' ( REQUIRE_KEY )+ ')' -> ^( REQUIREMENTS ( REQUIRE_KEY )+ ) ;
    def requireDef(self, ):

        retval = self.requireDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal21 = None
        string_literal22 = None
        REQUIRE_KEY23 = None
        char_literal24 = None

        char_literal21_tree = None
        string_literal22_tree = None
        REQUIRE_KEY23_tree = None
        char_literal24_tree = None
        stream_REQUIRE_KEY = RewriteRuleTokenStream(self._adaptor, "token REQUIRE_KEY")
        stream_58 = RewriteRuleTokenStream(self._adaptor, "token 58")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")

        try:
            try:
                # Pddl.g:122:2: ( '(' ':requirements' ( REQUIRE_KEY )+ ')' -> ^( REQUIREMENTS ( REQUIRE_KEY )+ ) )
                # Pddl.g:122:4: '(' ':requirements' ( REQUIRE_KEY )+ ')'
                pass 
                char_literal21=self.match(self.input, 54, self.FOLLOW_54_in_requireDef567) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal21)
                string_literal22=self.match(self.input, 58, self.FOLLOW_58_in_requireDef569) 
                if self._state.backtracking == 0:
                    stream_58.add(string_literal22)
                # Pddl.g:122:24: ( REQUIRE_KEY )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == REQUIRE_KEY) :
                        alt12 = 1


                    if alt12 == 1:
                        # Pddl.g:0:0: REQUIRE_KEY
                        pass 
                        REQUIRE_KEY23=self.match(self.input, REQUIRE_KEY, self.FOLLOW_REQUIRE_KEY_in_requireDef571) 
                        if self._state.backtracking == 0:
                            stream_REQUIRE_KEY.add(REQUIRE_KEY23)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1
                char_literal24=self.match(self.input, 56, self.FOLLOW_56_in_requireDef574) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal24)

                # AST Rewrite
                # elements: REQUIRE_KEY
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 123:2: -> ^( REQUIREMENTS ( REQUIRE_KEY )+ )
                    # Pddl.g:123:5: ^( REQUIREMENTS ( REQUIRE_KEY )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REQUIREMENTS, "REQUIREMENTS"), root_1)

                    # Pddl.g:123:20: ( REQUIRE_KEY )+
                    if not (stream_REQUIRE_KEY.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_REQUIRE_KEY.hasNext():
                        self._adaptor.addChild(root_1, stream_REQUIRE_KEY.nextNode())


                    stream_REQUIRE_KEY.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "requireDef"

    class typesDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.typesDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "typesDef"
    # Pddl.g:126:1: typesDef : '(' ':types' typedNameList ')' -> ^( TYPES typedNameList ) ;
    def typesDef(self, ):

        retval = self.typesDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal25 = None
        string_literal26 = None
        char_literal28 = None
        typedNameList27 = None


        char_literal25_tree = None
        string_literal26_tree = None
        char_literal28_tree = None
        stream_59 = RewriteRuleTokenStream(self._adaptor, "token 59")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_typedNameList = RewriteRuleSubtreeStream(self._adaptor, "rule typedNameList")
        try:
            try:
                # Pddl.g:127:2: ( '(' ':types' typedNameList ')' -> ^( TYPES typedNameList ) )
                # Pddl.g:127:4: '(' ':types' typedNameList ')'
                pass 
                char_literal25=self.match(self.input, 54, self.FOLLOW_54_in_typesDef595) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal25)
                string_literal26=self.match(self.input, 59, self.FOLLOW_59_in_typesDef597) 
                if self._state.backtracking == 0:
                    stream_59.add(string_literal26)
                self._state.following.append(self.FOLLOW_typedNameList_in_typesDef599)
                typedNameList27 = self.typedNameList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typedNameList.add(typedNameList27.tree)
                char_literal28=self.match(self.input, 56, self.FOLLOW_56_in_typesDef601) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal28)

                # AST Rewrite
                # elements: typedNameList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 128:4: -> ^( TYPES typedNameList )
                    # Pddl.g:128:7: ^( TYPES typedNameList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TYPES, "TYPES"), root_1)

                    self._adaptor.addChild(root_1, stream_typedNameList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typesDef"

    class typedNameList_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.typedNameList_return, self).__init__()

            self.tree = None




    # $ANTLR start "typedNameList"
    # Pddl.g:132:1: typedNameList : ( ( NAME )* | ( singleTypeNameList )+ ( NAME )* ) ;
    def typedNameList(self, ):

        retval = self.typedNameList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME29 = None
        NAME31 = None
        singleTypeNameList30 = None


        NAME29_tree = None
        NAME31_tree = None

        try:
            try:
                # Pddl.g:133:5: ( ( ( NAME )* | ( singleTypeNameList )+ ( NAME )* ) )
                # Pddl.g:133:7: ( ( NAME )* | ( singleTypeNameList )+ ( NAME )* )
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:133:7: ( ( NAME )* | ( singleTypeNameList )+ ( NAME )* )
                alt16 = 2
                alt16 = self.dfa16.predict(self.input)
                if alt16 == 1:
                    # Pddl.g:133:8: ( NAME )*
                    pass 
                    # Pddl.g:133:8: ( NAME )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == NAME) :
                            alt13 = 1


                        if alt13 == 1:
                            # Pddl.g:0:0: NAME
                            pass 
                            NAME29=self.match(self.input, NAME, self.FOLLOW_NAME_in_typedNameList628)
                            if self._state.backtracking == 0:

                                NAME29_tree = self._adaptor.createWithPayload(NAME29)
                                self._adaptor.addChild(root_0, NAME29_tree)



                        else:
                            break #loop13


                elif alt16 == 2:
                    # Pddl.g:133:16: ( singleTypeNameList )+ ( NAME )*
                    pass 
                    # Pddl.g:133:16: ( singleTypeNameList )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        alt14 = self.dfa14.predict(self.input)
                        if alt14 == 1:
                            # Pddl.g:0:0: singleTypeNameList
                            pass 
                            self._state.following.append(self.FOLLOW_singleTypeNameList_in_typedNameList633)
                            singleTypeNameList30 = self.singleTypeNameList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, singleTypeNameList30.tree)


                        else:
                            if cnt14 >= 1:
                                break #loop14

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1
                    # Pddl.g:133:36: ( NAME )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == NAME) :
                            alt15 = 1


                        if alt15 == 1:
                            # Pddl.g:0:0: NAME
                            pass 
                            NAME31=self.match(self.input, NAME, self.FOLLOW_NAME_in_typedNameList636)
                            if self._state.backtracking == 0:

                                NAME31_tree = self._adaptor.createWithPayload(NAME31)
                                self._adaptor.addChild(root_0, NAME31_tree)



                        else:
                            break #loop15






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typedNameList"

    class singleTypeNameList_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.singleTypeNameList_return, self).__init__()

            self.tree = None




    # $ANTLR start "singleTypeNameList"
    # Pddl.g:136:1: singleTypeNameList : ( ( NAME )+ '-' t= type ) -> ( ^( NAME $t) )+ ;
    def singleTypeNameList(self, ):

        retval = self.singleTypeNameList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME32 = None
        char_literal33 = None
        t = None


        NAME32_tree = None
        char_literal33_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # Pddl.g:137:5: ( ( ( NAME )+ '-' t= type ) -> ( ^( NAME $t) )+ )
                # Pddl.g:137:7: ( ( NAME )+ '-' t= type )
                pass 
                # Pddl.g:137:7: ( ( NAME )+ '-' t= type )
                # Pddl.g:137:8: ( NAME )+ '-' t= type
                pass 
                # Pddl.g:137:8: ( NAME )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == NAME) :
                        alt17 = 1


                    if alt17 == 1:
                        # Pddl.g:0:0: NAME
                        pass 
                        NAME32=self.match(self.input, NAME, self.FOLLOW_NAME_in_singleTypeNameList656) 
                        if self._state.backtracking == 0:
                            stream_NAME.add(NAME32)


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1
                char_literal33=self.match(self.input, 60, self.FOLLOW_60_in_singleTypeNameList659) 
                if self._state.backtracking == 0:
                    stream_60.add(char_literal33)
                self._state.following.append(self.FOLLOW_type_in_singleTypeNameList663)
                t = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(t.tree)




                # AST Rewrite
                # elements: t, NAME
                # token labels: 
                # rule labels: retval, t
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if t is not None:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "rule t", t.tree)
                    else:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "token t", None)


                    root_0 = self._adaptor.nil()
                    # 138:4: -> ( ^( NAME $t) )+
                    # Pddl.g:138:7: ( ^( NAME $t) )+
                    if not (stream_t.hasNext() or stream_NAME.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_t.hasNext() or stream_NAME.hasNext():
                        # Pddl.g:138:7: ^( NAME $t)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_NAME.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_t.nextTree())

                        self._adaptor.addChild(root_0, root_1)


                    stream_t.reset()
                    stream_NAME.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "singleTypeNameList"

    class type_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.type_return, self).__init__()

            self.tree = None




    # $ANTLR start "type"
    # Pddl.g:141:1: type : ( ( '(' 'either' ( primType )+ ')' ) -> ^( EITHER_TYPE ( primType )+ ) | primType );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal34 = None
        string_literal35 = None
        char_literal37 = None
        primType36 = None

        primType38 = None


        char_literal34_tree = None
        string_literal35_tree = None
        char_literal37_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_61 = RewriteRuleTokenStream(self._adaptor, "token 61")
        stream_primType = RewriteRuleSubtreeStream(self._adaptor, "rule primType")
        try:
            try:
                # Pddl.g:142:2: ( ( '(' 'either' ( primType )+ ')' ) -> ^( EITHER_TYPE ( primType )+ ) | primType )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == 54) :
                    alt19 = 1
                elif (LA19_0 == NAME) :
                    alt19 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # Pddl.g:142:4: ( '(' 'either' ( primType )+ ')' )
                    pass 
                    # Pddl.g:142:4: ( '(' 'either' ( primType )+ ')' )
                    # Pddl.g:142:6: '(' 'either' ( primType )+ ')'
                    pass 
                    char_literal34=self.match(self.input, 54, self.FOLLOW_54_in_type690) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal34)
                    string_literal35=self.match(self.input, 61, self.FOLLOW_61_in_type692) 
                    if self._state.backtracking == 0:
                        stream_61.add(string_literal35)
                    # Pddl.g:142:19: ( primType )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == NAME) :
                            alt18 = 1


                        if alt18 == 1:
                            # Pddl.g:0:0: primType
                            pass 
                            self._state.following.append(self.FOLLOW_primType_in_type694)
                            primType36 = self.primType()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_primType.add(primType36.tree)


                        else:
                            if cnt18 >= 1:
                                break #loop18

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1
                    char_literal37=self.match(self.input, 56, self.FOLLOW_56_in_type697) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal37)




                    # AST Rewrite
                    # elements: primType
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 143:4: -> ^( EITHER_TYPE ( primType )+ )
                        # Pddl.g:143:7: ^( EITHER_TYPE ( primType )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EITHER_TYPE, "EITHER_TYPE"), root_1)

                        # Pddl.g:143:21: ( primType )+
                        if not (stream_primType.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_primType.hasNext():
                            self._adaptor.addChild(root_1, stream_primType.nextTree())


                        stream_primType.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt19 == 2:
                    # Pddl.g:144:4: primType
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_primType_in_type716)
                    primType38 = self.primType()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, primType38.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "type"

    class primType_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.primType_return, self).__init__()

            self.tree = None




    # $ANTLR start "primType"
    # Pddl.g:147:1: primType : NAME ;
    def primType(self, ):

        retval = self.primType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME39 = None

        NAME39_tree = None

        try:
            try:
                # Pddl.g:147:10: ( NAME )
                # Pddl.g:147:12: NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME39=self.match(self.input, NAME, self.FOLLOW_NAME_in_primType726)
                if self._state.backtracking == 0:

                    NAME39_tree = self._adaptor.createWithPayload(NAME39)
                    self._adaptor.addChild(root_0, NAME39_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "primType"

    class functionsDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.functionsDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionsDef"
    # Pddl.g:149:1: functionsDef : '(' ':functions' functionList ')' -> ^( FUNCTIONS functionList ) ;
    def functionsDef(self, ):

        retval = self.functionsDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal40 = None
        string_literal41 = None
        char_literal43 = None
        functionList42 = None


        char_literal40_tree = None
        string_literal41_tree = None
        char_literal43_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_62 = RewriteRuleTokenStream(self._adaptor, "token 62")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_functionList = RewriteRuleSubtreeStream(self._adaptor, "rule functionList")
        try:
            try:
                # Pddl.g:150:2: ( '(' ':functions' functionList ')' -> ^( FUNCTIONS functionList ) )
                # Pddl.g:150:4: '(' ':functions' functionList ')'
                pass 
                char_literal40=self.match(self.input, 54, self.FOLLOW_54_in_functionsDef736) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal40)
                string_literal41=self.match(self.input, 62, self.FOLLOW_62_in_functionsDef738) 
                if self._state.backtracking == 0:
                    stream_62.add(string_literal41)
                self._state.following.append(self.FOLLOW_functionList_in_functionsDef740)
                functionList42 = self.functionList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_functionList.add(functionList42.tree)
                char_literal43=self.match(self.input, 56, self.FOLLOW_56_in_functionsDef742) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal43)

                # AST Rewrite
                # elements: functionList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 151:2: -> ^( FUNCTIONS functionList )
                    # Pddl.g:151:5: ^( FUNCTIONS functionList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNCTIONS, "FUNCTIONS"), root_1)

                    self._adaptor.addChild(root_1, stream_functionList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "functionsDef"

    class functionList_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.functionList_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionList"
    # Pddl.g:154:1: functionList : ( ( atomicFunctionSkeleton )+ ( '-' functionType )? )* ;
    def functionList(self, ):

        retval = self.functionList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal45 = None
        atomicFunctionSkeleton44 = None

        functionType46 = None


        char_literal45_tree = None

        try:
            try:
                # Pddl.g:155:2: ( ( ( atomicFunctionSkeleton )+ ( '-' functionType )? )* )
                # Pddl.g:155:4: ( ( atomicFunctionSkeleton )+ ( '-' functionType )? )*
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:155:4: ( ( atomicFunctionSkeleton )+ ( '-' functionType )? )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == 54) :
                        alt22 = 1


                    if alt22 == 1:
                        # Pddl.g:155:5: ( atomicFunctionSkeleton )+ ( '-' functionType )?
                        pass 
                        # Pddl.g:155:5: ( atomicFunctionSkeleton )+
                        cnt20 = 0
                        while True: #loop20
                            alt20 = 2
                            LA20_0 = self.input.LA(1)

                            if (LA20_0 == 54) :
                                LA20_2 = self.input.LA(2)

                                if (self.synpred20_Pddl()) :
                                    alt20 = 1




                            if alt20 == 1:
                                # Pddl.g:0:0: atomicFunctionSkeleton
                                pass 
                                self._state.following.append(self.FOLLOW_atomicFunctionSkeleton_in_functionList763)
                                atomicFunctionSkeleton44 = self.atomicFunctionSkeleton()

                                self._state.following.pop()
                                if self._state.backtracking == 0:
                                    self._adaptor.addChild(root_0, atomicFunctionSkeleton44.tree)


                            else:
                                if cnt20 >= 1:
                                    break #loop20

                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed

                                eee = EarlyExitException(20, self.input)
                                raise eee

                            cnt20 += 1
                        # Pddl.g:155:29: ( '-' functionType )?
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == 60) :
                            alt21 = 1
                        if alt21 == 1:
                            # Pddl.g:155:30: '-' functionType
                            pass 
                            char_literal45=self.match(self.input, 60, self.FOLLOW_60_in_functionList767)
                            if self._state.backtracking == 0:

                                char_literal45_tree = self._adaptor.createWithPayload(char_literal45)
                                self._adaptor.addChild(root_0, char_literal45_tree)

                            self._state.following.append(self.FOLLOW_functionType_in_functionList769)
                            functionType46 = self.functionType()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, functionType46.tree)





                    else:
                        break #loop22



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "functionList"

    class atomicFunctionSkeleton_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.atomicFunctionSkeleton_return, self).__init__()

            self.tree = None




    # $ANTLR start "atomicFunctionSkeleton"
    # Pddl.g:158:1: atomicFunctionSkeleton : '(' functionSymbol typedVariableList ')' ;
    def atomicFunctionSkeleton(self, ):

        retval = self.atomicFunctionSkeleton_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal47 = None
        char_literal50 = None
        functionSymbol48 = None

        typedVariableList49 = None


        char_literal47_tree = None
        char_literal50_tree = None

        try:
            try:
                # Pddl.g:159:2: ( '(' functionSymbol typedVariableList ')' )
                # Pddl.g:159:4: '(' functionSymbol typedVariableList ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal47=self.match(self.input, 54, self.FOLLOW_54_in_atomicFunctionSkeleton785)
                self._state.following.append(self.FOLLOW_functionSymbol_in_atomicFunctionSkeleton788)
                functionSymbol48 = self.functionSymbol()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    root_0 = self._adaptor.becomeRoot(functionSymbol48.tree, root_0)
                self._state.following.append(self.FOLLOW_typedVariableList_in_atomicFunctionSkeleton791)
                typedVariableList49 = self.typedVariableList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typedVariableList49.tree)
                char_literal50=self.match(self.input, 56, self.FOLLOW_56_in_atomicFunctionSkeleton793)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atomicFunctionSkeleton"

    class functionSymbol_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.functionSymbol_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionSymbol"
    # Pddl.g:162:1: functionSymbol : NAME ;
    def functionSymbol(self, ):

        retval = self.functionSymbol_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME51 = None

        NAME51_tree = None

        try:
            try:
                # Pddl.g:162:16: ( NAME )
                # Pddl.g:162:18: NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME51=self.match(self.input, NAME, self.FOLLOW_NAME_in_functionSymbol804)
                if self._state.backtracking == 0:

                    NAME51_tree = self._adaptor.createWithPayload(NAME51)
                    self._adaptor.addChild(root_0, NAME51_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "functionSymbol"

    class functionType_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.functionType_return, self).__init__()

            self.tree = None




    # $ANTLR start "functionType"
    # Pddl.g:164:1: functionType : 'number' ;
    def functionType(self, ):

        retval = self.functionType_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal52 = None

        string_literal52_tree = None

        try:
            try:
                # Pddl.g:164:14: ( 'number' )
                # Pddl.g:164:16: 'number'
                pass 
                root_0 = self._adaptor.nil()

                string_literal52=self.match(self.input, 63, self.FOLLOW_63_in_functionType813)
                if self._state.backtracking == 0:

                    string_literal52_tree = self._adaptor.createWithPayload(string_literal52)
                    self._adaptor.addChild(root_0, string_literal52_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "functionType"

    class constantsDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.constantsDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "constantsDef"
    # Pddl.g:166:1: constantsDef : '(' ':constants' typedNameList ')' -> ^( CONSTANTS typedNameList ) ;
    def constantsDef(self, ):

        retval = self.constantsDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal53 = None
        string_literal54 = None
        char_literal56 = None
        typedNameList55 = None


        char_literal53_tree = None
        string_literal54_tree = None
        char_literal56_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_64 = RewriteRuleTokenStream(self._adaptor, "token 64")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_typedNameList = RewriteRuleSubtreeStream(self._adaptor, "rule typedNameList")
        try:
            try:
                # Pddl.g:167:2: ( '(' ':constants' typedNameList ')' -> ^( CONSTANTS typedNameList ) )
                # Pddl.g:167:4: '(' ':constants' typedNameList ')'
                pass 
                char_literal53=self.match(self.input, 54, self.FOLLOW_54_in_constantsDef824) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal53)
                string_literal54=self.match(self.input, 64, self.FOLLOW_64_in_constantsDef826) 
                if self._state.backtracking == 0:
                    stream_64.add(string_literal54)
                self._state.following.append(self.FOLLOW_typedNameList_in_constantsDef828)
                typedNameList55 = self.typedNameList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typedNameList.add(typedNameList55.tree)
                char_literal56=self.match(self.input, 56, self.FOLLOW_56_in_constantsDef830) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal56)

                # AST Rewrite
                # elements: typedNameList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 168:2: -> ^( CONSTANTS typedNameList )
                    # Pddl.g:168:5: ^( CONSTANTS typedNameList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CONSTANTS, "CONSTANTS"), root_1)

                    self._adaptor.addChild(root_1, stream_typedNameList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "constantsDef"

    class predicatesDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.predicatesDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "predicatesDef"
    # Pddl.g:171:1: predicatesDef : '(' ':predicates' ( atomicFormulaSkeleton )+ ')' -> ^( PREDICATES ( atomicFormulaSkeleton )+ ) ;
    def predicatesDef(self, ):

        retval = self.predicatesDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal57 = None
        string_literal58 = None
        char_literal60 = None
        atomicFormulaSkeleton59 = None


        char_literal57_tree = None
        string_literal58_tree = None
        char_literal60_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_65 = RewriteRuleTokenStream(self._adaptor, "token 65")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_atomicFormulaSkeleton = RewriteRuleSubtreeStream(self._adaptor, "rule atomicFormulaSkeleton")
        try:
            try:
                # Pddl.g:172:2: ( '(' ':predicates' ( atomicFormulaSkeleton )+ ')' -> ^( PREDICATES ( atomicFormulaSkeleton )+ ) )
                # Pddl.g:172:4: '(' ':predicates' ( atomicFormulaSkeleton )+ ')'
                pass 
                char_literal57=self.match(self.input, 54, self.FOLLOW_54_in_predicatesDef850) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal57)
                string_literal58=self.match(self.input, 65, self.FOLLOW_65_in_predicatesDef852) 
                if self._state.backtracking == 0:
                    stream_65.add(string_literal58)
                # Pddl.g:172:22: ( atomicFormulaSkeleton )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == 54) :
                        alt23 = 1


                    if alt23 == 1:
                        # Pddl.g:0:0: atomicFormulaSkeleton
                        pass 
                        self._state.following.append(self.FOLLOW_atomicFormulaSkeleton_in_predicatesDef854)
                        atomicFormulaSkeleton59 = self.atomicFormulaSkeleton()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_atomicFormulaSkeleton.add(atomicFormulaSkeleton59.tree)


                    else:
                        if cnt23 >= 1:
                            break #loop23

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1
                char_literal60=self.match(self.input, 56, self.FOLLOW_56_in_predicatesDef857) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal60)

                # AST Rewrite
                # elements: atomicFormulaSkeleton
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 173:2: -> ^( PREDICATES ( atomicFormulaSkeleton )+ )
                    # Pddl.g:173:5: ^( PREDICATES ( atomicFormulaSkeleton )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PREDICATES, "PREDICATES"), root_1)

                    # Pddl.g:173:18: ( atomicFormulaSkeleton )+
                    if not (stream_atomicFormulaSkeleton.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_atomicFormulaSkeleton.hasNext():
                        self._adaptor.addChild(root_1, stream_atomicFormulaSkeleton.nextTree())


                    stream_atomicFormulaSkeleton.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "predicatesDef"

    class atomicFormulaSkeleton_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.atomicFormulaSkeleton_return, self).__init__()

            self.tree = None




    # $ANTLR start "atomicFormulaSkeleton"
    # Pddl.g:176:1: atomicFormulaSkeleton : '(' predicate typedVariableList ')' ;
    def atomicFormulaSkeleton(self, ):

        retval = self.atomicFormulaSkeleton_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal61 = None
        char_literal64 = None
        predicate62 = None

        typedVariableList63 = None


        char_literal61_tree = None
        char_literal64_tree = None

        try:
            try:
                # Pddl.g:177:2: ( '(' predicate typedVariableList ')' )
                # Pddl.g:177:4: '(' predicate typedVariableList ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal61=self.match(self.input, 54, self.FOLLOW_54_in_atomicFormulaSkeleton878)
                self._state.following.append(self.FOLLOW_predicate_in_atomicFormulaSkeleton881)
                predicate62 = self.predicate()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    root_0 = self._adaptor.becomeRoot(predicate62.tree, root_0)
                self._state.following.append(self.FOLLOW_typedVariableList_in_atomicFormulaSkeleton884)
                typedVariableList63 = self.typedVariableList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typedVariableList63.tree)
                char_literal64=self.match(self.input, 56, self.FOLLOW_56_in_atomicFormulaSkeleton886)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atomicFormulaSkeleton"

    class predicate_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.predicate_return, self).__init__()

            self.tree = None




    # $ANTLR start "predicate"
    # Pddl.g:180:1: predicate : NAME ;
    def predicate(self, ):

        retval = self.predicate_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME65 = None

        NAME65_tree = None

        try:
            try:
                # Pddl.g:180:11: ( NAME )
                # Pddl.g:180:13: NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME65=self.match(self.input, NAME, self.FOLLOW_NAME_in_predicate897)
                if self._state.backtracking == 0:

                    NAME65_tree = self._adaptor.createWithPayload(NAME65)
                    self._adaptor.addChild(root_0, NAME65_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "predicate"

    class typedVariableList_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.typedVariableList_return, self).__init__()

            self.tree = None




    # $ANTLR start "typedVariableList"
    # Pddl.g:183:1: typedVariableList : ( ( VARIABLE )* | ( singleTypeVarList )+ ( VARIABLE )* ) ;
    def typedVariableList(self, ):

        retval = self.typedVariableList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VARIABLE66 = None
        VARIABLE68 = None
        singleTypeVarList67 = None


        VARIABLE66_tree = None
        VARIABLE68_tree = None

        try:
            try:
                # Pddl.g:184:5: ( ( ( VARIABLE )* | ( singleTypeVarList )+ ( VARIABLE )* ) )
                # Pddl.g:184:7: ( ( VARIABLE )* | ( singleTypeVarList )+ ( VARIABLE )* )
                pass 
                root_0 = self._adaptor.nil()

                # Pddl.g:184:7: ( ( VARIABLE )* | ( singleTypeVarList )+ ( VARIABLE )* )
                alt27 = 2
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # Pddl.g:184:8: ( VARIABLE )*
                    pass 
                    # Pddl.g:184:8: ( VARIABLE )*
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == VARIABLE) :
                            alt24 = 1


                        if alt24 == 1:
                            # Pddl.g:0:0: VARIABLE
                            pass 
                            VARIABLE66=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_typedVariableList912)
                            if self._state.backtracking == 0:

                                VARIABLE66_tree = self._adaptor.createWithPayload(VARIABLE66)
                                self._adaptor.addChild(root_0, VARIABLE66_tree)



                        else:
                            break #loop24


                elif alt27 == 2:
                    # Pddl.g:184:20: ( singleTypeVarList )+ ( VARIABLE )*
                    pass 
                    # Pddl.g:184:20: ( singleTypeVarList )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        alt25 = self.dfa25.predict(self.input)
                        if alt25 == 1:
                            # Pddl.g:0:0: singleTypeVarList
                            pass 
                            self._state.following.append(self.FOLLOW_singleTypeVarList_in_typedVariableList917)
                            singleTypeVarList67 = self.singleTypeVarList()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, singleTypeVarList67.tree)


                        else:
                            if cnt25 >= 1:
                                break #loop25

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1
                    # Pddl.g:184:39: ( VARIABLE )*
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == VARIABLE) :
                            alt26 = 1


                        if alt26 == 1:
                            # Pddl.g:0:0: VARIABLE
                            pass 
                            VARIABLE68=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_typedVariableList920)
                            if self._state.backtracking == 0:

                                VARIABLE68_tree = self._adaptor.createWithPayload(VARIABLE68)
                                self._adaptor.addChild(root_0, VARIABLE68_tree)



                        else:
                            break #loop26






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "typedVariableList"

    class singleTypeVarList_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.singleTypeVarList_return, self).__init__()

            self.tree = None




    # $ANTLR start "singleTypeVarList"
    # Pddl.g:187:1: singleTypeVarList : ( ( VARIABLE )+ '-' t= type ) -> ( ^( VARIABLE $t) )+ ;
    def singleTypeVarList(self, ):

        retval = self.singleTypeVarList_return()
        retval.start = self.input.LT(1)

        root_0 = None

        VARIABLE69 = None
        char_literal70 = None
        t = None


        VARIABLE69_tree = None
        char_literal70_tree = None
        stream_VARIABLE = RewriteRuleTokenStream(self._adaptor, "token VARIABLE")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # Pddl.g:188:5: ( ( ( VARIABLE )+ '-' t= type ) -> ( ^( VARIABLE $t) )+ )
                # Pddl.g:188:7: ( ( VARIABLE )+ '-' t= type )
                pass 
                # Pddl.g:188:7: ( ( VARIABLE )+ '-' t= type )
                # Pddl.g:188:8: ( VARIABLE )+ '-' t= type
                pass 
                # Pddl.g:188:8: ( VARIABLE )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == VARIABLE) :
                        alt28 = 1


                    if alt28 == 1:
                        # Pddl.g:0:0: VARIABLE
                        pass 
                        VARIABLE69=self.match(self.input, VARIABLE, self.FOLLOW_VARIABLE_in_singleTypeVarList940) 
                        if self._state.backtracking == 0:
                            stream_VARIABLE.add(VARIABLE69)


                    else:
                        if cnt28 >= 1:
                            break #loop28

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1
                char_literal70=self.match(self.input, 60, self.FOLLOW_60_in_singleTypeVarList943) 
                if self._state.backtracking == 0:
                    stream_60.add(char_literal70)
                self._state.following.append(self.FOLLOW_type_in_singleTypeVarList947)
                t = self.type()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_type.add(t.tree)




                # AST Rewrite
                # elements: t, VARIABLE
                # token labels: 
                # rule labels: retval, t
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if t is not None:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "rule t", t.tree)
                    else:
                        stream_t = RewriteRuleSubtreeStream(self._adaptor, "token t", None)


                    root_0 = self._adaptor.nil()
                    # 189:7: -> ( ^( VARIABLE $t) )+
                    # Pddl.g:189:10: ( ^( VARIABLE $t) )+
                    if not (stream_t.hasNext() or stream_VARIABLE.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_t.hasNext() or stream_VARIABLE.hasNext():
                        # Pddl.g:189:10: ^( VARIABLE $t)
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(stream_VARIABLE.nextNode(), root_1)

                        self._adaptor.addChild(root_1, stream_t.nextTree())

                        self._adaptor.addChild(root_0, root_1)


                    stream_t.reset()
                    stream_VARIABLE.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "singleTypeVarList"

    class constraints_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.constraints_return, self).__init__()

            self.tree = None




    # $ANTLR start "constraints"
    # Pddl.g:192:1: constraints : '(' ':constraints' conGD ')' ;
    def constraints(self, ):

        retval = self.constraints_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal71 = None
        string_literal72 = None
        char_literal74 = None
        conGD73 = None


        char_literal71_tree = None
        string_literal72_tree = None
        char_literal74_tree = None

        try:
            try:
                # Pddl.g:193:2: ( '(' ':constraints' conGD ')' )
                # Pddl.g:193:4: '(' ':constraints' conGD ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal71=self.match(self.input, 54, self.FOLLOW_54_in_constraints978)
                string_literal72=self.match(self.input, 66, self.FOLLOW_66_in_constraints981)
                if self._state.backtracking == 0:

                    string_literal72_tree = self._adaptor.createWithPayload(string_literal72)
                    root_0 = self._adaptor.becomeRoot(string_literal72_tree, root_0)

                self._state.following.append(self.FOLLOW_conGD_in_constraints984)
                conGD73 = self.conGD()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, conGD73.tree)
                char_literal74=self.match(self.input, 56, self.FOLLOW_56_in_constraints986)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "constraints"

    class structureDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.structureDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "structureDef"
    # Pddl.g:196:1: structureDef : ( actionDef | durativeActionDef | derivedDef );
    def structureDef(self, ):

        retval = self.structureDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        actionDef75 = None

        durativeActionDef76 = None

        derivedDef77 = None



        try:
            try:
                # Pddl.g:197:2: ( actionDef | durativeActionDef | derivedDef )
                alt29 = 3
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 54) :
                    LA29 = self.input.LA(2)
                    if LA29 == 67:
                        alt29 = 1
                    elif LA29 == 77:
                        alt29 = 2
                    elif LA29 == 86:
                        alt29 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # Pddl.g:197:4: actionDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_actionDef_in_structureDef998)
                    actionDef75 = self.actionDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, actionDef75.tree)


                elif alt29 == 2:
                    # Pddl.g:198:4: durativeActionDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_durativeActionDef_in_structureDef1003)
                    durativeActionDef76 = self.durativeActionDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, durativeActionDef76.tree)


                elif alt29 == 3:
                    # Pddl.g:199:4: derivedDef
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_derivedDef_in_structureDef1008)
                    derivedDef77 = self.derivedDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, derivedDef77.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "structureDef"

    class actionDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.actionDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "actionDef"
    # Pddl.g:203:1: actionDef : '(' ':action' actionSymbol actionDefBody ')' -> ^( ACTION actionSymbol actionDefBody ) ;
    def actionDef(self, ):

        retval = self.actionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal78 = None
        string_literal79 = None
        char_literal82 = None
        actionSymbol80 = None

        actionDefBody81 = None


        char_literal78_tree = None
        string_literal79_tree = None
        char_literal82_tree = None
        stream_67 = RewriteRuleTokenStream(self._adaptor, "token 67")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_actionSymbol = RewriteRuleSubtreeStream(self._adaptor, "rule actionSymbol")
        stream_actionDefBody = RewriteRuleSubtreeStream(self._adaptor, "rule actionDefBody")
        try:
            try:
                # Pddl.g:206:2: ( '(' ':action' actionSymbol actionDefBody ')' -> ^( ACTION actionSymbol actionDefBody ) )
                # Pddl.g:206:4: '(' ':action' actionSymbol actionDefBody ')'
                pass 
                char_literal78=self.match(self.input, 54, self.FOLLOW_54_in_actionDef1023) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal78)
                string_literal79=self.match(self.input, 67, self.FOLLOW_67_in_actionDef1025) 
                if self._state.backtracking == 0:
                    stream_67.add(string_literal79)
                self._state.following.append(self.FOLLOW_actionSymbol_in_actionDef1027)
                actionSymbol80 = self.actionSymbol()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_actionSymbol.add(actionSymbol80.tree)
                self._state.following.append(self.FOLLOW_actionDefBody_in_actionDef1040)
                actionDefBody81 = self.actionDefBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_actionDefBody.add(actionDefBody81.tree)
                char_literal82=self.match(self.input, 56, self.FOLLOW_56_in_actionDef1042) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal82)

                # AST Rewrite
                # elements: actionSymbol, actionDefBody
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 208:8: -> ^( ACTION actionSymbol actionDefBody )
                    # Pddl.g:208:11: ^( ACTION actionSymbol actionDefBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ACTION, "ACTION"), root_1)

                    self._adaptor.addChild(root_1, stream_actionSymbol.nextTree())
                    self._adaptor.addChild(root_1, stream_actionDefBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "actionDef"

    class actionSymbol_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.actionSymbol_return, self).__init__()

            self.tree = None




    # $ANTLR start "actionSymbol"
    # Pddl.g:211:1: actionSymbol : NAME ;
    def actionSymbol(self, ):

        retval = self.actionSymbol_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NAME83 = None

        NAME83_tree = None

        try:
            try:
                # Pddl.g:211:14: ( NAME )
                # Pddl.g:211:16: NAME
                pass 
                root_0 = self._adaptor.nil()

                NAME83=self.match(self.input, NAME, self.FOLLOW_NAME_in_actionSymbol1072)
                if self._state.backtracking == 0:

                    NAME83_tree = self._adaptor.createWithPayload(NAME83)
                    self._adaptor.addChild(root_0, NAME83_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "actionSymbol"

    class actionDefBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.actionDefBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "actionDefBody"
    # Pddl.g:217:1: actionDefBody : ( ':parameters' '(' typedVariableList ')' )? ( ':precondition' ( ( '(' ')' ) | goalDesc ) )? ( ':effect' ( ( '(' ')' ) | effect ) )? -> ^( PARAMETERS ( typedVariableList )? ) ^( PRECONDITION ( goalDesc )? ) ^( EFFECT ( effect )? ) ;
    def actionDefBody(self, ):

        retval = self.actionDefBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal84 = None
        char_literal85 = None
        char_literal87 = None
        string_literal88 = None
        char_literal89 = None
        char_literal90 = None
        string_literal92 = None
        char_literal93 = None
        char_literal94 = None
        typedVariableList86 = None

        goalDesc91 = None

        effect95 = None


        string_literal84_tree = None
        char_literal85_tree = None
        char_literal87_tree = None
        string_literal88_tree = None
        char_literal89_tree = None
        char_literal90_tree = None
        string_literal92_tree = None
        char_literal93_tree = None
        char_literal94_tree = None
        stream_69 = RewriteRuleTokenStream(self._adaptor, "token 69")
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_70 = RewriteRuleTokenStream(self._adaptor, "token 70")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_effect = RewriteRuleSubtreeStream(self._adaptor, "rule effect")
        stream_goalDesc = RewriteRuleSubtreeStream(self._adaptor, "rule goalDesc")
        stream_typedVariableList = RewriteRuleSubtreeStream(self._adaptor, "rule typedVariableList")
        try:
            try:
                # Pddl.g:218:2: ( ( ':parameters' '(' typedVariableList ')' )? ( ':precondition' ( ( '(' ')' ) | goalDesc ) )? ( ':effect' ( ( '(' ')' ) | effect ) )? -> ^( PARAMETERS ( typedVariableList )? ) ^( PRECONDITION ( goalDesc )? ) ^( EFFECT ( effect )? ) )
                # Pddl.g:218:4: ( ':parameters' '(' typedVariableList ')' )? ( ':precondition' ( ( '(' ')' ) | goalDesc ) )? ( ':effect' ( ( '(' ')' ) | effect ) )?
                pass 
                # Pddl.g:218:4: ( ':parameters' '(' typedVariableList ')' )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == 68) :
                    alt30 = 1
                if alt30 == 1:
                    # Pddl.g:218:6: ':parameters' '(' typedVariableList ')'
                    pass 
                    string_literal84=self.match(self.input, 68, self.FOLLOW_68_in_actionDefBody1088) 
                    if self._state.backtracking == 0:
                        stream_68.add(string_literal84)
                    char_literal85=self.match(self.input, 54, self.FOLLOW_54_in_actionDefBody1090) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal85)
                    self._state.following.append(self.FOLLOW_typedVariableList_in_actionDefBody1092)
                    typedVariableList86 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typedVariableList.add(typedVariableList86.tree)
                    char_literal87=self.match(self.input, 56, self.FOLLOW_56_in_actionDefBody1094) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal87)



                # Pddl.g:219:7: ( ':precondition' ( ( '(' ')' ) | goalDesc ) )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 69) :
                    alt32 = 1
                if alt32 == 1:
                    # Pddl.g:219:9: ':precondition' ( ( '(' ')' ) | goalDesc )
                    pass 
                    string_literal88=self.match(self.input, 69, self.FOLLOW_69_in_actionDefBody1106) 
                    if self._state.backtracking == 0:
                        stream_69.add(string_literal88)
                    # Pddl.g:219:25: ( ( '(' ')' ) | goalDesc )
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == 54) :
                        LA31_1 = self.input.LA(2)

                        if (LA31_1 == 56) :
                            alt31 = 1
                        elif (LA31_1 == NAME or (71 <= LA31_1 <= 76) or (91 <= LA31_1 <= 95)) :
                            alt31 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 31, 1, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 31, 0, self.input)

                        raise nvae

                    if alt31 == 1:
                        # Pddl.g:219:26: ( '(' ')' )
                        pass 
                        # Pddl.g:219:26: ( '(' ')' )
                        # Pddl.g:219:27: '(' ')'
                        pass 
                        char_literal89=self.match(self.input, 54, self.FOLLOW_54_in_actionDefBody1110) 
                        if self._state.backtracking == 0:
                            stream_54.add(char_literal89)
                        char_literal90=self.match(self.input, 56, self.FOLLOW_56_in_actionDefBody1112) 
                        if self._state.backtracking == 0:
                            stream_56.add(char_literal90)





                    elif alt31 == 2:
                        # Pddl.g:219:38: goalDesc
                        pass 
                        self._state.following.append(self.FOLLOW_goalDesc_in_actionDefBody1117)
                        goalDesc91 = self.goalDesc()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_goalDesc.add(goalDesc91.tree)






                # Pddl.g:220:4: ( ':effect' ( ( '(' ')' ) | effect ) )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 70) :
                    alt34 = 1
                if alt34 == 1:
                    # Pddl.g:220:6: ':effect' ( ( '(' ')' ) | effect )
                    pass 
                    string_literal92=self.match(self.input, 70, self.FOLLOW_70_in_actionDefBody1127) 
                    if self._state.backtracking == 0:
                        stream_70.add(string_literal92)
                    # Pddl.g:220:16: ( ( '(' ')' ) | effect )
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 54) :
                        LA33_1 = self.input.LA(2)

                        if (LA33_1 == 56) :
                            alt33 = 1
                        elif (LA33_1 == NAME or LA33_1 == 71 or LA33_1 == 73 or LA33_1 == 76 or LA33_1 == 87 or (96 <= LA33_1 <= 100)) :
                            alt33 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 33, 1, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 33, 0, self.input)

                        raise nvae

                    if alt33 == 1:
                        # Pddl.g:220:17: ( '(' ')' )
                        pass 
                        # Pddl.g:220:17: ( '(' ')' )
                        # Pddl.g:220:18: '(' ')'
                        pass 
                        char_literal93=self.match(self.input, 54, self.FOLLOW_54_in_actionDefBody1131) 
                        if self._state.backtracking == 0:
                            stream_54.add(char_literal93)
                        char_literal94=self.match(self.input, 56, self.FOLLOW_56_in_actionDefBody1133) 
                        if self._state.backtracking == 0:
                            stream_56.add(char_literal94)





                    elif alt33 == 2:
                        # Pddl.g:220:29: effect
                        pass 
                        self._state.following.append(self.FOLLOW_effect_in_actionDefBody1138)
                        effect95 = self.effect()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_effect.add(effect95.tree)







                # AST Rewrite
                # elements: typedVariableList, goalDesc, effect
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 221:4: -> ^( PARAMETERS ( typedVariableList )? ) ^( PRECONDITION ( goalDesc )? ) ^( EFFECT ( effect )? )
                    # Pddl.g:221:7: ^( PARAMETERS ( typedVariableList )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMETERS, "PARAMETERS"), root_1)

                    # Pddl.g:221:20: ( typedVariableList )?
                    if stream_typedVariableList.hasNext():
                        self._adaptor.addChild(root_1, stream_typedVariableList.nextTree())


                    stream_typedVariableList.reset();

                    self._adaptor.addChild(root_0, root_1)
                    # Pddl.g:221:40: ^( PRECONDITION ( goalDesc )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PRECONDITION, "PRECONDITION"), root_1)

                    # Pddl.g:221:55: ( goalDesc )?
                    if stream_goalDesc.hasNext():
                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())


                    stream_goalDesc.reset();

                    self._adaptor.addChild(root_0, root_1)
                    # Pddl.g:221:66: ^( EFFECT ( effect )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EFFECT, "EFFECT"), root_1)

                    # Pddl.g:221:75: ( effect )?
                    if stream_effect.hasNext():
                        self._adaptor.addChild(root_1, stream_effect.nextTree())


                    stream_effect.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "actionDefBody"

    class goalDesc_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.goalDesc_return, self).__init__()

            self.tree = None




    # $ANTLR start "goalDesc"
    # Pddl.g:235:1: goalDesc : ( atomicTermFormula | '(' 'and' ( goalDesc )* ')' -> ^( AND_GD ( goalDesc )* ) | '(' 'or' ( goalDesc )* ')' -> ^( OR_GD ( goalDesc )* ) | '(' 'not' goalDesc ')' -> ^( NOT_GD goalDesc ) | '(' 'imply' goalDesc goalDesc ')' -> ^( IMPLY_GD goalDesc goalDesc ) | '(' 'exists' '(' typedVariableList ')' goalDesc ')' -> ^( EXISTS_GD typedVariableList goalDesc ) | '(' 'forall' '(' typedVariableList ')' goalDesc ')' -> ^( FORALL_GD typedVariableList goalDesc ) | fComp -> ^( COMPARISON_GD fComp ) );
    def goalDesc(self, ):

        retval = self.goalDesc_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal97 = None
        string_literal98 = None
        char_literal100 = None
        char_literal101 = None
        string_literal102 = None
        char_literal104 = None
        char_literal105 = None
        string_literal106 = None
        char_literal108 = None
        char_literal109 = None
        string_literal110 = None
        char_literal113 = None
        char_literal114 = None
        string_literal115 = None
        char_literal116 = None
        char_literal118 = None
        char_literal120 = None
        char_literal121 = None
        string_literal122 = None
        char_literal123 = None
        char_literal125 = None
        char_literal127 = None
        atomicTermFormula96 = None

        goalDesc99 = None

        goalDesc103 = None

        goalDesc107 = None

        goalDesc111 = None

        goalDesc112 = None

        typedVariableList117 = None

        goalDesc119 = None

        typedVariableList124 = None

        goalDesc126 = None

        fComp128 = None


        char_literal97_tree = None
        string_literal98_tree = None
        char_literal100_tree = None
        char_literal101_tree = None
        string_literal102_tree = None
        char_literal104_tree = None
        char_literal105_tree = None
        string_literal106_tree = None
        char_literal108_tree = None
        char_literal109_tree = None
        string_literal110_tree = None
        char_literal113_tree = None
        char_literal114_tree = None
        string_literal115_tree = None
        char_literal116_tree = None
        char_literal118_tree = None
        char_literal120_tree = None
        char_literal121_tree = None
        string_literal122_tree = None
        char_literal123_tree = None
        char_literal125_tree = None
        char_literal127_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_72 = RewriteRuleTokenStream(self._adaptor, "token 72")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_74 = RewriteRuleTokenStream(self._adaptor, "token 74")
        stream_75 = RewriteRuleTokenStream(self._adaptor, "token 75")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_fComp = RewriteRuleSubtreeStream(self._adaptor, "rule fComp")
        stream_goalDesc = RewriteRuleSubtreeStream(self._adaptor, "rule goalDesc")
        stream_typedVariableList = RewriteRuleSubtreeStream(self._adaptor, "rule typedVariableList")
        try:
            try:
                # Pddl.g:236:2: ( atomicTermFormula | '(' 'and' ( goalDesc )* ')' -> ^( AND_GD ( goalDesc )* ) | '(' 'or' ( goalDesc )* ')' -> ^( OR_GD ( goalDesc )* ) | '(' 'not' goalDesc ')' -> ^( NOT_GD goalDesc ) | '(' 'imply' goalDesc goalDesc ')' -> ^( IMPLY_GD goalDesc goalDesc ) | '(' 'exists' '(' typedVariableList ')' goalDesc ')' -> ^( EXISTS_GD typedVariableList goalDesc ) | '(' 'forall' '(' typedVariableList ')' goalDesc ')' -> ^( FORALL_GD typedVariableList goalDesc ) | fComp -> ^( COMPARISON_GD fComp ) )
                alt37 = 8
                alt37 = self.dfa37.predict(self.input)
                if alt37 == 1:
                    # Pddl.g:236:4: atomicTermFormula
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atomicTermFormula_in_goalDesc1189)
                    atomicTermFormula96 = self.atomicTermFormula()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atomicTermFormula96.tree)


                elif alt37 == 2:
                    # Pddl.g:237:4: '(' 'and' ( goalDesc )* ')'
                    pass 
                    char_literal97=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1194) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal97)
                    string_literal98=self.match(self.input, 71, self.FOLLOW_71_in_goalDesc1196) 
                    if self._state.backtracking == 0:
                        stream_71.add(string_literal98)
                    # Pddl.g:237:14: ( goalDesc )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == 54) :
                            alt35 = 1


                        if alt35 == 1:
                            # Pddl.g:0:0: goalDesc
                            pass 
                            self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1198)
                            goalDesc99 = self.goalDesc()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_goalDesc.add(goalDesc99.tree)


                        else:
                            break #loop35
                    char_literal100=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1201) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal100)

                    # AST Rewrite
                    # elements: goalDesc
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 238:12: -> ^( AND_GD ( goalDesc )* )
                        # Pddl.g:238:15: ^( AND_GD ( goalDesc )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AND_GD, "AND_GD"), root_1)

                        # Pddl.g:238:24: ( goalDesc )*
                        while stream_goalDesc.hasNext():
                            self._adaptor.addChild(root_1, stream_goalDesc.nextTree())


                        stream_goalDesc.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 3:
                    # Pddl.g:239:4: '(' 'or' ( goalDesc )* ')'
                    pass 
                    char_literal101=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1226) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal101)
                    string_literal102=self.match(self.input, 72, self.FOLLOW_72_in_goalDesc1228) 
                    if self._state.backtracking == 0:
                        stream_72.add(string_literal102)
                    # Pddl.g:239:13: ( goalDesc )*
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == 54) :
                            alt36 = 1


                        if alt36 == 1:
                            # Pddl.g:0:0: goalDesc
                            pass 
                            self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1230)
                            goalDesc103 = self.goalDesc()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_goalDesc.add(goalDesc103.tree)


                        else:
                            break #loop36
                    char_literal104=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1233) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal104)

                    # AST Rewrite
                    # elements: goalDesc
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 240:12: -> ^( OR_GD ( goalDesc )* )
                        # Pddl.g:240:15: ^( OR_GD ( goalDesc )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OR_GD, "OR_GD"), root_1)

                        # Pddl.g:240:23: ( goalDesc )*
                        while stream_goalDesc.hasNext():
                            self._adaptor.addChild(root_1, stream_goalDesc.nextTree())


                        stream_goalDesc.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 4:
                    # Pddl.g:241:4: '(' 'not' goalDesc ')'
                    pass 
                    char_literal105=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1258) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal105)
                    string_literal106=self.match(self.input, 73, self.FOLLOW_73_in_goalDesc1260) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal106)
                    self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1262)
                    goalDesc107 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc107.tree)
                    char_literal108=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1264) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal108)

                    # AST Rewrite
                    # elements: goalDesc
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 242:12: -> ^( NOT_GD goalDesc )
                        # Pddl.g:242:15: ^( NOT_GD goalDesc )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NOT_GD, "NOT_GD"), root_1)

                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 5:
                    # Pddl.g:243:4: '(' 'imply' goalDesc goalDesc ')'
                    pass 
                    char_literal109=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1288) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal109)
                    string_literal110=self.match(self.input, 74, self.FOLLOW_74_in_goalDesc1290) 
                    if self._state.backtracking == 0:
                        stream_74.add(string_literal110)
                    self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1292)
                    goalDesc111 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc111.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1294)
                    goalDesc112 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc112.tree)
                    char_literal113=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1296) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal113)

                    # AST Rewrite
                    # elements: goalDesc, goalDesc
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 244:12: -> ^( IMPLY_GD goalDesc goalDesc )
                        # Pddl.g:244:15: ^( IMPLY_GD goalDesc goalDesc )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(IMPLY_GD, "IMPLY_GD"), root_1)

                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())
                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 6:
                    # Pddl.g:245:4: '(' 'exists' '(' typedVariableList ')' goalDesc ')'
                    pass 
                    char_literal114=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1322) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal114)
                    string_literal115=self.match(self.input, 75, self.FOLLOW_75_in_goalDesc1324) 
                    if self._state.backtracking == 0:
                        stream_75.add(string_literal115)
                    char_literal116=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1326) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal116)
                    self._state.following.append(self.FOLLOW_typedVariableList_in_goalDesc1328)
                    typedVariableList117 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typedVariableList.add(typedVariableList117.tree)
                    char_literal118=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1330) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal118)
                    self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1332)
                    goalDesc119 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc119.tree)
                    char_literal120=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1334) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal120)

                    # AST Rewrite
                    # elements: goalDesc, typedVariableList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 246:12: -> ^( EXISTS_GD typedVariableList goalDesc )
                        # Pddl.g:246:15: ^( EXISTS_GD typedVariableList goalDesc )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXISTS_GD, "EXISTS_GD"), root_1)

                        self._adaptor.addChild(root_1, stream_typedVariableList.nextTree())
                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 7:
                    # Pddl.g:247:4: '(' 'forall' '(' typedVariableList ')' goalDesc ')'
                    pass 
                    char_literal121=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1360) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal121)
                    string_literal122=self.match(self.input, 76, self.FOLLOW_76_in_goalDesc1362) 
                    if self._state.backtracking == 0:
                        stream_76.add(string_literal122)
                    char_literal123=self.match(self.input, 54, self.FOLLOW_54_in_goalDesc1364) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal123)
                    self._state.following.append(self.FOLLOW_typedVariableList_in_goalDesc1366)
                    typedVariableList124 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typedVariableList.add(typedVariableList124.tree)
                    char_literal125=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1368) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal125)
                    self._state.following.append(self.FOLLOW_goalDesc_in_goalDesc1370)
                    goalDesc126 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc126.tree)
                    char_literal127=self.match(self.input, 56, self.FOLLOW_56_in_goalDesc1372) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal127)

                    # AST Rewrite
                    # elements: goalDesc, typedVariableList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 248:12: -> ^( FORALL_GD typedVariableList goalDesc )
                        # Pddl.g:248:15: ^( FORALL_GD typedVariableList goalDesc )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FORALL_GD, "FORALL_GD"), root_1)

                        self._adaptor.addChild(root_1, stream_typedVariableList.nextTree())
                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 8:
                    # Pddl.g:249:7: fComp
                    pass 
                    self._state.following.append(self.FOLLOW_fComp_in_goalDesc1401)
                    fComp128 = self.fComp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fComp.add(fComp128.tree)

                    # AST Rewrite
                    # elements: fComp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 250:15: -> ^( COMPARISON_GD fComp )
                        # Pddl.g:250:18: ^( COMPARISON_GD fComp )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(COMPARISON_GD, "COMPARISON_GD"), root_1)

                        self._adaptor.addChild(root_1, stream_fComp.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "goalDesc"

    class fComp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fComp_return, self).__init__()

            self.tree = None




    # $ANTLR start "fComp"
    # Pddl.g:253:1: fComp : '(' binaryComp fExp fExp ')' ;
    def fComp(self, ):

        retval = self.fComp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal129 = None
        char_literal133 = None
        binaryComp130 = None

        fExp131 = None

        fExp132 = None


        char_literal129_tree = None
        char_literal133_tree = None

        try:
            try:
                # Pddl.g:254:2: ( '(' binaryComp fExp fExp ')' )
                # Pddl.g:254:4: '(' binaryComp fExp fExp ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal129=self.match(self.input, 54, self.FOLLOW_54_in_fComp1437)
                self._state.following.append(self.FOLLOW_binaryComp_in_fComp1440)
                binaryComp130 = self.binaryComp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, binaryComp130.tree)
                self._state.following.append(self.FOLLOW_fExp_in_fComp1442)
                fExp131 = self.fExp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fExp131.tree)
                self._state.following.append(self.FOLLOW_fExp_in_fComp1444)
                fExp132 = self.fExp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fExp132.tree)
                char_literal133=self.match(self.input, 56, self.FOLLOW_56_in_fComp1446)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fComp"

    class atomicTermFormula_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.atomicTermFormula_return, self).__init__()

            self.tree = None




    # $ANTLR start "atomicTermFormula"
    # Pddl.g:257:1: atomicTermFormula : '(' predicate ( term )* ')' -> ^( PRED_HEAD predicate ( term )* ) ;
    def atomicTermFormula(self, ):

        retval = self.atomicTermFormula_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal134 = None
        char_literal137 = None
        predicate135 = None

        term136 = None


        char_literal134_tree = None
        char_literal137_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        stream_predicate = RewriteRuleSubtreeStream(self._adaptor, "rule predicate")
        try:
            try:
                # Pddl.g:258:2: ( '(' predicate ( term )* ')' -> ^( PRED_HEAD predicate ( term )* ) )
                # Pddl.g:258:4: '(' predicate ( term )* ')'
                pass 
                char_literal134=self.match(self.input, 54, self.FOLLOW_54_in_atomicTermFormula1458) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal134)
                self._state.following.append(self.FOLLOW_predicate_in_atomicTermFormula1460)
                predicate135 = self.predicate()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_predicate.add(predicate135.tree)
                # Pddl.g:258:18: ( term )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == NAME or LA38_0 == VARIABLE) :
                        alt38 = 1


                    if alt38 == 1:
                        # Pddl.g:0:0: term
                        pass 
                        self._state.following.append(self.FOLLOW_term_in_atomicTermFormula1462)
                        term136 = self.term()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_term.add(term136.tree)


                    else:
                        break #loop38
                char_literal137=self.match(self.input, 56, self.FOLLOW_56_in_atomicTermFormula1465) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal137)

                # AST Rewrite
                # elements: term, predicate
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 258:28: -> ^( PRED_HEAD predicate ( term )* )
                    # Pddl.g:258:31: ^( PRED_HEAD predicate ( term )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PRED_HEAD, "PRED_HEAD"), root_1)

                    self._adaptor.addChild(root_1, stream_predicate.nextTree())
                    # Pddl.g:258:53: ( term )*
                    while stream_term.hasNext():
                        self._adaptor.addChild(root_1, stream_term.nextTree())


                    stream_term.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atomicTermFormula"

    class term_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.term_return, self).__init__()

            self.tree = None




    # $ANTLR start "term"
    # Pddl.g:261:1: term : ( NAME | VARIABLE );
    def term(self, ):

        retval = self.term_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set138 = None

        set138_tree = None

        try:
            try:
                # Pddl.g:261:6: ( NAME | VARIABLE )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set138 = self.input.LT(1)
                if self.input.LA(1) == NAME or self.input.LA(1) == VARIABLE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set138))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "term"

    class durativeActionDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.durativeActionDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "durativeActionDef"
    # Pddl.g:263:1: durativeActionDef : '(' ':durative-action' actionSymbol ':parameters' '(' typedVariableList ')' daDefBody ')' -> ^( DURATIVE_ACTION actionSymbol typedVariableList daDefBody ) ;
    def durativeActionDef(self, ):

        retval = self.durativeActionDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal139 = None
        string_literal140 = None
        string_literal142 = None
        char_literal143 = None
        char_literal145 = None
        char_literal147 = None
        actionSymbol141 = None

        typedVariableList144 = None

        daDefBody146 = None


        char_literal139_tree = None
        string_literal140_tree = None
        string_literal142_tree = None
        char_literal143_tree = None
        char_literal145_tree = None
        char_literal147_tree = None
        stream_68 = RewriteRuleTokenStream(self._adaptor, "token 68")
        stream_77 = RewriteRuleTokenStream(self._adaptor, "token 77")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_actionSymbol = RewriteRuleSubtreeStream(self._adaptor, "rule actionSymbol")
        stream_daDefBody = RewriteRuleSubtreeStream(self._adaptor, "rule daDefBody")
        stream_typedVariableList = RewriteRuleSubtreeStream(self._adaptor, "rule typedVariableList")
        try:
            try:
                # Pddl.g:266:2: ( '(' ':durative-action' actionSymbol ':parameters' '(' typedVariableList ')' daDefBody ')' -> ^( DURATIVE_ACTION actionSymbol typedVariableList daDefBody ) )
                # Pddl.g:266:4: '(' ':durative-action' actionSymbol ':parameters' '(' typedVariableList ')' daDefBody ')'
                pass 
                char_literal139=self.match(self.input, 54, self.FOLLOW_54_in_durativeActionDef1503) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal139)
                string_literal140=self.match(self.input, 77, self.FOLLOW_77_in_durativeActionDef1505) 
                if self._state.backtracking == 0:
                    stream_77.add(string_literal140)
                self._state.following.append(self.FOLLOW_actionSymbol_in_durativeActionDef1507)
                actionSymbol141 = self.actionSymbol()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_actionSymbol.add(actionSymbol141.tree)
                string_literal142=self.match(self.input, 68, self.FOLLOW_68_in_durativeActionDef1516) 
                if self._state.backtracking == 0:
                    stream_68.add(string_literal142)
                char_literal143=self.match(self.input, 54, self.FOLLOW_54_in_durativeActionDef1518) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal143)
                self._state.following.append(self.FOLLOW_typedVariableList_in_durativeActionDef1520)
                typedVariableList144 = self.typedVariableList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typedVariableList.add(typedVariableList144.tree)
                char_literal145=self.match(self.input, 56, self.FOLLOW_56_in_durativeActionDef1522) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal145)
                self._state.following.append(self.FOLLOW_daDefBody_in_durativeActionDef1535)
                daDefBody146 = self.daDefBody()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_daDefBody.add(daDefBody146.tree)
                char_literal147=self.match(self.input, 56, self.FOLLOW_56_in_durativeActionDef1537) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal147)

                # AST Rewrite
                # elements: daDefBody, actionSymbol, typedVariableList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 269:8: -> ^( DURATIVE_ACTION actionSymbol typedVariableList daDefBody )
                    # Pddl.g:269:11: ^( DURATIVE_ACTION actionSymbol typedVariableList daDefBody )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(DURATIVE_ACTION, "DURATIVE_ACTION"), root_1)

                    self._adaptor.addChild(root_1, stream_actionSymbol.nextTree())
                    self._adaptor.addChild(root_1, stream_typedVariableList.nextTree())
                    self._adaptor.addChild(root_1, stream_daDefBody.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "durativeActionDef"

    class daDefBody_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.daDefBody_return, self).__init__()

            self.tree = None




    # $ANTLR start "daDefBody"
    # Pddl.g:272:1: daDefBody : ( ':duration' durationConstraint | ':condition' ( ( '(' ')' ) | daGD ) | ':effect' ( ( '(' ')' ) | daEffect ) );
    def daDefBody(self, ):

        retval = self.daDefBody_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal148 = None
        string_literal150 = None
        char_literal151 = None
        char_literal152 = None
        string_literal154 = None
        char_literal155 = None
        char_literal156 = None
        durationConstraint149 = None

        daGD153 = None

        daEffect157 = None


        string_literal148_tree = None
        string_literal150_tree = None
        char_literal151_tree = None
        char_literal152_tree = None
        string_literal154_tree = None
        char_literal155_tree = None
        char_literal156_tree = None

        try:
            try:
                # Pddl.g:273:2: ( ':duration' durationConstraint | ':condition' ( ( '(' ')' ) | daGD ) | ':effect' ( ( '(' ')' ) | daEffect ) )
                alt41 = 3
                LA41 = self.input.LA(1)
                if LA41 == 78:
                    alt41 = 1
                elif LA41 == 79:
                    alt41 = 2
                elif LA41 == 70:
                    alt41 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae

                if alt41 == 1:
                    # Pddl.g:273:4: ':duration' durationConstraint
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal148=self.match(self.input, 78, self.FOLLOW_78_in_daDefBody1570)
                    if self._state.backtracking == 0:

                        string_literal148_tree = self._adaptor.createWithPayload(string_literal148)
                        self._adaptor.addChild(root_0, string_literal148_tree)

                    self._state.following.append(self.FOLLOW_durationConstraint_in_daDefBody1572)
                    durationConstraint149 = self.durationConstraint()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, durationConstraint149.tree)


                elif alt41 == 2:
                    # Pddl.g:274:4: ':condition' ( ( '(' ')' ) | daGD )
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal150=self.match(self.input, 79, self.FOLLOW_79_in_daDefBody1577)
                    if self._state.backtracking == 0:

                        string_literal150_tree = self._adaptor.createWithPayload(string_literal150)
                        self._adaptor.addChild(root_0, string_literal150_tree)

                    # Pddl.g:274:17: ( ( '(' ')' ) | daGD )
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == 54) :
                        LA39_1 = self.input.LA(2)

                        if (LA39_1 == 56) :
                            alt39 = 1
                        elif (LA39_1 == 71 or LA39_1 == 76 or (80 <= LA39_1 <= 82)) :
                            alt39 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 39, 1, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 39, 0, self.input)

                        raise nvae

                    if alt39 == 1:
                        # Pddl.g:274:18: ( '(' ')' )
                        pass 
                        # Pddl.g:274:18: ( '(' ')' )
                        # Pddl.g:274:19: '(' ')'
                        pass 
                        char_literal151=self.match(self.input, 54, self.FOLLOW_54_in_daDefBody1581)
                        if self._state.backtracking == 0:

                            char_literal151_tree = self._adaptor.createWithPayload(char_literal151)
                            self._adaptor.addChild(root_0, char_literal151_tree)

                        char_literal152=self.match(self.input, 56, self.FOLLOW_56_in_daDefBody1583)
                        if self._state.backtracking == 0:

                            char_literal152_tree = self._adaptor.createWithPayload(char_literal152)
                            self._adaptor.addChild(root_0, char_literal152_tree)






                    elif alt39 == 2:
                        # Pddl.g:274:30: daGD
                        pass 
                        self._state.following.append(self.FOLLOW_daGD_in_daDefBody1588)
                        daGD153 = self.daGD()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, daGD153.tree)





                elif alt41 == 3:
                    # Pddl.g:275:7: ':effect' ( ( '(' ')' ) | daEffect )
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal154=self.match(self.input, 70, self.FOLLOW_70_in_daDefBody1597)
                    if self._state.backtracking == 0:

                        string_literal154_tree = self._adaptor.createWithPayload(string_literal154)
                        self._adaptor.addChild(root_0, string_literal154_tree)

                    # Pddl.g:275:17: ( ( '(' ')' ) | daEffect )
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 54) :
                        LA40_1 = self.input.LA(2)

                        if (LA40_1 == 56) :
                            alt40 = 1
                        elif (LA40_1 == 71 or LA40_1 == 76 or LA40_1 == 81 or LA40_1 == 87 or (96 <= LA40_1 <= 100)) :
                            alt40 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 40, 1, self.input)

                            raise nvae

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 40, 0, self.input)

                        raise nvae

                    if alt40 == 1:
                        # Pddl.g:275:18: ( '(' ')' )
                        pass 
                        # Pddl.g:275:18: ( '(' ')' )
                        # Pddl.g:275:19: '(' ')'
                        pass 
                        char_literal155=self.match(self.input, 54, self.FOLLOW_54_in_daDefBody1601)
                        if self._state.backtracking == 0:

                            char_literal155_tree = self._adaptor.createWithPayload(char_literal155)
                            self._adaptor.addChild(root_0, char_literal155_tree)

                        char_literal156=self.match(self.input, 56, self.FOLLOW_56_in_daDefBody1603)
                        if self._state.backtracking == 0:

                            char_literal156_tree = self._adaptor.createWithPayload(char_literal156)
                            self._adaptor.addChild(root_0, char_literal156_tree)






                    elif alt40 == 2:
                        # Pddl.g:275:30: daEffect
                        pass 
                        self._state.following.append(self.FOLLOW_daEffect_in_daDefBody1608)
                        daEffect157 = self.daEffect()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, daEffect157.tree)





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "daDefBody"

    class daGD_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.daGD_return, self).__init__()

            self.tree = None




    # $ANTLR start "daGD"
    # Pddl.g:278:1: daGD : ( prefTimedGD | '(' 'and' ( daGD )* ')' | '(' 'forall' '(' typedVariableList ')' daGD ')' );
    def daGD(self, ):

        retval = self.daGD_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal159 = None
        string_literal160 = None
        char_literal162 = None
        char_literal163 = None
        string_literal164 = None
        char_literal165 = None
        char_literal167 = None
        char_literal169 = None
        prefTimedGD158 = None

        daGD161 = None

        typedVariableList166 = None

        daGD168 = None


        char_literal159_tree = None
        string_literal160_tree = None
        char_literal162_tree = None
        char_literal163_tree = None
        string_literal164_tree = None
        char_literal165_tree = None
        char_literal167_tree = None
        char_literal169_tree = None

        try:
            try:
                # Pddl.g:279:2: ( prefTimedGD | '(' 'and' ( daGD )* ')' | '(' 'forall' '(' typedVariableList ')' daGD ')' )
                alt43 = 3
                LA43_0 = self.input.LA(1)

                if (LA43_0 == 54) :
                    LA43 = self.input.LA(2)
                    if LA43 == 80 or LA43 == 81 or LA43 == 82:
                        alt43 = 1
                    elif LA43 == 71:
                        alt43 = 2
                    elif LA43 == 76:
                        alt43 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 43, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 43, 0, self.input)

                    raise nvae

                if alt43 == 1:
                    # Pddl.g:279:4: prefTimedGD
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_prefTimedGD_in_daGD1623)
                    prefTimedGD158 = self.prefTimedGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prefTimedGD158.tree)


                elif alt43 == 2:
                    # Pddl.g:280:4: '(' 'and' ( daGD )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal159=self.match(self.input, 54, self.FOLLOW_54_in_daGD1628)
                    if self._state.backtracking == 0:

                        char_literal159_tree = self._adaptor.createWithPayload(char_literal159)
                        self._adaptor.addChild(root_0, char_literal159_tree)

                    string_literal160=self.match(self.input, 71, self.FOLLOW_71_in_daGD1630)
                    if self._state.backtracking == 0:

                        string_literal160_tree = self._adaptor.createWithPayload(string_literal160)
                        self._adaptor.addChild(root_0, string_literal160_tree)

                    # Pddl.g:280:14: ( daGD )*
                    while True: #loop42
                        alt42 = 2
                        LA42_0 = self.input.LA(1)

                        if (LA42_0 == 54) :
                            alt42 = 1


                        if alt42 == 1:
                            # Pddl.g:0:0: daGD
                            pass 
                            self._state.following.append(self.FOLLOW_daGD_in_daGD1632)
                            daGD161 = self.daGD()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, daGD161.tree)


                        else:
                            break #loop42
                    char_literal162=self.match(self.input, 56, self.FOLLOW_56_in_daGD1635)
                    if self._state.backtracking == 0:

                        char_literal162_tree = self._adaptor.createWithPayload(char_literal162)
                        self._adaptor.addChild(root_0, char_literal162_tree)



                elif alt43 == 3:
                    # Pddl.g:281:4: '(' 'forall' '(' typedVariableList ')' daGD ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal163=self.match(self.input, 54, self.FOLLOW_54_in_daGD1640)
                    if self._state.backtracking == 0:

                        char_literal163_tree = self._adaptor.createWithPayload(char_literal163)
                        self._adaptor.addChild(root_0, char_literal163_tree)

                    string_literal164=self.match(self.input, 76, self.FOLLOW_76_in_daGD1642)
                    if self._state.backtracking == 0:

                        string_literal164_tree = self._adaptor.createWithPayload(string_literal164)
                        self._adaptor.addChild(root_0, string_literal164_tree)

                    char_literal165=self.match(self.input, 54, self.FOLLOW_54_in_daGD1644)
                    if self._state.backtracking == 0:

                        char_literal165_tree = self._adaptor.createWithPayload(char_literal165)
                        self._adaptor.addChild(root_0, char_literal165_tree)

                    self._state.following.append(self.FOLLOW_typedVariableList_in_daGD1646)
                    typedVariableList166 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typedVariableList166.tree)
                    char_literal167=self.match(self.input, 56, self.FOLLOW_56_in_daGD1648)
                    if self._state.backtracking == 0:

                        char_literal167_tree = self._adaptor.createWithPayload(char_literal167)
                        self._adaptor.addChild(root_0, char_literal167_tree)

                    self._state.following.append(self.FOLLOW_daGD_in_daGD1650)
                    daGD168 = self.daGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, daGD168.tree)
                    char_literal169=self.match(self.input, 56, self.FOLLOW_56_in_daGD1652)
                    if self._state.backtracking == 0:

                        char_literal169_tree = self._adaptor.createWithPayload(char_literal169)
                        self._adaptor.addChild(root_0, char_literal169_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "daGD"

    class prefTimedGD_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.prefTimedGD_return, self).__init__()

            self.tree = None




    # $ANTLR start "prefTimedGD"
    # Pddl.g:284:1: prefTimedGD : ( timedGD | '(' 'preference' ( NAME )? timedGD ')' );
    def prefTimedGD(self, ):

        retval = self.prefTimedGD_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal171 = None
        string_literal172 = None
        NAME173 = None
        char_literal175 = None
        timedGD170 = None

        timedGD174 = None


        char_literal171_tree = None
        string_literal172_tree = None
        NAME173_tree = None
        char_literal175_tree = None

        try:
            try:
                # Pddl.g:285:2: ( timedGD | '(' 'preference' ( NAME )? timedGD ')' )
                alt45 = 2
                LA45_0 = self.input.LA(1)

                if (LA45_0 == 54) :
                    LA45_1 = self.input.LA(2)

                    if ((81 <= LA45_1 <= 82)) :
                        alt45 = 1
                    elif (LA45_1 == 80) :
                        alt45 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 45, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae

                if alt45 == 1:
                    # Pddl.g:285:4: timedGD
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_timedGD_in_prefTimedGD1663)
                    timedGD170 = self.timedGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timedGD170.tree)


                elif alt45 == 2:
                    # Pddl.g:286:4: '(' 'preference' ( NAME )? timedGD ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal171=self.match(self.input, 54, self.FOLLOW_54_in_prefTimedGD1668)
                    if self._state.backtracking == 0:

                        char_literal171_tree = self._adaptor.createWithPayload(char_literal171)
                        self._adaptor.addChild(root_0, char_literal171_tree)

                    string_literal172=self.match(self.input, 80, self.FOLLOW_80_in_prefTimedGD1670)
                    if self._state.backtracking == 0:

                        string_literal172_tree = self._adaptor.createWithPayload(string_literal172)
                        self._adaptor.addChild(root_0, string_literal172_tree)

                    # Pddl.g:286:21: ( NAME )?
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == NAME) :
                        alt44 = 1
                    if alt44 == 1:
                        # Pddl.g:0:0: NAME
                        pass 
                        NAME173=self.match(self.input, NAME, self.FOLLOW_NAME_in_prefTimedGD1672)
                        if self._state.backtracking == 0:

                            NAME173_tree = self._adaptor.createWithPayload(NAME173)
                            self._adaptor.addChild(root_0, NAME173_tree)




                    self._state.following.append(self.FOLLOW_timedGD_in_prefTimedGD1675)
                    timedGD174 = self.timedGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timedGD174.tree)
                    char_literal175=self.match(self.input, 56, self.FOLLOW_56_in_prefTimedGD1677)
                    if self._state.backtracking == 0:

                        char_literal175_tree = self._adaptor.createWithPayload(char_literal175)
                        self._adaptor.addChild(root_0, char_literal175_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prefTimedGD"

    class timedGD_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.timedGD_return, self).__init__()

            self.tree = None




    # $ANTLR start "timedGD"
    # Pddl.g:289:1: timedGD : ( '(' 'at' timeSpecifier goalDesc ')' | '(' 'over' interval goalDesc ')' );
    def timedGD(self, ):

        retval = self.timedGD_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal176 = None
        string_literal177 = None
        char_literal180 = None
        char_literal181 = None
        string_literal182 = None
        char_literal185 = None
        timeSpecifier178 = None

        goalDesc179 = None

        interval183 = None

        goalDesc184 = None


        char_literal176_tree = None
        string_literal177_tree = None
        char_literal180_tree = None
        char_literal181_tree = None
        string_literal182_tree = None
        char_literal185_tree = None

        try:
            try:
                # Pddl.g:290:2: ( '(' 'at' timeSpecifier goalDesc ')' | '(' 'over' interval goalDesc ')' )
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == 54) :
                    LA46_1 = self.input.LA(2)

                    if (LA46_1 == 81) :
                        alt46 = 1
                    elif (LA46_1 == 82) :
                        alt46 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 46, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae

                if alt46 == 1:
                    # Pddl.g:290:4: '(' 'at' timeSpecifier goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal176=self.match(self.input, 54, self.FOLLOW_54_in_timedGD1688)
                    if self._state.backtracking == 0:

                        char_literal176_tree = self._adaptor.createWithPayload(char_literal176)
                        self._adaptor.addChild(root_0, char_literal176_tree)

                    string_literal177=self.match(self.input, 81, self.FOLLOW_81_in_timedGD1690)
                    if self._state.backtracking == 0:

                        string_literal177_tree = self._adaptor.createWithPayload(string_literal177)
                        self._adaptor.addChild(root_0, string_literal177_tree)

                    self._state.following.append(self.FOLLOW_timeSpecifier_in_timedGD1692)
                    timeSpecifier178 = self.timeSpecifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timeSpecifier178.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_timedGD1694)
                    goalDesc179 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc179.tree)
                    char_literal180=self.match(self.input, 56, self.FOLLOW_56_in_timedGD1696)
                    if self._state.backtracking == 0:

                        char_literal180_tree = self._adaptor.createWithPayload(char_literal180)
                        self._adaptor.addChild(root_0, char_literal180_tree)



                elif alt46 == 2:
                    # Pddl.g:291:4: '(' 'over' interval goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal181=self.match(self.input, 54, self.FOLLOW_54_in_timedGD1701)
                    if self._state.backtracking == 0:

                        char_literal181_tree = self._adaptor.createWithPayload(char_literal181)
                        self._adaptor.addChild(root_0, char_literal181_tree)

                    string_literal182=self.match(self.input, 82, self.FOLLOW_82_in_timedGD1703)
                    if self._state.backtracking == 0:

                        string_literal182_tree = self._adaptor.createWithPayload(string_literal182)
                        self._adaptor.addChild(root_0, string_literal182_tree)

                    self._state.following.append(self.FOLLOW_interval_in_timedGD1705)
                    interval183 = self.interval()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, interval183.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_timedGD1707)
                    goalDesc184 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc184.tree)
                    char_literal185=self.match(self.input, 56, self.FOLLOW_56_in_timedGD1709)
                    if self._state.backtracking == 0:

                        char_literal185_tree = self._adaptor.createWithPayload(char_literal185)
                        self._adaptor.addChild(root_0, char_literal185_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "timedGD"

    class timeSpecifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.timeSpecifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "timeSpecifier"
    # Pddl.g:294:1: timeSpecifier : ( 'start' | 'end' );
    def timeSpecifier(self, ):

        retval = self.timeSpecifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set186 = None

        set186_tree = None

        try:
            try:
                # Pddl.g:294:15: ( 'start' | 'end' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set186 = self.input.LT(1)
                if (83 <= self.input.LA(1) <= 84):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set186))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "timeSpecifier"

    class interval_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.interval_return, self).__init__()

            self.tree = None




    # $ANTLR start "interval"
    # Pddl.g:295:1: interval : 'all' ;
    def interval(self, ):

        retval = self.interval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        string_literal187 = None

        string_literal187_tree = None

        try:
            try:
                # Pddl.g:295:10: ( 'all' )
                # Pddl.g:295:12: 'all'
                pass 
                root_0 = self._adaptor.nil()

                string_literal187=self.match(self.input, 85, self.FOLLOW_85_in_interval1731)
                if self._state.backtracking == 0:

                    string_literal187_tree = self._adaptor.createWithPayload(string_literal187)
                    self._adaptor.addChild(root_0, string_literal187_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "interval"

    class derivedDef_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.derivedDef_return, self).__init__()

            self.tree = None




    # $ANTLR start "derivedDef"
    # Pddl.g:297:1: derivedDef : '(' ':derived' typedVariableList goalDesc ')' ;
    def derivedDef(self, ):

        retval = self.derivedDef_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal188 = None
        string_literal189 = None
        char_literal192 = None
        typedVariableList190 = None

        goalDesc191 = None


        char_literal188_tree = None
        string_literal189_tree = None
        char_literal192_tree = None

        try:
            try:
                # Pddl.g:300:2: ( '(' ':derived' typedVariableList goalDesc ')' )
                # Pddl.g:300:4: '(' ':derived' typedVariableList goalDesc ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal188=self.match(self.input, 54, self.FOLLOW_54_in_derivedDef1744)
                string_literal189=self.match(self.input, 86, self.FOLLOW_86_in_derivedDef1747)
                if self._state.backtracking == 0:

                    string_literal189_tree = self._adaptor.createWithPayload(string_literal189)
                    root_0 = self._adaptor.becomeRoot(string_literal189_tree, root_0)

                self._state.following.append(self.FOLLOW_typedVariableList_in_derivedDef1750)
                typedVariableList190 = self.typedVariableList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, typedVariableList190.tree)
                self._state.following.append(self.FOLLOW_goalDesc_in_derivedDef1752)
                goalDesc191 = self.goalDesc()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, goalDesc191.tree)
                char_literal192=self.match(self.input, 56, self.FOLLOW_56_in_derivedDef1754)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "derivedDef"

    class fExp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fExp_return, self).__init__()

            self.tree = None




    # $ANTLR start "fExp"
    # Pddl.g:303:1: fExp : ( NUMBER | '(' binaryOp fExp fExp2 ')' -> ^( BINARY_OP binaryOp fExp fExp2 ) | '(' '-' fExp ')' -> ^( UNARY_MINUS fExp ) | fHead );
    def fExp(self, ):

        retval = self.fExp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER193 = None
        char_literal194 = None
        char_literal198 = None
        char_literal199 = None
        char_literal200 = None
        char_literal202 = None
        binaryOp195 = None

        fExp196 = None

        fExp2197 = None

        fExp201 = None

        fHead203 = None


        NUMBER193_tree = None
        char_literal194_tree = None
        char_literal198_tree = None
        char_literal199_tree = None
        char_literal200_tree = None
        char_literal202_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_60 = RewriteRuleTokenStream(self._adaptor, "token 60")
        stream_fExp2 = RewriteRuleSubtreeStream(self._adaptor, "rule fExp2")
        stream_fExp = RewriteRuleSubtreeStream(self._adaptor, "rule fExp")
        stream_binaryOp = RewriteRuleSubtreeStream(self._adaptor, "rule binaryOp")
        try:
            try:
                # Pddl.g:306:2: ( NUMBER | '(' binaryOp fExp fExp2 ')' -> ^( BINARY_OP binaryOp fExp fExp2 ) | '(' '-' fExp ')' -> ^( UNARY_MINUS fExp ) | fHead )
                alt47 = 4
                LA47 = self.input.LA(1)
                if LA47 == NUMBER:
                    alt47 = 1
                elif LA47 == 54:
                    LA47_2 = self.input.LA(2)

                    if (self.synpred59_Pddl()) :
                        alt47 = 2
                    elif (self.synpred60_Pddl()) :
                        alt47 = 3
                    elif (True) :
                        alt47 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 47, 2, self.input)

                        raise nvae

                elif LA47 == NAME:
                    alt47 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # Pddl.g:306:4: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER193=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_fExp1769)
                    if self._state.backtracking == 0:

                        NUMBER193_tree = self._adaptor.createWithPayload(NUMBER193)
                        self._adaptor.addChild(root_0, NUMBER193_tree)



                elif alt47 == 2:
                    # Pddl.g:307:4: '(' binaryOp fExp fExp2 ')'
                    pass 
                    char_literal194=self.match(self.input, 54, self.FOLLOW_54_in_fExp1774) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal194)
                    self._state.following.append(self.FOLLOW_binaryOp_in_fExp1776)
                    binaryOp195 = self.binaryOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_binaryOp.add(binaryOp195.tree)
                    self._state.following.append(self.FOLLOW_fExp_in_fExp1778)
                    fExp196 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fExp.add(fExp196.tree)
                    self._state.following.append(self.FOLLOW_fExp2_in_fExp1780)
                    fExp2197 = self.fExp2()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fExp2.add(fExp2197.tree)
                    char_literal198=self.match(self.input, 56, self.FOLLOW_56_in_fExp1782) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal198)

                    # AST Rewrite
                    # elements: fExp, fExp2, binaryOp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 307:32: -> ^( BINARY_OP binaryOp fExp fExp2 )
                        # Pddl.g:307:35: ^( BINARY_OP binaryOp fExp fExp2 )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BINARY_OP, "BINARY_OP"), root_1)

                        self._adaptor.addChild(root_1, stream_binaryOp.nextTree())
                        self._adaptor.addChild(root_1, stream_fExp.nextTree())
                        self._adaptor.addChild(root_1, stream_fExp2.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 3:
                    # Pddl.g:308:4: '(' '-' fExp ')'
                    pass 
                    char_literal199=self.match(self.input, 54, self.FOLLOW_54_in_fExp1799) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal199)
                    char_literal200=self.match(self.input, 60, self.FOLLOW_60_in_fExp1801) 
                    if self._state.backtracking == 0:
                        stream_60.add(char_literal200)
                    self._state.following.append(self.FOLLOW_fExp_in_fExp1803)
                    fExp201 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fExp.add(fExp201.tree)
                    char_literal202=self.match(self.input, 56, self.FOLLOW_56_in_fExp1805) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal202)

                    # AST Rewrite
                    # elements: fExp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 308:21: -> ^( UNARY_MINUS fExp )
                        # Pddl.g:308:24: ^( UNARY_MINUS fExp )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(UNARY_MINUS, "UNARY_MINUS"), root_1)

                        self._adaptor.addChild(root_1, stream_fExp.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 4:
                    # Pddl.g:309:4: fHead
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fHead_in_fExp1818)
                    fHead203 = self.fHead()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fHead203.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fExp"

    class fExp2_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fExp2_return, self).__init__()

            self.tree = None




    # $ANTLR start "fExp2"
    # Pddl.g:314:1: fExp2 : fExp ;
    def fExp2(self, ):

        retval = self.fExp2_return()
        retval.start = self.input.LT(1)

        root_0 = None

        fExp204 = None



        try:
            try:
                # Pddl.g:314:7: ( fExp )
                # Pddl.g:314:9: fExp
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_fExp_in_fExp21830)
                fExp204 = self.fExp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fExp204.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fExp2"

    class fHead_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fHead_return, self).__init__()

            self.tree = None




    # $ANTLR start "fHead"
    # Pddl.g:316:1: fHead : ( '(' functionSymbol ( term )* ')' -> ^( FUNC_HEAD functionSymbol ( term )* ) | functionSymbol -> ^( FUNC_HEAD functionSymbol ) );
    def fHead(self, ):

        retval = self.fHead_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal205 = None
        char_literal208 = None
        functionSymbol206 = None

        term207 = None

        functionSymbol209 = None


        char_literal205_tree = None
        char_literal208_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_term = RewriteRuleSubtreeStream(self._adaptor, "rule term")
        stream_functionSymbol = RewriteRuleSubtreeStream(self._adaptor, "rule functionSymbol")
        try:
            try:
                # Pddl.g:317:2: ( '(' functionSymbol ( term )* ')' -> ^( FUNC_HEAD functionSymbol ( term )* ) | functionSymbol -> ^( FUNC_HEAD functionSymbol ) )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == 54) :
                    alt49 = 1
                elif (LA49_0 == NAME) :
                    alt49 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # Pddl.g:317:4: '(' functionSymbol ( term )* ')'
                    pass 
                    char_literal205=self.match(self.input, 54, self.FOLLOW_54_in_fHead1840) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal205)
                    self._state.following.append(self.FOLLOW_functionSymbol_in_fHead1842)
                    functionSymbol206 = self.functionSymbol()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_functionSymbol.add(functionSymbol206.tree)
                    # Pddl.g:317:23: ( term )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == NAME or LA48_0 == VARIABLE) :
                            alt48 = 1


                        if alt48 == 1:
                            # Pddl.g:0:0: term
                            pass 
                            self._state.following.append(self.FOLLOW_term_in_fHead1844)
                            term207 = self.term()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_term.add(term207.tree)


                        else:
                            break #loop48
                    char_literal208=self.match(self.input, 56, self.FOLLOW_56_in_fHead1847) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal208)

                    # AST Rewrite
                    # elements: functionSymbol, term
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 317:33: -> ^( FUNC_HEAD functionSymbol ( term )* )
                        # Pddl.g:317:36: ^( FUNC_HEAD functionSymbol ( term )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_HEAD, "FUNC_HEAD"), root_1)

                        self._adaptor.addChild(root_1, stream_functionSymbol.nextTree())
                        # Pddl.g:317:63: ( term )*
                        while stream_term.hasNext():
                            self._adaptor.addChild(root_1, stream_term.nextTree())


                        stream_term.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt49 == 2:
                    # Pddl.g:318:4: functionSymbol
                    pass 
                    self._state.following.append(self.FOLLOW_functionSymbol_in_fHead1863)
                    functionSymbol209 = self.functionSymbol()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_functionSymbol.add(functionSymbol209.tree)

                    # AST Rewrite
                    # elements: functionSymbol
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 318:19: -> ^( FUNC_HEAD functionSymbol )
                        # Pddl.g:318:22: ^( FUNC_HEAD functionSymbol )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_HEAD, "FUNC_HEAD"), root_1)

                        self._adaptor.addChild(root_1, stream_functionSymbol.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fHead"

    class effect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.effect_return, self).__init__()

            self.tree = None




    # $ANTLR start "effect"
    # Pddl.g:321:1: effect : ( '(' 'and' ( cEffect )* ')' -> ^( AND_EFFECT ( cEffect )* ) | cEffect );
    def effect(self, ):

        retval = self.effect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal210 = None
        string_literal211 = None
        char_literal213 = None
        cEffect212 = None

        cEffect214 = None


        char_literal210_tree = None
        string_literal211_tree = None
        char_literal213_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_cEffect = RewriteRuleSubtreeStream(self._adaptor, "rule cEffect")
        try:
            try:
                # Pddl.g:322:2: ( '(' 'and' ( cEffect )* ')' -> ^( AND_EFFECT ( cEffect )* ) | cEffect )
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if (LA51_0 == 54) :
                    LA51_1 = self.input.LA(2)

                    if (LA51_1 == 71) :
                        alt51 = 1
                    elif (LA51_1 == NAME or LA51_1 == 73 or LA51_1 == 76 or LA51_1 == 87 or (96 <= LA51_1 <= 100)) :
                        alt51 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 51, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # Pddl.g:322:4: '(' 'and' ( cEffect )* ')'
                    pass 
                    char_literal210=self.match(self.input, 54, self.FOLLOW_54_in_effect1882) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal210)
                    string_literal211=self.match(self.input, 71, self.FOLLOW_71_in_effect1884) 
                    if self._state.backtracking == 0:
                        stream_71.add(string_literal211)
                    # Pddl.g:322:14: ( cEffect )*
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == 54) :
                            alt50 = 1


                        if alt50 == 1:
                            # Pddl.g:0:0: cEffect
                            pass 
                            self._state.following.append(self.FOLLOW_cEffect_in_effect1886)
                            cEffect212 = self.cEffect()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_cEffect.add(cEffect212.tree)


                        else:
                            break #loop50
                    char_literal213=self.match(self.input, 56, self.FOLLOW_56_in_effect1889) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal213)

                    # AST Rewrite
                    # elements: cEffect
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 322:27: -> ^( AND_EFFECT ( cEffect )* )
                        # Pddl.g:322:30: ^( AND_EFFECT ( cEffect )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AND_EFFECT, "AND_EFFECT"), root_1)

                        # Pddl.g:322:43: ( cEffect )*
                        while stream_cEffect.hasNext():
                            self._adaptor.addChild(root_1, stream_cEffect.nextTree())


                        stream_cEffect.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 2:
                    # Pddl.g:323:4: cEffect
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cEffect_in_effect1903)
                    cEffect214 = self.cEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cEffect214.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "effect"

    class cEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.cEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "cEffect"
    # Pddl.g:326:1: cEffect : ( '(' 'forall' '(' typedVariableList ')' effect ')' -> ^( FORALL_EFFECT typedVariableList effect ) | '(' 'when' goalDesc condEffect ')' -> ^( WHEN_EFFECT goalDesc condEffect ) | pEffect );
    def cEffect(self, ):

        retval = self.cEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal215 = None
        string_literal216 = None
        char_literal217 = None
        char_literal219 = None
        char_literal221 = None
        char_literal222 = None
        string_literal223 = None
        char_literal226 = None
        typedVariableList218 = None

        effect220 = None

        goalDesc224 = None

        condEffect225 = None

        pEffect227 = None


        char_literal215_tree = None
        string_literal216_tree = None
        char_literal217_tree = None
        char_literal219_tree = None
        char_literal221_tree = None
        char_literal222_tree = None
        string_literal223_tree = None
        char_literal226_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_87 = RewriteRuleTokenStream(self._adaptor, "token 87")
        stream_76 = RewriteRuleTokenStream(self._adaptor, "token 76")
        stream_effect = RewriteRuleSubtreeStream(self._adaptor, "rule effect")
        stream_condEffect = RewriteRuleSubtreeStream(self._adaptor, "rule condEffect")
        stream_goalDesc = RewriteRuleSubtreeStream(self._adaptor, "rule goalDesc")
        stream_typedVariableList = RewriteRuleSubtreeStream(self._adaptor, "rule typedVariableList")
        try:
            try:
                # Pddl.g:327:2: ( '(' 'forall' '(' typedVariableList ')' effect ')' -> ^( FORALL_EFFECT typedVariableList effect ) | '(' 'when' goalDesc condEffect ')' -> ^( WHEN_EFFECT goalDesc condEffect ) | pEffect )
                alt52 = 3
                LA52_0 = self.input.LA(1)

                if (LA52_0 == 54) :
                    LA52 = self.input.LA(2)
                    if LA52 == 76:
                        alt52 = 1
                    elif LA52 == 87:
                        alt52 = 2
                    elif LA52 == NAME or LA52 == 73 or LA52 == 96 or LA52 == 97 or LA52 == 98 or LA52 == 99 or LA52 == 100:
                        alt52 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 52, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae

                if alt52 == 1:
                    # Pddl.g:327:4: '(' 'forall' '(' typedVariableList ')' effect ')'
                    pass 
                    char_literal215=self.match(self.input, 54, self.FOLLOW_54_in_cEffect1914) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal215)
                    string_literal216=self.match(self.input, 76, self.FOLLOW_76_in_cEffect1916) 
                    if self._state.backtracking == 0:
                        stream_76.add(string_literal216)
                    char_literal217=self.match(self.input, 54, self.FOLLOW_54_in_cEffect1918) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal217)
                    self._state.following.append(self.FOLLOW_typedVariableList_in_cEffect1920)
                    typedVariableList218 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_typedVariableList.add(typedVariableList218.tree)
                    char_literal219=self.match(self.input, 56, self.FOLLOW_56_in_cEffect1922) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal219)
                    self._state.following.append(self.FOLLOW_effect_in_cEffect1924)
                    effect220 = self.effect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_effect.add(effect220.tree)
                    char_literal221=self.match(self.input, 56, self.FOLLOW_56_in_cEffect1926) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal221)

                    # AST Rewrite
                    # elements: effect, typedVariableList
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 328:4: -> ^( FORALL_EFFECT typedVariableList effect )
                        # Pddl.g:328:7: ^( FORALL_EFFECT typedVariableList effect )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FORALL_EFFECT, "FORALL_EFFECT"), root_1)

                        self._adaptor.addChild(root_1, stream_typedVariableList.nextTree())
                        self._adaptor.addChild(root_1, stream_effect.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt52 == 2:
                    # Pddl.g:329:4: '(' 'when' goalDesc condEffect ')'
                    pass 
                    char_literal222=self.match(self.input, 54, self.FOLLOW_54_in_cEffect1944) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal222)
                    string_literal223=self.match(self.input, 87, self.FOLLOW_87_in_cEffect1946) 
                    if self._state.backtracking == 0:
                        stream_87.add(string_literal223)
                    self._state.following.append(self.FOLLOW_goalDesc_in_cEffect1948)
                    goalDesc224 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_goalDesc.add(goalDesc224.tree)
                    self._state.following.append(self.FOLLOW_condEffect_in_cEffect1950)
                    condEffect225 = self.condEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_condEffect.add(condEffect225.tree)
                    char_literal226=self.match(self.input, 56, self.FOLLOW_56_in_cEffect1952) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal226)

                    # AST Rewrite
                    # elements: condEffect, goalDesc
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 330:4: -> ^( WHEN_EFFECT goalDesc condEffect )
                        # Pddl.g:330:7: ^( WHEN_EFFECT goalDesc condEffect )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(WHEN_EFFECT, "WHEN_EFFECT"), root_1)

                        self._adaptor.addChild(root_1, stream_goalDesc.nextTree())
                        self._adaptor.addChild(root_1, stream_condEffect.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt52 == 3:
                    # Pddl.g:331:4: pEffect
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pEffect_in_cEffect1970)
                    pEffect227 = self.pEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pEffect227.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "cEffect"

    class pEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.pEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "pEffect"
    # Pddl.g:334:1: pEffect : ( '(' assignOp fHead fExp ')' -> ^( ASSIGN_EFFECT assignOp fHead fExp ) | '(' 'not' atomicTermFormula ')' -> ^( NOT_EFFECT atomicTermFormula ) | atomicTermFormula );
    def pEffect(self, ):

        retval = self.pEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal228 = None
        char_literal232 = None
        char_literal233 = None
        string_literal234 = None
        char_literal236 = None
        assignOp229 = None

        fHead230 = None

        fExp231 = None

        atomicTermFormula235 = None

        atomicTermFormula237 = None


        char_literal228_tree = None
        char_literal232_tree = None
        char_literal233_tree = None
        string_literal234_tree = None
        char_literal236_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_fHead = RewriteRuleSubtreeStream(self._adaptor, "rule fHead")
        stream_assignOp = RewriteRuleSubtreeStream(self._adaptor, "rule assignOp")
        stream_atomicTermFormula = RewriteRuleSubtreeStream(self._adaptor, "rule atomicTermFormula")
        stream_fExp = RewriteRuleSubtreeStream(self._adaptor, "rule fExp")
        try:
            try:
                # Pddl.g:335:2: ( '(' assignOp fHead fExp ')' -> ^( ASSIGN_EFFECT assignOp fHead fExp ) | '(' 'not' atomicTermFormula ')' -> ^( NOT_EFFECT atomicTermFormula ) | atomicTermFormula )
                alt53 = 3
                LA53_0 = self.input.LA(1)

                if (LA53_0 == 54) :
                    LA53 = self.input.LA(2)
                    if LA53 == 73:
                        alt53 = 2
                    elif LA53 == NAME:
                        alt53 = 3
                    elif LA53 == 96 or LA53 == 97 or LA53 == 98 or LA53 == 99 or LA53 == 100:
                        alt53 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 53, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 53, 0, self.input)

                    raise nvae

                if alt53 == 1:
                    # Pddl.g:335:4: '(' assignOp fHead fExp ')'
                    pass 
                    char_literal228=self.match(self.input, 54, self.FOLLOW_54_in_pEffect1981) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal228)
                    self._state.following.append(self.FOLLOW_assignOp_in_pEffect1983)
                    assignOp229 = self.assignOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_assignOp.add(assignOp229.tree)
                    self._state.following.append(self.FOLLOW_fHead_in_pEffect1985)
                    fHead230 = self.fHead()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fHead.add(fHead230.tree)
                    self._state.following.append(self.FOLLOW_fExp_in_pEffect1987)
                    fExp231 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fExp.add(fExp231.tree)
                    char_literal232=self.match(self.input, 56, self.FOLLOW_56_in_pEffect1989) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal232)

                    # AST Rewrite
                    # elements: fExp, fHead, assignOp
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 336:4: -> ^( ASSIGN_EFFECT assignOp fHead fExp )
                        # Pddl.g:336:7: ^( ASSIGN_EFFECT assignOp fHead fExp )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ASSIGN_EFFECT, "ASSIGN_EFFECT"), root_1)

                        self._adaptor.addChild(root_1, stream_assignOp.nextTree())
                        self._adaptor.addChild(root_1, stream_fHead.nextTree())
                        self._adaptor.addChild(root_1, stream_fExp.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 2:
                    # Pddl.g:337:4: '(' 'not' atomicTermFormula ')'
                    pass 
                    char_literal233=self.match(self.input, 54, self.FOLLOW_54_in_pEffect2009) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal233)
                    string_literal234=self.match(self.input, 73, self.FOLLOW_73_in_pEffect2011) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal234)
                    self._state.following.append(self.FOLLOW_atomicTermFormula_in_pEffect2013)
                    atomicTermFormula235 = self.atomicTermFormula()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atomicTermFormula.add(atomicTermFormula235.tree)
                    char_literal236=self.match(self.input, 56, self.FOLLOW_56_in_pEffect2015) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal236)

                    # AST Rewrite
                    # elements: atomicTermFormula
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 338:4: -> ^( NOT_EFFECT atomicTermFormula )
                        # Pddl.g:338:7: ^( NOT_EFFECT atomicTermFormula )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NOT_EFFECT, "NOT_EFFECT"), root_1)

                        self._adaptor.addChild(root_1, stream_atomicTermFormula.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt53 == 3:
                    # Pddl.g:339:4: atomicTermFormula
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atomicTermFormula_in_pEffect2031)
                    atomicTermFormula237 = self.atomicTermFormula()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atomicTermFormula237.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "pEffect"

    class condEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.condEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "condEffect"
    # Pddl.g:344:1: condEffect : ( '(' 'and' ( pEffect )* ')' -> ^( AND_EFFECT ( pEffect )* ) | pEffect );
    def condEffect(self, ):

        retval = self.condEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal238 = None
        string_literal239 = None
        char_literal241 = None
        pEffect240 = None

        pEffect242 = None


        char_literal238_tree = None
        string_literal239_tree = None
        char_literal241_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_71 = RewriteRuleTokenStream(self._adaptor, "token 71")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_pEffect = RewriteRuleSubtreeStream(self._adaptor, "rule pEffect")
        try:
            try:
                # Pddl.g:345:2: ( '(' 'and' ( pEffect )* ')' -> ^( AND_EFFECT ( pEffect )* ) | pEffect )
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == 54) :
                    LA55_1 = self.input.LA(2)

                    if (LA55_1 == 71) :
                        alt55 = 1
                    elif (LA55_1 == NAME or LA55_1 == 73 or (96 <= LA55_1 <= 100)) :
                        alt55 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 55, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # Pddl.g:345:4: '(' 'and' ( pEffect )* ')'
                    pass 
                    char_literal238=self.match(self.input, 54, self.FOLLOW_54_in_condEffect2044) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal238)
                    string_literal239=self.match(self.input, 71, self.FOLLOW_71_in_condEffect2046) 
                    if self._state.backtracking == 0:
                        stream_71.add(string_literal239)
                    # Pddl.g:345:14: ( pEffect )*
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == 54) :
                            alt54 = 1


                        if alt54 == 1:
                            # Pddl.g:0:0: pEffect
                            pass 
                            self._state.following.append(self.FOLLOW_pEffect_in_condEffect2048)
                            pEffect240 = self.pEffect()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_pEffect.add(pEffect240.tree)


                        else:
                            break #loop54
                    char_literal241=self.match(self.input, 56, self.FOLLOW_56_in_condEffect2051) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal241)

                    # AST Rewrite
                    # elements: pEffect
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 345:27: -> ^( AND_EFFECT ( pEffect )* )
                        # Pddl.g:345:30: ^( AND_EFFECT ( pEffect )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(AND_EFFECT, "AND_EFFECT"), root_1)

                        # Pddl.g:345:43: ( pEffect )*
                        while stream_pEffect.hasNext():
                            self._adaptor.addChild(root_1, stream_pEffect.nextTree())


                        stream_pEffect.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt55 == 2:
                    # Pddl.g:346:4: pEffect
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_pEffect_in_condEffect2065)
                    pEffect242 = self.pEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, pEffect242.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "condEffect"

    class binaryOp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.binaryOp_return, self).__init__()

            self.tree = None




    # $ANTLR start "binaryOp"
    # Pddl.g:350:1: binaryOp : ( '*' | '+' | '-' | '/' );
    def binaryOp(self, ):

        retval = self.binaryOp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set243 = None

        set243_tree = None

        try:
            try:
                # Pddl.g:350:10: ( '*' | '+' | '-' | '/' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set243 = self.input.LT(1)
                if self.input.LA(1) == 60 or (88 <= self.input.LA(1) <= 90):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set243))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "binaryOp"

    class binaryComp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.binaryComp_return, self).__init__()

            self.tree = None




    # $ANTLR start "binaryComp"
    # Pddl.g:352:1: binaryComp : ( '>' | '<' | '=' | '>=' | '<=' );
    def binaryComp(self, ):

        retval = self.binaryComp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set244 = None

        set244_tree = None

        try:
            try:
                # Pddl.g:352:12: ( '>' | '<' | '=' | '>=' | '<=' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set244 = self.input.LT(1)
                if (91 <= self.input.LA(1) <= 95):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set244))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "binaryComp"

    class assignOp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.assignOp_return, self).__init__()

            self.tree = None




    # $ANTLR start "assignOp"
    # Pddl.g:354:1: assignOp : ( 'assign' | 'scale-up' | 'scale-down' | 'increase' | 'decrease' );
    def assignOp(self, ):

        retval = self.assignOp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set245 = None

        set245_tree = None

        try:
            try:
                # Pddl.g:354:10: ( 'assign' | 'scale-up' | 'scale-down' | 'increase' | 'decrease' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set245 = self.input.LT(1)
                if (96 <= self.input.LA(1) <= 100):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set245))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "assignOp"

    class durationConstraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.durationConstraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "durationConstraint"
    # Pddl.g:357:1: durationConstraint : ( '(' 'and' ( simpleDurationConstraint )+ ')' | '(' ')' | simpleDurationConstraint );
    def durationConstraint(self, ):

        retval = self.durationConstraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal246 = None
        string_literal247 = None
        char_literal249 = None
        char_literal250 = None
        char_literal251 = None
        simpleDurationConstraint248 = None

        simpleDurationConstraint252 = None


        char_literal246_tree = None
        string_literal247_tree = None
        char_literal249_tree = None
        char_literal250_tree = None
        char_literal251_tree = None

        try:
            try:
                # Pddl.g:360:2: ( '(' 'and' ( simpleDurationConstraint )+ ')' | '(' ')' | simpleDurationConstraint )
                alt57 = 3
                LA57_0 = self.input.LA(1)

                if (LA57_0 == 54) :
                    LA57 = self.input.LA(2)
                    if LA57 == 71:
                        alt57 = 1
                    elif LA57 == 56:
                        alt57 = 2
                    elif LA57 == 81 or LA57 == 93 or LA57 == 94 or LA57 == 95:
                        alt57 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 57, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # Pddl.g:360:4: '(' 'and' ( simpleDurationConstraint )+ ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal246=self.match(self.input, 54, self.FOLLOW_54_in_durationConstraint2152)
                    if self._state.backtracking == 0:

                        char_literal246_tree = self._adaptor.createWithPayload(char_literal246)
                        self._adaptor.addChild(root_0, char_literal246_tree)

                    string_literal247=self.match(self.input, 71, self.FOLLOW_71_in_durationConstraint2154)
                    if self._state.backtracking == 0:

                        string_literal247_tree = self._adaptor.createWithPayload(string_literal247)
                        self._adaptor.addChild(root_0, string_literal247_tree)

                    # Pddl.g:360:14: ( simpleDurationConstraint )+
                    cnt56 = 0
                    while True: #loop56
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == 54) :
                            alt56 = 1


                        if alt56 == 1:
                            # Pddl.g:0:0: simpleDurationConstraint
                            pass 
                            self._state.following.append(self.FOLLOW_simpleDurationConstraint_in_durationConstraint2156)
                            simpleDurationConstraint248 = self.simpleDurationConstraint()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, simpleDurationConstraint248.tree)


                        else:
                            if cnt56 >= 1:
                                break #loop56

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(56, self.input)
                            raise eee

                        cnt56 += 1
                    char_literal249=self.match(self.input, 56, self.FOLLOW_56_in_durationConstraint2159)
                    if self._state.backtracking == 0:

                        char_literal249_tree = self._adaptor.createWithPayload(char_literal249)
                        self._adaptor.addChild(root_0, char_literal249_tree)



                elif alt57 == 2:
                    # Pddl.g:361:4: '(' ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal250=self.match(self.input, 54, self.FOLLOW_54_in_durationConstraint2164)
                    if self._state.backtracking == 0:

                        char_literal250_tree = self._adaptor.createWithPayload(char_literal250)
                        self._adaptor.addChild(root_0, char_literal250_tree)

                    char_literal251=self.match(self.input, 56, self.FOLLOW_56_in_durationConstraint2166)
                    if self._state.backtracking == 0:

                        char_literal251_tree = self._adaptor.createWithPayload(char_literal251)
                        self._adaptor.addChild(root_0, char_literal251_tree)



                elif alt57 == 3:
                    # Pddl.g:362:4: simpleDurationConstraint
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simpleDurationConstraint_in_durationConstraint2171)
                    simpleDurationConstraint252 = self.simpleDurationConstraint()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleDurationConstraint252.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "durationConstraint"

    class simpleDurationConstraint_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.simpleDurationConstraint_return, self).__init__()

            self.tree = None




    # $ANTLR start "simpleDurationConstraint"
    # Pddl.g:365:1: simpleDurationConstraint : ( '(' durOp '?duration' durValue ')' | '(' 'at' timeSpecifier simpleDurationConstraint ')' );
    def simpleDurationConstraint(self, ):

        retval = self.simpleDurationConstraint_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal253 = None
        string_literal255 = None
        char_literal257 = None
        char_literal258 = None
        string_literal259 = None
        char_literal262 = None
        durOp254 = None

        durValue256 = None

        timeSpecifier260 = None

        simpleDurationConstraint261 = None


        char_literal253_tree = None
        string_literal255_tree = None
        char_literal257_tree = None
        char_literal258_tree = None
        string_literal259_tree = None
        char_literal262_tree = None

        try:
            try:
                # Pddl.g:366:2: ( '(' durOp '?duration' durValue ')' | '(' 'at' timeSpecifier simpleDurationConstraint ')' )
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == 54) :
                    LA58_1 = self.input.LA(2)

                    if (LA58_1 == 81) :
                        alt58 = 2
                    elif ((93 <= LA58_1 <= 95)) :
                        alt58 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 58, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae

                if alt58 == 1:
                    # Pddl.g:366:4: '(' durOp '?duration' durValue ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal253=self.match(self.input, 54, self.FOLLOW_54_in_simpleDurationConstraint2182)
                    if self._state.backtracking == 0:

                        char_literal253_tree = self._adaptor.createWithPayload(char_literal253)
                        self._adaptor.addChild(root_0, char_literal253_tree)

                    self._state.following.append(self.FOLLOW_durOp_in_simpleDurationConstraint2184)
                    durOp254 = self.durOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, durOp254.tree)
                    string_literal255=self.match(self.input, 101, self.FOLLOW_101_in_simpleDurationConstraint2186)
                    if self._state.backtracking == 0:

                        string_literal255_tree = self._adaptor.createWithPayload(string_literal255)
                        self._adaptor.addChild(root_0, string_literal255_tree)

                    self._state.following.append(self.FOLLOW_durValue_in_simpleDurationConstraint2188)
                    durValue256 = self.durValue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, durValue256.tree)
                    char_literal257=self.match(self.input, 56, self.FOLLOW_56_in_simpleDurationConstraint2190)
                    if self._state.backtracking == 0:

                        char_literal257_tree = self._adaptor.createWithPayload(char_literal257)
                        self._adaptor.addChild(root_0, char_literal257_tree)



                elif alt58 == 2:
                    # Pddl.g:367:4: '(' 'at' timeSpecifier simpleDurationConstraint ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal258=self.match(self.input, 54, self.FOLLOW_54_in_simpleDurationConstraint2195)
                    if self._state.backtracking == 0:

                        char_literal258_tree = self._adaptor.createWithPayload(char_literal258)
                        self._adaptor.addChild(root_0, char_literal258_tree)

                    string_literal259=self.match(self.input, 81, self.FOLLOW_81_in_simpleDurationConstraint2197)
                    if self._state.backtracking == 0:

                        string_literal259_tree = self._adaptor.createWithPayload(string_literal259)
                        self._adaptor.addChild(root_0, string_literal259_tree)

                    self._state.following.append(self.FOLLOW_timeSpecifier_in_simpleDurationConstraint2199)
                    timeSpecifier260 = self.timeSpecifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timeSpecifier260.tree)
                    self._state.following.append(self.FOLLOW_simpleDurationConstraint_in_simpleDurationConstraint2201)
                    simpleDurationConstraint261 = self.simpleDurationConstraint()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simpleDurationConstraint261.tree)
                    char_literal262=self.match(self.input, 56, self.FOLLOW_56_in_simpleDurationConstraint2203)
                    if self._state.backtracking == 0:

                        char_literal262_tree = self._adaptor.createWithPayload(char_literal262)
                        self._adaptor.addChild(root_0, char_literal262_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "simpleDurationConstraint"

    class durOp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.durOp_return, self).__init__()

            self.tree = None




    # $ANTLR start "durOp"
    # Pddl.g:370:1: durOp : ( '<=' | '>=' | '=' );
    def durOp(self, ):

        retval = self.durOp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set263 = None

        set263_tree = None

        try:
            try:
                # Pddl.g:370:7: ( '<=' | '>=' | '=' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set263 = self.input.LT(1)
                if (93 <= self.input.LA(1) <= 95):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set263))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "durOp"

    class durValue_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.durValue_return, self).__init__()

            self.tree = None




    # $ANTLR start "durValue"
    # Pddl.g:372:1: durValue : ( NUMBER | fExp );
    def durValue(self, ):

        retval = self.durValue_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NUMBER264 = None
        fExp265 = None


        NUMBER264_tree = None

        try:
            try:
                # Pddl.g:372:10: ( NUMBER | fExp )
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == NUMBER) :
                    LA59_1 = self.input.LA(2)

                    if (self.synpred88_Pddl()) :
                        alt59 = 1
                    elif (True) :
                        alt59 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 59, 1, self.input)

                        raise nvae

                elif (LA59_0 == NAME or LA59_0 == 54) :
                    alt59 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 59, 0, self.input)

                    raise nvae

                if alt59 == 1:
                    # Pddl.g:372:12: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER264=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_durValue2230)
                    if self._state.backtracking == 0:

                        NUMBER264_tree = self._adaptor.createWithPayload(NUMBER264)
                        self._adaptor.addChild(root_0, NUMBER264_tree)



                elif alt59 == 2:
                    # Pddl.g:372:21: fExp
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fExp_in_durValue2234)
                    fExp265 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fExp265.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "durValue"

    class daEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.daEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "daEffect"
    # Pddl.g:374:1: daEffect : ( '(' 'and' ( daEffect )* ')' | timedEffect | '(' 'forall' '(' typedVariableList ')' daEffect ')' | '(' 'when' daGD timedEffect ')' | '(' assignOp fHead fExpDA ')' );
    def daEffect(self, ):

        retval = self.daEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal266 = None
        string_literal267 = None
        char_literal269 = None
        char_literal271 = None
        string_literal272 = None
        char_literal273 = None
        char_literal275 = None
        char_literal277 = None
        char_literal278 = None
        string_literal279 = None
        char_literal282 = None
        char_literal283 = None
        char_literal287 = None
        daEffect268 = None

        timedEffect270 = None

        typedVariableList274 = None

        daEffect276 = None

        daGD280 = None

        timedEffect281 = None

        assignOp284 = None

        fHead285 = None

        fExpDA286 = None


        char_literal266_tree = None
        string_literal267_tree = None
        char_literal269_tree = None
        char_literal271_tree = None
        string_literal272_tree = None
        char_literal273_tree = None
        char_literal275_tree = None
        char_literal277_tree = None
        char_literal278_tree = None
        string_literal279_tree = None
        char_literal282_tree = None
        char_literal283_tree = None
        char_literal287_tree = None

        try:
            try:
                # Pddl.g:375:2: ( '(' 'and' ( daEffect )* ')' | timedEffect | '(' 'forall' '(' typedVariableList ')' daEffect ')' | '(' 'when' daGD timedEffect ')' | '(' assignOp fHead fExpDA ')' )
                alt61 = 5
                LA61_0 = self.input.LA(1)

                if (LA61_0 == 54) :
                    LA61_1 = self.input.LA(2)

                    if (self.synpred90_Pddl()) :
                        alt61 = 1
                    elif (self.synpred91_Pddl()) :
                        alt61 = 2
                    elif (self.synpred92_Pddl()) :
                        alt61 = 3
                    elif (self.synpred93_Pddl()) :
                        alt61 = 4
                    elif (True) :
                        alt61 = 5
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 61, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae

                if alt61 == 1:
                    # Pddl.g:375:4: '(' 'and' ( daEffect )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal266=self.match(self.input, 54, self.FOLLOW_54_in_daEffect2244)
                    if self._state.backtracking == 0:

                        char_literal266_tree = self._adaptor.createWithPayload(char_literal266)
                        self._adaptor.addChild(root_0, char_literal266_tree)

                    string_literal267=self.match(self.input, 71, self.FOLLOW_71_in_daEffect2246)
                    if self._state.backtracking == 0:

                        string_literal267_tree = self._adaptor.createWithPayload(string_literal267)
                        self._adaptor.addChild(root_0, string_literal267_tree)

                    # Pddl.g:375:14: ( daEffect )*
                    while True: #loop60
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if (LA60_0 == 54) :
                            alt60 = 1


                        if alt60 == 1:
                            # Pddl.g:0:0: daEffect
                            pass 
                            self._state.following.append(self.FOLLOW_daEffect_in_daEffect2248)
                            daEffect268 = self.daEffect()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, daEffect268.tree)


                        else:
                            break #loop60
                    char_literal269=self.match(self.input, 56, self.FOLLOW_56_in_daEffect2251)
                    if self._state.backtracking == 0:

                        char_literal269_tree = self._adaptor.createWithPayload(char_literal269)
                        self._adaptor.addChild(root_0, char_literal269_tree)



                elif alt61 == 2:
                    # Pddl.g:376:4: timedEffect
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_timedEffect_in_daEffect2256)
                    timedEffect270 = self.timedEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timedEffect270.tree)


                elif alt61 == 3:
                    # Pddl.g:377:4: '(' 'forall' '(' typedVariableList ')' daEffect ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal271=self.match(self.input, 54, self.FOLLOW_54_in_daEffect2261)
                    if self._state.backtracking == 0:

                        char_literal271_tree = self._adaptor.createWithPayload(char_literal271)
                        self._adaptor.addChild(root_0, char_literal271_tree)

                    string_literal272=self.match(self.input, 76, self.FOLLOW_76_in_daEffect2263)
                    if self._state.backtracking == 0:

                        string_literal272_tree = self._adaptor.createWithPayload(string_literal272)
                        self._adaptor.addChild(root_0, string_literal272_tree)

                    char_literal273=self.match(self.input, 54, self.FOLLOW_54_in_daEffect2265)
                    if self._state.backtracking == 0:

                        char_literal273_tree = self._adaptor.createWithPayload(char_literal273)
                        self._adaptor.addChild(root_0, char_literal273_tree)

                    self._state.following.append(self.FOLLOW_typedVariableList_in_daEffect2267)
                    typedVariableList274 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typedVariableList274.tree)
                    char_literal275=self.match(self.input, 56, self.FOLLOW_56_in_daEffect2269)
                    if self._state.backtracking == 0:

                        char_literal275_tree = self._adaptor.createWithPayload(char_literal275)
                        self._adaptor.addChild(root_0, char_literal275_tree)

                    self._state.following.append(self.FOLLOW_daEffect_in_daEffect2271)
                    daEffect276 = self.daEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, daEffect276.tree)
                    char_literal277=self.match(self.input, 56, self.FOLLOW_56_in_daEffect2273)
                    if self._state.backtracking == 0:

                        char_literal277_tree = self._adaptor.createWithPayload(char_literal277)
                        self._adaptor.addChild(root_0, char_literal277_tree)



                elif alt61 == 4:
                    # Pddl.g:378:4: '(' 'when' daGD timedEffect ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal278=self.match(self.input, 54, self.FOLLOW_54_in_daEffect2278)
                    if self._state.backtracking == 0:

                        char_literal278_tree = self._adaptor.createWithPayload(char_literal278)
                        self._adaptor.addChild(root_0, char_literal278_tree)

                    string_literal279=self.match(self.input, 87, self.FOLLOW_87_in_daEffect2280)
                    if self._state.backtracking == 0:

                        string_literal279_tree = self._adaptor.createWithPayload(string_literal279)
                        self._adaptor.addChild(root_0, string_literal279_tree)

                    self._state.following.append(self.FOLLOW_daGD_in_daEffect2282)
                    daGD280 = self.daGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, daGD280.tree)
                    self._state.following.append(self.FOLLOW_timedEffect_in_daEffect2284)
                    timedEffect281 = self.timedEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timedEffect281.tree)
                    char_literal282=self.match(self.input, 56, self.FOLLOW_56_in_daEffect2286)
                    if self._state.backtracking == 0:

                        char_literal282_tree = self._adaptor.createWithPayload(char_literal282)
                        self._adaptor.addChild(root_0, char_literal282_tree)



                elif alt61 == 5:
                    # Pddl.g:379:4: '(' assignOp fHead fExpDA ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal283=self.match(self.input, 54, self.FOLLOW_54_in_daEffect2291)
                    if self._state.backtracking == 0:

                        char_literal283_tree = self._adaptor.createWithPayload(char_literal283)
                        self._adaptor.addChild(root_0, char_literal283_tree)

                    self._state.following.append(self.FOLLOW_assignOp_in_daEffect2293)
                    assignOp284 = self.assignOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignOp284.tree)
                    self._state.following.append(self.FOLLOW_fHead_in_daEffect2295)
                    fHead285 = self.fHead()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fHead285.tree)
                    self._state.following.append(self.FOLLOW_fExpDA_in_daEffect2297)
                    fExpDA286 = self.fExpDA()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fExpDA286.tree)
                    char_literal287=self.match(self.input, 56, self.FOLLOW_56_in_daEffect2299)
                    if self._state.backtracking == 0:

                        char_literal287_tree = self._adaptor.createWithPayload(char_literal287)
                        self._adaptor.addChild(root_0, char_literal287_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "daEffect"

    class timedEffect_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.timedEffect_return, self).__init__()

            self.tree = None




    # $ANTLR start "timedEffect"
    # Pddl.g:382:1: timedEffect : ( '(' 'at' timeSpecifier daEffect ')' | '(' 'at' timeSpecifier fAssignDA ')' | '(' assignOp fHead fExp ')' );
    def timedEffect(self, ):

        retval = self.timedEffect_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal288 = None
        string_literal289 = None
        char_literal292 = None
        char_literal293 = None
        string_literal294 = None
        char_literal297 = None
        char_literal298 = None
        char_literal302 = None
        timeSpecifier290 = None

        daEffect291 = None

        timeSpecifier295 = None

        fAssignDA296 = None

        assignOp299 = None

        fHead300 = None

        fExp301 = None


        char_literal288_tree = None
        string_literal289_tree = None
        char_literal292_tree = None
        char_literal293_tree = None
        string_literal294_tree = None
        char_literal297_tree = None
        char_literal298_tree = None
        char_literal302_tree = None

        try:
            try:
                # Pddl.g:383:2: ( '(' 'at' timeSpecifier daEffect ')' | '(' 'at' timeSpecifier fAssignDA ')' | '(' assignOp fHead fExp ')' )
                alt62 = 3
                LA62_0 = self.input.LA(1)

                if (LA62_0 == 54) :
                    LA62_1 = self.input.LA(2)

                    if (self.synpred94_Pddl()) :
                        alt62 = 1
                    elif (self.synpred95_Pddl()) :
                        alt62 = 2
                    elif (True) :
                        alt62 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 62, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 62, 0, self.input)

                    raise nvae

                if alt62 == 1:
                    # Pddl.g:383:4: '(' 'at' timeSpecifier daEffect ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal288=self.match(self.input, 54, self.FOLLOW_54_in_timedEffect2310)
                    if self._state.backtracking == 0:

                        char_literal288_tree = self._adaptor.createWithPayload(char_literal288)
                        self._adaptor.addChild(root_0, char_literal288_tree)

                    string_literal289=self.match(self.input, 81, self.FOLLOW_81_in_timedEffect2312)
                    if self._state.backtracking == 0:

                        string_literal289_tree = self._adaptor.createWithPayload(string_literal289)
                        self._adaptor.addChild(root_0, string_literal289_tree)

                    self._state.following.append(self.FOLLOW_timeSpecifier_in_timedEffect2314)
                    timeSpecifier290 = self.timeSpecifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timeSpecifier290.tree)
                    self._state.following.append(self.FOLLOW_daEffect_in_timedEffect2316)
                    daEffect291 = self.daEffect()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, daEffect291.tree)
                    char_literal292=self.match(self.input, 56, self.FOLLOW_56_in_timedEffect2318)
                    if self._state.backtracking == 0:

                        char_literal292_tree = self._adaptor.createWithPayload(char_literal292)
                        self._adaptor.addChild(root_0, char_literal292_tree)



                elif alt62 == 2:
                    # Pddl.g:384:4: '(' 'at' timeSpecifier fAssignDA ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal293=self.match(self.input, 54, self.FOLLOW_54_in_timedEffect2328)
                    if self._state.backtracking == 0:

                        char_literal293_tree = self._adaptor.createWithPayload(char_literal293)
                        self._adaptor.addChild(root_0, char_literal293_tree)

                    string_literal294=self.match(self.input, 81, self.FOLLOW_81_in_timedEffect2330)
                    if self._state.backtracking == 0:

                        string_literal294_tree = self._adaptor.createWithPayload(string_literal294)
                        self._adaptor.addChild(root_0, string_literal294_tree)

                    self._state.following.append(self.FOLLOW_timeSpecifier_in_timedEffect2332)
                    timeSpecifier295 = self.timeSpecifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, timeSpecifier295.tree)
                    self._state.following.append(self.FOLLOW_fAssignDA_in_timedEffect2334)
                    fAssignDA296 = self.fAssignDA()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fAssignDA296.tree)
                    char_literal297=self.match(self.input, 56, self.FOLLOW_56_in_timedEffect2336)
                    if self._state.backtracking == 0:

                        char_literal297_tree = self._adaptor.createWithPayload(char_literal297)
                        self._adaptor.addChild(root_0, char_literal297_tree)



                elif alt62 == 3:
                    # Pddl.g:385:4: '(' assignOp fHead fExp ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal298=self.match(self.input, 54, self.FOLLOW_54_in_timedEffect2341)
                    if self._state.backtracking == 0:

                        char_literal298_tree = self._adaptor.createWithPayload(char_literal298)
                        self._adaptor.addChild(root_0, char_literal298_tree)

                    self._state.following.append(self.FOLLOW_assignOp_in_timedEffect2343)
                    assignOp299 = self.assignOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, assignOp299.tree)
                    self._state.following.append(self.FOLLOW_fHead_in_timedEffect2345)
                    fHead300 = self.fHead()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fHead300.tree)
                    self._state.following.append(self.FOLLOW_fExp_in_timedEffect2347)
                    fExp301 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fExp301.tree)
                    char_literal302=self.match(self.input, 56, self.FOLLOW_56_in_timedEffect2349)
                    if self._state.backtracking == 0:

                        char_literal302_tree = self._adaptor.createWithPayload(char_literal302)
                        self._adaptor.addChild(root_0, char_literal302_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "timedEffect"

    class fAssignDA_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fAssignDA_return, self).__init__()

            self.tree = None




    # $ANTLR start "fAssignDA"
    # Pddl.g:388:1: fAssignDA : '(' assignOp fHead fExpDA ')' ;
    def fAssignDA(self, ):

        retval = self.fAssignDA_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal303 = None
        char_literal307 = None
        assignOp304 = None

        fHead305 = None

        fExpDA306 = None


        char_literal303_tree = None
        char_literal307_tree = None

        try:
            try:
                # Pddl.g:389:2: ( '(' assignOp fHead fExpDA ')' )
                # Pddl.g:389:4: '(' assignOp fHead fExpDA ')'
                pass 
                root_0 = self._adaptor.nil()

                char_literal303=self.match(self.input, 54, self.FOLLOW_54_in_fAssignDA2369)
                if self._state.backtracking == 0:

                    char_literal303_tree = self._adaptor.createWithPayload(char_literal303)
                    self._adaptor.addChild(root_0, char_literal303_tree)

                self._state.following.append(self.FOLLOW_assignOp_in_fAssignDA2371)
                assignOp304 = self.assignOp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, assignOp304.tree)
                self._state.following.append(self.FOLLOW_fHead_in_fAssignDA2373)
                fHead305 = self.fHead()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fHead305.tree)
                self._state.following.append(self.FOLLOW_fExpDA_in_fAssignDA2375)
                fExpDA306 = self.fExpDA()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, fExpDA306.tree)
                char_literal307=self.match(self.input, 56, self.FOLLOW_56_in_fAssignDA2377)
                if self._state.backtracking == 0:

                    char_literal307_tree = self._adaptor.createWithPayload(char_literal307)
                    self._adaptor.addChild(root_0, char_literal307_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fAssignDA"

    class fExpDA_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.fExpDA_return, self).__init__()

            self.tree = None




    # $ANTLR start "fExpDA"
    # Pddl.g:392:1: fExpDA : ( '(' ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) ) ')' | '?duration' | fExp );
    def fExpDA(self, ):

        retval = self.fExpDA_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal308 = None
        char_literal312 = None
        char_literal314 = None
        string_literal315 = None
        binaryOp309 = None

        fExpDA310 = None

        fExpDA311 = None

        fExpDA313 = None

        fExp316 = None


        char_literal308_tree = None
        char_literal312_tree = None
        char_literal314_tree = None
        string_literal315_tree = None

        try:
            try:
                # Pddl.g:393:2: ( '(' ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) ) ')' | '?duration' | fExp )
                alt64 = 3
                LA64 = self.input.LA(1)
                if LA64 == 54:
                    LA64_1 = self.input.LA(2)

                    if (self.synpred97_Pddl()) :
                        alt64 = 1
                    elif (True) :
                        alt64 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 64, 1, self.input)

                        raise nvae

                elif LA64 == 101:
                    alt64 = 2
                elif LA64 == NAME or LA64 == NUMBER:
                    alt64 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 64, 0, self.input)

                    raise nvae

                if alt64 == 1:
                    # Pddl.g:393:4: '(' ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) ) ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal308=self.match(self.input, 54, self.FOLLOW_54_in_fExpDA2388)
                    if self._state.backtracking == 0:

                        char_literal308_tree = self._adaptor.createWithPayload(char_literal308)
                        self._adaptor.addChild(root_0, char_literal308_tree)

                    # Pddl.g:393:8: ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) )
                    alt63 = 2
                    LA63_0 = self.input.LA(1)

                    if (LA63_0 == 60) :
                        LA63_1 = self.input.LA(2)

                        if (self.synpred96_Pddl()) :
                            alt63 = 1
                        elif (True) :
                            alt63 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 63, 1, self.input)

                            raise nvae

                    elif ((88 <= LA63_0 <= 90)) :
                        alt63 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 63, 0, self.input)

                        raise nvae

                    if alt63 == 1:
                        # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
                        pass 
                        # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
                        # Pddl.g:393:10: binaryOp fExpDA fExpDA
                        pass 
                        self._state.following.append(self.FOLLOW_binaryOp_in_fExpDA2392)
                        binaryOp309 = self.binaryOp()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, binaryOp309.tree)
                        self._state.following.append(self.FOLLOW_fExpDA_in_fExpDA2394)
                        fExpDA310 = self.fExpDA()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fExpDA310.tree)
                        self._state.following.append(self.FOLLOW_fExpDA_in_fExpDA2396)
                        fExpDA311 = self.fExpDA()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fExpDA311.tree)





                    elif alt63 == 2:
                        # Pddl.g:393:36: ( '-' fExpDA )
                        pass 
                        # Pddl.g:393:36: ( '-' fExpDA )
                        # Pddl.g:393:37: '-' fExpDA
                        pass 
                        char_literal312=self.match(self.input, 60, self.FOLLOW_60_in_fExpDA2402)
                        if self._state.backtracking == 0:

                            char_literal312_tree = self._adaptor.createWithPayload(char_literal312)
                            self._adaptor.addChild(root_0, char_literal312_tree)

                        self._state.following.append(self.FOLLOW_fExpDA_in_fExpDA2404)
                        fExpDA313 = self.fExpDA()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, fExpDA313.tree)






                    char_literal314=self.match(self.input, 56, self.FOLLOW_56_in_fExpDA2408)
                    if self._state.backtracking == 0:

                        char_literal314_tree = self._adaptor.createWithPayload(char_literal314)
                        self._adaptor.addChild(root_0, char_literal314_tree)



                elif alt64 == 2:
                    # Pddl.g:394:4: '?duration'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal315=self.match(self.input, 101, self.FOLLOW_101_in_fExpDA2413)
                    if self._state.backtracking == 0:

                        string_literal315_tree = self._adaptor.createWithPayload(string_literal315)
                        self._adaptor.addChild(root_0, string_literal315_tree)



                elif alt64 == 3:
                    # Pddl.g:395:4: fExp
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_fExp_in_fExpDA2418)
                    fExp316 = self.fExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fExp316.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "fExpDA"

    class problem_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.problem_return, self).__init__()

            self.tree = None




    # $ANTLR start "problem"
    # Pddl.g:398:1: problem : '(' 'define' problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? ')' -> ^( PROBLEM problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? ) ;
    def problem(self, ):

        retval = self.problem_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal317 = None
        string_literal318 = None
        char_literal327 = None
        problemDecl319 = None

        problemDomain320 = None

        requireDef321 = None

        objectDecl322 = None

        init323 = None

        goal324 = None

        probConstraints325 = None

        metricSpec326 = None


        char_literal317_tree = None
        string_literal318_tree = None
        char_literal327_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_55 = RewriteRuleTokenStream(self._adaptor, "token 55")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_metricSpec = RewriteRuleSubtreeStream(self._adaptor, "rule metricSpec")
        stream_objectDecl = RewriteRuleSubtreeStream(self._adaptor, "rule objectDecl")
        stream_problemDecl = RewriteRuleSubtreeStream(self._adaptor, "rule problemDecl")
        stream_probConstraints = RewriteRuleSubtreeStream(self._adaptor, "rule probConstraints")
        stream_requireDef = RewriteRuleSubtreeStream(self._adaptor, "rule requireDef")
        stream_init = RewriteRuleSubtreeStream(self._adaptor, "rule init")
        stream_problemDomain = RewriteRuleSubtreeStream(self._adaptor, "rule problemDomain")
        stream_goal = RewriteRuleSubtreeStream(self._adaptor, "rule goal")
        try:
            try:
                # Pddl.g:401:2: ( '(' 'define' problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? ')' -> ^( PROBLEM problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? ) )
                # Pddl.g:401:4: '(' 'define' problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? ')'
                pass 
                char_literal317=self.match(self.input, 54, self.FOLLOW_54_in_problem2432) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal317)
                string_literal318=self.match(self.input, 55, self.FOLLOW_55_in_problem2434) 
                if self._state.backtracking == 0:
                    stream_55.add(string_literal318)
                self._state.following.append(self.FOLLOW_problemDecl_in_problem2436)
                problemDecl319 = self.problemDecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_problemDecl.add(problemDecl319.tree)
                self._state.following.append(self.FOLLOW_problemDomain_in_problem2441)
                problemDomain320 = self.problemDomain()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_problemDomain.add(problemDomain320.tree)
                # Pddl.g:403:7: ( requireDef )?
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == 54) :
                    LA65_1 = self.input.LA(2)

                    if (LA65_1 == 58) :
                        alt65 = 1
                if alt65 == 1:
                    # Pddl.g:0:0: requireDef
                    pass 
                    self._state.following.append(self.FOLLOW_requireDef_in_problem2449)
                    requireDef321 = self.requireDef()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_requireDef.add(requireDef321.tree)



                # Pddl.g:404:7: ( objectDecl )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == 54) :
                    LA66_1 = self.input.LA(2)

                    if (LA66_1 == 104) :
                        alt66 = 1
                if alt66 == 1:
                    # Pddl.g:0:0: objectDecl
                    pass 
                    self._state.following.append(self.FOLLOW_objectDecl_in_problem2458)
                    objectDecl322 = self.objectDecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_objectDecl.add(objectDecl322.tree)



                self._state.following.append(self.FOLLOW_init_in_problem2467)
                init323 = self.init()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_init.add(init323.tree)
                self._state.following.append(self.FOLLOW_goal_in_problem2475)
                goal324 = self.goal()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_goal.add(goal324.tree)
                # Pddl.g:407:7: ( probConstraints )?
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == 54) :
                    LA67_1 = self.input.LA(2)

                    if (LA67_1 == 66) :
                        alt67 = 1
                if alt67 == 1:
                    # Pddl.g:0:0: probConstraints
                    pass 
                    self._state.following.append(self.FOLLOW_probConstraints_in_problem2483)
                    probConstraints325 = self.probConstraints()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_probConstraints.add(probConstraints325.tree)



                # Pddl.g:408:7: ( metricSpec )?
                alt68 = 2
                LA68_0 = self.input.LA(1)

                if (LA68_0 == 54) :
                    alt68 = 1
                if alt68 == 1:
                    # Pddl.g:0:0: metricSpec
                    pass 
                    self._state.following.append(self.FOLLOW_metricSpec_in_problem2492)
                    metricSpec326 = self.metricSpec()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_metricSpec.add(metricSpec326.tree)



                char_literal327=self.match(self.input, 56, self.FOLLOW_56_in_problem2508) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal327)

                # AST Rewrite
                # elements: metricSpec, objectDecl, problemDecl, goal, init, requireDef, problemDomain, probConstraints
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 411:7: -> ^( PROBLEM problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? )
                    # Pddl.g:411:10: ^( PROBLEM problemDecl problemDomain ( requireDef )? ( objectDecl )? init goal ( probConstraints )? ( metricSpec )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROBLEM, "PROBLEM"), root_1)

                    self._adaptor.addChild(root_1, stream_problemDecl.nextTree())
                    self._adaptor.addChild(root_1, stream_problemDomain.nextTree())
                    # Pddl.g:411:46: ( requireDef )?
                    if stream_requireDef.hasNext():
                        self._adaptor.addChild(root_1, stream_requireDef.nextTree())


                    stream_requireDef.reset();
                    # Pddl.g:411:58: ( objectDecl )?
                    if stream_objectDecl.hasNext():
                        self._adaptor.addChild(root_1, stream_objectDecl.nextTree())


                    stream_objectDecl.reset();
                    self._adaptor.addChild(root_1, stream_init.nextTree())
                    self._adaptor.addChild(root_1, stream_goal.nextTree())
                    # Pddl.g:412:19: ( probConstraints )?
                    if stream_probConstraints.hasNext():
                        self._adaptor.addChild(root_1, stream_probConstraints.nextTree())


                    stream_probConstraints.reset();
                    # Pddl.g:412:36: ( metricSpec )?
                    if stream_metricSpec.hasNext():
                        self._adaptor.addChild(root_1, stream_metricSpec.nextTree())


                    stream_metricSpec.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "problem"

    class problemDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.problemDecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "problemDecl"
    # Pddl.g:415:1: problemDecl : '(' 'problem' NAME ')' -> ^( PROBLEM_NAME NAME ) ;
    def problemDecl(self, ):

        retval = self.problemDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal328 = None
        string_literal329 = None
        NAME330 = None
        char_literal331 = None

        char_literal328_tree = None
        string_literal329_tree = None
        NAME330_tree = None
        char_literal331_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")

        try:
            try:
                # Pddl.g:416:5: ( '(' 'problem' NAME ')' -> ^( PROBLEM_NAME NAME ) )
                # Pddl.g:416:7: '(' 'problem' NAME ')'
                pass 
                char_literal328=self.match(self.input, 54, self.FOLLOW_54_in_problemDecl2565) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal328)
                string_literal329=self.match(self.input, 102, self.FOLLOW_102_in_problemDecl2567) 
                if self._state.backtracking == 0:
                    stream_102.add(string_literal329)
                NAME330=self.match(self.input, NAME, self.FOLLOW_NAME_in_problemDecl2569) 
                if self._state.backtracking == 0:
                    stream_NAME.add(NAME330)
                char_literal331=self.match(self.input, 56, self.FOLLOW_56_in_problemDecl2571) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal331)

                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 417:5: -> ^( PROBLEM_NAME NAME )
                    # Pddl.g:417:8: ^( PROBLEM_NAME NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROBLEM_NAME, "PROBLEM_NAME"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "problemDecl"

    class problemDomain_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.problemDomain_return, self).__init__()

            self.tree = None




    # $ANTLR start "problemDomain"
    # Pddl.g:420:1: problemDomain : '(' ':domain' NAME ')' -> ^( PROBLEM_DOMAIN NAME ) ;
    def problemDomain(self, ):

        retval = self.problemDomain_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal332 = None
        string_literal333 = None
        NAME334 = None
        char_literal335 = None

        char_literal332_tree = None
        string_literal333_tree = None
        NAME334_tree = None
        char_literal335_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")

        try:
            try:
                # Pddl.g:421:2: ( '(' ':domain' NAME ')' -> ^( PROBLEM_DOMAIN NAME ) )
                # Pddl.g:421:4: '(' ':domain' NAME ')'
                pass 
                char_literal332=self.match(self.input, 54, self.FOLLOW_54_in_problemDomain2597) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal332)
                string_literal333=self.match(self.input, 103, self.FOLLOW_103_in_problemDomain2599) 
                if self._state.backtracking == 0:
                    stream_103.add(string_literal333)
                NAME334=self.match(self.input, NAME, self.FOLLOW_NAME_in_problemDomain2601) 
                if self._state.backtracking == 0:
                    stream_NAME.add(NAME334)
                char_literal335=self.match(self.input, 56, self.FOLLOW_56_in_problemDomain2603) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal335)

                # AST Rewrite
                # elements: NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 422:2: -> ^( PROBLEM_DOMAIN NAME )
                    # Pddl.g:422:5: ^( PROBLEM_DOMAIN NAME )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROBLEM_DOMAIN, "PROBLEM_DOMAIN"), root_1)

                    self._adaptor.addChild(root_1, stream_NAME.nextNode())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "problemDomain"

    class objectDecl_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.objectDecl_return, self).__init__()

            self.tree = None




    # $ANTLR start "objectDecl"
    # Pddl.g:425:1: objectDecl : '(' ':objects' typedNameList ')' -> ^( OBJECTS typedNameList ) ;
    def objectDecl(self, ):

        retval = self.objectDecl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal336 = None
        string_literal337 = None
        char_literal339 = None
        typedNameList338 = None


        char_literal336_tree = None
        string_literal337_tree = None
        char_literal339_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_104 = RewriteRuleTokenStream(self._adaptor, "token 104")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_typedNameList = RewriteRuleSubtreeStream(self._adaptor, "rule typedNameList")
        try:
            try:
                # Pddl.g:426:2: ( '(' ':objects' typedNameList ')' -> ^( OBJECTS typedNameList ) )
                # Pddl.g:426:4: '(' ':objects' typedNameList ')'
                pass 
                char_literal336=self.match(self.input, 54, self.FOLLOW_54_in_objectDecl2623) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal336)
                string_literal337=self.match(self.input, 104, self.FOLLOW_104_in_objectDecl2625) 
                if self._state.backtracking == 0:
                    stream_104.add(string_literal337)
                self._state.following.append(self.FOLLOW_typedNameList_in_objectDecl2627)
                typedNameList338 = self.typedNameList()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_typedNameList.add(typedNameList338.tree)
                char_literal339=self.match(self.input, 56, self.FOLLOW_56_in_objectDecl2629) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal339)

                # AST Rewrite
                # elements: typedNameList
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 427:2: -> ^( OBJECTS typedNameList )
                    # Pddl.g:427:5: ^( OBJECTS typedNameList )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(OBJECTS, "OBJECTS"), root_1)

                    self._adaptor.addChild(root_1, stream_typedNameList.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "objectDecl"

    class init_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.init_return, self).__init__()

            self.tree = None




    # $ANTLR start "init"
    # Pddl.g:430:1: init : '(' ':init' ( initEl )* ')' -> ^( INIT ( initEl )* ) ;
    def init(self, ):

        retval = self.init_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal340 = None
        string_literal341 = None
        char_literal343 = None
        initEl342 = None


        char_literal340_tree = None
        string_literal341_tree = None
        char_literal343_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_105 = RewriteRuleTokenStream(self._adaptor, "token 105")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_initEl = RewriteRuleSubtreeStream(self._adaptor, "rule initEl")
        try:
            try:
                # Pddl.g:431:2: ( '(' ':init' ( initEl )* ')' -> ^( INIT ( initEl )* ) )
                # Pddl.g:431:4: '(' ':init' ( initEl )* ')'
                pass 
                char_literal340=self.match(self.input, 54, self.FOLLOW_54_in_init2649) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal340)
                string_literal341=self.match(self.input, 105, self.FOLLOW_105_in_init2651) 
                if self._state.backtracking == 0:
                    stream_105.add(string_literal341)
                # Pddl.g:431:16: ( initEl )*
                while True: #loop69
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == 54) :
                        alt69 = 1


                    if alt69 == 1:
                        # Pddl.g:0:0: initEl
                        pass 
                        self._state.following.append(self.FOLLOW_initEl_in_init2653)
                        initEl342 = self.initEl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_initEl.add(initEl342.tree)


                    else:
                        break #loop69
                char_literal343=self.match(self.input, 56, self.FOLLOW_56_in_init2656) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal343)

                # AST Rewrite
                # elements: initEl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 432:2: -> ^( INIT ( initEl )* )
                    # Pddl.g:432:5: ^( INIT ( initEl )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT, "INIT"), root_1)

                    # Pddl.g:432:12: ( initEl )*
                    while stream_initEl.hasNext():
                        self._adaptor.addChild(root_1, stream_initEl.nextTree())


                    stream_initEl.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "init"

    class initEl_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.initEl_return, self).__init__()

            self.tree = None




    # $ANTLR start "initEl"
    # Pddl.g:435:1: initEl : ( nameLiteral | '(' '=' fHead NUMBER ')' -> ^( INIT_EQ fHead NUMBER ) | '(' 'at' NUMBER nameLiteral ')' -> ^( INIT_AT NUMBER nameLiteral ) );
    def initEl(self, ):

        retval = self.initEl_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal345 = None
        char_literal346 = None
        NUMBER348 = None
        char_literal349 = None
        char_literal350 = None
        string_literal351 = None
        NUMBER352 = None
        char_literal354 = None
        nameLiteral344 = None

        fHead347 = None

        nameLiteral353 = None


        char_literal345_tree = None
        char_literal346_tree = None
        NUMBER348_tree = None
        char_literal349_tree = None
        char_literal350_tree = None
        string_literal351_tree = None
        NUMBER352_tree = None
        char_literal354_tree = None
        stream_93 = RewriteRuleTokenStream(self._adaptor, "token 93")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_81 = RewriteRuleTokenStream(self._adaptor, "token 81")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")
        stream_fHead = RewriteRuleSubtreeStream(self._adaptor, "rule fHead")
        stream_nameLiteral = RewriteRuleSubtreeStream(self._adaptor, "rule nameLiteral")
        try:
            try:
                # Pddl.g:436:2: ( nameLiteral | '(' '=' fHead NUMBER ')' -> ^( INIT_EQ fHead NUMBER ) | '(' 'at' NUMBER nameLiteral ')' -> ^( INIT_AT NUMBER nameLiteral ) )
                alt70 = 3
                LA70_0 = self.input.LA(1)

                if (LA70_0 == 54) :
                    LA70 = self.input.LA(2)
                    if LA70 == NAME or LA70 == 73:
                        alt70 = 1
                    elif LA70 == 93:
                        alt70 = 2
                    elif LA70 == 81:
                        alt70 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 70, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 70, 0, self.input)

                    raise nvae

                if alt70 == 1:
                    # Pddl.g:436:4: nameLiteral
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nameLiteral_in_initEl2677)
                    nameLiteral344 = self.nameLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nameLiteral344.tree)


                elif alt70 == 2:
                    # Pddl.g:437:4: '(' '=' fHead NUMBER ')'
                    pass 
                    char_literal345=self.match(self.input, 54, self.FOLLOW_54_in_initEl2682) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal345)
                    char_literal346=self.match(self.input, 93, self.FOLLOW_93_in_initEl2684) 
                    if self._state.backtracking == 0:
                        stream_93.add(char_literal346)
                    self._state.following.append(self.FOLLOW_fHead_in_initEl2686)
                    fHead347 = self.fHead()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_fHead.add(fHead347.tree)
                    NUMBER348=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_initEl2688) 
                    if self._state.backtracking == 0:
                        stream_NUMBER.add(NUMBER348)
                    char_literal349=self.match(self.input, 56, self.FOLLOW_56_in_initEl2690) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal349)

                    # AST Rewrite
                    # elements: fHead, NUMBER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 437:37: -> ^( INIT_EQ fHead NUMBER )
                        # Pddl.g:437:40: ^( INIT_EQ fHead NUMBER )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT_EQ, "INIT_EQ"), root_1)

                        self._adaptor.addChild(root_1, stream_fHead.nextTree())
                        self._adaptor.addChild(root_1, stream_NUMBER.nextNode())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt70 == 3:
                    # Pddl.g:438:4: '(' 'at' NUMBER nameLiteral ')'
                    pass 
                    char_literal350=self.match(self.input, 54, self.FOLLOW_54_in_initEl2713) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal350)
                    string_literal351=self.match(self.input, 81, self.FOLLOW_81_in_initEl2715) 
                    if self._state.backtracking == 0:
                        stream_81.add(string_literal351)
                    NUMBER352=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_initEl2717) 
                    if self._state.backtracking == 0:
                        stream_NUMBER.add(NUMBER352)
                    self._state.following.append(self.FOLLOW_nameLiteral_in_initEl2719)
                    nameLiteral353 = self.nameLiteral()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_nameLiteral.add(nameLiteral353.tree)
                    char_literal354=self.match(self.input, 56, self.FOLLOW_56_in_initEl2721) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal354)

                    # AST Rewrite
                    # elements: nameLiteral, NUMBER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 438:37: -> ^( INIT_AT NUMBER nameLiteral )
                        # Pddl.g:438:40: ^( INIT_AT NUMBER nameLiteral )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(INIT_AT, "INIT_AT"), root_1)

                        self._adaptor.addChild(root_1, stream_NUMBER.nextNode())
                        self._adaptor.addChild(root_1, stream_nameLiteral.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "initEl"

    class nameLiteral_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.nameLiteral_return, self).__init__()

            self.tree = None




    # $ANTLR start "nameLiteral"
    # Pddl.g:441:1: nameLiteral : ( atomicNameFormula | '(' 'not' atomicNameFormula ')' -> ^( NOT_PRED_INIT atomicNameFormula ) );
    def nameLiteral(self, ):

        retval = self.nameLiteral_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal356 = None
        string_literal357 = None
        char_literal359 = None
        atomicNameFormula355 = None

        atomicNameFormula358 = None


        char_literal356_tree = None
        string_literal357_tree = None
        char_literal359_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_73 = RewriteRuleTokenStream(self._adaptor, "token 73")
        stream_atomicNameFormula = RewriteRuleSubtreeStream(self._adaptor, "rule atomicNameFormula")
        try:
            try:
                # Pddl.g:442:2: ( atomicNameFormula | '(' 'not' atomicNameFormula ')' -> ^( NOT_PRED_INIT atomicNameFormula ) )
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if (LA71_0 == 54) :
                    LA71_1 = self.input.LA(2)

                    if (LA71_1 == 73) :
                        alt71 = 2
                    elif (LA71_1 == NAME) :
                        alt71 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 71, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 71, 0, self.input)

                    raise nvae

                if alt71 == 1:
                    # Pddl.g:442:4: atomicNameFormula
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_atomicNameFormula_in_nameLiteral2743)
                    atomicNameFormula355 = self.atomicNameFormula()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, atomicNameFormula355.tree)


                elif alt71 == 2:
                    # Pddl.g:443:4: '(' 'not' atomicNameFormula ')'
                    pass 
                    char_literal356=self.match(self.input, 54, self.FOLLOW_54_in_nameLiteral2748) 
                    if self._state.backtracking == 0:
                        stream_54.add(char_literal356)
                    string_literal357=self.match(self.input, 73, self.FOLLOW_73_in_nameLiteral2750) 
                    if self._state.backtracking == 0:
                        stream_73.add(string_literal357)
                    self._state.following.append(self.FOLLOW_atomicNameFormula_in_nameLiteral2752)
                    atomicNameFormula358 = self.atomicNameFormula()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_atomicNameFormula.add(atomicNameFormula358.tree)
                    char_literal359=self.match(self.input, 56, self.FOLLOW_56_in_nameLiteral2754) 
                    if self._state.backtracking == 0:
                        stream_56.add(char_literal359)

                    # AST Rewrite
                    # elements: atomicNameFormula
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 443:36: -> ^( NOT_PRED_INIT atomicNameFormula )
                        # Pddl.g:443:39: ^( NOT_PRED_INIT atomicNameFormula )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NOT_PRED_INIT, "NOT_PRED_INIT"), root_1)

                        self._adaptor.addChild(root_1, stream_atomicNameFormula.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "nameLiteral"

    class atomicNameFormula_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.atomicNameFormula_return, self).__init__()

            self.tree = None




    # $ANTLR start "atomicNameFormula"
    # Pddl.g:446:1: atomicNameFormula : '(' predicate ( NAME )* ')' -> ^( PRED_INST predicate ( NAME )* ) ;
    def atomicNameFormula(self, ):

        retval = self.atomicNameFormula_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal360 = None
        NAME362 = None
        char_literal363 = None
        predicate361 = None


        char_literal360_tree = None
        NAME362_tree = None
        char_literal363_tree = None
        stream_NAME = RewriteRuleTokenStream(self._adaptor, "token NAME")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_predicate = RewriteRuleSubtreeStream(self._adaptor, "rule predicate")
        try:
            try:
                # Pddl.g:447:2: ( '(' predicate ( NAME )* ')' -> ^( PRED_INST predicate ( NAME )* ) )
                # Pddl.g:447:4: '(' predicate ( NAME )* ')'
                pass 
                char_literal360=self.match(self.input, 54, self.FOLLOW_54_in_atomicNameFormula2773) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal360)
                self._state.following.append(self.FOLLOW_predicate_in_atomicNameFormula2775)
                predicate361 = self.predicate()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_predicate.add(predicate361.tree)
                # Pddl.g:447:18: ( NAME )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == NAME) :
                        alt72 = 1


                    if alt72 == 1:
                        # Pddl.g:0:0: NAME
                        pass 
                        NAME362=self.match(self.input, NAME, self.FOLLOW_NAME_in_atomicNameFormula2777) 
                        if self._state.backtracking == 0:
                            stream_NAME.add(NAME362)


                    else:
                        break #loop72
                char_literal363=self.match(self.input, 56, self.FOLLOW_56_in_atomicNameFormula2780) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal363)

                # AST Rewrite
                # elements: predicate, NAME
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 447:28: -> ^( PRED_INST predicate ( NAME )* )
                    # Pddl.g:447:31: ^( PRED_INST predicate ( NAME )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PRED_INST, "PRED_INST"), root_1)

                    self._adaptor.addChild(root_1, stream_predicate.nextTree())
                    # Pddl.g:447:53: ( NAME )*
                    while stream_NAME.hasNext():
                        self._adaptor.addChild(root_1, stream_NAME.nextNode())


                    stream_NAME.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "atomicNameFormula"

    class goal_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.goal_return, self).__init__()

            self.tree = None




    # $ANTLR start "goal"
    # Pddl.g:454:1: goal : '(' ':goal' goalDesc ')' -> ^( GOAL goalDesc ) ;
    def goal(self, ):

        retval = self.goal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal364 = None
        string_literal365 = None
        char_literal367 = None
        goalDesc366 = None


        char_literal364_tree = None
        string_literal365_tree = None
        char_literal367_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_106 = RewriteRuleTokenStream(self._adaptor, "token 106")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_goalDesc = RewriteRuleSubtreeStream(self._adaptor, "rule goalDesc")
        try:
            try:
                # Pddl.g:454:6: ( '(' ':goal' goalDesc ')' -> ^( GOAL goalDesc ) )
                # Pddl.g:454:8: '(' ':goal' goalDesc ')'
                pass 
                char_literal364=self.match(self.input, 54, self.FOLLOW_54_in_goal2805) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal364)
                string_literal365=self.match(self.input, 106, self.FOLLOW_106_in_goal2807) 
                if self._state.backtracking == 0:
                    stream_106.add(string_literal365)
                self._state.following.append(self.FOLLOW_goalDesc_in_goal2809)
                goalDesc366 = self.goalDesc()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_goalDesc.add(goalDesc366.tree)
                char_literal367=self.match(self.input, 56, self.FOLLOW_56_in_goal2811) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal367)

                # AST Rewrite
                # elements: goalDesc
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 454:33: -> ^( GOAL goalDesc )
                    # Pddl.g:454:36: ^( GOAL goalDesc )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(GOAL, "GOAL"), root_1)

                    self._adaptor.addChild(root_1, stream_goalDesc.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "goal"

    class probConstraints_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.probConstraints_return, self).__init__()

            self.tree = None




    # $ANTLR start "probConstraints"
    # Pddl.g:456:1: probConstraints : '(' ':constraints' prefConGD ')' -> ^( PROBLEM_CONSTRAINT prefConGD ) ;
    def probConstraints(self, ):

        retval = self.probConstraints_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal368 = None
        string_literal369 = None
        char_literal371 = None
        prefConGD370 = None


        char_literal368_tree = None
        string_literal369_tree = None
        char_literal371_tree = None
        stream_66 = RewriteRuleTokenStream(self._adaptor, "token 66")
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_prefConGD = RewriteRuleSubtreeStream(self._adaptor, "rule prefConGD")
        try:
            try:
                # Pddl.g:457:2: ( '(' ':constraints' prefConGD ')' -> ^( PROBLEM_CONSTRAINT prefConGD ) )
                # Pddl.g:457:4: '(' ':constraints' prefConGD ')'
                pass 
                char_literal368=self.match(self.input, 54, self.FOLLOW_54_in_probConstraints2829) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal368)
                string_literal369=self.match(self.input, 66, self.FOLLOW_66_in_probConstraints2831) 
                if self._state.backtracking == 0:
                    stream_66.add(string_literal369)
                self._state.following.append(self.FOLLOW_prefConGD_in_probConstraints2834)
                prefConGD370 = self.prefConGD()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_prefConGD.add(prefConGD370.tree)
                char_literal371=self.match(self.input, 56, self.FOLLOW_56_in_probConstraints2836) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal371)

                # AST Rewrite
                # elements: prefConGD
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 458:4: -> ^( PROBLEM_CONSTRAINT prefConGD )
                    # Pddl.g:458:7: ^( PROBLEM_CONSTRAINT prefConGD )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROBLEM_CONSTRAINT, "PROBLEM_CONSTRAINT"), root_1)

                    self._adaptor.addChild(root_1, stream_prefConGD.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "probConstraints"

    class prefConGD_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.prefConGD_return, self).__init__()

            self.tree = None




    # $ANTLR start "prefConGD"
    # Pddl.g:461:1: prefConGD : ( '(' 'and' ( prefConGD )* ')' | '(' 'forall' '(' typedVariableList ')' prefConGD ')' | '(' 'preference' ( NAME )? conGD ')' | conGD );
    def prefConGD(self, ):

        retval = self.prefConGD_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal372 = None
        string_literal373 = None
        char_literal375 = None
        char_literal376 = None
        string_literal377 = None
        char_literal378 = None
        char_literal380 = None
        char_literal382 = None
        char_literal383 = None
        string_literal384 = None
        NAME385 = None
        char_literal387 = None
        prefConGD374 = None

        typedVariableList379 = None

        prefConGD381 = None

        conGD386 = None

        conGD388 = None


        char_literal372_tree = None
        string_literal373_tree = None
        char_literal375_tree = None
        char_literal376_tree = None
        string_literal377_tree = None
        char_literal378_tree = None
        char_literal380_tree = None
        char_literal382_tree = None
        char_literal383_tree = None
        string_literal384_tree = None
        NAME385_tree = None
        char_literal387_tree = None

        try:
            try:
                # Pddl.g:462:2: ( '(' 'and' ( prefConGD )* ')' | '(' 'forall' '(' typedVariableList ')' prefConGD ')' | '(' 'preference' ( NAME )? conGD ')' | conGD )
                alt75 = 4
                LA75_0 = self.input.LA(1)

                if (LA75_0 == 54) :
                    LA75_1 = self.input.LA(2)

                    if (self.synpred109_Pddl()) :
                        alt75 = 1
                    elif (self.synpred110_Pddl()) :
                        alt75 = 2
                    elif (self.synpred112_Pddl()) :
                        alt75 = 3
                    elif (True) :
                        alt75 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 75, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 75, 0, self.input)

                    raise nvae

                if alt75 == 1:
                    # Pddl.g:462:4: '(' 'and' ( prefConGD )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal372=self.match(self.input, 54, self.FOLLOW_54_in_prefConGD2858)
                    if self._state.backtracking == 0:

                        char_literal372_tree = self._adaptor.createWithPayload(char_literal372)
                        self._adaptor.addChild(root_0, char_literal372_tree)

                    string_literal373=self.match(self.input, 71, self.FOLLOW_71_in_prefConGD2860)
                    if self._state.backtracking == 0:

                        string_literal373_tree = self._adaptor.createWithPayload(string_literal373)
                        self._adaptor.addChild(root_0, string_literal373_tree)

                    # Pddl.g:462:14: ( prefConGD )*
                    while True: #loop73
                        alt73 = 2
                        LA73_0 = self.input.LA(1)

                        if (LA73_0 == 54) :
                            alt73 = 1


                        if alt73 == 1:
                            # Pddl.g:0:0: prefConGD
                            pass 
                            self._state.following.append(self.FOLLOW_prefConGD_in_prefConGD2862)
                            prefConGD374 = self.prefConGD()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, prefConGD374.tree)


                        else:
                            break #loop73
                    char_literal375=self.match(self.input, 56, self.FOLLOW_56_in_prefConGD2865)
                    if self._state.backtracking == 0:

                        char_literal375_tree = self._adaptor.createWithPayload(char_literal375)
                        self._adaptor.addChild(root_0, char_literal375_tree)



                elif alt75 == 2:
                    # Pddl.g:463:4: '(' 'forall' '(' typedVariableList ')' prefConGD ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal376=self.match(self.input, 54, self.FOLLOW_54_in_prefConGD2870)
                    if self._state.backtracking == 0:

                        char_literal376_tree = self._adaptor.createWithPayload(char_literal376)
                        self._adaptor.addChild(root_0, char_literal376_tree)

                    string_literal377=self.match(self.input, 76, self.FOLLOW_76_in_prefConGD2872)
                    if self._state.backtracking == 0:

                        string_literal377_tree = self._adaptor.createWithPayload(string_literal377)
                        self._adaptor.addChild(root_0, string_literal377_tree)

                    char_literal378=self.match(self.input, 54, self.FOLLOW_54_in_prefConGD2874)
                    if self._state.backtracking == 0:

                        char_literal378_tree = self._adaptor.createWithPayload(char_literal378)
                        self._adaptor.addChild(root_0, char_literal378_tree)

                    self._state.following.append(self.FOLLOW_typedVariableList_in_prefConGD2876)
                    typedVariableList379 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typedVariableList379.tree)
                    char_literal380=self.match(self.input, 56, self.FOLLOW_56_in_prefConGD2878)
                    if self._state.backtracking == 0:

                        char_literal380_tree = self._adaptor.createWithPayload(char_literal380)
                        self._adaptor.addChild(root_0, char_literal380_tree)

                    self._state.following.append(self.FOLLOW_prefConGD_in_prefConGD2880)
                    prefConGD381 = self.prefConGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, prefConGD381.tree)
                    char_literal382=self.match(self.input, 56, self.FOLLOW_56_in_prefConGD2882)
                    if self._state.backtracking == 0:

                        char_literal382_tree = self._adaptor.createWithPayload(char_literal382)
                        self._adaptor.addChild(root_0, char_literal382_tree)



                elif alt75 == 3:
                    # Pddl.g:464:4: '(' 'preference' ( NAME )? conGD ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal383=self.match(self.input, 54, self.FOLLOW_54_in_prefConGD2887)
                    if self._state.backtracking == 0:

                        char_literal383_tree = self._adaptor.createWithPayload(char_literal383)
                        self._adaptor.addChild(root_0, char_literal383_tree)

                    string_literal384=self.match(self.input, 80, self.FOLLOW_80_in_prefConGD2889)
                    if self._state.backtracking == 0:

                        string_literal384_tree = self._adaptor.createWithPayload(string_literal384)
                        self._adaptor.addChild(root_0, string_literal384_tree)

                    # Pddl.g:464:21: ( NAME )?
                    alt74 = 2
                    LA74_0 = self.input.LA(1)

                    if (LA74_0 == NAME) :
                        alt74 = 1
                    if alt74 == 1:
                        # Pddl.g:0:0: NAME
                        pass 
                        NAME385=self.match(self.input, NAME, self.FOLLOW_NAME_in_prefConGD2891)
                        if self._state.backtracking == 0:

                            NAME385_tree = self._adaptor.createWithPayload(NAME385)
                            self._adaptor.addChild(root_0, NAME385_tree)




                    self._state.following.append(self.FOLLOW_conGD_in_prefConGD2894)
                    conGD386 = self.conGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conGD386.tree)
                    char_literal387=self.match(self.input, 56, self.FOLLOW_56_in_prefConGD2896)
                    if self._state.backtracking == 0:

                        char_literal387_tree = self._adaptor.createWithPayload(char_literal387)
                        self._adaptor.addChild(root_0, char_literal387_tree)



                elif alt75 == 4:
                    # Pddl.g:465:4: conGD
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_conGD_in_prefConGD2901)
                    conGD388 = self.conGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conGD388.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "prefConGD"

    class metricSpec_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.metricSpec_return, self).__init__()

            self.tree = None




    # $ANTLR start "metricSpec"
    # Pddl.g:468:1: metricSpec : '(' ':metric' optimization metricFExp ')' -> ^( PROBLEM_METRIC optimization metricFExp ) ;
    def metricSpec(self, ):

        retval = self.metricSpec_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal389 = None
        string_literal390 = None
        char_literal393 = None
        optimization391 = None

        metricFExp392 = None


        char_literal389_tree = None
        string_literal390_tree = None
        char_literal393_tree = None
        stream_56 = RewriteRuleTokenStream(self._adaptor, "token 56")
        stream_107 = RewriteRuleTokenStream(self._adaptor, "token 107")
        stream_54 = RewriteRuleTokenStream(self._adaptor, "token 54")
        stream_optimization = RewriteRuleSubtreeStream(self._adaptor, "rule optimization")
        stream_metricFExp = RewriteRuleSubtreeStream(self._adaptor, "rule metricFExp")
        try:
            try:
                # Pddl.g:469:2: ( '(' ':metric' optimization metricFExp ')' -> ^( PROBLEM_METRIC optimization metricFExp ) )
                # Pddl.g:469:4: '(' ':metric' optimization metricFExp ')'
                pass 
                char_literal389=self.match(self.input, 54, self.FOLLOW_54_in_metricSpec2912) 
                if self._state.backtracking == 0:
                    stream_54.add(char_literal389)
                string_literal390=self.match(self.input, 107, self.FOLLOW_107_in_metricSpec2914) 
                if self._state.backtracking == 0:
                    stream_107.add(string_literal390)
                self._state.following.append(self.FOLLOW_optimization_in_metricSpec2916)
                optimization391 = self.optimization()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_optimization.add(optimization391.tree)
                self._state.following.append(self.FOLLOW_metricFExp_in_metricSpec2918)
                metricFExp392 = self.metricFExp()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_metricFExp.add(metricFExp392.tree)
                char_literal393=self.match(self.input, 56, self.FOLLOW_56_in_metricSpec2920) 
                if self._state.backtracking == 0:
                    stream_56.add(char_literal393)

                # AST Rewrite
                # elements: optimization, metricFExp
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 470:4: -> ^( PROBLEM_METRIC optimization metricFExp )
                    # Pddl.g:470:7: ^( PROBLEM_METRIC optimization metricFExp )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PROBLEM_METRIC, "PROBLEM_METRIC"), root_1)

                    self._adaptor.addChild(root_1, stream_optimization.nextTree())
                    self._adaptor.addChild(root_1, stream_metricFExp.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "metricSpec"

    class optimization_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.optimization_return, self).__init__()

            self.tree = None




    # $ANTLR start "optimization"
    # Pddl.g:473:1: optimization : ( 'minimize' | 'maximize' );
    def optimization(self, ):

        retval = self.optimization_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set394 = None

        set394_tree = None

        try:
            try:
                # Pddl.g:473:14: ( 'minimize' | 'maximize' )
                # Pddl.g:
                pass 
                root_0 = self._adaptor.nil()

                set394 = self.input.LT(1)
                if (108 <= self.input.LA(1) <= 109):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set394))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "optimization"

    class metricFExp_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.metricFExp_return, self).__init__()

            self.tree = None




    # $ANTLR start "metricFExp"
    # Pddl.g:475:1: metricFExp : ( '(' binaryOp metricFExp metricFExp ')' | '(' ( '*' | '/' ) metricFExp ( metricFExp )+ ')' | '(' '-' metricFExp ')' | NUMBER | '(' functionSymbol ( NAME )* ')' | functionSymbol | 'total-time' | '(' 'is-violated' NAME ')' );
    def metricFExp(self, ):

        retval = self.metricFExp_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal395 = None
        char_literal399 = None
        char_literal400 = None
        set401 = None
        char_literal404 = None
        char_literal405 = None
        char_literal406 = None
        char_literal408 = None
        NUMBER409 = None
        char_literal410 = None
        NAME412 = None
        char_literal413 = None
        string_literal415 = None
        char_literal416 = None
        string_literal417 = None
        NAME418 = None
        char_literal419 = None
        binaryOp396 = None

        metricFExp397 = None

        metricFExp398 = None

        metricFExp402 = None

        metricFExp403 = None

        metricFExp407 = None

        functionSymbol411 = None

        functionSymbol414 = None


        char_literal395_tree = None
        char_literal399_tree = None
        char_literal400_tree = None
        set401_tree = None
        char_literal404_tree = None
        char_literal405_tree = None
        char_literal406_tree = None
        char_literal408_tree = None
        NUMBER409_tree = None
        char_literal410_tree = None
        NAME412_tree = None
        char_literal413_tree = None
        string_literal415_tree = None
        char_literal416_tree = None
        string_literal417_tree = None
        NAME418_tree = None
        char_literal419_tree = None

        try:
            try:
                # Pddl.g:476:2: ( '(' binaryOp metricFExp metricFExp ')' | '(' ( '*' | '/' ) metricFExp ( metricFExp )+ ')' | '(' '-' metricFExp ')' | NUMBER | '(' functionSymbol ( NAME )* ')' | functionSymbol | 'total-time' | '(' 'is-violated' NAME ')' )
                alt78 = 8
                alt78 = self.dfa78.predict(self.input)
                if alt78 == 1:
                    # Pddl.g:476:4: '(' binaryOp metricFExp metricFExp ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal395=self.match(self.input, 54, self.FOLLOW_54_in_metricFExp2957)
                    if self._state.backtracking == 0:

                        char_literal395_tree = self._adaptor.createWithPayload(char_literal395)
                        self._adaptor.addChild(root_0, char_literal395_tree)

                    self._state.following.append(self.FOLLOW_binaryOp_in_metricFExp2959)
                    binaryOp396 = self.binaryOp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, binaryOp396.tree)
                    self._state.following.append(self.FOLLOW_metricFExp_in_metricFExp2961)
                    metricFExp397 = self.metricFExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, metricFExp397.tree)
                    self._state.following.append(self.FOLLOW_metricFExp_in_metricFExp2963)
                    metricFExp398 = self.metricFExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, metricFExp398.tree)
                    char_literal399=self.match(self.input, 56, self.FOLLOW_56_in_metricFExp2965)
                    if self._state.backtracking == 0:

                        char_literal399_tree = self._adaptor.createWithPayload(char_literal399)
                        self._adaptor.addChild(root_0, char_literal399_tree)



                elif alt78 == 2:
                    # Pddl.g:477:4: '(' ( '*' | '/' ) metricFExp ( metricFExp )+ ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal400=self.match(self.input, 54, self.FOLLOW_54_in_metricFExp2970)
                    if self._state.backtracking == 0:

                        char_literal400_tree = self._adaptor.createWithPayload(char_literal400)
                        self._adaptor.addChild(root_0, char_literal400_tree)

                    set401 = self.input.LT(1)
                    if self.input.LA(1) == 88 or self.input.LA(1) == 90:
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set401))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    self._state.following.append(self.FOLLOW_metricFExp_in_metricFExp2978)
                    metricFExp402 = self.metricFExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, metricFExp402.tree)
                    # Pddl.g:477:29: ( metricFExp )+
                    cnt76 = 0
                    while True: #loop76
                        alt76 = 2
                        LA76_0 = self.input.LA(1)

                        if (LA76_0 == NAME or LA76_0 == NUMBER or LA76_0 == 54 or LA76_0 == 110) :
                            alt76 = 1


                        if alt76 == 1:
                            # Pddl.g:0:0: metricFExp
                            pass 
                            self._state.following.append(self.FOLLOW_metricFExp_in_metricFExp2980)
                            metricFExp403 = self.metricFExp()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, metricFExp403.tree)


                        else:
                            if cnt76 >= 1:
                                break #loop76

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(76, self.input)
                            raise eee

                        cnt76 += 1
                    char_literal404=self.match(self.input, 56, self.FOLLOW_56_in_metricFExp2983)
                    if self._state.backtracking == 0:

                        char_literal404_tree = self._adaptor.createWithPayload(char_literal404)
                        self._adaptor.addChild(root_0, char_literal404_tree)



                elif alt78 == 3:
                    # Pddl.g:478:4: '(' '-' metricFExp ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal405=self.match(self.input, 54, self.FOLLOW_54_in_metricFExp2988)
                    if self._state.backtracking == 0:

                        char_literal405_tree = self._adaptor.createWithPayload(char_literal405)
                        self._adaptor.addChild(root_0, char_literal405_tree)

                    char_literal406=self.match(self.input, 60, self.FOLLOW_60_in_metricFExp2990)
                    if self._state.backtracking == 0:

                        char_literal406_tree = self._adaptor.createWithPayload(char_literal406)
                        self._adaptor.addChild(root_0, char_literal406_tree)

                    self._state.following.append(self.FOLLOW_metricFExp_in_metricFExp2992)
                    metricFExp407 = self.metricFExp()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, metricFExp407.tree)
                    char_literal408=self.match(self.input, 56, self.FOLLOW_56_in_metricFExp2994)
                    if self._state.backtracking == 0:

                        char_literal408_tree = self._adaptor.createWithPayload(char_literal408)
                        self._adaptor.addChild(root_0, char_literal408_tree)



                elif alt78 == 4:
                    # Pddl.g:479:4: NUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    NUMBER409=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_metricFExp2999)
                    if self._state.backtracking == 0:

                        NUMBER409_tree = self._adaptor.createWithPayload(NUMBER409)
                        self._adaptor.addChild(root_0, NUMBER409_tree)



                elif alt78 == 5:
                    # Pddl.g:480:4: '(' functionSymbol ( NAME )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal410=self.match(self.input, 54, self.FOLLOW_54_in_metricFExp3004)
                    if self._state.backtracking == 0:

                        char_literal410_tree = self._adaptor.createWithPayload(char_literal410)
                        self._adaptor.addChild(root_0, char_literal410_tree)

                    self._state.following.append(self.FOLLOW_functionSymbol_in_metricFExp3006)
                    functionSymbol411 = self.functionSymbol()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionSymbol411.tree)
                    # Pddl.g:480:23: ( NAME )*
                    while True: #loop77
                        alt77 = 2
                        LA77_0 = self.input.LA(1)

                        if (LA77_0 == NAME) :
                            alt77 = 1


                        if alt77 == 1:
                            # Pddl.g:0:0: NAME
                            pass 
                            NAME412=self.match(self.input, NAME, self.FOLLOW_NAME_in_metricFExp3008)
                            if self._state.backtracking == 0:

                                NAME412_tree = self._adaptor.createWithPayload(NAME412)
                                self._adaptor.addChild(root_0, NAME412_tree)



                        else:
                            break #loop77
                    char_literal413=self.match(self.input, 56, self.FOLLOW_56_in_metricFExp3011)
                    if self._state.backtracking == 0:

                        char_literal413_tree = self._adaptor.createWithPayload(char_literal413)
                        self._adaptor.addChild(root_0, char_literal413_tree)



                elif alt78 == 6:
                    # Pddl.g:481:4: functionSymbol
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_functionSymbol_in_metricFExp3016)
                    functionSymbol414 = self.functionSymbol()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, functionSymbol414.tree)


                elif alt78 == 7:
                    # Pddl.g:482:7: 'total-time'
                    pass 
                    root_0 = self._adaptor.nil()

                    string_literal415=self.match(self.input, 110, self.FOLLOW_110_in_metricFExp3024)
                    if self._state.backtracking == 0:

                        string_literal415_tree = self._adaptor.createWithPayload(string_literal415)
                        self._adaptor.addChild(root_0, string_literal415_tree)



                elif alt78 == 8:
                    # Pddl.g:483:4: '(' 'is-violated' NAME ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal416=self.match(self.input, 54, self.FOLLOW_54_in_metricFExp3029)
                    if self._state.backtracking == 0:

                        char_literal416_tree = self._adaptor.createWithPayload(char_literal416)
                        self._adaptor.addChild(root_0, char_literal416_tree)

                    string_literal417=self.match(self.input, 111, self.FOLLOW_111_in_metricFExp3031)
                    if self._state.backtracking == 0:

                        string_literal417_tree = self._adaptor.createWithPayload(string_literal417)
                        self._adaptor.addChild(root_0, string_literal417_tree)

                    NAME418=self.match(self.input, NAME, self.FOLLOW_NAME_in_metricFExp3033)
                    if self._state.backtracking == 0:

                        NAME418_tree = self._adaptor.createWithPayload(NAME418)
                        self._adaptor.addChild(root_0, NAME418_tree)

                    char_literal419=self.match(self.input, 56, self.FOLLOW_56_in_metricFExp3035)
                    if self._state.backtracking == 0:

                        char_literal419_tree = self._adaptor.createWithPayload(char_literal419)
                        self._adaptor.addChild(root_0, char_literal419_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "metricFExp"

    class conGD_return(ParserRuleReturnScope):
        def __init__(self):
            super(PddlParser.conGD_return, self).__init__()

            self.tree = None




    # $ANTLR start "conGD"
    # Pddl.g:486:1: conGD : ( '(' 'and' ( conGD )* ')' | '(' 'forall' '(' typedVariableList ')' conGD ')' | '(' 'at' 'end' goalDesc ')' | '(' 'always' goalDesc ')' | '(' 'sometime' goalDesc ')' | '(' 'within' NUMBER goalDesc ')' | '(' 'at-most-once' goalDesc ')' | '(' 'sometime-after' goalDesc goalDesc ')' | '(' 'sometime-before' goalDesc goalDesc ')' | '(' 'always-within' NUMBER goalDesc goalDesc ')' | '(' 'hold-during' NUMBER NUMBER goalDesc ')' | '(' 'hold-after' NUMBER goalDesc ')' );
    def conGD(self, ):

        retval = self.conGD_return()
        retval.start = self.input.LT(1)

        root_0 = None

        char_literal420 = None
        string_literal421 = None
        char_literal423 = None
        char_literal424 = None
        string_literal425 = None
        char_literal426 = None
        char_literal428 = None
        char_literal430 = None
        char_literal431 = None
        string_literal432 = None
        string_literal433 = None
        char_literal435 = None
        char_literal436 = None
        string_literal437 = None
        char_literal439 = None
        char_literal440 = None
        string_literal441 = None
        char_literal443 = None
        char_literal444 = None
        string_literal445 = None
        NUMBER446 = None
        char_literal448 = None
        char_literal449 = None
        string_literal450 = None
        char_literal452 = None
        char_literal453 = None
        string_literal454 = None
        char_literal457 = None
        char_literal458 = None
        string_literal459 = None
        char_literal462 = None
        char_literal463 = None
        string_literal464 = None
        NUMBER465 = None
        char_literal468 = None
        char_literal469 = None
        string_literal470 = None
        NUMBER471 = None
        NUMBER472 = None
        char_literal474 = None
        char_literal475 = None
        string_literal476 = None
        NUMBER477 = None
        char_literal479 = None
        conGD422 = None

        typedVariableList427 = None

        conGD429 = None

        goalDesc434 = None

        goalDesc438 = None

        goalDesc442 = None

        goalDesc447 = None

        goalDesc451 = None

        goalDesc455 = None

        goalDesc456 = None

        goalDesc460 = None

        goalDesc461 = None

        goalDesc466 = None

        goalDesc467 = None

        goalDesc473 = None

        goalDesc478 = None


        char_literal420_tree = None
        string_literal421_tree = None
        char_literal423_tree = None
        char_literal424_tree = None
        string_literal425_tree = None
        char_literal426_tree = None
        char_literal428_tree = None
        char_literal430_tree = None
        char_literal431_tree = None
        string_literal432_tree = None
        string_literal433_tree = None
        char_literal435_tree = None
        char_literal436_tree = None
        string_literal437_tree = None
        char_literal439_tree = None
        char_literal440_tree = None
        string_literal441_tree = None
        char_literal443_tree = None
        char_literal444_tree = None
        string_literal445_tree = None
        NUMBER446_tree = None
        char_literal448_tree = None
        char_literal449_tree = None
        string_literal450_tree = None
        char_literal452_tree = None
        char_literal453_tree = None
        string_literal454_tree = None
        char_literal457_tree = None
        char_literal458_tree = None
        string_literal459_tree = None
        char_literal462_tree = None
        char_literal463_tree = None
        string_literal464_tree = None
        NUMBER465_tree = None
        char_literal468_tree = None
        char_literal469_tree = None
        string_literal470_tree = None
        NUMBER471_tree = None
        NUMBER472_tree = None
        char_literal474_tree = None
        char_literal475_tree = None
        string_literal476_tree = None
        NUMBER477_tree = None
        char_literal479_tree = None

        try:
            try:
                # Pddl.g:489:2: ( '(' 'and' ( conGD )* ')' | '(' 'forall' '(' typedVariableList ')' conGD ')' | '(' 'at' 'end' goalDesc ')' | '(' 'always' goalDesc ')' | '(' 'sometime' goalDesc ')' | '(' 'within' NUMBER goalDesc ')' | '(' 'at-most-once' goalDesc ')' | '(' 'sometime-after' goalDesc goalDesc ')' | '(' 'sometime-before' goalDesc goalDesc ')' | '(' 'always-within' NUMBER goalDesc goalDesc ')' | '(' 'hold-during' NUMBER NUMBER goalDesc ')' | '(' 'hold-after' NUMBER goalDesc ')' )
                alt80 = 12
                alt80 = self.dfa80.predict(self.input)
                if alt80 == 1:
                    # Pddl.g:489:4: '(' 'and' ( conGD )* ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal420=self.match(self.input, 54, self.FOLLOW_54_in_conGD3049)
                    if self._state.backtracking == 0:

                        char_literal420_tree = self._adaptor.createWithPayload(char_literal420)
                        self._adaptor.addChild(root_0, char_literal420_tree)

                    string_literal421=self.match(self.input, 71, self.FOLLOW_71_in_conGD3051)
                    if self._state.backtracking == 0:

                        string_literal421_tree = self._adaptor.createWithPayload(string_literal421)
                        self._adaptor.addChild(root_0, string_literal421_tree)

                    # Pddl.g:489:14: ( conGD )*
                    while True: #loop79
                        alt79 = 2
                        LA79_0 = self.input.LA(1)

                        if (LA79_0 == 54) :
                            alt79 = 1


                        if alt79 == 1:
                            # Pddl.g:0:0: conGD
                            pass 
                            self._state.following.append(self.FOLLOW_conGD_in_conGD3053)
                            conGD422 = self.conGD()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, conGD422.tree)


                        else:
                            break #loop79
                    char_literal423=self.match(self.input, 56, self.FOLLOW_56_in_conGD3056)
                    if self._state.backtracking == 0:

                        char_literal423_tree = self._adaptor.createWithPayload(char_literal423)
                        self._adaptor.addChild(root_0, char_literal423_tree)



                elif alt80 == 2:
                    # Pddl.g:490:4: '(' 'forall' '(' typedVariableList ')' conGD ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal424=self.match(self.input, 54, self.FOLLOW_54_in_conGD3061)
                    if self._state.backtracking == 0:

                        char_literal424_tree = self._adaptor.createWithPayload(char_literal424)
                        self._adaptor.addChild(root_0, char_literal424_tree)

                    string_literal425=self.match(self.input, 76, self.FOLLOW_76_in_conGD3063)
                    if self._state.backtracking == 0:

                        string_literal425_tree = self._adaptor.createWithPayload(string_literal425)
                        self._adaptor.addChild(root_0, string_literal425_tree)

                    char_literal426=self.match(self.input, 54, self.FOLLOW_54_in_conGD3065)
                    if self._state.backtracking == 0:

                        char_literal426_tree = self._adaptor.createWithPayload(char_literal426)
                        self._adaptor.addChild(root_0, char_literal426_tree)

                    self._state.following.append(self.FOLLOW_typedVariableList_in_conGD3067)
                    typedVariableList427 = self.typedVariableList()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, typedVariableList427.tree)
                    char_literal428=self.match(self.input, 56, self.FOLLOW_56_in_conGD3069)
                    if self._state.backtracking == 0:

                        char_literal428_tree = self._adaptor.createWithPayload(char_literal428)
                        self._adaptor.addChild(root_0, char_literal428_tree)

                    self._state.following.append(self.FOLLOW_conGD_in_conGD3071)
                    conGD429 = self.conGD()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, conGD429.tree)
                    char_literal430=self.match(self.input, 56, self.FOLLOW_56_in_conGD3073)
                    if self._state.backtracking == 0:

                        char_literal430_tree = self._adaptor.createWithPayload(char_literal430)
                        self._adaptor.addChild(root_0, char_literal430_tree)



                elif alt80 == 3:
                    # Pddl.g:491:4: '(' 'at' 'end' goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal431=self.match(self.input, 54, self.FOLLOW_54_in_conGD3078)
                    if self._state.backtracking == 0:

                        char_literal431_tree = self._adaptor.createWithPayload(char_literal431)
                        self._adaptor.addChild(root_0, char_literal431_tree)

                    string_literal432=self.match(self.input, 81, self.FOLLOW_81_in_conGD3080)
                    if self._state.backtracking == 0:

                        string_literal432_tree = self._adaptor.createWithPayload(string_literal432)
                        self._adaptor.addChild(root_0, string_literal432_tree)

                    string_literal433=self.match(self.input, 84, self.FOLLOW_84_in_conGD3082)
                    if self._state.backtracking == 0:

                        string_literal433_tree = self._adaptor.createWithPayload(string_literal433)
                        self._adaptor.addChild(root_0, string_literal433_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3084)
                    goalDesc434 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc434.tree)
                    char_literal435=self.match(self.input, 56, self.FOLLOW_56_in_conGD3086)
                    if self._state.backtracking == 0:

                        char_literal435_tree = self._adaptor.createWithPayload(char_literal435)
                        self._adaptor.addChild(root_0, char_literal435_tree)



                elif alt80 == 4:
                    # Pddl.g:492:7: '(' 'always' goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal436=self.match(self.input, 54, self.FOLLOW_54_in_conGD3094)
                    if self._state.backtracking == 0:

                        char_literal436_tree = self._adaptor.createWithPayload(char_literal436)
                        self._adaptor.addChild(root_0, char_literal436_tree)

                    string_literal437=self.match(self.input, 112, self.FOLLOW_112_in_conGD3096)
                    if self._state.backtracking == 0:

                        string_literal437_tree = self._adaptor.createWithPayload(string_literal437)
                        self._adaptor.addChild(root_0, string_literal437_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3098)
                    goalDesc438 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc438.tree)
                    char_literal439=self.match(self.input, 56, self.FOLLOW_56_in_conGD3100)
                    if self._state.backtracking == 0:

                        char_literal439_tree = self._adaptor.createWithPayload(char_literal439)
                        self._adaptor.addChild(root_0, char_literal439_tree)



                elif alt80 == 5:
                    # Pddl.g:493:4: '(' 'sometime' goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal440=self.match(self.input, 54, self.FOLLOW_54_in_conGD3105)
                    if self._state.backtracking == 0:

                        char_literal440_tree = self._adaptor.createWithPayload(char_literal440)
                        self._adaptor.addChild(root_0, char_literal440_tree)

                    string_literal441=self.match(self.input, 113, self.FOLLOW_113_in_conGD3107)
                    if self._state.backtracking == 0:

                        string_literal441_tree = self._adaptor.createWithPayload(string_literal441)
                        self._adaptor.addChild(root_0, string_literal441_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3109)
                    goalDesc442 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc442.tree)
                    char_literal443=self.match(self.input, 56, self.FOLLOW_56_in_conGD3111)
                    if self._state.backtracking == 0:

                        char_literal443_tree = self._adaptor.createWithPayload(char_literal443)
                        self._adaptor.addChild(root_0, char_literal443_tree)



                elif alt80 == 6:
                    # Pddl.g:494:5: '(' 'within' NUMBER goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal444=self.match(self.input, 54, self.FOLLOW_54_in_conGD3117)
                    if self._state.backtracking == 0:

                        char_literal444_tree = self._adaptor.createWithPayload(char_literal444)
                        self._adaptor.addChild(root_0, char_literal444_tree)

                    string_literal445=self.match(self.input, 114, self.FOLLOW_114_in_conGD3119)
                    if self._state.backtracking == 0:

                        string_literal445_tree = self._adaptor.createWithPayload(string_literal445)
                        self._adaptor.addChild(root_0, string_literal445_tree)

                    NUMBER446=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_conGD3121)
                    if self._state.backtracking == 0:

                        NUMBER446_tree = self._adaptor.createWithPayload(NUMBER446)
                        self._adaptor.addChild(root_0, NUMBER446_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3123)
                    goalDesc447 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc447.tree)
                    char_literal448=self.match(self.input, 56, self.FOLLOW_56_in_conGD3125)
                    if self._state.backtracking == 0:

                        char_literal448_tree = self._adaptor.createWithPayload(char_literal448)
                        self._adaptor.addChild(root_0, char_literal448_tree)



                elif alt80 == 7:
                    # Pddl.g:495:4: '(' 'at-most-once' goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal449=self.match(self.input, 54, self.FOLLOW_54_in_conGD3130)
                    if self._state.backtracking == 0:

                        char_literal449_tree = self._adaptor.createWithPayload(char_literal449)
                        self._adaptor.addChild(root_0, char_literal449_tree)

                    string_literal450=self.match(self.input, 115, self.FOLLOW_115_in_conGD3132)
                    if self._state.backtracking == 0:

                        string_literal450_tree = self._adaptor.createWithPayload(string_literal450)
                        self._adaptor.addChild(root_0, string_literal450_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3134)
                    goalDesc451 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc451.tree)
                    char_literal452=self.match(self.input, 56, self.FOLLOW_56_in_conGD3136)
                    if self._state.backtracking == 0:

                        char_literal452_tree = self._adaptor.createWithPayload(char_literal452)
                        self._adaptor.addChild(root_0, char_literal452_tree)



                elif alt80 == 8:
                    # Pddl.g:496:4: '(' 'sometime-after' goalDesc goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal453=self.match(self.input, 54, self.FOLLOW_54_in_conGD3141)
                    if self._state.backtracking == 0:

                        char_literal453_tree = self._adaptor.createWithPayload(char_literal453)
                        self._adaptor.addChild(root_0, char_literal453_tree)

                    string_literal454=self.match(self.input, 116, self.FOLLOW_116_in_conGD3143)
                    if self._state.backtracking == 0:

                        string_literal454_tree = self._adaptor.createWithPayload(string_literal454)
                        self._adaptor.addChild(root_0, string_literal454_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3145)
                    goalDesc455 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc455.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3147)
                    goalDesc456 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc456.tree)
                    char_literal457=self.match(self.input, 56, self.FOLLOW_56_in_conGD3149)
                    if self._state.backtracking == 0:

                        char_literal457_tree = self._adaptor.createWithPayload(char_literal457)
                        self._adaptor.addChild(root_0, char_literal457_tree)



                elif alt80 == 9:
                    # Pddl.g:497:4: '(' 'sometime-before' goalDesc goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal458=self.match(self.input, 54, self.FOLLOW_54_in_conGD3154)
                    if self._state.backtracking == 0:

                        char_literal458_tree = self._adaptor.createWithPayload(char_literal458)
                        self._adaptor.addChild(root_0, char_literal458_tree)

                    string_literal459=self.match(self.input, 117, self.FOLLOW_117_in_conGD3156)
                    if self._state.backtracking == 0:

                        string_literal459_tree = self._adaptor.createWithPayload(string_literal459)
                        self._adaptor.addChild(root_0, string_literal459_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3158)
                    goalDesc460 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc460.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3160)
                    goalDesc461 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc461.tree)
                    char_literal462=self.match(self.input, 56, self.FOLLOW_56_in_conGD3162)
                    if self._state.backtracking == 0:

                        char_literal462_tree = self._adaptor.createWithPayload(char_literal462)
                        self._adaptor.addChild(root_0, char_literal462_tree)



                elif alt80 == 10:
                    # Pddl.g:498:4: '(' 'always-within' NUMBER goalDesc goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal463=self.match(self.input, 54, self.FOLLOW_54_in_conGD3167)
                    if self._state.backtracking == 0:

                        char_literal463_tree = self._adaptor.createWithPayload(char_literal463)
                        self._adaptor.addChild(root_0, char_literal463_tree)

                    string_literal464=self.match(self.input, 118, self.FOLLOW_118_in_conGD3169)
                    if self._state.backtracking == 0:

                        string_literal464_tree = self._adaptor.createWithPayload(string_literal464)
                        self._adaptor.addChild(root_0, string_literal464_tree)

                    NUMBER465=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_conGD3171)
                    if self._state.backtracking == 0:

                        NUMBER465_tree = self._adaptor.createWithPayload(NUMBER465)
                        self._adaptor.addChild(root_0, NUMBER465_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3173)
                    goalDesc466 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc466.tree)
                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3175)
                    goalDesc467 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc467.tree)
                    char_literal468=self.match(self.input, 56, self.FOLLOW_56_in_conGD3177)
                    if self._state.backtracking == 0:

                        char_literal468_tree = self._adaptor.createWithPayload(char_literal468)
                        self._adaptor.addChild(root_0, char_literal468_tree)



                elif alt80 == 11:
                    # Pddl.g:499:4: '(' 'hold-during' NUMBER NUMBER goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal469=self.match(self.input, 54, self.FOLLOW_54_in_conGD3182)
                    if self._state.backtracking == 0:

                        char_literal469_tree = self._adaptor.createWithPayload(char_literal469)
                        self._adaptor.addChild(root_0, char_literal469_tree)

                    string_literal470=self.match(self.input, 119, self.FOLLOW_119_in_conGD3184)
                    if self._state.backtracking == 0:

                        string_literal470_tree = self._adaptor.createWithPayload(string_literal470)
                        self._adaptor.addChild(root_0, string_literal470_tree)

                    NUMBER471=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_conGD3186)
                    if self._state.backtracking == 0:

                        NUMBER471_tree = self._adaptor.createWithPayload(NUMBER471)
                        self._adaptor.addChild(root_0, NUMBER471_tree)

                    NUMBER472=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_conGD3188)
                    if self._state.backtracking == 0:

                        NUMBER472_tree = self._adaptor.createWithPayload(NUMBER472)
                        self._adaptor.addChild(root_0, NUMBER472_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3190)
                    goalDesc473 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc473.tree)
                    char_literal474=self.match(self.input, 56, self.FOLLOW_56_in_conGD3192)
                    if self._state.backtracking == 0:

                        char_literal474_tree = self._adaptor.createWithPayload(char_literal474)
                        self._adaptor.addChild(root_0, char_literal474_tree)



                elif alt80 == 12:
                    # Pddl.g:500:4: '(' 'hold-after' NUMBER goalDesc ')'
                    pass 
                    root_0 = self._adaptor.nil()

                    char_literal475=self.match(self.input, 54, self.FOLLOW_54_in_conGD3197)
                    if self._state.backtracking == 0:

                        char_literal475_tree = self._adaptor.createWithPayload(char_literal475)
                        self._adaptor.addChild(root_0, char_literal475_tree)

                    string_literal476=self.match(self.input, 120, self.FOLLOW_120_in_conGD3199)
                    if self._state.backtracking == 0:

                        string_literal476_tree = self._adaptor.createWithPayload(string_literal476)
                        self._adaptor.addChild(root_0, string_literal476_tree)

                    NUMBER477=self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_conGD3201)
                    if self._state.backtracking == 0:

                        NUMBER477_tree = self._adaptor.createWithPayload(NUMBER477)
                        self._adaptor.addChild(root_0, NUMBER477_tree)

                    self._state.following.append(self.FOLLOW_goalDesc_in_conGD3203)
                    goalDesc478 = self.goalDesc()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, goalDesc478.tree)
                    char_literal479=self.match(self.input, 56, self.FOLLOW_56_in_conGD3205)
                    if self._state.backtracking == 0:

                        char_literal479_tree = self._adaptor.createWithPayload(char_literal479)
                        self._adaptor.addChild(root_0, char_literal479_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "conGD"

    # $ANTLR start "synpred20_Pddl"
    def synpred20_Pddl_fragment(self, ):
        # Pddl.g:155:5: ( atomicFunctionSkeleton )
        # Pddl.g:155:5: atomicFunctionSkeleton
        pass 
        self._state.following.append(self.FOLLOW_atomicFunctionSkeleton_in_synpred20_Pddl763)
        self.atomicFunctionSkeleton()

        self._state.following.pop()


    # $ANTLR end "synpred20_Pddl"



    # $ANTLR start "synpred59_Pddl"
    def synpred59_Pddl_fragment(self, ):
        # Pddl.g:307:4: ( '(' binaryOp fExp fExp2 ')' )
        # Pddl.g:307:4: '(' binaryOp fExp fExp2 ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred59_Pddl1774)
        self._state.following.append(self.FOLLOW_binaryOp_in_synpred59_Pddl1776)
        self.binaryOp()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_fExp_in_synpred59_Pddl1778)
        self.fExp()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_fExp2_in_synpred59_Pddl1780)
        self.fExp2()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred59_Pddl1782)


    # $ANTLR end "synpred59_Pddl"



    # $ANTLR start "synpred60_Pddl"
    def synpred60_Pddl_fragment(self, ):
        # Pddl.g:308:4: ( '(' '-' fExp ')' )
        # Pddl.g:308:4: '(' '-' fExp ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred60_Pddl1799)
        self.match(self.input, 60, self.FOLLOW_60_in_synpred60_Pddl1801)
        self._state.following.append(self.FOLLOW_fExp_in_synpred60_Pddl1803)
        self.fExp()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred60_Pddl1805)


    # $ANTLR end "synpred60_Pddl"



    # $ANTLR start "synpred88_Pddl"
    def synpred88_Pddl_fragment(self, ):
        # Pddl.g:372:12: ( NUMBER )
        # Pddl.g:372:12: NUMBER
        pass 
        self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_synpred88_Pddl2230)


    # $ANTLR end "synpred88_Pddl"



    # $ANTLR start "synpred90_Pddl"
    def synpred90_Pddl_fragment(self, ):
        # Pddl.g:375:4: ( '(' 'and' ( daEffect )* ')' )
        # Pddl.g:375:4: '(' 'and' ( daEffect )* ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred90_Pddl2244)
        self.match(self.input, 71, self.FOLLOW_71_in_synpred90_Pddl2246)
        # Pddl.g:375:14: ( daEffect )*
        while True: #loop96
            alt96 = 2
            LA96_0 = self.input.LA(1)

            if (LA96_0 == 54) :
                alt96 = 1


            if alt96 == 1:
                # Pddl.g:0:0: daEffect
                pass 
                self._state.following.append(self.FOLLOW_daEffect_in_synpred90_Pddl2248)
                self.daEffect()

                self._state.following.pop()


            else:
                break #loop96
        self.match(self.input, 56, self.FOLLOW_56_in_synpred90_Pddl2251)


    # $ANTLR end "synpred90_Pddl"



    # $ANTLR start "synpred91_Pddl"
    def synpred91_Pddl_fragment(self, ):
        # Pddl.g:376:4: ( timedEffect )
        # Pddl.g:376:4: timedEffect
        pass 
        self._state.following.append(self.FOLLOW_timedEffect_in_synpred91_Pddl2256)
        self.timedEffect()

        self._state.following.pop()


    # $ANTLR end "synpred91_Pddl"



    # $ANTLR start "synpred92_Pddl"
    def synpred92_Pddl_fragment(self, ):
        # Pddl.g:377:4: ( '(' 'forall' '(' typedVariableList ')' daEffect ')' )
        # Pddl.g:377:4: '(' 'forall' '(' typedVariableList ')' daEffect ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred92_Pddl2261)
        self.match(self.input, 76, self.FOLLOW_76_in_synpred92_Pddl2263)
        self.match(self.input, 54, self.FOLLOW_54_in_synpred92_Pddl2265)
        self._state.following.append(self.FOLLOW_typedVariableList_in_synpred92_Pddl2267)
        self.typedVariableList()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred92_Pddl2269)
        self._state.following.append(self.FOLLOW_daEffect_in_synpred92_Pddl2271)
        self.daEffect()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred92_Pddl2273)


    # $ANTLR end "synpred92_Pddl"



    # $ANTLR start "synpred93_Pddl"
    def synpred93_Pddl_fragment(self, ):
        # Pddl.g:378:4: ( '(' 'when' daGD timedEffect ')' )
        # Pddl.g:378:4: '(' 'when' daGD timedEffect ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred93_Pddl2278)
        self.match(self.input, 87, self.FOLLOW_87_in_synpred93_Pddl2280)
        self._state.following.append(self.FOLLOW_daGD_in_synpred93_Pddl2282)
        self.daGD()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_timedEffect_in_synpred93_Pddl2284)
        self.timedEffect()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred93_Pddl2286)


    # $ANTLR end "synpred93_Pddl"



    # $ANTLR start "synpred94_Pddl"
    def synpred94_Pddl_fragment(self, ):
        # Pddl.g:383:4: ( '(' 'at' timeSpecifier daEffect ')' )
        # Pddl.g:383:4: '(' 'at' timeSpecifier daEffect ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred94_Pddl2310)
        self.match(self.input, 81, self.FOLLOW_81_in_synpred94_Pddl2312)
        self._state.following.append(self.FOLLOW_timeSpecifier_in_synpred94_Pddl2314)
        self.timeSpecifier()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_daEffect_in_synpred94_Pddl2316)
        self.daEffect()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred94_Pddl2318)


    # $ANTLR end "synpred94_Pddl"



    # $ANTLR start "synpred95_Pddl"
    def synpred95_Pddl_fragment(self, ):
        # Pddl.g:384:4: ( '(' 'at' timeSpecifier fAssignDA ')' )
        # Pddl.g:384:4: '(' 'at' timeSpecifier fAssignDA ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred95_Pddl2328)
        self.match(self.input, 81, self.FOLLOW_81_in_synpred95_Pddl2330)
        self._state.following.append(self.FOLLOW_timeSpecifier_in_synpred95_Pddl2332)
        self.timeSpecifier()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_fAssignDA_in_synpred95_Pddl2334)
        self.fAssignDA()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred95_Pddl2336)


    # $ANTLR end "synpred95_Pddl"



    # $ANTLR start "synpred96_Pddl"
    def synpred96_Pddl_fragment(self, ):
        # Pddl.g:393:9: ( ( binaryOp fExpDA fExpDA ) )
        # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
        pass 
        # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
        # Pddl.g:393:10: binaryOp fExpDA fExpDA
        pass 
        self._state.following.append(self.FOLLOW_binaryOp_in_synpred96_Pddl2392)
        self.binaryOp()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_fExpDA_in_synpred96_Pddl2394)
        self.fExpDA()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_fExpDA_in_synpred96_Pddl2396)
        self.fExpDA()

        self._state.following.pop()





    # $ANTLR end "synpred96_Pddl"



    # $ANTLR start "synpred97_Pddl"
    def synpred97_Pddl_fragment(self, ):
        # Pddl.g:393:4: ( '(' ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) ) ')' )
        # Pddl.g:393:4: '(' ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) ) ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred97_Pddl2388)
        # Pddl.g:393:8: ( ( binaryOp fExpDA fExpDA ) | ( '-' fExpDA ) )
        alt97 = 2
        LA97_0 = self.input.LA(1)

        if (LA97_0 == 60) :
            LA97_1 = self.input.LA(2)

            if (self.synpred96_Pddl()) :
                alt97 = 1
            elif (True) :
                alt97 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 97, 1, self.input)

                raise nvae

        elif ((88 <= LA97_0 <= 90)) :
            alt97 = 1
        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException("", 97, 0, self.input)

            raise nvae

        if alt97 == 1:
            # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
            pass 
            # Pddl.g:393:9: ( binaryOp fExpDA fExpDA )
            # Pddl.g:393:10: binaryOp fExpDA fExpDA
            pass 
            self._state.following.append(self.FOLLOW_binaryOp_in_synpred97_Pddl2392)
            self.binaryOp()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_fExpDA_in_synpred97_Pddl2394)
            self.fExpDA()

            self._state.following.pop()
            self._state.following.append(self.FOLLOW_fExpDA_in_synpred97_Pddl2396)
            self.fExpDA()

            self._state.following.pop()





        elif alt97 == 2:
            # Pddl.g:393:36: ( '-' fExpDA )
            pass 
            # Pddl.g:393:36: ( '-' fExpDA )
            # Pddl.g:393:37: '-' fExpDA
            pass 
            self.match(self.input, 60, self.FOLLOW_60_in_synpred97_Pddl2402)
            self._state.following.append(self.FOLLOW_fExpDA_in_synpred97_Pddl2404)
            self.fExpDA()

            self._state.following.pop()






        self.match(self.input, 56, self.FOLLOW_56_in_synpred97_Pddl2408)


    # $ANTLR end "synpred97_Pddl"



    # $ANTLR start "synpred109_Pddl"
    def synpred109_Pddl_fragment(self, ):
        # Pddl.g:462:4: ( '(' 'and' ( prefConGD )* ')' )
        # Pddl.g:462:4: '(' 'and' ( prefConGD )* ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred109_Pddl2858)
        self.match(self.input, 71, self.FOLLOW_71_in_synpred109_Pddl2860)
        # Pddl.g:462:14: ( prefConGD )*
        while True: #loop98
            alt98 = 2
            LA98_0 = self.input.LA(1)

            if (LA98_0 == 54) :
                alt98 = 1


            if alt98 == 1:
                # Pddl.g:0:0: prefConGD
                pass 
                self._state.following.append(self.FOLLOW_prefConGD_in_synpred109_Pddl2862)
                self.prefConGD()

                self._state.following.pop()


            else:
                break #loop98
        self.match(self.input, 56, self.FOLLOW_56_in_synpred109_Pddl2865)


    # $ANTLR end "synpred109_Pddl"



    # $ANTLR start "synpred110_Pddl"
    def synpred110_Pddl_fragment(self, ):
        # Pddl.g:463:4: ( '(' 'forall' '(' typedVariableList ')' prefConGD ')' )
        # Pddl.g:463:4: '(' 'forall' '(' typedVariableList ')' prefConGD ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred110_Pddl2870)
        self.match(self.input, 76, self.FOLLOW_76_in_synpred110_Pddl2872)
        self.match(self.input, 54, self.FOLLOW_54_in_synpred110_Pddl2874)
        self._state.following.append(self.FOLLOW_typedVariableList_in_synpred110_Pddl2876)
        self.typedVariableList()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred110_Pddl2878)
        self._state.following.append(self.FOLLOW_prefConGD_in_synpred110_Pddl2880)
        self.prefConGD()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred110_Pddl2882)


    # $ANTLR end "synpred110_Pddl"



    # $ANTLR start "synpred112_Pddl"
    def synpred112_Pddl_fragment(self, ):
        # Pddl.g:464:4: ( '(' 'preference' ( NAME )? conGD ')' )
        # Pddl.g:464:4: '(' 'preference' ( NAME )? conGD ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred112_Pddl2887)
        self.match(self.input, 80, self.FOLLOW_80_in_synpred112_Pddl2889)
        # Pddl.g:464:21: ( NAME )?
        alt99 = 2
        LA99_0 = self.input.LA(1)

        if (LA99_0 == NAME) :
            alt99 = 1
        if alt99 == 1:
            # Pddl.g:0:0: NAME
            pass 
            self.match(self.input, NAME, self.FOLLOW_NAME_in_synpred112_Pddl2891)



        self._state.following.append(self.FOLLOW_conGD_in_synpred112_Pddl2894)
        self.conGD()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred112_Pddl2896)


    # $ANTLR end "synpred112_Pddl"



    # $ANTLR start "synpred114_Pddl"
    def synpred114_Pddl_fragment(self, ):
        # Pddl.g:476:4: ( '(' binaryOp metricFExp metricFExp ')' )
        # Pddl.g:476:4: '(' binaryOp metricFExp metricFExp ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred114_Pddl2957)
        self._state.following.append(self.FOLLOW_binaryOp_in_synpred114_Pddl2959)
        self.binaryOp()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_metricFExp_in_synpred114_Pddl2961)
        self.metricFExp()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_metricFExp_in_synpred114_Pddl2963)
        self.metricFExp()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred114_Pddl2965)


    # $ANTLR end "synpred114_Pddl"



    # $ANTLR start "synpred117_Pddl"
    def synpred117_Pddl_fragment(self, ):
        # Pddl.g:477:4: ( '(' ( '*' | '/' ) metricFExp ( metricFExp )+ ')' )
        # Pddl.g:477:4: '(' ( '*' | '/' ) metricFExp ( metricFExp )+ ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred117_Pddl2970)
        if self.input.LA(1) == 88 or self.input.LA(1) == 90:
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        self._state.following.append(self.FOLLOW_metricFExp_in_synpred117_Pddl2978)
        self.metricFExp()

        self._state.following.pop()
        # Pddl.g:477:29: ( metricFExp )+
        cnt100 = 0
        while True: #loop100
            alt100 = 2
            LA100_0 = self.input.LA(1)

            if (LA100_0 == NAME or LA100_0 == NUMBER or LA100_0 == 54 or LA100_0 == 110) :
                alt100 = 1


            if alt100 == 1:
                # Pddl.g:0:0: metricFExp
                pass 
                self._state.following.append(self.FOLLOW_metricFExp_in_synpred117_Pddl2980)
                self.metricFExp()

                self._state.following.pop()


            else:
                if cnt100 >= 1:
                    break #loop100

                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                eee = EarlyExitException(100, self.input)
                raise eee

            cnt100 += 1
        self.match(self.input, 56, self.FOLLOW_56_in_synpred117_Pddl2983)


    # $ANTLR end "synpred117_Pddl"



    # $ANTLR start "synpred118_Pddl"
    def synpred118_Pddl_fragment(self, ):
        # Pddl.g:478:4: ( '(' '-' metricFExp ')' )
        # Pddl.g:478:4: '(' '-' metricFExp ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred118_Pddl2988)
        self.match(self.input, 60, self.FOLLOW_60_in_synpred118_Pddl2990)
        self._state.following.append(self.FOLLOW_metricFExp_in_synpred118_Pddl2992)
        self.metricFExp()

        self._state.following.pop()
        self.match(self.input, 56, self.FOLLOW_56_in_synpred118_Pddl2994)


    # $ANTLR end "synpred118_Pddl"



    # $ANTLR start "synpred121_Pddl"
    def synpred121_Pddl_fragment(self, ):
        # Pddl.g:480:4: ( '(' functionSymbol ( NAME )* ')' )
        # Pddl.g:480:4: '(' functionSymbol ( NAME )* ')'
        pass 
        self.match(self.input, 54, self.FOLLOW_54_in_synpred121_Pddl3004)
        self._state.following.append(self.FOLLOW_functionSymbol_in_synpred121_Pddl3006)
        self.functionSymbol()

        self._state.following.pop()
        # Pddl.g:480:23: ( NAME )*
        while True: #loop101
            alt101 = 2
            LA101_0 = self.input.LA(1)

            if (LA101_0 == NAME) :
                alt101 = 1


            if alt101 == 1:
                # Pddl.g:0:0: NAME
                pass 
                self.match(self.input, NAME, self.FOLLOW_NAME_in_synpred121_Pddl3008)


            else:
                break #loop101
        self.match(self.input, 56, self.FOLLOW_56_in_synpred121_Pddl3011)


    # $ANTLR end "synpred121_Pddl"




    # Delegated rules

    def synpred94_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred94_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred88_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred88_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred96_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred96_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred121_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred121_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred114_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred114_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred60_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred60_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred95_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred95_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred118_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred118_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred93_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred93_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred109_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred109_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred117_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred117_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred59_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred59_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred112_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred112_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred20_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred20_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred91_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred91_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred92_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred92_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred110_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred110_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred90_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred90_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred97_Pddl(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred97_Pddl_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\70\1\74\2\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA16_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA16_transition = [
        DFA.unpack(u"\1\1\12\uffff\1\2"),
        DFA.unpack(u"\1\1\12\uffff\1\2\3\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\2\55\2\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\70\1\74\2\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA14_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA14_transition = [
        DFA.unpack(u"\1\1\12\uffff\1\2"),
        DFA.unpack(u"\1\1\12\uffff\1\2\3\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA27_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA27_min = DFA.unpack(
        u"\2\57\2\uffff"
        )

    DFA27_max = DFA.unpack(
        u"\1\70\1\74\2\uffff"
        )

    DFA27_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA27_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA27_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\2\1\uffff\1\2"),
        DFA.unpack(u"\1\1\6\uffff\1\2\1\uffff\1\2\3\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


    # lookup tables for DFA #25

    DFA25_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA25_eof = DFA.unpack(
        u"\4\uffff"
        )

    DFA25_min = DFA.unpack(
        u"\2\57\2\uffff"
        )

    DFA25_max = DFA.unpack(
        u"\1\70\1\74\2\uffff"
        )

    DFA25_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1"
        )

    DFA25_special = DFA.unpack(
        u"\4\uffff"
        )

            
    DFA25_transition = [
        DFA.unpack(u"\1\1\6\uffff\1\2\1\uffff\1\2"),
        DFA.unpack(u"\1\1\6\uffff\1\2\1\uffff\1\2\3\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #25

    class DFA25(DFA):
        pass


    # lookup tables for DFA #37

    DFA37_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA37_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA37_min = DFA.unpack(
        u"\1\66\1\55\10\uffff"
        )

    DFA37_max = DFA.unpack(
        u"\1\66\1\137\10\uffff"
        )

    DFA37_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\1"
        )

    DFA37_special = DFA.unpack(
        u"\12\uffff"
        )

            
    DFA37_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\11\31\uffff\1\2\1\3\1\4\1\5\1\6\1\7\16\uffff\5\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #37

    class DFA37(DFA):
        pass


    # lookup tables for DFA #78

    DFA78_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA78_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA78_min = DFA.unpack(
        u"\1\55\1\0\10\uffff"
        )

    DFA78_max = DFA.unpack(
        u"\1\156\1\0\10\uffff"
        )

    DFA78_accept = DFA.unpack(
        u"\2\uffff\1\4\1\6\1\7\1\1\1\2\1\3\1\5\1\10"
        )

    DFA78_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA78_transition = [
        DFA.unpack(u"\1\3\2\uffff\1\2\5\uffff\1\1\67\uffff\1\4"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #78

    class DFA78(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA78_1 = input.LA(1)

                 
                index78_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred114_Pddl()):
                    s = 5

                elif (self.synpred117_Pddl()):
                    s = 6

                elif (self.synpred118_Pddl()):
                    s = 7

                elif (self.synpred121_Pddl()):
                    s = 8

                elif (True):
                    s = 9

                 
                input.seek(index78_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 78, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #80

    DFA80_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA80_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA80_min = DFA.unpack(
        u"\1\66\1\107\14\uffff"
        )

    DFA80_max = DFA.unpack(
        u"\1\66\1\170\14\uffff"
        )

    DFA80_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14"
        )

    DFA80_special = DFA.unpack(
        u"\16\uffff"
        )

            
    DFA80_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2\4\uffff\1\3\4\uffff\1\4\36\uffff\1\5\1\6\1\7\1"
        u"\10\1\11\1\12\1\13\1\14\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #80

    class DFA80(DFA):
        pass


 

    FOLLOW_domain_in_prog281 = frozenset([1, 54])
    FOLLOW_domain_in_getdomain297 = frozenset([1, 54])
    FOLLOW_problem_in_getproblem311 = frozenset([1, 54])
    FOLLOW_domain_in_pddlDoc356 = frozenset([1])
    FOLLOW_problem_in_pddlDoc360 = frozenset([1])
    FOLLOW_54_in_domain375 = frozenset([55])
    FOLLOW_55_in_domain377 = frozenset([54])
    FOLLOW_domainName_in_domain379 = frozenset([54, 56])
    FOLLOW_requireDef_in_domain387 = frozenset([54, 56])
    FOLLOW_typesDef_in_domain396 = frozenset([54, 56])
    FOLLOW_constantsDef_in_domain405 = frozenset([54, 56])
    FOLLOW_predicatesDef_in_domain414 = frozenset([54, 56])
    FOLLOW_functionsDef_in_domain423 = frozenset([54, 56])
    FOLLOW_constraints_in_domain432 = frozenset([54, 56])
    FOLLOW_structureDef_in_domain441 = frozenset([54, 56])
    FOLLOW_56_in_domain450 = frozenset([1])
    FOLLOW_54_in_domainName534 = frozenset([57])
    FOLLOW_57_in_domainName536 = frozenset([45])
    FOLLOW_NAME_in_domainName538 = frozenset([56])
    FOLLOW_56_in_domainName540 = frozenset([1])
    FOLLOW_54_in_requireDef567 = frozenset([58])
    FOLLOW_58_in_requireDef569 = frozenset([46])
    FOLLOW_REQUIRE_KEY_in_requireDef571 = frozenset([46, 56])
    FOLLOW_56_in_requireDef574 = frozenset([1])
    FOLLOW_54_in_typesDef595 = frozenset([59])
    FOLLOW_59_in_typesDef597 = frozenset([45, 56])
    FOLLOW_typedNameList_in_typesDef599 = frozenset([56])
    FOLLOW_56_in_typesDef601 = frozenset([1])
    FOLLOW_NAME_in_typedNameList628 = frozenset([1, 45])
    FOLLOW_singleTypeNameList_in_typedNameList633 = frozenset([1, 45])
    FOLLOW_NAME_in_typedNameList636 = frozenset([1, 45])
    FOLLOW_NAME_in_singleTypeNameList656 = frozenset([45, 60])
    FOLLOW_60_in_singleTypeNameList659 = frozenset([45, 54])
    FOLLOW_type_in_singleTypeNameList663 = frozenset([1])
    FOLLOW_54_in_type690 = frozenset([61])
    FOLLOW_61_in_type692 = frozenset([45, 54])
    FOLLOW_primType_in_type694 = frozenset([45, 54, 56])
    FOLLOW_56_in_type697 = frozenset([1])
    FOLLOW_primType_in_type716 = frozenset([1])
    FOLLOW_NAME_in_primType726 = frozenset([1])
    FOLLOW_54_in_functionsDef736 = frozenset([62])
    FOLLOW_62_in_functionsDef738 = frozenset([54, 56])
    FOLLOW_functionList_in_functionsDef740 = frozenset([56])
    FOLLOW_56_in_functionsDef742 = frozenset([1])
    FOLLOW_atomicFunctionSkeleton_in_functionList763 = frozenset([1, 54, 60])
    FOLLOW_60_in_functionList767 = frozenset([63])
    FOLLOW_functionType_in_functionList769 = frozenset([1, 54])
    FOLLOW_54_in_atomicFunctionSkeleton785 = frozenset([45])
    FOLLOW_functionSymbol_in_atomicFunctionSkeleton788 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_atomicFunctionSkeleton791 = frozenset([56])
    FOLLOW_56_in_atomicFunctionSkeleton793 = frozenset([1])
    FOLLOW_NAME_in_functionSymbol804 = frozenset([1])
    FOLLOW_63_in_functionType813 = frozenset([1])
    FOLLOW_54_in_constantsDef824 = frozenset([64])
    FOLLOW_64_in_constantsDef826 = frozenset([45, 56])
    FOLLOW_typedNameList_in_constantsDef828 = frozenset([56])
    FOLLOW_56_in_constantsDef830 = frozenset([1])
    FOLLOW_54_in_predicatesDef850 = frozenset([65])
    FOLLOW_65_in_predicatesDef852 = frozenset([54])
    FOLLOW_atomicFormulaSkeleton_in_predicatesDef854 = frozenset([54, 56])
    FOLLOW_56_in_predicatesDef857 = frozenset([1])
    FOLLOW_54_in_atomicFormulaSkeleton878 = frozenset([45])
    FOLLOW_predicate_in_atomicFormulaSkeleton881 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_atomicFormulaSkeleton884 = frozenset([56])
    FOLLOW_56_in_atomicFormulaSkeleton886 = frozenset([1])
    FOLLOW_NAME_in_predicate897 = frozenset([1])
    FOLLOW_VARIABLE_in_typedVariableList912 = frozenset([1, 47])
    FOLLOW_singleTypeVarList_in_typedVariableList917 = frozenset([1, 47])
    FOLLOW_VARIABLE_in_typedVariableList920 = frozenset([1, 47])
    FOLLOW_VARIABLE_in_singleTypeVarList940 = frozenset([47, 60])
    FOLLOW_60_in_singleTypeVarList943 = frozenset([45, 54])
    FOLLOW_type_in_singleTypeVarList947 = frozenset([1])
    FOLLOW_54_in_constraints978 = frozenset([66])
    FOLLOW_66_in_constraints981 = frozenset([54])
    FOLLOW_conGD_in_constraints984 = frozenset([56])
    FOLLOW_56_in_constraints986 = frozenset([1])
    FOLLOW_actionDef_in_structureDef998 = frozenset([1])
    FOLLOW_durativeActionDef_in_structureDef1003 = frozenset([1])
    FOLLOW_derivedDef_in_structureDef1008 = frozenset([1])
    FOLLOW_54_in_actionDef1023 = frozenset([67])
    FOLLOW_67_in_actionDef1025 = frozenset([45])
    FOLLOW_actionSymbol_in_actionDef1027 = frozenset([56, 68, 69, 70])
    FOLLOW_actionDefBody_in_actionDef1040 = frozenset([56])
    FOLLOW_56_in_actionDef1042 = frozenset([1])
    FOLLOW_NAME_in_actionSymbol1072 = frozenset([1])
    FOLLOW_68_in_actionDefBody1088 = frozenset([54])
    FOLLOW_54_in_actionDefBody1090 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_actionDefBody1092 = frozenset([56])
    FOLLOW_56_in_actionDefBody1094 = frozenset([1, 69, 70])
    FOLLOW_69_in_actionDefBody1106 = frozenset([54])
    FOLLOW_54_in_actionDefBody1110 = frozenset([56])
    FOLLOW_56_in_actionDefBody1112 = frozenset([1, 70])
    FOLLOW_goalDesc_in_actionDefBody1117 = frozenset([1, 70])
    FOLLOW_70_in_actionDefBody1127 = frozenset([54])
    FOLLOW_54_in_actionDefBody1131 = frozenset([56])
    FOLLOW_56_in_actionDefBody1133 = frozenset([1])
    FOLLOW_effect_in_actionDefBody1138 = frozenset([1])
    FOLLOW_atomicTermFormula_in_goalDesc1189 = frozenset([1])
    FOLLOW_54_in_goalDesc1194 = frozenset([71])
    FOLLOW_71_in_goalDesc1196 = frozenset([54, 56])
    FOLLOW_goalDesc_in_goalDesc1198 = frozenset([54, 56])
    FOLLOW_56_in_goalDesc1201 = frozenset([1])
    FOLLOW_54_in_goalDesc1226 = frozenset([72])
    FOLLOW_72_in_goalDesc1228 = frozenset([54, 56])
    FOLLOW_goalDesc_in_goalDesc1230 = frozenset([54, 56])
    FOLLOW_56_in_goalDesc1233 = frozenset([1])
    FOLLOW_54_in_goalDesc1258 = frozenset([73])
    FOLLOW_73_in_goalDesc1260 = frozenset([54])
    FOLLOW_goalDesc_in_goalDesc1262 = frozenset([56])
    FOLLOW_56_in_goalDesc1264 = frozenset([1])
    FOLLOW_54_in_goalDesc1288 = frozenset([74])
    FOLLOW_74_in_goalDesc1290 = frozenset([54])
    FOLLOW_goalDesc_in_goalDesc1292 = frozenset([54])
    FOLLOW_goalDesc_in_goalDesc1294 = frozenset([56])
    FOLLOW_56_in_goalDesc1296 = frozenset([1])
    FOLLOW_54_in_goalDesc1322 = frozenset([75])
    FOLLOW_75_in_goalDesc1324 = frozenset([54])
    FOLLOW_54_in_goalDesc1326 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_goalDesc1328 = frozenset([56])
    FOLLOW_56_in_goalDesc1330 = frozenset([54])
    FOLLOW_goalDesc_in_goalDesc1332 = frozenset([56])
    FOLLOW_56_in_goalDesc1334 = frozenset([1])
    FOLLOW_54_in_goalDesc1360 = frozenset([76])
    FOLLOW_76_in_goalDesc1362 = frozenset([54])
    FOLLOW_54_in_goalDesc1364 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_goalDesc1366 = frozenset([56])
    FOLLOW_56_in_goalDesc1368 = frozenset([54])
    FOLLOW_goalDesc_in_goalDesc1370 = frozenset([56])
    FOLLOW_56_in_goalDesc1372 = frozenset([1])
    FOLLOW_fComp_in_goalDesc1401 = frozenset([1])
    FOLLOW_54_in_fComp1437 = frozenset([91, 92, 93, 94, 95])
    FOLLOW_binaryComp_in_fComp1440 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_fComp1442 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_fComp1444 = frozenset([56])
    FOLLOW_56_in_fComp1446 = frozenset([1])
    FOLLOW_54_in_atomicTermFormula1458 = frozenset([45])
    FOLLOW_predicate_in_atomicTermFormula1460 = frozenset([45, 47, 56])
    FOLLOW_term_in_atomicTermFormula1462 = frozenset([45, 47, 56])
    FOLLOW_56_in_atomicTermFormula1465 = frozenset([1])
    FOLLOW_set_in_term0 = frozenset([1])
    FOLLOW_54_in_durativeActionDef1503 = frozenset([77])
    FOLLOW_77_in_durativeActionDef1505 = frozenset([45])
    FOLLOW_actionSymbol_in_durativeActionDef1507 = frozenset([68])
    FOLLOW_68_in_durativeActionDef1516 = frozenset([54])
    FOLLOW_54_in_durativeActionDef1518 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_durativeActionDef1520 = frozenset([56])
    FOLLOW_56_in_durativeActionDef1522 = frozenset([70, 78, 79])
    FOLLOW_daDefBody_in_durativeActionDef1535 = frozenset([56])
    FOLLOW_56_in_durativeActionDef1537 = frozenset([1])
    FOLLOW_78_in_daDefBody1570 = frozenset([54])
    FOLLOW_durationConstraint_in_daDefBody1572 = frozenset([1])
    FOLLOW_79_in_daDefBody1577 = frozenset([54])
    FOLLOW_54_in_daDefBody1581 = frozenset([56])
    FOLLOW_56_in_daDefBody1583 = frozenset([1])
    FOLLOW_daGD_in_daDefBody1588 = frozenset([1])
    FOLLOW_70_in_daDefBody1597 = frozenset([54])
    FOLLOW_54_in_daDefBody1601 = frozenset([56])
    FOLLOW_56_in_daDefBody1603 = frozenset([1])
    FOLLOW_daEffect_in_daDefBody1608 = frozenset([1])
    FOLLOW_prefTimedGD_in_daGD1623 = frozenset([1])
    FOLLOW_54_in_daGD1628 = frozenset([71])
    FOLLOW_71_in_daGD1630 = frozenset([54, 56])
    FOLLOW_daGD_in_daGD1632 = frozenset([54, 56])
    FOLLOW_56_in_daGD1635 = frozenset([1])
    FOLLOW_54_in_daGD1640 = frozenset([76])
    FOLLOW_76_in_daGD1642 = frozenset([54])
    FOLLOW_54_in_daGD1644 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_daGD1646 = frozenset([56])
    FOLLOW_56_in_daGD1648 = frozenset([54])
    FOLLOW_daGD_in_daGD1650 = frozenset([56])
    FOLLOW_56_in_daGD1652 = frozenset([1])
    FOLLOW_timedGD_in_prefTimedGD1663 = frozenset([1])
    FOLLOW_54_in_prefTimedGD1668 = frozenset([80])
    FOLLOW_80_in_prefTimedGD1670 = frozenset([45, 54])
    FOLLOW_NAME_in_prefTimedGD1672 = frozenset([54])
    FOLLOW_timedGD_in_prefTimedGD1675 = frozenset([56])
    FOLLOW_56_in_prefTimedGD1677 = frozenset([1])
    FOLLOW_54_in_timedGD1688 = frozenset([81])
    FOLLOW_81_in_timedGD1690 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_timedGD1692 = frozenset([54])
    FOLLOW_goalDesc_in_timedGD1694 = frozenset([56])
    FOLLOW_56_in_timedGD1696 = frozenset([1])
    FOLLOW_54_in_timedGD1701 = frozenset([82])
    FOLLOW_82_in_timedGD1703 = frozenset([85])
    FOLLOW_interval_in_timedGD1705 = frozenset([54])
    FOLLOW_goalDesc_in_timedGD1707 = frozenset([56])
    FOLLOW_56_in_timedGD1709 = frozenset([1])
    FOLLOW_set_in_timeSpecifier0 = frozenset([1])
    FOLLOW_85_in_interval1731 = frozenset([1])
    FOLLOW_54_in_derivedDef1744 = frozenset([86])
    FOLLOW_86_in_derivedDef1747 = frozenset([47, 54])
    FOLLOW_typedVariableList_in_derivedDef1750 = frozenset([54])
    FOLLOW_goalDesc_in_derivedDef1752 = frozenset([56])
    FOLLOW_56_in_derivedDef1754 = frozenset([1])
    FOLLOW_NUMBER_in_fExp1769 = frozenset([1])
    FOLLOW_54_in_fExp1774 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_fExp1776 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_fExp1778 = frozenset([45, 48, 54])
    FOLLOW_fExp2_in_fExp1780 = frozenset([56])
    FOLLOW_56_in_fExp1782 = frozenset([1])
    FOLLOW_54_in_fExp1799 = frozenset([60])
    FOLLOW_60_in_fExp1801 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_fExp1803 = frozenset([56])
    FOLLOW_56_in_fExp1805 = frozenset([1])
    FOLLOW_fHead_in_fExp1818 = frozenset([1])
    FOLLOW_fExp_in_fExp21830 = frozenset([1])
    FOLLOW_54_in_fHead1840 = frozenset([45])
    FOLLOW_functionSymbol_in_fHead1842 = frozenset([45, 47, 56])
    FOLLOW_term_in_fHead1844 = frozenset([45, 47, 56])
    FOLLOW_56_in_fHead1847 = frozenset([1])
    FOLLOW_functionSymbol_in_fHead1863 = frozenset([1])
    FOLLOW_54_in_effect1882 = frozenset([71])
    FOLLOW_71_in_effect1884 = frozenset([54, 56])
    FOLLOW_cEffect_in_effect1886 = frozenset([54, 56])
    FOLLOW_56_in_effect1889 = frozenset([1])
    FOLLOW_cEffect_in_effect1903 = frozenset([1])
    FOLLOW_54_in_cEffect1914 = frozenset([76])
    FOLLOW_76_in_cEffect1916 = frozenset([54])
    FOLLOW_54_in_cEffect1918 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_cEffect1920 = frozenset([56])
    FOLLOW_56_in_cEffect1922 = frozenset([54])
    FOLLOW_effect_in_cEffect1924 = frozenset([56])
    FOLLOW_56_in_cEffect1926 = frozenset([1])
    FOLLOW_54_in_cEffect1944 = frozenset([87])
    FOLLOW_87_in_cEffect1946 = frozenset([54])
    FOLLOW_goalDesc_in_cEffect1948 = frozenset([54])
    FOLLOW_condEffect_in_cEffect1950 = frozenset([56])
    FOLLOW_56_in_cEffect1952 = frozenset([1])
    FOLLOW_pEffect_in_cEffect1970 = frozenset([1])
    FOLLOW_54_in_pEffect1981 = frozenset([96, 97, 98, 99, 100])
    FOLLOW_assignOp_in_pEffect1983 = frozenset([45, 48, 54])
    FOLLOW_fHead_in_pEffect1985 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_pEffect1987 = frozenset([56])
    FOLLOW_56_in_pEffect1989 = frozenset([1])
    FOLLOW_54_in_pEffect2009 = frozenset([73])
    FOLLOW_73_in_pEffect2011 = frozenset([54])
    FOLLOW_atomicTermFormula_in_pEffect2013 = frozenset([56])
    FOLLOW_56_in_pEffect2015 = frozenset([1])
    FOLLOW_atomicTermFormula_in_pEffect2031 = frozenset([1])
    FOLLOW_54_in_condEffect2044 = frozenset([71])
    FOLLOW_71_in_condEffect2046 = frozenset([54, 56])
    FOLLOW_pEffect_in_condEffect2048 = frozenset([54, 56])
    FOLLOW_56_in_condEffect2051 = frozenset([1])
    FOLLOW_pEffect_in_condEffect2065 = frozenset([1])
    FOLLOW_set_in_binaryOp0 = frozenset([1])
    FOLLOW_set_in_binaryComp0 = frozenset([1])
    FOLLOW_set_in_assignOp0 = frozenset([1])
    FOLLOW_54_in_durationConstraint2152 = frozenset([71])
    FOLLOW_71_in_durationConstraint2154 = frozenset([54])
    FOLLOW_simpleDurationConstraint_in_durationConstraint2156 = frozenset([54, 56])
    FOLLOW_56_in_durationConstraint2159 = frozenset([1])
    FOLLOW_54_in_durationConstraint2164 = frozenset([56])
    FOLLOW_56_in_durationConstraint2166 = frozenset([1])
    FOLLOW_simpleDurationConstraint_in_durationConstraint2171 = frozenset([1])
    FOLLOW_54_in_simpleDurationConstraint2182 = frozenset([93, 94, 95])
    FOLLOW_durOp_in_simpleDurationConstraint2184 = frozenset([101])
    FOLLOW_101_in_simpleDurationConstraint2186 = frozenset([45, 48, 54])
    FOLLOW_durValue_in_simpleDurationConstraint2188 = frozenset([56])
    FOLLOW_56_in_simpleDurationConstraint2190 = frozenset([1])
    FOLLOW_54_in_simpleDurationConstraint2195 = frozenset([81])
    FOLLOW_81_in_simpleDurationConstraint2197 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_simpleDurationConstraint2199 = frozenset([54])
    FOLLOW_simpleDurationConstraint_in_simpleDurationConstraint2201 = frozenset([56])
    FOLLOW_56_in_simpleDurationConstraint2203 = frozenset([1])
    FOLLOW_set_in_durOp0 = frozenset([1])
    FOLLOW_NUMBER_in_durValue2230 = frozenset([1])
    FOLLOW_fExp_in_durValue2234 = frozenset([1])
    FOLLOW_54_in_daEffect2244 = frozenset([71])
    FOLLOW_71_in_daEffect2246 = frozenset([54, 56])
    FOLLOW_daEffect_in_daEffect2248 = frozenset([54, 56])
    FOLLOW_56_in_daEffect2251 = frozenset([1])
    FOLLOW_timedEffect_in_daEffect2256 = frozenset([1])
    FOLLOW_54_in_daEffect2261 = frozenset([76])
    FOLLOW_76_in_daEffect2263 = frozenset([54])
    FOLLOW_54_in_daEffect2265 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_daEffect2267 = frozenset([56])
    FOLLOW_56_in_daEffect2269 = frozenset([54])
    FOLLOW_daEffect_in_daEffect2271 = frozenset([56])
    FOLLOW_56_in_daEffect2273 = frozenset([1])
    FOLLOW_54_in_daEffect2278 = frozenset([87])
    FOLLOW_87_in_daEffect2280 = frozenset([54])
    FOLLOW_daGD_in_daEffect2282 = frozenset([54])
    FOLLOW_timedEffect_in_daEffect2284 = frozenset([56])
    FOLLOW_56_in_daEffect2286 = frozenset([1])
    FOLLOW_54_in_daEffect2291 = frozenset([96, 97, 98, 99, 100])
    FOLLOW_assignOp_in_daEffect2293 = frozenset([45, 48, 54])
    FOLLOW_fHead_in_daEffect2295 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_daEffect2297 = frozenset([56])
    FOLLOW_56_in_daEffect2299 = frozenset([1])
    FOLLOW_54_in_timedEffect2310 = frozenset([81])
    FOLLOW_81_in_timedEffect2312 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_timedEffect2314 = frozenset([54])
    FOLLOW_daEffect_in_timedEffect2316 = frozenset([56])
    FOLLOW_56_in_timedEffect2318 = frozenset([1])
    FOLLOW_54_in_timedEffect2328 = frozenset([81])
    FOLLOW_81_in_timedEffect2330 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_timedEffect2332 = frozenset([54])
    FOLLOW_fAssignDA_in_timedEffect2334 = frozenset([56])
    FOLLOW_56_in_timedEffect2336 = frozenset([1])
    FOLLOW_54_in_timedEffect2341 = frozenset([96, 97, 98, 99, 100])
    FOLLOW_assignOp_in_timedEffect2343 = frozenset([45, 48, 54])
    FOLLOW_fHead_in_timedEffect2345 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_timedEffect2347 = frozenset([56])
    FOLLOW_56_in_timedEffect2349 = frozenset([1])
    FOLLOW_54_in_fAssignDA2369 = frozenset([96, 97, 98, 99, 100])
    FOLLOW_assignOp_in_fAssignDA2371 = frozenset([45, 48, 54])
    FOLLOW_fHead_in_fAssignDA2373 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_fAssignDA2375 = frozenset([56])
    FOLLOW_56_in_fAssignDA2377 = frozenset([1])
    FOLLOW_54_in_fExpDA2388 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_fExpDA2392 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_fExpDA2394 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_fExpDA2396 = frozenset([56])
    FOLLOW_60_in_fExpDA2402 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_fExpDA2404 = frozenset([56])
    FOLLOW_56_in_fExpDA2408 = frozenset([1])
    FOLLOW_101_in_fExpDA2413 = frozenset([1])
    FOLLOW_fExp_in_fExpDA2418 = frozenset([1])
    FOLLOW_54_in_problem2432 = frozenset([55])
    FOLLOW_55_in_problem2434 = frozenset([54])
    FOLLOW_problemDecl_in_problem2436 = frozenset([54])
    FOLLOW_problemDomain_in_problem2441 = frozenset([54])
    FOLLOW_requireDef_in_problem2449 = frozenset([54])
    FOLLOW_objectDecl_in_problem2458 = frozenset([54])
    FOLLOW_init_in_problem2467 = frozenset([54])
    FOLLOW_goal_in_problem2475 = frozenset([54, 56])
    FOLLOW_probConstraints_in_problem2483 = frozenset([54, 56])
    FOLLOW_metricSpec_in_problem2492 = frozenset([56])
    FOLLOW_56_in_problem2508 = frozenset([1])
    FOLLOW_54_in_problemDecl2565 = frozenset([102])
    FOLLOW_102_in_problemDecl2567 = frozenset([45])
    FOLLOW_NAME_in_problemDecl2569 = frozenset([56])
    FOLLOW_56_in_problemDecl2571 = frozenset([1])
    FOLLOW_54_in_problemDomain2597 = frozenset([103])
    FOLLOW_103_in_problemDomain2599 = frozenset([45])
    FOLLOW_NAME_in_problemDomain2601 = frozenset([56])
    FOLLOW_56_in_problemDomain2603 = frozenset([1])
    FOLLOW_54_in_objectDecl2623 = frozenset([104])
    FOLLOW_104_in_objectDecl2625 = frozenset([45, 56])
    FOLLOW_typedNameList_in_objectDecl2627 = frozenset([56])
    FOLLOW_56_in_objectDecl2629 = frozenset([1])
    FOLLOW_54_in_init2649 = frozenset([105])
    FOLLOW_105_in_init2651 = frozenset([54, 56])
    FOLLOW_initEl_in_init2653 = frozenset([54, 56])
    FOLLOW_56_in_init2656 = frozenset([1])
    FOLLOW_nameLiteral_in_initEl2677 = frozenset([1])
    FOLLOW_54_in_initEl2682 = frozenset([93])
    FOLLOW_93_in_initEl2684 = frozenset([45, 48, 54])
    FOLLOW_fHead_in_initEl2686 = frozenset([48])
    FOLLOW_NUMBER_in_initEl2688 = frozenset([56])
    FOLLOW_56_in_initEl2690 = frozenset([1])
    FOLLOW_54_in_initEl2713 = frozenset([81])
    FOLLOW_81_in_initEl2715 = frozenset([48])
    FOLLOW_NUMBER_in_initEl2717 = frozenset([54])
    FOLLOW_nameLiteral_in_initEl2719 = frozenset([56])
    FOLLOW_56_in_initEl2721 = frozenset([1])
    FOLLOW_atomicNameFormula_in_nameLiteral2743 = frozenset([1])
    FOLLOW_54_in_nameLiteral2748 = frozenset([73])
    FOLLOW_73_in_nameLiteral2750 = frozenset([54])
    FOLLOW_atomicNameFormula_in_nameLiteral2752 = frozenset([56])
    FOLLOW_56_in_nameLiteral2754 = frozenset([1])
    FOLLOW_54_in_atomicNameFormula2773 = frozenset([45])
    FOLLOW_predicate_in_atomicNameFormula2775 = frozenset([45, 56])
    FOLLOW_NAME_in_atomicNameFormula2777 = frozenset([45, 56])
    FOLLOW_56_in_atomicNameFormula2780 = frozenset([1])
    FOLLOW_54_in_goal2805 = frozenset([106])
    FOLLOW_106_in_goal2807 = frozenset([54])
    FOLLOW_goalDesc_in_goal2809 = frozenset([56])
    FOLLOW_56_in_goal2811 = frozenset([1])
    FOLLOW_54_in_probConstraints2829 = frozenset([66])
    FOLLOW_66_in_probConstraints2831 = frozenset([54])
    FOLLOW_prefConGD_in_probConstraints2834 = frozenset([56])
    FOLLOW_56_in_probConstraints2836 = frozenset([1])
    FOLLOW_54_in_prefConGD2858 = frozenset([71])
    FOLLOW_71_in_prefConGD2860 = frozenset([54, 56])
    FOLLOW_prefConGD_in_prefConGD2862 = frozenset([54, 56])
    FOLLOW_56_in_prefConGD2865 = frozenset([1])
    FOLLOW_54_in_prefConGD2870 = frozenset([76])
    FOLLOW_76_in_prefConGD2872 = frozenset([54])
    FOLLOW_54_in_prefConGD2874 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_prefConGD2876 = frozenset([56])
    FOLLOW_56_in_prefConGD2878 = frozenset([54])
    FOLLOW_prefConGD_in_prefConGD2880 = frozenset([56])
    FOLLOW_56_in_prefConGD2882 = frozenset([1])
    FOLLOW_54_in_prefConGD2887 = frozenset([80])
    FOLLOW_80_in_prefConGD2889 = frozenset([45, 54])
    FOLLOW_NAME_in_prefConGD2891 = frozenset([54])
    FOLLOW_conGD_in_prefConGD2894 = frozenset([56])
    FOLLOW_56_in_prefConGD2896 = frozenset([1])
    FOLLOW_conGD_in_prefConGD2901 = frozenset([1])
    FOLLOW_54_in_metricSpec2912 = frozenset([107])
    FOLLOW_107_in_metricSpec2914 = frozenset([108, 109])
    FOLLOW_optimization_in_metricSpec2916 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricSpec2918 = frozenset([56])
    FOLLOW_56_in_metricSpec2920 = frozenset([1])
    FOLLOW_set_in_optimization0 = frozenset([1])
    FOLLOW_54_in_metricFExp2957 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_metricFExp2959 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricFExp2961 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricFExp2963 = frozenset([56])
    FOLLOW_56_in_metricFExp2965 = frozenset([1])
    FOLLOW_54_in_metricFExp2970 = frozenset([88, 90])
    FOLLOW_set_in_metricFExp2972 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricFExp2978 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricFExp2980 = frozenset([45, 48, 54, 56, 110])
    FOLLOW_56_in_metricFExp2983 = frozenset([1])
    FOLLOW_54_in_metricFExp2988 = frozenset([60])
    FOLLOW_60_in_metricFExp2990 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_metricFExp2992 = frozenset([56])
    FOLLOW_56_in_metricFExp2994 = frozenset([1])
    FOLLOW_NUMBER_in_metricFExp2999 = frozenset([1])
    FOLLOW_54_in_metricFExp3004 = frozenset([45])
    FOLLOW_functionSymbol_in_metricFExp3006 = frozenset([45, 56])
    FOLLOW_NAME_in_metricFExp3008 = frozenset([45, 56])
    FOLLOW_56_in_metricFExp3011 = frozenset([1])
    FOLLOW_functionSymbol_in_metricFExp3016 = frozenset([1])
    FOLLOW_110_in_metricFExp3024 = frozenset([1])
    FOLLOW_54_in_metricFExp3029 = frozenset([111])
    FOLLOW_111_in_metricFExp3031 = frozenset([45])
    FOLLOW_NAME_in_metricFExp3033 = frozenset([56])
    FOLLOW_56_in_metricFExp3035 = frozenset([1])
    FOLLOW_54_in_conGD3049 = frozenset([71])
    FOLLOW_71_in_conGD3051 = frozenset([54, 56])
    FOLLOW_conGD_in_conGD3053 = frozenset([54, 56])
    FOLLOW_56_in_conGD3056 = frozenset([1])
    FOLLOW_54_in_conGD3061 = frozenset([76])
    FOLLOW_76_in_conGD3063 = frozenset([54])
    FOLLOW_54_in_conGD3065 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_conGD3067 = frozenset([56])
    FOLLOW_56_in_conGD3069 = frozenset([54])
    FOLLOW_conGD_in_conGD3071 = frozenset([56])
    FOLLOW_56_in_conGD3073 = frozenset([1])
    FOLLOW_54_in_conGD3078 = frozenset([81])
    FOLLOW_81_in_conGD3080 = frozenset([84])
    FOLLOW_84_in_conGD3082 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3084 = frozenset([56])
    FOLLOW_56_in_conGD3086 = frozenset([1])
    FOLLOW_54_in_conGD3094 = frozenset([112])
    FOLLOW_112_in_conGD3096 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3098 = frozenset([56])
    FOLLOW_56_in_conGD3100 = frozenset([1])
    FOLLOW_54_in_conGD3105 = frozenset([113])
    FOLLOW_113_in_conGD3107 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3109 = frozenset([56])
    FOLLOW_56_in_conGD3111 = frozenset([1])
    FOLLOW_54_in_conGD3117 = frozenset([114])
    FOLLOW_114_in_conGD3119 = frozenset([48])
    FOLLOW_NUMBER_in_conGD3121 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3123 = frozenset([56])
    FOLLOW_56_in_conGD3125 = frozenset([1])
    FOLLOW_54_in_conGD3130 = frozenset([115])
    FOLLOW_115_in_conGD3132 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3134 = frozenset([56])
    FOLLOW_56_in_conGD3136 = frozenset([1])
    FOLLOW_54_in_conGD3141 = frozenset([116])
    FOLLOW_116_in_conGD3143 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3145 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3147 = frozenset([56])
    FOLLOW_56_in_conGD3149 = frozenset([1])
    FOLLOW_54_in_conGD3154 = frozenset([117])
    FOLLOW_117_in_conGD3156 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3158 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3160 = frozenset([56])
    FOLLOW_56_in_conGD3162 = frozenset([1])
    FOLLOW_54_in_conGD3167 = frozenset([118])
    FOLLOW_118_in_conGD3169 = frozenset([48])
    FOLLOW_NUMBER_in_conGD3171 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3173 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3175 = frozenset([56])
    FOLLOW_56_in_conGD3177 = frozenset([1])
    FOLLOW_54_in_conGD3182 = frozenset([119])
    FOLLOW_119_in_conGD3184 = frozenset([48])
    FOLLOW_NUMBER_in_conGD3186 = frozenset([48])
    FOLLOW_NUMBER_in_conGD3188 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3190 = frozenset([56])
    FOLLOW_56_in_conGD3192 = frozenset([1])
    FOLLOW_54_in_conGD3197 = frozenset([120])
    FOLLOW_120_in_conGD3199 = frozenset([48])
    FOLLOW_NUMBER_in_conGD3201 = frozenset([54])
    FOLLOW_goalDesc_in_conGD3203 = frozenset([56])
    FOLLOW_56_in_conGD3205 = frozenset([1])
    FOLLOW_atomicFunctionSkeleton_in_synpred20_Pddl763 = frozenset([1])
    FOLLOW_54_in_synpred59_Pddl1774 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_synpred59_Pddl1776 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_synpred59_Pddl1778 = frozenset([45, 48, 54])
    FOLLOW_fExp2_in_synpred59_Pddl1780 = frozenset([56])
    FOLLOW_56_in_synpred59_Pddl1782 = frozenset([1])
    FOLLOW_54_in_synpred60_Pddl1799 = frozenset([60])
    FOLLOW_60_in_synpred60_Pddl1801 = frozenset([45, 48, 54])
    FOLLOW_fExp_in_synpred60_Pddl1803 = frozenset([56])
    FOLLOW_56_in_synpred60_Pddl1805 = frozenset([1])
    FOLLOW_NUMBER_in_synpred88_Pddl2230 = frozenset([1])
    FOLLOW_54_in_synpred90_Pddl2244 = frozenset([71])
    FOLLOW_71_in_synpred90_Pddl2246 = frozenset([54, 56])
    FOLLOW_daEffect_in_synpred90_Pddl2248 = frozenset([54, 56])
    FOLLOW_56_in_synpred90_Pddl2251 = frozenset([1])
    FOLLOW_timedEffect_in_synpred91_Pddl2256 = frozenset([1])
    FOLLOW_54_in_synpred92_Pddl2261 = frozenset([76])
    FOLLOW_76_in_synpred92_Pddl2263 = frozenset([54])
    FOLLOW_54_in_synpred92_Pddl2265 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_synpred92_Pddl2267 = frozenset([56])
    FOLLOW_56_in_synpred92_Pddl2269 = frozenset([54])
    FOLLOW_daEffect_in_synpred92_Pddl2271 = frozenset([56])
    FOLLOW_56_in_synpred92_Pddl2273 = frozenset([1])
    FOLLOW_54_in_synpred93_Pddl2278 = frozenset([87])
    FOLLOW_87_in_synpred93_Pddl2280 = frozenset([54])
    FOLLOW_daGD_in_synpred93_Pddl2282 = frozenset([54])
    FOLLOW_timedEffect_in_synpred93_Pddl2284 = frozenset([56])
    FOLLOW_56_in_synpred93_Pddl2286 = frozenset([1])
    FOLLOW_54_in_synpred94_Pddl2310 = frozenset([81])
    FOLLOW_81_in_synpred94_Pddl2312 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_synpred94_Pddl2314 = frozenset([54])
    FOLLOW_daEffect_in_synpred94_Pddl2316 = frozenset([56])
    FOLLOW_56_in_synpred94_Pddl2318 = frozenset([1])
    FOLLOW_54_in_synpred95_Pddl2328 = frozenset([81])
    FOLLOW_81_in_synpred95_Pddl2330 = frozenset([83, 84])
    FOLLOW_timeSpecifier_in_synpred95_Pddl2332 = frozenset([54])
    FOLLOW_fAssignDA_in_synpred95_Pddl2334 = frozenset([56])
    FOLLOW_56_in_synpred95_Pddl2336 = frozenset([1])
    FOLLOW_binaryOp_in_synpred96_Pddl2392 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_synpred96_Pddl2394 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_synpred96_Pddl2396 = frozenset([1])
    FOLLOW_54_in_synpred97_Pddl2388 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_synpred97_Pddl2392 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_synpred97_Pddl2394 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_synpred97_Pddl2396 = frozenset([56])
    FOLLOW_60_in_synpred97_Pddl2402 = frozenset([45, 48, 54, 101])
    FOLLOW_fExpDA_in_synpred97_Pddl2404 = frozenset([56])
    FOLLOW_56_in_synpred97_Pddl2408 = frozenset([1])
    FOLLOW_54_in_synpred109_Pddl2858 = frozenset([71])
    FOLLOW_71_in_synpred109_Pddl2860 = frozenset([54, 56])
    FOLLOW_prefConGD_in_synpred109_Pddl2862 = frozenset([54, 56])
    FOLLOW_56_in_synpred109_Pddl2865 = frozenset([1])
    FOLLOW_54_in_synpred110_Pddl2870 = frozenset([76])
    FOLLOW_76_in_synpred110_Pddl2872 = frozenset([54])
    FOLLOW_54_in_synpred110_Pddl2874 = frozenset([47, 56])
    FOLLOW_typedVariableList_in_synpred110_Pddl2876 = frozenset([56])
    FOLLOW_56_in_synpred110_Pddl2878 = frozenset([54])
    FOLLOW_prefConGD_in_synpred110_Pddl2880 = frozenset([56])
    FOLLOW_56_in_synpred110_Pddl2882 = frozenset([1])
    FOLLOW_54_in_synpred112_Pddl2887 = frozenset([80])
    FOLLOW_80_in_synpred112_Pddl2889 = frozenset([45, 54])
    FOLLOW_NAME_in_synpred112_Pddl2891 = frozenset([54])
    FOLLOW_conGD_in_synpred112_Pddl2894 = frozenset([56])
    FOLLOW_56_in_synpred112_Pddl2896 = frozenset([1])
    FOLLOW_54_in_synpred114_Pddl2957 = frozenset([60, 88, 89, 90])
    FOLLOW_binaryOp_in_synpred114_Pddl2959 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_synpred114_Pddl2961 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_synpred114_Pddl2963 = frozenset([56])
    FOLLOW_56_in_synpred114_Pddl2965 = frozenset([1])
    FOLLOW_54_in_synpred117_Pddl2970 = frozenset([88, 90])
    FOLLOW_set_in_synpred117_Pddl2972 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_synpred117_Pddl2978 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_synpred117_Pddl2980 = frozenset([45, 48, 54, 56, 110])
    FOLLOW_56_in_synpred117_Pddl2983 = frozenset([1])
    FOLLOW_54_in_synpred118_Pddl2988 = frozenset([60])
    FOLLOW_60_in_synpred118_Pddl2990 = frozenset([45, 48, 54, 110])
    FOLLOW_metricFExp_in_synpred118_Pddl2992 = frozenset([56])
    FOLLOW_56_in_synpred118_Pddl2994 = frozenset([1])
    FOLLOW_54_in_synpred121_Pddl3004 = frozenset([45])
    FOLLOW_functionSymbol_in_synpred121_Pddl3006 = frozenset([45, 56])
    FOLLOW_NAME_in_synpred121_Pddl3008 = frozenset([45, 56])
    FOLLOW_56_in_synpred121_Pddl3011 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("PddlLexer", PddlParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
