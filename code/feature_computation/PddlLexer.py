# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 Pddl.g 2011-11-28 11:16:32

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


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
OBJECTS=18
PROBLEM_DOMAIN=17
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
T__103=103
T__59=59
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
GOAL=36
BINARY_OP=37
FORALL_GD=28
T__102=102
T__101=101
T__100=100
DOMAIN=4
WHEN_EFFECT=32
PRECONDITION=21
EFFECT=22
AND_EFFECT=30
PROBLEM_CONSTRAINT=43
EITHER_TYPE=8
FORALL_EFFECT=31
REQUIREMENTS=6


class PddlLexer(Lexer):

    grammarFileName = "Pddl.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(PddlLexer, self).__init__(input, state)


        self.dfa1 = self.DFA1(
            self, 1,
            eot = self.DFA1_eot,
            eof = self.DFA1_eof,
            min = self.DFA1_min,
            max = self.DFA1_max,
            accept = self.DFA1_accept,
            special = self.DFA1_special,
            transition = self.DFA1_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )






    # $ANTLR start "T__54"
    def mT__54(self, ):

        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # Pddl.g:7:7: ( '(' )
            # Pddl.g:7:9: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):

        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # Pddl.g:8:7: ( 'define' )
            # Pddl.g:8:9: 'define'
            pass 
            self.match("define")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):

        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # Pddl.g:9:7: ( ')' )
            # Pddl.g:9:9: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):

        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # Pddl.g:10:7: ( 'domain' )
            # Pddl.g:10:9: 'domain'
            pass 
            self.match("domain")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):

        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # Pddl.g:11:7: ( ':requirements' )
            # Pddl.g:11:9: ':requirements'
            pass 
            self.match(":requirements")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):

        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # Pddl.g:12:7: ( ':types' )
            # Pddl.g:12:9: ':types'
            pass 
            self.match(":types")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__59"



    # $ANTLR start "T__60"
    def mT__60(self, ):

        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # Pddl.g:13:7: ( '-' )
            # Pddl.g:13:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__60"



    # $ANTLR start "T__61"
    def mT__61(self, ):

        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # Pddl.g:14:7: ( 'either' )
            # Pddl.g:14:9: 'either'
            pass 
            self.match("either")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__61"



    # $ANTLR start "T__62"
    def mT__62(self, ):

        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # Pddl.g:15:7: ( ':functions' )
            # Pddl.g:15:9: ':functions'
            pass 
            self.match(":functions")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__62"



    # $ANTLR start "T__63"
    def mT__63(self, ):

        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # Pddl.g:16:7: ( 'number' )
            # Pddl.g:16:9: 'number'
            pass 
            self.match("number")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__63"



    # $ANTLR start "T__64"
    def mT__64(self, ):

        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # Pddl.g:17:7: ( ':constants' )
            # Pddl.g:17:9: ':constants'
            pass 
            self.match(":constants")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):

        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # Pddl.g:18:7: ( ':predicates' )
            # Pddl.g:18:9: ':predicates'
            pass 
            self.match(":predicates")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):

        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # Pddl.g:19:7: ( ':constraints' )
            # Pddl.g:19:9: ':constraints'
            pass 
            self.match(":constraints")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):

        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # Pddl.g:20:7: ( ':action' )
            # Pddl.g:20:9: ':action'
            pass 
            self.match(":action")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):

        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # Pddl.g:21:7: ( ':parameters' )
            # Pddl.g:21:9: ':parameters'
            pass 
            self.match(":parameters")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):

        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # Pddl.g:22:7: ( ':precondition' )
            # Pddl.g:22:9: ':precondition'
            pass 
            self.match(":precondition")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):

        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # Pddl.g:23:7: ( ':effect' )
            # Pddl.g:23:9: ':effect'
            pass 
            self.match(":effect")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):

        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # Pddl.g:24:7: ( 'and' )
            # Pddl.g:24:9: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):

        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # Pddl.g:25:7: ( 'or' )
            # Pddl.g:25:9: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):

        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # Pddl.g:26:7: ( 'not' )
            # Pddl.g:26:9: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):

        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # Pddl.g:27:7: ( 'imply' )
            # Pddl.g:27:9: 'imply'
            pass 
            self.match("imply")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):

        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # Pddl.g:28:7: ( 'exists' )
            # Pddl.g:28:9: 'exists'
            pass 
            self.match("exists")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):

        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # Pddl.g:29:7: ( 'forall' )
            # Pddl.g:29:9: 'forall'
            pass 
            self.match("forall")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):

        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # Pddl.g:30:7: ( ':durative-action' )
            # Pddl.g:30:9: ':durative-action'
            pass 
            self.match(":durative-action")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):

        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # Pddl.g:31:7: ( ':duration' )
            # Pddl.g:31:9: ':duration'
            pass 
            self.match(":duration")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):

        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # Pddl.g:32:7: ( ':condition' )
            # Pddl.g:32:9: ':condition'
            pass 
            self.match(":condition")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):

        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # Pddl.g:33:7: ( 'preference' )
            # Pddl.g:33:9: 'preference'
            pass 
            self.match("preference")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):

        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # Pddl.g:34:7: ( 'at' )
            # Pddl.g:34:9: 'at'
            pass 
            self.match("at")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):

        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # Pddl.g:35:7: ( 'over' )
            # Pddl.g:35:9: 'over'
            pass 
            self.match("over")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):

        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # Pddl.g:36:7: ( 'start' )
            # Pddl.g:36:9: 'start'
            pass 
            self.match("start")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):

        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # Pddl.g:37:7: ( 'end' )
            # Pddl.g:37:9: 'end'
            pass 
            self.match("end")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):

        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # Pddl.g:38:7: ( 'all' )
            # Pddl.g:38:9: 'all'
            pass 
            self.match("all")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):

        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # Pddl.g:39:7: ( ':derived' )
            # Pddl.g:39:9: ':derived'
            pass 
            self.match(":derived")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):

        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # Pddl.g:40:7: ( 'when' )
            # Pddl.g:40:9: 'when'
            pass 
            self.match("when")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):

        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # Pddl.g:41:7: ( '*' )
            # Pddl.g:41:9: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):

        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # Pddl.g:42:7: ( '+' )
            # Pddl.g:42:9: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):

        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # Pddl.g:43:7: ( '/' )
            # Pddl.g:43:9: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):

        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # Pddl.g:44:7: ( '>' )
            # Pddl.g:44:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):

        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # Pddl.g:45:7: ( '<' )
            # Pddl.g:45:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):

        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # Pddl.g:46:7: ( '=' )
            # Pddl.g:46:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):

        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # Pddl.g:47:7: ( '>=' )
            # Pddl.g:47:9: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):

        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # Pddl.g:48:7: ( '<=' )
            # Pddl.g:48:9: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):

        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # Pddl.g:49:7: ( 'assign' )
            # Pddl.g:49:9: 'assign'
            pass 
            self.match("assign")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):

        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # Pddl.g:50:7: ( 'scale-up' )
            # Pddl.g:50:9: 'scale-up'
            pass 
            self.match("scale-up")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):

        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # Pddl.g:51:7: ( 'scale-down' )
            # Pddl.g:51:9: 'scale-down'
            pass 
            self.match("scale-down")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):

        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # Pddl.g:52:7: ( 'increase' )
            # Pddl.g:52:9: 'increase'
            pass 
            self.match("increase")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):

        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # Pddl.g:53:8: ( 'decrease' )
            # Pddl.g:53:10: 'decrease'
            pass 
            self.match("decrease")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):

        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # Pddl.g:54:8: ( '?duration' )
            # Pddl.g:54:10: '?duration'
            pass 
            self.match("?duration")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):

        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # Pddl.g:55:8: ( 'problem' )
            # Pddl.g:55:10: 'problem'
            pass 
            self.match("problem")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):

        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # Pddl.g:56:8: ( ':domain' )
            # Pddl.g:56:10: ':domain'
            pass 
            self.match(":domain")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__103"



    # $ANTLR start "T__104"
    def mT__104(self, ):

        try:
            _type = T__104
            _channel = DEFAULT_CHANNEL

            # Pddl.g:57:8: ( ':objects' )
            # Pddl.g:57:10: ':objects'
            pass 
            self.match(":objects")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__104"



    # $ANTLR start "T__105"
    def mT__105(self, ):

        try:
            _type = T__105
            _channel = DEFAULT_CHANNEL

            # Pddl.g:58:8: ( ':init' )
            # Pddl.g:58:10: ':init'
            pass 
            self.match(":init")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__105"



    # $ANTLR start "T__106"
    def mT__106(self, ):

        try:
            _type = T__106
            _channel = DEFAULT_CHANNEL

            # Pddl.g:59:8: ( ':goal' )
            # Pddl.g:59:10: ':goal'
            pass 
            self.match(":goal")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__106"



    # $ANTLR start "T__107"
    def mT__107(self, ):

        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # Pddl.g:60:8: ( ':metric' )
            # Pddl.g:60:10: ':metric'
            pass 
            self.match(":metric")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__107"



    # $ANTLR start "T__108"
    def mT__108(self, ):

        try:
            _type = T__108
            _channel = DEFAULT_CHANNEL

            # Pddl.g:61:8: ( 'minimize' )
            # Pddl.g:61:10: 'minimize'
            pass 
            self.match("minimize")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__108"



    # $ANTLR start "T__109"
    def mT__109(self, ):

        try:
            _type = T__109
            _channel = DEFAULT_CHANNEL

            # Pddl.g:62:8: ( 'maximize' )
            # Pddl.g:62:10: 'maximize'
            pass 
            self.match("maximize")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__109"



    # $ANTLR start "T__110"
    def mT__110(self, ):

        try:
            _type = T__110
            _channel = DEFAULT_CHANNEL

            # Pddl.g:63:8: ( 'total-time' )
            # Pddl.g:63:10: 'total-time'
            pass 
            self.match("total-time")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__110"



    # $ANTLR start "T__111"
    def mT__111(self, ):

        try:
            _type = T__111
            _channel = DEFAULT_CHANNEL

            # Pddl.g:64:8: ( 'is-violated' )
            # Pddl.g:64:10: 'is-violated'
            pass 
            self.match("is-violated")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__111"



    # $ANTLR start "T__112"
    def mT__112(self, ):

        try:
            _type = T__112
            _channel = DEFAULT_CHANNEL

            # Pddl.g:65:8: ( 'always' )
            # Pddl.g:65:10: 'always'
            pass 
            self.match("always")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__112"



    # $ANTLR start "T__113"
    def mT__113(self, ):

        try:
            _type = T__113
            _channel = DEFAULT_CHANNEL

            # Pddl.g:66:8: ( 'sometime' )
            # Pddl.g:66:10: 'sometime'
            pass 
            self.match("sometime")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__113"



    # $ANTLR start "T__114"
    def mT__114(self, ):

        try:
            _type = T__114
            _channel = DEFAULT_CHANNEL

            # Pddl.g:67:8: ( 'within' )
            # Pddl.g:67:10: 'within'
            pass 
            self.match("within")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__114"



    # $ANTLR start "T__115"
    def mT__115(self, ):

        try:
            _type = T__115
            _channel = DEFAULT_CHANNEL

            # Pddl.g:68:8: ( 'at-most-once' )
            # Pddl.g:68:10: 'at-most-once'
            pass 
            self.match("at-most-once")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__115"



    # $ANTLR start "T__116"
    def mT__116(self, ):

        try:
            _type = T__116
            _channel = DEFAULT_CHANNEL

            # Pddl.g:69:8: ( 'sometime-after' )
            # Pddl.g:69:10: 'sometime-after'
            pass 
            self.match("sometime-after")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__116"



    # $ANTLR start "T__117"
    def mT__117(self, ):

        try:
            _type = T__117
            _channel = DEFAULT_CHANNEL

            # Pddl.g:70:8: ( 'sometime-before' )
            # Pddl.g:70:10: 'sometime-before'
            pass 
            self.match("sometime-before")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__117"



    # $ANTLR start "T__118"
    def mT__118(self, ):

        try:
            _type = T__118
            _channel = DEFAULT_CHANNEL

            # Pddl.g:71:8: ( 'always-within' )
            # Pddl.g:71:10: 'always-within'
            pass 
            self.match("always-within")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__118"



    # $ANTLR start "T__119"
    def mT__119(self, ):

        try:
            _type = T__119
            _channel = DEFAULT_CHANNEL

            # Pddl.g:72:8: ( 'hold-during' )
            # Pddl.g:72:10: 'hold-during'
            pass 
            self.match("hold-during")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__119"



    # $ANTLR start "T__120"
    def mT__120(self, ):

        try:
            _type = T__120
            _channel = DEFAULT_CHANNEL

            # Pddl.g:73:8: ( 'hold-after' )
            # Pddl.g:73:10: 'hold-after'
            pass 
            self.match("hold-after")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__120"



    # $ANTLR start "REQUIRE_KEY"
    def mREQUIRE_KEY(self, ):

        try:
            _type = REQUIRE_KEY
            _channel = DEFAULT_CHANNEL

            # Pddl.g:509:5: ( ':strips' | ':typing' | ':negative-preconditions' | ':disjunctive-preconditions' | ':equality' | ':existential-preconditions' | ':universal-preconditions' | ':quantified-preconditions' | ':conditional-effects' | ':fluents' | ':adl' | ':durative-actions' | ':derived-predicates' | ':timed-initial-literals' | ':preferences' | ':constraints' )
            alt1 = 16
            alt1 = self.dfa1.predict(self.input)
            if alt1 == 1:
                # Pddl.g:509:7: ':strips'
                pass 
                self.match(":strips")


            elif alt1 == 2:
                # Pddl.g:510:7: ':typing'
                pass 
                self.match(":typing")


            elif alt1 == 3:
                # Pddl.g:511:7: ':negative-preconditions'
                pass 
                self.match(":negative-preconditions")


            elif alt1 == 4:
                # Pddl.g:512:7: ':disjunctive-preconditions'
                pass 
                self.match(":disjunctive-preconditions")


            elif alt1 == 5:
                # Pddl.g:513:7: ':equality'
                pass 
                self.match(":equality")


            elif alt1 == 6:
                # Pddl.g:514:7: ':existential-preconditions'
                pass 
                self.match(":existential-preconditions")


            elif alt1 == 7:
                # Pddl.g:515:7: ':universal-preconditions'
                pass 
                self.match(":universal-preconditions")


            elif alt1 == 8:
                # Pddl.g:516:7: ':quantified-preconditions'
                pass 
                self.match(":quantified-preconditions")


            elif alt1 == 9:
                # Pddl.g:517:7: ':conditional-effects'
                pass 
                self.match(":conditional-effects")


            elif alt1 == 10:
                # Pddl.g:518:7: ':fluents'
                pass 
                self.match(":fluents")


            elif alt1 == 11:
                # Pddl.g:519:7: ':adl'
                pass 
                self.match(":adl")


            elif alt1 == 12:
                # Pddl.g:520:7: ':durative-actions'
                pass 
                self.match(":durative-actions")


            elif alt1 == 13:
                # Pddl.g:521:7: ':derived-predicates'
                pass 
                self.match(":derived-predicates")


            elif alt1 == 14:
                # Pddl.g:522:7: ':timed-initial-literals'
                pass 
                self.match(":timed-initial-literals")


            elif alt1 == 15:
                # Pddl.g:523:7: ':preferences'
                pass 
                self.match(":preferences")


            elif alt1 == 16:
                # Pddl.g:524:7: ':constraints'
                pass 
                self.match(":constraints")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "REQUIRE_KEY"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # Pddl.g:528:5: ( LETTER ( ANY_CHAR )* )
            # Pddl.g:528:10: LETTER ( ANY_CHAR )*
            pass 
            self.mLETTER()
            # Pddl.g:528:17: ( ANY_CHAR )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 45 or (48 <= LA2_0 <= 57) or (65 <= LA2_0 <= 90) or LA2_0 == 95 or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # Pddl.g:528:17: ANY_CHAR
                    pass 
                    self.mANY_CHAR()


                else:
                    break #loop2



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # Pddl.g:530:16: ( 'a' .. 'z' | 'A' .. 'Z' )
            # Pddl.g:
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "ANY_CHAR"
    def mANY_CHAR(self, ):

        try:
            # Pddl.g:532:18: ( LETTER | '0' .. '9' | '-' | '_' )
            # Pddl.g:
            pass 
            if self.input.LA(1) == 45 or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "ANY_CHAR"



    # $ANTLR start "VARIABLE"
    def mVARIABLE(self, ):

        try:
            _type = VARIABLE
            _channel = DEFAULT_CHANNEL

            # Pddl.g:534:10: ( '?' LETTER ( ANY_CHAR )* )
            # Pddl.g:534:12: '?' LETTER ( ANY_CHAR )*
            pass 
            self.match(63)
            self.mLETTER()
            # Pddl.g:534:23: ( ANY_CHAR )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 45 or (48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # Pddl.g:534:23: ANY_CHAR
                    pass 
                    self.mANY_CHAR()


                else:
                    break #loop3



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VARIABLE"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):

        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # Pddl.g:536:8: ( ( DIGIT )+ ( '.' ( DIGIT )+ )? )
            # Pddl.g:536:10: ( DIGIT )+ ( '.' ( DIGIT )+ )?
            pass 
            # Pddl.g:536:10: ( DIGIT )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((48 <= LA4_0 <= 57)) :
                    alt4 = 1


                if alt4 == 1:
                    # Pddl.g:536:10: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1
            # Pddl.g:536:17: ( '.' ( DIGIT )+ )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 46) :
                alt6 = 1
            if alt6 == 1:
                # Pddl.g:536:18: '.' ( DIGIT )+
                pass 
                self.match(46)
                # Pddl.g:536:22: ( DIGIT )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((48 <= LA5_0 <= 57)) :
                        alt5 = 1


                    if alt5 == 1:
                        # Pddl.g:536:22: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # Pddl.g:538:15: ( '0' .. '9' )
            # Pddl.g:538:17: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LINE_COMMENT"
    def mLINE_COMMENT(self, ):

        try:
            _type = LINE_COMMENT
            _channel = DEFAULT_CHANNEL

            # Pddl.g:541:5: ( ';' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # Pddl.g:541:7: ';' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match(59)
            # Pddl.g:541:11: (~ ( '\\n' | '\\r' ) )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 9) or (11 <= LA7_0 <= 12) or (14 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # Pddl.g:541:11: ~ ( '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7
            # Pddl.g:541:25: ( '\\r' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 13) :
                alt8 = 1
            if alt8 == 1:
                # Pddl.g:541:25: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LINE_COMMENT"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # Pddl.g:545:5: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            # Pddl.g:545:9: ( ' ' | '\\t' | '\\r' | '\\n' )+
            pass 
            # Pddl.g:545:9: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((9 <= LA9_0 <= 10) or LA9_0 == 13 or LA9_0 == 32) :
                    alt9 = 1


                if alt9 == 1:
                    # Pddl.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # Pddl.g:1:8: ( T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | T__104 | T__105 | T__106 | T__107 | T__108 | T__109 | T__110 | T__111 | T__112 | T__113 | T__114 | T__115 | T__116 | T__117 | T__118 | T__119 | T__120 | REQUIRE_KEY | NAME | VARIABLE | NUMBER | LINE_COMMENT | WHITESPACE )
        alt10 = 73
        alt10 = self.dfa10.predict(self.input)
        if alt10 == 1:
            # Pddl.g:1:10: T__54
            pass 
            self.mT__54()


        elif alt10 == 2:
            # Pddl.g:1:16: T__55
            pass 
            self.mT__55()


        elif alt10 == 3:
            # Pddl.g:1:22: T__56
            pass 
            self.mT__56()


        elif alt10 == 4:
            # Pddl.g:1:28: T__57
            pass 
            self.mT__57()


        elif alt10 == 5:
            # Pddl.g:1:34: T__58
            pass 
            self.mT__58()


        elif alt10 == 6:
            # Pddl.g:1:40: T__59
            pass 
            self.mT__59()


        elif alt10 == 7:
            # Pddl.g:1:46: T__60
            pass 
            self.mT__60()


        elif alt10 == 8:
            # Pddl.g:1:52: T__61
            pass 
            self.mT__61()


        elif alt10 == 9:
            # Pddl.g:1:58: T__62
            pass 
            self.mT__62()


        elif alt10 == 10:
            # Pddl.g:1:64: T__63
            pass 
            self.mT__63()


        elif alt10 == 11:
            # Pddl.g:1:70: T__64
            pass 
            self.mT__64()


        elif alt10 == 12:
            # Pddl.g:1:76: T__65
            pass 
            self.mT__65()


        elif alt10 == 13:
            # Pddl.g:1:82: T__66
            pass 
            self.mT__66()


        elif alt10 == 14:
            # Pddl.g:1:88: T__67
            pass 
            self.mT__67()


        elif alt10 == 15:
            # Pddl.g:1:94: T__68
            pass 
            self.mT__68()


        elif alt10 == 16:
            # Pddl.g:1:100: T__69
            pass 
            self.mT__69()


        elif alt10 == 17:
            # Pddl.g:1:106: T__70
            pass 
            self.mT__70()


        elif alt10 == 18:
            # Pddl.g:1:112: T__71
            pass 
            self.mT__71()


        elif alt10 == 19:
            # Pddl.g:1:118: T__72
            pass 
            self.mT__72()


        elif alt10 == 20:
            # Pddl.g:1:124: T__73
            pass 
            self.mT__73()


        elif alt10 == 21:
            # Pddl.g:1:130: T__74
            pass 
            self.mT__74()


        elif alt10 == 22:
            # Pddl.g:1:136: T__75
            pass 
            self.mT__75()


        elif alt10 == 23:
            # Pddl.g:1:142: T__76
            pass 
            self.mT__76()


        elif alt10 == 24:
            # Pddl.g:1:148: T__77
            pass 
            self.mT__77()


        elif alt10 == 25:
            # Pddl.g:1:154: T__78
            pass 
            self.mT__78()


        elif alt10 == 26:
            # Pddl.g:1:160: T__79
            pass 
            self.mT__79()


        elif alt10 == 27:
            # Pddl.g:1:166: T__80
            pass 
            self.mT__80()


        elif alt10 == 28:
            # Pddl.g:1:172: T__81
            pass 
            self.mT__81()


        elif alt10 == 29:
            # Pddl.g:1:178: T__82
            pass 
            self.mT__82()


        elif alt10 == 30:
            # Pddl.g:1:184: T__83
            pass 
            self.mT__83()


        elif alt10 == 31:
            # Pddl.g:1:190: T__84
            pass 
            self.mT__84()


        elif alt10 == 32:
            # Pddl.g:1:196: T__85
            pass 
            self.mT__85()


        elif alt10 == 33:
            # Pddl.g:1:202: T__86
            pass 
            self.mT__86()


        elif alt10 == 34:
            # Pddl.g:1:208: T__87
            pass 
            self.mT__87()


        elif alt10 == 35:
            # Pddl.g:1:214: T__88
            pass 
            self.mT__88()


        elif alt10 == 36:
            # Pddl.g:1:220: T__89
            pass 
            self.mT__89()


        elif alt10 == 37:
            # Pddl.g:1:226: T__90
            pass 
            self.mT__90()


        elif alt10 == 38:
            # Pddl.g:1:232: T__91
            pass 
            self.mT__91()


        elif alt10 == 39:
            # Pddl.g:1:238: T__92
            pass 
            self.mT__92()


        elif alt10 == 40:
            # Pddl.g:1:244: T__93
            pass 
            self.mT__93()


        elif alt10 == 41:
            # Pddl.g:1:250: T__94
            pass 
            self.mT__94()


        elif alt10 == 42:
            # Pddl.g:1:256: T__95
            pass 
            self.mT__95()


        elif alt10 == 43:
            # Pddl.g:1:262: T__96
            pass 
            self.mT__96()


        elif alt10 == 44:
            # Pddl.g:1:268: T__97
            pass 
            self.mT__97()


        elif alt10 == 45:
            # Pddl.g:1:274: T__98
            pass 
            self.mT__98()


        elif alt10 == 46:
            # Pddl.g:1:280: T__99
            pass 
            self.mT__99()


        elif alt10 == 47:
            # Pddl.g:1:286: T__100
            pass 
            self.mT__100()


        elif alt10 == 48:
            # Pddl.g:1:293: T__101
            pass 
            self.mT__101()


        elif alt10 == 49:
            # Pddl.g:1:300: T__102
            pass 
            self.mT__102()


        elif alt10 == 50:
            # Pddl.g:1:307: T__103
            pass 
            self.mT__103()


        elif alt10 == 51:
            # Pddl.g:1:314: T__104
            pass 
            self.mT__104()


        elif alt10 == 52:
            # Pddl.g:1:321: T__105
            pass 
            self.mT__105()


        elif alt10 == 53:
            # Pddl.g:1:328: T__106
            pass 
            self.mT__106()


        elif alt10 == 54:
            # Pddl.g:1:335: T__107
            pass 
            self.mT__107()


        elif alt10 == 55:
            # Pddl.g:1:342: T__108
            pass 
            self.mT__108()


        elif alt10 == 56:
            # Pddl.g:1:349: T__109
            pass 
            self.mT__109()


        elif alt10 == 57:
            # Pddl.g:1:356: T__110
            pass 
            self.mT__110()


        elif alt10 == 58:
            # Pddl.g:1:363: T__111
            pass 
            self.mT__111()


        elif alt10 == 59:
            # Pddl.g:1:370: T__112
            pass 
            self.mT__112()


        elif alt10 == 60:
            # Pddl.g:1:377: T__113
            pass 
            self.mT__113()


        elif alt10 == 61:
            # Pddl.g:1:384: T__114
            pass 
            self.mT__114()


        elif alt10 == 62:
            # Pddl.g:1:391: T__115
            pass 
            self.mT__115()


        elif alt10 == 63:
            # Pddl.g:1:398: T__116
            pass 
            self.mT__116()


        elif alt10 == 64:
            # Pddl.g:1:405: T__117
            pass 
            self.mT__117()


        elif alt10 == 65:
            # Pddl.g:1:412: T__118
            pass 
            self.mT__118()


        elif alt10 == 66:
            # Pddl.g:1:419: T__119
            pass 
            self.mT__119()


        elif alt10 == 67:
            # Pddl.g:1:426: T__120
            pass 
            self.mT__120()


        elif alt10 == 68:
            # Pddl.g:1:433: REQUIRE_KEY
            pass 
            self.mREQUIRE_KEY()


        elif alt10 == 69:
            # Pddl.g:1:445: NAME
            pass 
            self.mNAME()


        elif alt10 == 70:
            # Pddl.g:1:450: VARIABLE
            pass 
            self.mVARIABLE()


        elif alt10 == 71:
            # Pddl.g:1:459: NUMBER
            pass 
            self.mNUMBER()


        elif alt10 == 72:
            # Pddl.g:1:466: LINE_COMMENT
            pass 
            self.mLINE_COMMENT()


        elif alt10 == 73:
            # Pddl.g:1:479: WHITESPACE
            pass 
            self.mWHITESPACE()







    # lookup tables for DFA #1

    DFA1_eot = DFA.unpack(
        u"\30\uffff"
        )

    DFA1_eof = DFA.unpack(
        u"\30\uffff"
        )

    DFA1_min = DFA.unpack(
        u"\1\72\1\141\1\uffff\1\151\1\uffff\1\145\1\161\2\uffff\1\157\12"
        u"\uffff\1\156\1\144\2\uffff"
        )

    DFA1_max = DFA.unpack(
        u"\1\72\1\165\1\uffff\1\171\1\uffff\1\165\1\170\2\uffff\1\157\12"
        u"\uffff\1\156\1\163\2\uffff"
        )

    DFA1_accept = DFA.unpack(
        u"\2\uffff\1\1\1\uffff\1\3\2\uffff\1\7\1\10\1\uffff\1\12\1\13\1\17"
        u"\1\2\1\16\1\4\1\14\1\15\1\5\1\6\2\uffff\1\11\1\20"
        )

    DFA1_special = DFA.unpack(
        u"\30\uffff"
        )

            
    DFA1_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\13\1\uffff\1\11\1\5\1\6\1\12\7\uffff\1\4\1\uffff"
        u"\1\14\1\10\1\uffff\1\2\1\3\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\17\uffff\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\21\3\uffff\1\17\13\uffff\1\20"),
        DFA.unpack(u"\1\22\6\uffff\1\23"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\24"),
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
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26\16\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #1

    class DFA1(DFA):
        pass


    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\2\uffff\1\31\3\uffff\11\31\3\uffff\1\102\1\104\2\uffff\3\31\4"
        u"\uffff\2\31\15\uffff\6\31\1\137\2\31\1\143\13\31\4\uffff\1\106"
        u"\1\uffff\7\31\12\uffff\2\31\1\177\1\31\1\u0081\1\u0082\1\31\1\uffff"
        u"\1\u0084\2\31\1\uffff\14\31\1\106\7\31\5\uffff\2\31\1\uffff\1\31"
        u"\2\uffff\1\31\1\uffff\2\31\1\u00a8\11\31\1\u00b2\1\31\1\106\7\31"
        u"\7\uffff\6\31\1\uffff\1\u00c6\5\31\1\u00cc\2\31\1\uffff\1\31\1"
        u"\106\4\31\1\u00d6\1\31\1\u00d8\4\uffff\1\u00de\1\u00df\1\u00e0"
        u"\1\31\1\u00e3\1\u00e4\1\uffff\2\31\1\u00e7\2\31\1\uffff\2\31\1"
        u"\u00ed\1\106\5\31\1\uffff\1\31\11\uffff\2\31\2\uffff\2\31\1\uffff"
        u"\1\31\1\u00ff\3\31\1\uffff\1\106\5\31\1\u0109\4\uffff\1\u010d\2"
        u"\31\1\u0110\2\31\1\uffff\1\u0113\1\31\1\u0116\1\106\1\u0118\1\u0119"
        u"\3\31\5\uffff\2\31\1\uffff\2\31\1\uffff\2\31\1\uffff\1\u0127\2"
        u"\uffff\3\31\1\uffff\1\u012c\1\uffff\3\31\1\u0131\1\u0132\2\31\1"
        u"\uffff\1\u0135\1\31\1\u0137\3\uffff\2\31\1\u013c\2\uffff\2\31\1"
        u"\uffff\1\u013f\3\uffff\1\u0142\1\31\1\uffff\2\31\4\uffff\1\u0147"
        u"\2\31\2\uffff\1\u014b\1\31\2\uffff\1\u014e\1\u014f\2\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\u0150\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\11\1\uffff\1\145\1\uffff\1\141\1\uffff\1\151\1\157\1\154\1\162"
        u"\1\155\1\157\1\162\1\143\1\150\3\uffff\2\75\1\uffff\1\101\1\141"
        u"\2\157\4\uffff\1\143\1\155\1\uffff\1\151\1\154\1\157\1\141\1\143"
        u"\1\146\1\145\5\uffff\1\164\1\151\1\144\1\155\1\164\1\144\1\55\1"
        u"\154\1\163\1\55\1\145\1\160\1\143\1\55\1\162\1\145\2\141\1\155"
        u"\1\145\1\164\4\uffff\1\165\1\uffff\1\156\1\170\1\164\1\154\1\151"
        u"\1\162\1\141\1\160\1\uffff\1\156\1\145\3\uffff\2\162\1\uffff\1"
        u"\150\1\163\1\55\1\142\2\55\1\155\1\uffff\1\55\1\141\1\151\1\uffff"
        u"\1\162\1\154\1\162\1\166\1\141\1\146\1\142\1\162\1\154\1\145\1"
        u"\156\1\150\1\162\2\151\1\141\1\144\1\156\1\145\1\151\1\145\1\144"
        u"\1\143\1\141\1\151\1\145\1\164\1\uffff\1\145\2\uffff\1\157\1\uffff"
        u"\1\171\1\147\1\55\1\171\1\145\1\151\1\154\1\145\1\154\1\164\1\145"
        u"\1\164\1\55\1\151\1\141\2\155\1\154\1\55\1\145\1\141\1\156\1\uffff"
        u"\1\164\1\151\2\uffff\1\164\1\166\1\162\1\163\1\162\2\163\1\156"
        u"\1\uffff\1\55\1\141\1\157\1\154\1\162\1\145\2\55\1\151\1\uffff"
        u"\1\156\1\164\2\151\1\55\1\141\1\55\1\163\1\55\1\141\1\164\1\151"
        u"\1\145\3\55\1\164\2\55\1\uffff\1\163\1\154\1\55\1\145\1\155\1\uffff"
        u"\1\144\1\155\1\55\1\151\2\172\1\164\1\165\1\146\1\uffff\1\145\2"
        u"\uffff\1\141\1\151\1\157\1\144\3\uffff\1\55\1\167\2\uffff\1\145"
        u"\1\141\1\uffff\1\156\1\55\1\160\1\157\1\145\1\uffff\1\157\2\145"
        u"\1\151\1\162\1\164\1\55\1\151\1\157\1\145\1\uffff\1\55\1\157\1"
        u"\151\1\55\1\164\1\143\1\uffff\1\55\1\167\1\55\1\156\2\55\1\155"
        u"\1\151\1\145\1\uffff\2\156\1\55\1\uffff\1\156\1\164\1\uffff\2\145"
        u"\1\uffff\1\156\1\141\1\uffff\1\55\2\uffff\1\145\1\156\1\162\1\164"
        u"\2\141\1\143\1\150\1\144\2\55\1\146\1\145\1\uffff\1\55\1\147\1"
        u"\55\1\163\1\uffff\1\143\1\145\1\151\1\55\2\uffff\1\164\1\146\1"
        u"\uffff\1\55\2\uffff\1\164\1\55\1\156\1\uffff\1\145\1\157\2\uffff"
        u"\1\151\1\uffff\1\55\2\162\1\157\1\uffff\1\55\1\145\1\156\1\uffff"
        u"\1\55\1\163\2\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\172\1\uffff\1\157\1\uffff\1\165\1\uffff\1\170\1\165\1\164\1"
        u"\166\1\163\1\157\1\162\1\164\1\151\3\uffff\2\75\1\uffff\1\172\1"
        u"\151\2\157\4\uffff\1\146\1\155\1\uffff\1\171\1\165\1\157\1\162"
        u"\1\144\1\170\1\165\5\uffff\1\164\1\151\1\144\1\155\1\164\1\144"
        u"\1\172\1\167\1\163\1\172\1\145\1\160\1\143\1\55\1\162\1\157\2\141"
        u"\1\155\1\145\1\164\4\uffff\1\165\1\uffff\1\156\1\170\1\164\1\154"
        u"\1\151\1\162\1\141\1\160\1\uffff\1\156\1\145\3\uffff\2\162\1\uffff"
        u"\1\150\1\163\1\172\1\142\2\172\1\155\1\uffff\1\172\1\141\1\151"
        u"\1\uffff\1\162\1\154\1\162\1\166\1\141\1\146\1\142\1\162\1\154"
        u"\1\145\1\156\1\150\1\162\2\151\1\141\1\144\1\156\1\145\2\151\1"
        u"\163\1\146\1\141\1\151\1\145\1\164\1\uffff\1\145\2\uffff\1\157"
        u"\1\uffff\1\171\1\147\1\172\1\171\1\145\1\151\1\154\1\145\1\154"
        u"\1\164\1\145\1\164\1\172\1\151\1\141\2\155\1\154\1\55\1\145\1\141"
        u"\1\156\1\uffff\1\164\1\151\2\uffff\1\164\1\166\1\162\1\163\1\162"
        u"\2\163\1\156\1\uffff\1\172\1\141\1\157\1\154\1\162\1\145\1\172"
        u"\1\55\1\151\1\uffff\1\156\1\164\2\151\1\55\1\144\1\172\1\163\1"
        u"\172\1\162\1\164\1\151\1\145\3\172\1\164\2\172\1\uffff\1\163\1"
        u"\154\1\172\1\145\1\155\1\uffff\1\165\1\155\1\172\1\151\2\172\1"
        u"\164\1\165\1\146\1\uffff\1\145\2\uffff\1\141\1\151\1\166\1\144"
        u"\3\uffff\1\55\1\167\2\uffff\1\145\1\141\1\uffff\1\156\1\172\1\160"
        u"\1\157\1\145\1\uffff\1\157\2\145\1\151\1\162\1\164\1\172\1\151"
        u"\1\157\1\145\1\uffff\1\55\1\157\1\151\1\172\1\164\1\143\1\uffff"
        u"\1\172\1\167\1\172\1\156\2\172\1\155\1\151\1\145\1\uffff\2\156"
        u"\1\55\1\uffff\1\156\1\164\1\uffff\2\145\1\uffff\1\156\1\142\1\uffff"
        u"\1\172\2\uffff\1\145\1\156\1\162\1\164\2\141\1\143\1\150\1\144"
        u"\2\172\1\146\1\145\1\uffff\1\172\1\147\1\172\1\163\1\uffff\1\143"
        u"\1\145\1\151\1\172\2\uffff\1\164\1\146\1\uffff\1\172\2\uffff\1"
        u"\164\1\172\1\156\1\uffff\1\145\1\157\2\uffff\1\151\1\uffff\1\172"
        u"\2\162\1\157\1\uffff\1\172\1\145\1\156\1\uffff\1\172\1\163\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\uffff\1\7\11\uffff\1\43\1\44\1\45\2"
        u"\uffff\1\50\4\uffff\1\105\1\107\1\110\1\111\2\uffff\1\5\7\uffff"
        u"\1\63\1\64\1\65\1\66\1\104\25\uffff\1\51\1\46\1\52\1\47\1\uffff"
        u"\1\106\10\uffff\1\11\2\uffff\1\17\1\16\1\21\2\uffff\1\62\7\uffff"
        u"\1\34\3\uffff\1\23\33\uffff\1\37\1\uffff\1\24\1\22\1\uffff\1\40"
        u"\26\uffff\1\6\2\uffff\1\14\1\20\10\uffff\1\35\11\uffff\1\42\23"
        u"\uffff\1\25\5\uffff\1\36\11\uffff\1\2\1\uffff\1\4\1\13\4\uffff"
        u"\1\10\1\26\1\12\2\uffff\1\73\1\53\2\uffff\1\27\5\uffff\1\75\12"
        u"\uffff\1\31\6\uffff\1\61\11\uffff\1\57\3\uffff\1\41\2\uffff\1\56"
        u"\2\uffff\1\54\2\uffff\1\74\1\uffff\1\67\1\70\15\uffff\1\60\4\uffff"
        u"\1\32\4\uffff\1\33\1\55\2\uffff\1\71\1\uffff\1\103\1\15\3\uffff"
        u"\1\72\2\uffff\1\102\1\15\1\uffff\1\76\4\uffff\1\101\3\uffff\1\77"
        u"\2\uffff\1\100\1\30"
        )

    DFA10_special = DFA.unpack(
        u"\u0150\uffff"
        )

            
    DFA10_transition = [
        DFA.unpack(u"\2\34\2\uffff\1\34\22\uffff\1\34\7\uffff\1\1\1\3\1\17"
        u"\1\20\1\uffff\1\5\1\uffff\1\21\12\32\1\4\1\33\1\23\1\24\1\22\1"
        u"\25\1\uffff\32\31\6\uffff\1\10\2\31\1\2\1\6\1\13\1\31\1\30\1\12"
        u"\3\31\1\26\1\7\1\11\1\14\2\31\1\15\1\27\2\31\1\16\3\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\35\11\uffff\1\36"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44\1\uffff\1\42\1\46\1\45\1\41\1\51\1\uffff\1\50"
        u"\3\uffff\1\52\1\53\1\47\1\43\1\53\1\37\1\53\1\40\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54\4\uffff\1\56\11\uffff\1\55"),
        DFA.unpack(u"\1\60\5\uffff\1\57"),
        DFA.unpack(u"\1\63\1\uffff\1\61\4\uffff\1\64\1\62"),
        DFA.unpack(u"\1\65\3\uffff\1\66"),
        DFA.unpack(u"\1\67\1\70\4\uffff\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\75\13\uffff\1\76\4\uffff\1\74"),
        DFA.unpack(u"\1\77\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u"\32\106\6\uffff\3\106\1\105\26\106"),
        DFA.unpack(u"\1\110\7\uffff\1\107"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\114\2\uffff\1\113"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53\17\uffff\1\116"),
        DFA.unpack(u"\1\53\10\uffff\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\122\20\uffff\1\121"),
        DFA.unpack(u"\1\123\1\53"),
        DFA.unpack(u"\1\124\12\uffff\1\53\6\uffff\1\53"),
        DFA.unpack(u"\1\126\3\uffff\1\53\5\uffff\1\127\5\uffff\1\125"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\140\12\uffff\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\151\11\uffff\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b\3\uffff\1\53"),
        DFA.unpack(u"\1\u009d\16\uffff\1\u009c"),
        DFA.unpack(u"\1\u009f\1\u009e\1\uffff\1\53"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\1\u00c5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d5\2\uffff\1\u00d4"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00d9\20\uffff\1\u00da"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\u00e2\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1"
        u"\uffff\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u"\1\u00e9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00eb\20\uffff\1\u00ea"),
        DFA.unpack(u"\1\u00ec"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u00ee"),
        DFA.unpack(u"\1\u00ef"),
        DFA.unpack(u"\1\u00f0"),
        DFA.unpack(u"\1\u00f1"),
        DFA.unpack(u"\1\u00f2"),
        DFA.unpack(u"\1\u00f3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f5"),
        DFA.unpack(u"\1\u00f6"),
        DFA.unpack(u"\1\u00f8\6\uffff\1\u00f7"),
        DFA.unpack(u"\1\u00f9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fa"),
        DFA.unpack(u"\1\u00fb"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fc"),
        DFA.unpack(u"\1\u00fd"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fe"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u"\1\u0101"),
        DFA.unpack(u"\1\u0102"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\1\u0105"),
        DFA.unpack(u"\1\u0106"),
        DFA.unpack(u"\1\u0107"),
        DFA.unpack(u"\1\u0108"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u010a"),
        DFA.unpack(u"\1\u010b"),
        DFA.unpack(u"\1\u010c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\u010e"),
        DFA.unpack(u"\1\u010f"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0111"),
        DFA.unpack(u"\1\u0112"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0114"),
        DFA.unpack(u"\1\u0115\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1"
        u"\uffff\32\31"),
        DFA.unpack(u"\1\u0117"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\1\u011b"),
        DFA.unpack(u"\1\u011c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u011d"),
        DFA.unpack(u"\1\u011e"),
        DFA.unpack(u"\1\u011f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0120"),
        DFA.unpack(u"\1\u0121"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0122"),
        DFA.unpack(u"\1\u0123"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0124"),
        DFA.unpack(u"\1\u0125\1\u0126"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\106\2\uffff\12\106\7\uffff\32\106\4\uffff\1\106"
        u"\1\uffff\32\106"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0128"),
        DFA.unpack(u"\1\u0129"),
        DFA.unpack(u"\1\u012a"),
        DFA.unpack(u"\1\u012b"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\u012d"),
        DFA.unpack(u"\1\u012e"),
        DFA.unpack(u"\1\u012f"),
        DFA.unpack(u"\1\u0130"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0133"),
        DFA.unpack(u"\1\u0134"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0136"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0138"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0139"),
        DFA.unpack(u"\1\u013a"),
        DFA.unpack(u"\1\u013b"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u013d"),
        DFA.unpack(u"\1\u013e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0141"),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0143"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0144"),
        DFA.unpack(u"\1\u0145"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0146"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u0148"),
        DFA.unpack(u"\1\u0149"),
        DFA.unpack(u"\1\u014a"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\u014c"),
        DFA.unpack(u"\1\u014d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\31\2\uffff\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff"
        u"\32\31"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(PddlLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
