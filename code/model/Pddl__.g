lexer grammar Pddl;
options {
  language=C;

}

T54 : '(' ;
T55 : 'define' ;
T56 : ')' ;
T57 : 'domain' ;
T58 : ':requirements' ;
T59 : ':types' ;
T60 : '-' ;
T61 : 'either' ;
T62 : ':functions' ;
T63 : 'number' ;
T64 : ':constants' ;
T65 : ':predicates' ;
T66 : ':constraints' ;
T67 : ':action' ;
T68 : ':parameters' ;
T69 : ':precondition' ;
T70 : ':effect' ;
T71 : 'and' ;
T72 : 'or' ;
T73 : 'not' ;
T74 : 'imply' ;
T75 : 'exists' ;
T76 : 'forall' ;
T77 : ':durative-action' ;
T78 : ':duration' ;
T79 : ':condition' ;
T80 : 'preference' ;
T81 : 'at' ;
T82 : 'over' ;
T83 : 'start' ;
T84 : 'end' ;
T85 : 'all' ;
T86 : ':derived' ;
T87 : 'when' ;
T88 : '*' ;
T89 : '+' ;
T90 : '/' ;
T91 : '>' ;
T92 : '<' ;
T93 : '=' ;
T94 : '>=' ;
T95 : '<=' ;
T96 : 'assign' ;
T97 : 'scale-up' ;
T98 : 'scale-down' ;
T99 : 'increase' ;
T100 : 'decrease' ;
T101 : '?duration' ;
T102 : 'problem' ;
T103 : ':domain' ;
T104 : ':objects' ;
T105 : ':init' ;
T106 : ':goal' ;
T107 : ':metric' ;
T108 : 'minimize' ;
T109 : 'maximize' ;
T110 : 'total-time' ;
T111 : 'is-violated' ;
T112 : 'always' ;
T113 : 'sometime' ;
T114 : 'within' ;
T115 : 'at-most-once' ;
T116 : 'sometime-after' ;
T117 : 'sometime-before' ;
T118 : 'always-within' ;
T119 : 'hold-during' ;
T120 : 'hold-after' ;

// $ANTLR src "Pddl.g" 506
/************* LEXER ****************************/


REQUIRE_KEY
    : ':strips'
    | ':typing'
    | ':negative-preconditions'
    | ':disjunctive-preconditions'
    | ':equality'
    | ':existential-preconditions'
    | ':universal-preconditions'
    | ':quantified-preconditions'
    | ':conditional-effects'
    | ':fluents'
    | ':adl'
    | ':durative-actions'
    | ':derived-predicates'
    | ':timed-initial-literals'
    | ':preferences'
    | ':constraints'
    ;


// $ANTLR src "Pddl.g" 529
NAME:    LETTER ANY_CHAR* ;

// $ANTLR src "Pddl.g" 531
fragment LETTER:	'a'..'z' | 'A'..'Z';

// $ANTLR src "Pddl.g" 533
fragment ANY_CHAR: LETTER | '0'..'9' | '-' | '_';

// $ANTLR src "Pddl.g" 535
VARIABLE : '?' LETTER ANY_CHAR* ;

// $ANTLR src "Pddl.g" 537
NUMBER : DIGIT+ ('.' DIGIT+)? ;

// $ANTLR src "Pddl.g" 539
fragment DIGIT: '0'..'9';

// $ANTLR src "Pddl.g" 541
LINE_COMMENT
    : ';' ~('\n'|'\r')* '\r'? '\n' { $channel = HIDDEN; }
    ;

// $ANTLR src "Pddl.g" 545
WHITESPACE
    :   (   ' '
        |   '\t'
        |   '\r'
        |   '\n'
        )+
        { $channel = HIDDEN; }
    ;
