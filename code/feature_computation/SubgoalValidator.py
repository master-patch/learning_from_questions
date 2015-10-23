#!/usr/bin/python
import os;

#
def construct_command (_sPathToFF, _sTimelimit, _sDomainFile, _sProblemFile, bOptimize):
	sOptimize = ' -O ' if bOptimize else '';
	sMainCommand = _sPathToFF + sOptimize + ' -o ' + _sDomainFile + ' -f ' + _sProblemFile + ' & \n';
	print "Running:", sMainCommand;

	sCommand = 'runtime=' + _sTimelimit + ' ;\n' +\
	    sMainCommand + \
				'cpid=$! ;\n' +\
				'trap \'kill -9 $cpid; exit 1\' 1 2 9 15 ;\n' +\
				'for x in `seq $runtime`; do \n' +\
					'sleep 1 ;\n' +\
					'kill -0 $cpid > /dev/null  2>&1;\n' +\
					'if [ $? -eq 1 ]; then \n' +\
						'break;\n' +\
					'fi;\n' +\
				'done;\n' +\
				'kill -0 $cpid > /dev/null  2>&1;\n' +\
				'if [ $? -eq 0 ]; then\n' +\
					'kill -9 $cpid ;\n' +\
					'echo "[killed planner on timeout]" ;\n' +\
				'fi; \n'

	return sCommand


def GenerateProblemFile (sProblemPddl, sGoalPredicate, sOutputProblemPath):

    sGoalSection = '(:goal\n%s\n)\n)' % sGoalPredicate;
    iPos = sProblemPddl.find('(:goal');
    if iPos == -1:
        assert(sProblemPddl.endswith(')')), 'Invalid Problem Pddl';
        iPos = len(sProblemPddl) - 1;
    sProblemPddl = sProblemPddl[:iPos] + sGoalSection;

    fout = open(sOutputProblemPath, 'w');
    fout.write(sProblemPddl);
    fout.close();

def RunMetricFF (sDomainPath, sProblemPath, sFFPath, sNextPlanPath, bOptimize, iLimitSecs):

    #print '\tRunning FF to get plan...';

    #sCmd = '%s -o %s -f %s' % (sFFPath, sDomainPath, sProblemPath);
    #print '\t%s' % sCmd;
    sCmd = construct_command (sFFPath, str(iLimitSecs), sDomainPath, sProblemPath, bOptimize);
    pipe = os.popen(sCmd);
    lstResponse = pipe.readlines();
    sResponse = ''.join(lstResponse);
    pipe.close();

    fout = open(sNextPlanPath, 'w');
    fout.write(sResponse);
    fout.close();

    #print '\tDone.';

def ComputeEndState (sDomainPath, sProblemPath, sPlanPath, sMainPath):

    #print '\tRunning lhla exe to get end state...';

    sCmd = '%s test_domain=%s test_problem=%s test_plan=%s' % (sMainPath, sDomainPath, sProblemPath, sPlanPath);
    pipe = os.popen(sCmd);
    sNextPddl = pipe.read();
    sNextPddl = sNextPddl.strip();
    pipe.close();

    return sNextPddl;

def TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath, bOptimize, 
		  iLimitSecs = 60):

    print '';

    fin = open(sProblemPath);
    sProblemPddl = fin.read();
    fin.close();

    iSubgoals = len(lstSubgoals);
    for i in range(0,iSubgoals):
        sGoalPredicate = lstSubgoals[i];
        sGoalPredicate = sGoalPredicate.strip();
        if not sGoalPredicate.startswith('('):
            sGoalPredicate = '(' + sGoalPredicate + ')';

        sNextProblemPath = '%s.%d.pddl' % (sTempProblemPath, i);
        sNextPlanPath = '%s.%d.plan' % (sTempProblemPath, i);

        print ' %s' % sGoalPredicate;
        GenerateProblemFile(sProblemPddl, sGoalPredicate, sNextProblemPath);
        RunMetricFF(sDomainPath, sNextProblemPath, sFFPath, sNextPlanPath, bOptimize, iLimitSecs);
        sProblemPddl = ComputeEndState(sDomainPath, sNextProblemPath, sNextPlanPath, sMainPath);

        if len(sProblemPddl) == 0:
            print ' Failed to achieve subgoal!';
            return False;

    return True;


def test2():
    sDomainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/data/domain-no-stone-iron-tools-simple-furnace.v120.pddl';
    sFFPath = '/home/nkushman/hierarchical_planning/ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/lhla_v24 /home/nkushman/hierarchical_planning/model/subgoal_learning/run_compute_end_state.cfg';

    sProblemPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources-rand2/shears.72.pddl'
    #sProblemPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources-rand2/shears.73.pddl'
    lstSubgoals = [                                 \
                    '(> (thing-available wood) 0)', \
                    '(> (thing-available plank) 3)', \
                    '(> (thing-available stick) 3)', \
                    '(> (thing-available wood-pickaxe) 2)', \
                    '(> (thing-available ironore) 5)', \
                    '(> (thing-available iron) 3)', \
                    '(> (thing-available shears) 0)' ];
    sTempProblemPath = '/home/nkushman/hierarchical_planning/model/pddl_features/tmp/test.shears.73.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath, bOptimize = False, iLimitSecs = 120);


def test():
    sDomainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/data/domain.v120.pddl';
    sFFPath = '/home/nkushman/hierarchical_planning/ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/lhla_v4 /home/nkushman/hierarchical_planning/model/subgoal_learning/run_compute_end_state.cfg';

    sProblemPath = 'data/problems/harvest-all1step/wood-door.4.pddl';
    lstSubgoals = [                                 \
                    #'(> (thing-available wood) 0)',\
                    '(> (thing-available wood) 1)', \
                    '(> (thing-available plank) 5)', \
                    '(> (thing-available wood-door) 0)' ];
    sTempProblemPath = '/home/nkushman/hierarchical_planning/model/pddl_features/tmp/test.wood-door.4.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);


    sProblemPath = 'data/problems/harvest-all1step/stone-axe.55.pddl';
    lstSubgoals = [                                 \
                    #'(> (thing-available wood) 0)', \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    '(> (thing-available stone-axe) 0)' ];
    sTempProblemPath = 'data/stone-axe.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/furnace.28.pddl';
    lstSubgoals = [                                 \
                    '(> (thing-available wood) 0)', \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #   '(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    '(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    #'(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    #'(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)' ];
    sTempProblemPath = '/home/nkushman/hierarchical_planning/model/pddl_features/tmp/test.furnace.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/coal.8.pddl';
    lstSubgoals = [                                 \
            #'(> (thing-available wood) 0)', \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available coal) 0)' ];
    sTempProblemPath = '/home/nkushman/hierarchical_planning/model/pddl_features/tmp/test.coal.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/torch.51.pddl';
    lstSubgoals = [                                 \
            #'(> (thing-available wood) 0)', \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available torch) 0)' ];
    sTempProblemPath = 'data/torch.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);


if __name__=='__main__':
    test2();

