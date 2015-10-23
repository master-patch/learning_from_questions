
import os;
import sys;

def GenerateTestProblem(pddl, pred):
    parts = pred.split('|');
    assert(len(parts)==3);

    goal = '(' + parts[2] + ')';
    if parts[1]=='1':
        goal = '(> ' + goal + ' 0)';

    testProblem = pddl.replace('[GOAL_PREDICATE]', goal);

    return testProblem;

def ReadPddlFile(inputFile):

    fin = open(inputFile);
    line = fin.read();
    fin.close();

    return line;

def ReadPredicateDict(inputFile):

    fin = open(inputFile);
    lines = fin.readlines();
    fin.close();

    return lines;

def CheckPredicatePlan(_sPlan):

    if _sPlan.find('ff: found legal plan as follows') != -1:
        return (True, '');
    elif _sPlan.find('ff: goal can be simplified to true.') != -1:
        return (False, '');
    elif _sPlan.find('[killed planner on timeout]') != -1:
        return (True, '');
    elif _sPlan.find('ff: goal can be simplified to false.') != -1:
        return (False, '');
    elif _sPlan.find('ff: goal accesses a fluent that will never have a defined value.') != -1:
        return (False, '');
    elif 'problem unsolvable' in _sPlan:
        return (False, '');
    elif 'undefined fluent' in _sPlan:
        return (False, '');
    elif _sPlan.find('unknown constant') != -1:
        return (False, '');

    return (False, '[UNKNOWN PLAN OUTCOME]\n' + _sPlan);

