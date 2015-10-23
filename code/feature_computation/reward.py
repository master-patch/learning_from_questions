import collections;

import sys
import data;
import config
import predicate

def LoadRewardsDict():
    sFileRewards = config.get_string('REWARDS_FILE');
    dConnRewardsIndexes = collections.defaultdict(lambda:{'iNumNeg':0, 'iNumPos':0});
    iMaxIter = config.get_int('REWARDS_MAX_ITER');
    iMinIter = config.get_int('REWARDS_MIN_ITER');
    iCurIter = 0;
    for sLine in open(sFileRewards):
        sLine = sLine.strip();
        lConns = sLine.split();
        if len(lConns) > 5:
            iCurIter += 1;
            if iCurIter > iMaxIter:
                break;
            if iCurIter < iMinIter:
                continue;
        for sConn in lConns:
            iFrom, iTo, iNumPos, iNumNeg = sConn.split(':');
            iNumPos = int(iNumPos);
            iNumNeg = int(iNumNeg);
            iFrom = int(iFrom);
            iTo = int(iTo);
            dConnRewardsIndexes[(iFrom,iTo)]['iNumNeg'] += iNumNeg; 
            dConnRewardsIndexes[(iFrom,iTo)]['iNumPos'] += iNumPos; 
    dIndexToPredList = predicate.PredDictFileToPredListDict(config.get_string('PRED_DICT_FILE'), lambda x:x.iIndex);
    dConnRewardsStrings = collections.defaultdict(lambda:{'iNumNeg':0, 'iNumPos':0});
    for (iFrom, iTo), dPosNeg in dConnRewardsIndexes.items():
        sFrom = dIndexToPredList[iFrom][0].GetObject();
        sTo = dIndexToPredList[iTo][0].GetObject();
        dConnRewardsStrings[(sFrom, sTo)]['iNumNeg'] += dPosNeg['iNumNeg'];
        dConnRewardsStrings[(sFrom, sTo)]['iNumPos'] += dPosNeg['iNumPos'];
    return dConnRewardsStrings;


class SubgoalResult:
    PLAN_FOUND = 1;
    TRIVIAL_GOAL = 2;
    UNSOLVABLE = 3;
    TIMEOUT = 4;
    SYNTAX_ERROR = 5;
    FF_CODE_CHANGE = 6;
    OUTSIDE_KNOWN_WORLD = 7;
    UNKNOWN = 8;
    
    def __init__(self, sResult, bAllowUnknown):
        if sResult == 'plan-found':
            self.result = SubgoalResult.PLAN_FOUND;
        elif sResult == 'trivial-goal':
            self.result = SubgoalResult.TRIVIAL_GOAL;
        elif sResult == 'unsolvable':
            self.result = SubgoalResult.UNSOLVABLE;
        elif sResult == 'timeout':
            self.result = SubgoalResult.TIMEOUT;
        elif sResult == 'pddl-syntax-error':
            self.result = SubgoalResult.SYNTAX_ERROR;
            assert False, 'pddl syntax error';
        elif sResult == 'ff-code-change':
            self.result = SubgoalResult.FF_CODE_CHANGE;
        elif sResult == 'outside-known-world':
            self.result = SubgoalResult.OUTSIDE_KNOWN_WORLD;
        elif sResult == '<??>':
            self.result = SubgoalResult.UNKNOWN;
            assert bAllowUnknown, 'Inappropriate Unknown';
        else:
            assert False, 'Bad Result:' + sResult + ':';
    def IsSuccess(self):
        return((self.result == SubgoalResult.PLAN_FOUND) or (self.result == SubgoalResult.TRIVIAL_GOAL));
    def IsKnown(self):
        return (not ((self.result == SubgoalResult.UNKNOWN) or (self.result == SubgoalResult.OUTSIDE_KNOWN_WORLD)))
            
            


def PredListFromString(sSubgoals, bIsFf):
    if sSubgoals.strip() == '':
        return [];
    lSplit = sSubgoals.split('|');
    lPreds = [];
    iNumSubgoals = int(len(lSplit)/2.0);
    assert(2*iNumSubgoals == len(lSplit));
    bSeenFailure = False;
    for iSubgoal in range(iNumSubgoals):
        sCurPred = lSplit[iSubgoal*2];
        sCurResult = lSplit[iSubgoal*2+1];
        predCur = predicate.Predicate();
        predCur.FromPddlLine(sCurPred.strip());
        lPreds.append(predCur);
        predCur.result = SubgoalResult(sCurResult.strip(), bIsFf or bSeenFailure);
        bSeenFailure |= not predCur.result.IsSuccess();
    return lPreds;
        

class CompressedReward:
    def __init__(self):
        self.iNumPos = 0;
        self.iNumEarlierNeg = 0;
        self.iNumNoReachNeg = 0;

    def GetNumPos(self):
        if config.get_bool('REWARDS_SIMPLE_POS_NEG'):
            return self.iNumPos;
        elif self.iNumEarlierNeg > 0:
            return 0;
        else:
            return self.iNumPos;
    
    def GetNumNeg(self):
        if config.get_bool('REWARDS_SIMPLE_POS_NEG'):
            return self.iNumNoReachNeg  + self.iNumEarlierNeg;
        elif self.GetNumPos() > 0:
            return 0;
        else:
            return self.iNumNoReachNeg  + self.iNumEarlierNeg;



class Reward:
    def __init__(self, sLinePred, sLineFf):
        self.predTarget = None;
        self.lFfPreds = [];
        self.lSubgoalPreds = [];
        self.bSuccess = False;
        self.IntegrateLine(sLinePred, 'PRED');
        self.IntegrateLine(sLineFf, 'FF');
        self.FixBug();

    def FixBug(self):
        # fix branvan's bug
        if self.bSuccess:
            if (len(self.lFfPreds) == 0) or (self.lFfPreds[-1].ToString() != self.predTarget.ToString()):
                self.lFfPreds.append(self.predTarget);
    
    def IntegrateLine(self, sLine, sTypeExpected):
        (sSuccess, sTarget, sType, sSubgoals) = sLine.strip().split(':');
        bSuccess = bool(int(sSuccess.strip()));
        assert(sType.strip() == sTypeExpected);
        if sTypeExpected == 'PRED':
            self.bSuccess = bSuccess;
        else:
            assert(self.bSuccess == bSuccess), "Bad Success on:" + sLine;

        predTarget = predicate.Predicate();
        predTarget.FromPddlLine(sTarget.strip());
        if self.predTarget == None:
            self.predTarget = predTarget;
        else:
            assert(self.predTarget.ToString() == predTarget.ToString());

        if sSubgoals.strip()  == '[SUBGOALS NOT NEEDED]':
            self.bSubgoalsNotNeeded = True;
            assert(sTypeExpected == 'PRED');
            self.lSubgoalPreds = [];
        elif sTypeExpected == 'PRED':
            self.lSubgoalPreds = PredListFromString(sSubgoals, bIsFf = False);
        else:
            self.lFfPreds = PredListFromString(sSubgoals, bIsFf = True);

            
    def ComputeCompressedReward(self, dConnRewards, lAllPreds):
        if len(self.lFfPreds) == 0:
            return;
        sPrev = self.lFfPreds[0].GetObject();
        setEarlier = set([sPrev]);
        for predSubgoal in self.lFfPreds:
            sCur = predSubgoal.GetObject();
            if sPrev != sCur:
                dConnRewards[(sPrev,sCur)].iNumPos += 1;
            if config.get_bool('REWARD_USE_EARLIER_NEGS'):
                # add all the negs from earlier
                for sNegPred  in lAllPreds:
                    if sNegPred not in setEarlier:
                        if sNegPred != sCur:
                            dConnRewards[(sNegPred, sCur)].iNumEarlierNeg += 1;
            setEarlier.add(sCur);
            sPrev = sCur;
        if config.get_bool('REWARD_USE_TARGET_NO_REACH_NEGS') and not self.bSuccess:
            # couldn't reach neg
            sTarget = self.predTarget.GetObject();
            sLastReached = self.lFfPreds[-1].GetObject();
            if sLastReached != sTarget:
                dConnRewards[(sLastReached, sTarget)].iNumNoReachNeg += 1;
        if config.get_bool('REWARD_USE_NEXT_HOP_NO_REACH_NEGS') and not self.bSuccess:
            # couldn't reach neg
            predPrev = None;
            for predCur in self.lSubgoalPreds:
                if not predCur.result.IsKnown():
                    break;
                elif not predCur.result.IsSuccess():
                    if predPrev != None:
                        dConnRewards[(predPrev.GetObject(), predCur.GetObject())].iNumNoReachNeg += 1;
                    break;
                else:
                    predPrev = predCur;

        if config.get_bool('REWARD_USE_PRED_POS'):
            predPrev = None;
            for predCur in self.lSubgoalPreds:
                if not predCur.result.IsKnown():
                    break;
                elif not predCur.result.IsSuccess():
                    break;
                else:
                    if predPrev != None:
                        dConnRewards[(predPrev.GetObject(), predCur.GetObject())].iNumPos += 1;
                    predPrev = predCur;
    def ComputeNumFfs(self):
        iNumFfs = 0;
        for predCur in self.lSubgoalPreds:
            iNumFfs += 1;
            if not predCur.result.IsSuccess():
                break;
        return iNumFfs
                
    @staticmethod
    def ComputeCompressedRewardFromList(lReward):
        dConnRewards = collections.defaultdict(lambda:CompressedReward());
        lAllPreds = list(predicate.LoadPredStringSet());
        for reward in lReward:
            reward.ComputeCompressedReward(dConnRewards, lAllPreds);
        return dConnRewards;

    @staticmethod
    def ComputeNumFfsFromList(lReward):
        iNumFfs = 0;
        for reward in lReward:
            iNumFfs += reward.ComputeNumFfs();
        return iNumFfs;
            


def LoadAllFullRewardsFiles():
    sRewardsDir = config.get_string('FULL_REWARDS_LOG_DIR');
    lRewards = [];
    print "Loading 200 Files From:", sRewardsDir;
    for iFileNum in range(config.get_int('REWARDS_MIN_ITER'), config.get_int('REWARDS_MAX_ITER')):
        sFile = sRewardsDir + '/predictions.log.' + str(iFileNum);
        lRewards.extend(LoadSingleFullRewardsFile(sFile));
    print "Done Loading";
    print "NumFF:", Reward.ComputeNumFfsFromList(lRewards);
    sys.exit(-1);
    return lRewards;

def LoadSingleFullRewardsFile(sRewardsFile):
    lLines = open(sRewardsFile).readlines();
    iProblems = int(len(lLines)/2.0);
    assert(iProblems*2 == len(lLines));
    lRewards = [];
    for iCurProblem in range(iProblems):
        sPredLine = lLines[iCurProblem*2];
        sFfLine = lLines[iCurProblem*2+1];
        reward = Reward(sPredLine, sFfLine);
        lRewards.append(reward);
    return lRewards;


def LoadFullRewardsDict():
    lRewards = LoadAllFullRewardsFiles();
    data.obj_to_file(lRewards, 'debug.json');
    print "LenRewards:", len(lRewards);
    dConnRewards = Reward.ComputeCompressedRewardFromList(lRewards);
    return dConnRewards;
