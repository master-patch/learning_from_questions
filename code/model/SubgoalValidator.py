import os;

#
def construct_command (_sPathToFF, _sTimelimit, _sDomainFile, _sProblemFile):
	sCommand = 'runtime=' + _sTimelimit + ' ;\n' +\
				_sPathToFF + ' -o ' + _sDomainFile + ' -f ' + _sProblemFile + ' & \n' +\
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

def RunMetricFF (sDomainPath, sProblemPath, sFFPath, sNextPlanPath):

    #print '\tRunning FF to get plan...';

    #sCmd = '%s -o %s -f %s' % (sFFPath, sDomainPath, sProblemPath);
    #print '\t%s' % sCmd;
    sCmd = construct_command (sFFPath, '60', sDomainPath, sProblemPath);
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

def TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath):


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
        RunMetricFF(sDomainPath, sNextProblemPath, sFFPath, sNextPlanPath);
        sProblemPddl = ComputeEndState(sDomainPath, sNextProblemPath, sNextPlanPath, sMainPath);

        if len(sProblemPddl) == 0:
            print ' Failed to achieve subgoal!';
            return False;

    return True;


def test():
    sDomainPath = 'data/domain.v120.pddl';
    sFFPath = '../../ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = './lhla_v3 ./run_compute_end_state.cfg';

    sProblemPath = 'data/problems/harvest-all1step/wood-door.4.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood) 1)', \
                    '(> (thing-available plank) 5)', \
                    '(> (thing-available wood-door) 0)' ];
    sTempProblemPath = 'data/wood-door.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);


    sProblemPath = 'data/problems/harvest-all1step/stone-shovel.57.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone-shovel) 0)' ];
    sTempProblemPath = 'data/stone-shovel.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/furnace.28.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
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
    sTempProblemPath = 'data/furnace.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);
#
    sProblemPath = 'data/problems/harvest-all1step/coal.8.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available coal) 0)' ];
    sTempProblemPath = 'data/coal.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/torch.51.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available torch) 0)' ];
    sTempProblemPath = 'data/torch.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/sugar.25.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-axe) 0)', \
                    '(> (thing-available sugar) 0)' ];
    sTempProblemPath = 'data/torch.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/clayblock.14.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available clay) 3)', \
                    '(> (thing-available clayblock) 0)' ];
    sTempProblemPath = 'data/clayblock.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/fence.19.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available stick) 5)', \
                    '(> (thing-available fence) 0)' ];
    sTempProblemPath = 'data/fence.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/ladder.20.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available stick) 6)', \
                    '(> (thing-available ladder) 0)' ];
    sTempProblemPath = 'data/ladder.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/paper.26.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-axe) 0)', \
                    '(> (thing-available cut-sugarcane) 2)', \
                    '(> (thing-available paper) 0)' ];
    sTempProblemPath = 'data/paper.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/claybrick.15.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #   '(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    '(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    #'(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    #'(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available clay) 0)', \
                    '(> (thing-available claybrick) 0)'\
                    ];
    sTempProblemPath = 'data/claybrick.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/bucket.24.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    # '(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 2)', \
                    '(> (thing-available bucket) 0)'\
                    ];
    sTempProblemPath = 'data/bucket.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/stone-axe.55.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone) 2)', \
                    '(> (thing-available stone-axe) 0)' ];
    sTempProblemPath = 'data/stone-axe.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/stone-hoe.56.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone) 1)', \
                    '(> (thing-available stone-hoe) 0)' ];
    sTempProblemPath = 'data/stone-hoe.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);


    sProblemPath = 'data/problems/harvest-all1step/sandstone.38.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available sandstone) 0)' ];
    sTempProblemPath = 'data/sandstone.38.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/wool.7.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    # '(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)', \
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available wool) 0)'\
                    ];
    sTempProblemPath = 'data/wool.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);
#

    sProblemPath = 'data/problems/harvest-all1step/wood-stairs.47.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood) 1)', \
                    '(> (thing-available plank) 5)', \
                    '(> (thing-available wood-stairs) 0)' ];
    sTempProblemPath = 'data/wood-stairs.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/milk.22.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 2)', \
                    '(> (thing-available bucket) 0)', \
                    '(> (thing-available milk) 0)' \
                    ];
    sTempProblemPath = 'data/milk.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/irondoor.46.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available ironore) 5)', \
                    '(> (thing-available iron) 5)', \
                    '(> (thing-available iron-door) 0)' \
                    ];
    sTempProblemPath = 'data/irondoor.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/bed.49.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)', \
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available wool) 2)', \
                    '(> (thing-available bed) 0)' \
                    ];
    sTempProblemPath = 'data/bed.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/iron.18.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 0)'\
                    ];
    sTempProblemPath = 'data/iron.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/cookedfish.31.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)',\
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available string) 2)', \
                    '(> (thing-available fishingrod) 0)', \
                    '(> (thing-available fish) 0)', \
                    '(> (thing-available cookedfish) 0)' \
                    ];
    sTempProblemPath = 'data/cookedfish.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/fishingrod.30.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)',\
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available string) 2)', \
                    '(> (thing-available fishingrod) 0)' \
                    ];
    sTempProblemPath = 'data/fishingrod.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/brick.44.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available wood-shovel) 0)',\
                    '(> (thing-available clay) 3)', \
                    '(> (thing-available claybrick) 3)', \
                    '(> (thing-available brick) 0)' \
                    ];
    sTempProblemPath = 'data/brick.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/glasspane.32.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    '(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available wood-shovel) 0)',\
                    '(> (thing-available sand) 5)', \
                    '(> (thing-available glass) 5)', \
                    '(> (thing-available glasspane) 0)' \
                    ];
    sTempProblemPath = 'data/glasspane.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/glass.16.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available wood-shovel) 0)',\
                    '(> (thing-available sand) 0)', \
                    '(> (thing-available glass) 0)' \
                    ];
    sTempProblemPath = 'data/glass.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/string.17.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)',\
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available string) 0)' \
                    ];
    sTempProblemPath = 'data/string.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/shears.52.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)',\
                    '(> (thing-available shears) 0)'\
                    ];
    sTempProblemPath = 'data/shears.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/stonebrick.43.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    '(> (thing-available stone) 3)', \
                    '(> (thing-available stonebrick) 0)'\
                    ];
    sTempProblemPath = 'data/stonebrick.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/stone-stairs.48.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone-stairs) 0)'\
                    ];
    sTempProblemPath = 'data/stone-stairs.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/fish.29.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available coal) 0)', \
                    '(> (furnace-fuel) 3)', \
                    '(> (thing-available iron) 1)',\
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available string) 2)', \
                    '(> (thing-available wood) 0)', \
                    '(> (thing-available stick) 2)', \
                    '(> (thing-available fishingrod) 0)', \
                    '(> (thing-available fish) 0)' \
                    ];
    sTempProblemPath = 'data/fish.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/stone-pickaxe.53.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    '(> (thing-available stone) 2)', \
                    '(> (thing-available stone-pickaxe) 0)'\
                    ];
    sTempProblemPath = 'data/stone-pickaxe.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/ironbar.45.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    #'(> (thing-available stone) 0)', \
                    #'(> (thing-available stone) 1)', \
                    #'(> (thing-available stone) 2)', \
                    #'(> (thing-available stone) 3)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available ironore) 5)', \
                    '(> (thing-available iron) 5)', \
                    '(> (thing-available ironbar) 0)' \
                    ];
    sTempProblemPath = 'data/ironbar.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/seeds.35.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)', \
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available bone) 0)', \
                    '(> (thing-available bonemeal) 0)', \
                    '(> (thing-available seeds) 0)' \
                    ];
    sTempProblemPath = 'data/seeds.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/wheat.36.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)', \
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available bone) 0)', \
                    '(> (thing-available bonemeal) 0)', \
                    '(> (thing-available seeds) 0)',\
                    '(> (thing-available wood-hoe) 0)', \
                    '(> (thing-available wheat) 0)' \
                    ];
    sTempProblemPath = 'data/wheat.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);

    sProblemPath = 'data/problems/harvest-all1step/bread.50.pddl';
    print sProblemPath;
    lstSubgoals = [                                 \
                    '(> (thing-available wood-pickaxe) 0)', \
                    '(> (thing-available stone) 4)', \
                    '(> (thing-available stone) 5)', \
                    '(> (thing-available stone) 6)', \
                    '(> (thing-available stone) 7)', \
                    '(> (thing-available furnace) 0)',\
                    '(> (thing-available iron) 1)', \
                    '(> (thing-available shears) 0)', \
                    '(> (thing-available bone) 0)', \
                    '(> (thing-available bonemeal) 0)', \
                    '(> (thing-available seeds) 0)',\
                    '(> (thing-available wood-hoe) 0)', \
                    '(> (thing-available wheat) 2)', \
                    '(> (thing-available bread) 0)' \
                    ];
    sTempProblemPath = 'data/bread.subgoals';
    print TestSubgoals (sDomainPath, sProblemPath, lstSubgoals, sFFPath, sMainPath, sTempProblemPath);


if __name__=='__main__':
    test();

