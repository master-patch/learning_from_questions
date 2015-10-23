#!/usr/bin/python
import random
import sys
import numpy as np;
import collections
import math
import copy

import config
import svm
import log_linear
import Sample
import Sentence
import FeatureSpace
import data
import predicate
import reward

def SplitSampleBySentence(lSamples):
    dSentenceTolSamples = {};
    dSentenceTolPosSamples = {};
    for i in range(len(lSamples)):
        sample = lSamples[i];
        sSentence = sample.pddlconn.textconn.sentence.sText;
        if sSentence not in dSentenceTolSamples:
            dSentenceTolSamples[sSentence] = [ i ];
        else:
            dSentenceTolSamples[sSentence].append(i);
        if not sample.bPos: continue;
        if sSentence not in dSentenceTolPosSamples:
            dSentenceTolPosSamples[sSentence] = [ i ];
        else:
            dSentenceTolPosSamples[sSentence].append(i);

    # seleted sentences for the first half
    setSelected = set();

    # 50-50 split positive samples
    lPosKeys = [ x for x in dSentenceTolPosSamples.keys() ];
    random.shuffle(lPosKeys);
    lPosSampleNum = map(lambda key: len(dSentenceTolPosSamples[key]), lPosKeys);
    iTot = sum(lPosSampleNum);
    iMid = iTot/2;
    iPosSplit = 1;
    iSplit = 1;
    for key, sampleNum in zip(lPosKeys, lPosSampleNum):
        iPosSplit += sampleNum;
        iSplit += len(dSentenceTolSamples[key]);
        setSelected.add(key);
        if iPosSplit >= iMid: break;
    print 'Positive Examples: ', iTot, iPosSplit, iSplit;

    # 50-50 split for all samples
    lKeys = [ x for x in dSentenceTolSamples.keys() ];
    random.shuffle(lKeys);
    lSampleNum = map(lambda key: len(dSentenceTolSamples[key]), lKeys);
    iMid = len(lSamples)/2;
    for key, sampleNum in zip(lKeys, lSampleNum):
        if key in dSentenceTolPosSamples: continue;
        iSplit += sampleNum;
        setSelected.add(key);
        if iSplit >= iMid: break;
    lRandomIndexes = [ x for sKey in setSelected for x in dSentenceTolSamples[sKey] ];
    lRandomIndexes.extend( [ x for sKey in lKeys if sKey not in setSelected for x in dSentenceTolSamples[sKey] ] );
    print 'All Examples: ', len(lSamples), iSplit;
    return lRandomIndexes, iSplit;

def SplitTrainTest(lSamples):
    if config.get_bool('SPLIT_BY_EASY_HARD'):
        setEasy = set(data.file_to_obj(config.get_string('EASY_CONNECTIONS_LIST_FILE')));
        lTrain = filter(lambda samp: samp.pddlconn.sPddlTo in setEasy, lSamples);
        lTest = filter(lambda samp: samp.pddlconn.sPddlTo not in setEasy, lSamples);
        print "NUM Train:", len(lTrain), "Test:", len(lTest);
        return lTrain, lTest;
    if config.get_bool('SPLIT_BY_FIRST_30'):
        setFirst30 = set(data.file_to_obj(config.get_string('FIRST_30_CONNECTIONS_LIST_FILE')));
        lTrain = filter(lambda samp: samp.pddlconn.sPddlTo in setFirst30, lSamples);
        lTest = filter(lambda samp: samp.pddlconn.sPddlTo not in setFirst30, lSamples);
        print "NUM Train:", len(lTrain), "Test:", len(lTest);
        return lTrain, lTest;
    if config.get_bool('SPLIT_BY_SENTENCE'):
        lRandomIndexes, iSplit = SplitSampleBySentence(lSamples);
    else:
        lRandomIndexes = range(len(lSamples));
        random.shuffle(lRandomIndexes);
        iSplit = len(lSamples)/2;
    if config.get_bool('TRAIN_AND_TEST_ON_ALL'):
        assert(not config.get_bool('TRAIN_ON_HALF_TEST_ON_ALL'));
        lTrainIndexes = range(len(lSamples));
        lTestIndexes = range(len(lSamples));
    elif config.get_bool('TRAIN_ON_HALF_TEST_ON_ALL'):
        lTrainIndexes = lRandomIndexes[:iSplit];
        lTestIndexes = range(len(lSamples));
    elif config.get_bool('TRAIN_ON_HALF_TEST_ON_HALF'):
        lTrainIndexes = lRandomIndexes[:iSplit];
        lTestIndexes = lRandomIndexes[iSplit:];
    else:
        assert False, 'No Test Train Split Method Specified';

    lTrain = map(lambda x:lSamples[x], lTrainIndexes);
    lTest = map(lambda x:lSamples[x], lTestIndexes);
    return lTrain, lTest;


def LoadGoldStringConnSet():
    sGoldDepFile = config.get_string('GOLD_DEP_FILE');
    assert(sGoldDepFile != '');
    dGoldDeps = data.file_to_obj_with_comments(sGoldDepFile);
    setGoldConns = set();
    for sTo, dFrom in dGoldDeps.items():
        for sFrom in dFrom:
            if sFrom == 'num':
                continue;
            setGoldConns.add((sFrom, sTo));
    return setGoldConns;
    iNumGold = len(setGoldConns);

def LoadGoldIndexesConnSet():
    setGoldStringConns = LoadGoldStringConnSet();
    dObjToPredList = predicate.PredDictFileToPredListDict(config.get_string('PRED_DICT_FILE'), lambda x:x.GetObject());
    setGoldIndexConns = set();
    for sFrom, sTo in setGoldStringConns:
        for predFrom in dObjToPredList[sFrom]:
            for predTo in dObjToPredList[sTo]:
                setGoldIndexConns.add((predFrom.iIndex,predTo.iIndex));
    return setGoldIndexConns;

def AnalyzePredsSimple(lSamples):
    if config.get_bool('FORCE_SINGLE_DIR'):
        dSamples = {};
        for sample in lSamples:
            tKey = (sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo);
            assert(tKey not in dSamples);
            dSamples[tKey] = sample;

    iNumTotal = 0;
    iNumCorrect = 0;
    iTruePos = 0;
    iFalsePos = 0;
    iTrueNeg = 0;
    iFalseNeg = 0;
    iThres = 0;
    if config.get_bool('SVM'):
        fThres = config.get_int('SVM_THRESHOLD');
    elif config.get_bool('LOG_LINEAR'):
        fThres = 0.5
    else:
        assert False;

    if config.get_bool('CALC_FSCORE_ON_GOLD'):
        setGoldStringConns = LoadGoldStringConnSet()
        iNumGold = len(setGoldStringConns);

    if config.get_bool('ANALYZE_ON_HARD'):
        lEasy = data.file_to_obj(config.get_string('EASY_CONNECTIONS_LIST_FILE'));
    fPredMin = sys.float_info.max;
    fPredMax = -sys.float_info.max;
    for sample in lSamples:
        if config.get_bool('ANALYZE_ON_HARD'):
            if sample.pddlconn.sPddlTo in lEasy:
                continue;

        if config.get_bool('TRAIN_ON_REWARD_EVAL_ON_GOLD'):
            bActual = sample.GetGoldPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_EVAL'));
        else:
            bActual = sample.GetPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_EVAL'));
        if config.get_bool('FORCE_SINGLE_DIR'):
            fPred = sample.fPred;
            tReverseKey = (sample.pddlconn.sPddlTo, sample.pddlconn.sPddlFrom);
            fReversePred = dSamples[tReverseKey].fPred if tReverseKey in dSamples else -sys.maxint;
            bNormalPred = (float(sample.fPred) > fThres);
            bPred = ((float(sample.fPred) > fThres) and (float(fPred) >= float(fReversePred)));
            if tReverseKey not in dSamples:
                print "FORCE-MISSING";
            elif (bNormalPred == bActual) and (bPred != bActual):
                print "FORCE-BAD:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
            elif  (bNormalPred != bActual) and (bPred == bActual):
                print "FORCE-GOOD:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
            else:
                print "FORCE-NEITHER:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
        else:
            bPred = sample.GetPredPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_EVAL'));
        fPredMin = min(fPredMin, sample.fPred);
        fPredMax = max(fPredMax, sample.fPred);

        iNumTotal += 1;
        if bPred == bActual:
            iNumCorrect += 1;
        if bPred:
            if bActual:
                iTruePos += 1;
            else:
                iFalsePos += 1;
        else:
            if bActual:
                iFalseNeg += 1;
            else:
                iTrueNeg += 1;

    if config.get_bool('CALC_FSCORE_ON_GOLD'):
        iFalseNeg = iNumGold - iTruePos;
        if config.get_bool('ANALYZE_ON_HARD'):
            iFalseNeg = iNumGold - iTruePos - len(lEasy);

    fPrecision = float(iTruePos)/float(iTruePos+iFalsePos) if iTruePos > 0 else 0;
    fRecall = float(iTruePos)/float(iTruePos+iFalseNeg) if iTruePos > 0 else 0;
    fScore = 2*fPrecision*fRecall/(fPrecision+fRecall) if (fPrecision*fRecall) > 0 else 0;
    print "FPred: min:", fPredMin, "max:", fPredMax;
    print "FScore:", fScore, fPrecision, fRecall;
    print "Frac Correct:", float(iNumCorrect)/float(iNumTotal), iNumCorrect, iNumTotal;
    print "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
    print "FracPos:", float(iTruePos+iFalsePos)/float(iTrueNeg+iFalseNeg+iTruePos+iFalsePos);
    return fScore, fPrecision, fRecall;



def WriteCountsFile(dCounts, dTotalCounts, sFileName):
    lTups = sorted(dCounts.items(), key=lambda tup: tup[1].iCount/float(dTotalCounts[tup[0]]));
    fOut = open(sFileName, 'w');
    for (sFrom, sTo), preddata in lTups:
        print >> fOut, '********', sFrom, sTo, preddata.iCount/float(dTotalCounts[(sFrom,sTo)]), preddata.iCount, dTotalCounts[(sFrom,sTo)];
        lFeatureTups = sorted(preddata.dFeatureWeights.items(), key = lambda tup:tup[1], reverse=True);
        for iFeature, fAvgWeight in lFeatureTups:
            print >> fOut, '\tFeature:', FeatureSpace.FeatureString(iFeature), fAvgWeight;
        for pddlconn, iConnCount in preddata.dPddlConnCounts.items():
            print >> fOut, '\tSentence-' + str(pddlconn.textconn.sentence.iIndex) + ': ', iConnCount, '::', pddlconn.textconn.iFrom, '-->', \
                pddlconn.textconn.iTo, pddlconn.textconn.sentence.sText;
            dCurFeatureWeights = preddata.dPddlConnFeatureWeights[pddlconn];
            lCurFeatureTups = sorted(dCurFeatureWeights.items(), key = lambda tup:tup[1], reverse=True);
            for iCurFeature, fCurAvgWeight in lCurFeatureTups:
                print >> fOut, '\t\tFeature:', FeatureSpace.FeatureString(iCurFeature), fCurAvgWeight;

def WriteBadPredCounts(dFalsePosCounts, dFalseNegCounts, dTruePosCounts, dTotalCounts):
    if config.get_string('FALSE_POS_COUNTS_FILE') != '':
        WriteCountsFile(dFalsePosCounts, dTotalCounts, config.get_string('FALSE_POS_COUNTS_FILE'));
    if config.get_string('FALSE_NEG_COUNTS_FILE') != '':
        WriteCountsFile(dFalseNegCounts, dTotalCounts, config.get_string('FALSE_NEG_COUNTS_FILE'));
    if config.get_string('TRUE_POS_COUNTS_FILE') != '':
        WriteCountsFile(dTruePosCounts, dTotalCounts, config.get_string('TRUE_POS_COUNTS_FILE'));

def Evaluate(lSamples):
    bCollapseFirst = config.get_bool('COLLAPSE_FIRST');
    lFScores = [];
    lPrecisions = [];
    lRecalls = [];
    dFalsePosCounts = collections.defaultdict(lambda:PredData(bPos = True));
    dFalseNegCounts = collections.defaultdict(lambda:PredData(bPos = False));
    dTruePosCounts = collections.defaultdict(lambda:PredData(bPos = True));
    dTotalCounts = collections.defaultdict(lambda:0);
    for iIter in range(config.get_int('NUM_ITER')):
        lTrain, lTest = SplitTrainTest(lSamples);
        if config.get_bool('SVM'):
            assert not config.get_bool('LOG_LINEAR');
            lTest, dFeatureWeights = TrainAndTestSvm(lTrain, lTest);
        elif config.get_bool('LOG_LINEAR'):
            lTest, dFeatureWeights = log_linear.TrainAndTestFromGranular(lTrain, lTest);
        else:
            assert False;

        if config.get_bool('WRITE_TRUE_POS_AND_FALSE_NEG'):
            UpdateBadPredCounts(dFalsePosCounts, dFalseNegCounts, dTruePosCounts, dTotalCounts, dFeatureWeights, lTest);
        fScore, fPrec, fRecall = AnalyzePredsSimple(lTest);
        lFScores.append(fScore);
        lPrecisions.append(fPrec);
        lRecalls.append(fRecall);
    if config.get_bool('WRITE_TRUE_POS_AND_FALSE_NEG'):
        WriteBadPredCounts(dFalsePosCounts, dFalseNegCounts, dTruePosCounts, dTotalCounts);
    for fScore in lFScores:
        print "FScore is:", fScore;
    print "Average Precision: ", np.average(lPrecisions), "\tStd: ", np.std(lPrecisions);
    print "Average Recall: ", np.average(lRecalls), "\tStd: ", np.std(lRecalls);
    print "Average F-Score: ", np.average(lFScores), "\tStd: ", np.std(lFScores);

def TrainAndTestSvm(lTrainGranular, lTestGranular):
    if config.get_bool('COLLAPSE_FIRST'):
        assert not config.get_bool('TEST_AND_TRAIN_ON_BOTH_HALVES');
        lTrainCollapsed = Sample.CollapseSamples(lTrainGranular);
        lTestCollapsed = Sample.CollapseSamples(lTestGranular);
        svm.Train(lTrainCollapsed);
        svm.Test(lTestCollapsed);
    else:
        if config.get_bool('TEST_AND_TRAIN_ON_BOTH_HALVES'):
            svm.Train(lTrainGranular);
            svm.Test(lTestGranular);
            svm.Train(lTestGranular);
            svm.Test(lTrainGranular);
            lTestCollapsed = Sample.CollapseSamples(lTrainGranular+lTestGranular);
        else:
            svm.Train(lTrainGranular);
            svm.Test(lTestGranular);
            lTrainCollapsed = Sample.CollapseSamples(lTrainGranular);
            lTestCollapsed = Sample.CollapseSamples(lTestGranular);
    fThreshold, dFeatureWeights = svm.GetNormalizedWeights();
    return lTestCollapsed, dFeatureWeights;


class PredData:
    def __init__(self, bPos):
        self.iCount = 0;
        self.dPddlConnCounts = collections.defaultdict(lambda:0);
        self.dPddlConnFeatureWeights = collections.defaultdict(lambda:collections.defaultdict(lambda:0.0));
        # feature index to sum of weights
        self.dFeatureWeights = collections.defaultdict(lambda:0);
        self.bPos = bPos;
        self.dFeatureWeights = collections.defaultdict(lambda:0.0);
    def AddSample(self, collsamp, dFeatureWeights):
        self.iCount += 1;
        lFeatureTups = collsamp.GetFeatureTupList();
        for iFeature, fValue in lFeatureTups:
            fWeight = fValue*dFeatureWeights[iFeature];
            if fWeight != 0:
                self.dFeatureWeights[iFeature] += fWeight;
                for gransamp in collsamp.lGranularSamples:
                    if (not self.bPos) or gransamp.bPredPos:
                        self.dPddlConnFeatureWeights[gransamp.pddlconn][iFeature] += fWeight;
        for gransamp in collsamp.lGranularSamples:
            if (not self.bPos) or gransamp.bPredPos:
                self.dPddlConnCounts[gransamp.pddlconn] += 1;
                for iFeature in gransamp.features.GetFeatureIndexList():
                    fWeight = dFeatureWeights[iFeature];
                    if fWeight != 0:
                        self.dPddlConnFeatureWeights[gransamp.pddlconn][iFeature] += fWeight;

            
    


def UpdateBadPredCounts(dFalsePosCounts, dFalseNegCounts, dTruePosCounts, dTotalCounts, dFeatureWeights, lCollapsedTest):
    for collsamp in lCollapsedTest:
        tKey = (collsamp.pddlconn.sPddlFrom, collsamp.pddlconn.sPddlTo);
        dTotalCounts[tKey] += 1;
        if collsamp.bManualPos and not collsamp.bPredPos:
            dFalseNegCounts[tKey].AddSample(collsamp, dFeatureWeights);
        if not collsamp.bManualPos and collsamp.bPredPos:
            dFalsePosCounts[tKey].AddSample(collsamp, dFeatureWeights);
        if collsamp.bManualPos and collsamp.bPredPos:
            dTruePosCounts[tKey].AddSample(collsamp, dFeatureWeights);
            

def WriteFirst30SvmConnectionsFile(lGranularSamples):
    assert config.get_bool('SPLIT_BY_FIRST_30');
    lTrainGranular, lTestGranular = SplitTrainTest(lGranularSamples);

    lTestCollapsed, dFeatureWeights = TrainAndTestSvm(lTrainGranular, lTestGranular);
    fScore, fPrec, fRecall = AnalyzePredsSimple(lTestCollapsed);
    Sample.CollapsedSample.WriteConnections(lTestCollapsed, config.get_string('FIRST_30_SVM_CONNECTIONS_FILE'), 
                                            bAppend=False, bWritePredictions = True, bPosOnly = True);
    # note that this one is train on train and test on train (yes those words are correct)
    lTrainCollapsed, dFeatureWeights = TrainAndTestSvm(lTrainGranular, lTrainGranular);
    fScore, fPrec, fRecall = AnalyzePredsSimple(lTrainCollapsed);
    Sample.CollapsedSample.WriteConnections(lTrainCollapsed, config.get_string('FIRST_30_SVM_CONNECTIONS_FILE'), 
                                                    bAppend=True, bWritePredictions = True, bPosOnly = True);


# NK: this doesn't work right now and needs to be update
# def WriteSvmConnectionsFile(lGranularSamples):
#     lTrainGranular, lTestGranular = SplitTrainTest(lGranularSamples);

#     lTestCollapsed = TrainAndTestSvm(lTrainGranular, lTestGranular);
#     fScore, fPrec, fRecall = AnalyzePredsSimple(lTestCollapsed);
#     Sample.CollapsedSample.WritePositiveConnections(lTestCollapsed, config.get_string('SVM_CONNECTIONS_FILE'), 
#                                                     bAppend=False, bWritePredictions = True);
#     lTrainCollapsed = TrainAndTestSvm(lTestGranular, lTrainGranular);
#     fScore, fPrec, fRecall = AnalyzePredsSimple(lTrainCollapsed);
#     Sample.CollapsedSample.WritePositiveConnections(lTrainCollapsed, config.get_string('SVM_CONNECTIONS_FILE'), 
#                                                     bAppend=True, bWritePredictions = True);

    

def PrintDebugInfo(dConnRewards):
    setGoldConns = LoadGoldStringConnSet();
    setFound = set();
    iNumPosGold = 0;
    iNumNegGold = 0;
    iNumPosNonGold = 0;
    iNumNegNonGold = 0;
    for (sFrom, sTo), dRewards in dConnRewards.items():
        if sFrom == sTo:
            continue

        if dRewards['iNumPos'] > 0:
            setFound.add((sFrom, sTo));

        bGold = (sFrom, sTo) in setGoldConns;
        if bGold:
            iNumPosGold += dRewards['iNumPos']
            if dRewards['iNumPos'] == 0:
                iNumNegGold += dRewards['iNumNeg']
        else:
            iNumPosNonGold += dRewards['iNumPos']
            if dRewards['iNumPos'] == 0:
                iNumNegNonGold += dRewards['iNumNeg']
            else:
                print "Pred:", sFrom, sTo, dRewards['iNumPos'];
                
    setMissing = setGoldConns.difference(setFound);
    setWrong = setFound.difference(setGoldConns);
    print "Gold:", len(setGoldConns), "Found:", len(setFound), "Missing:", len(setMissing), "Wrong:", len(setWrong);
    print "PosGold:", iNumPosGold, "NegGold:", iNumNegGold, "PosNonGold:", iNumPosNonGold, "NegNonGold:", iNumNegNonGold;
    fMult = float(iNumPosGold + iNumPosNonGold)/float(iNumNegGold + iNumNegNonGold); 
    print "Mult is:", fMult;
    sys.exit(0);
    return fMult;

def TrainOnRewardEvalOnGold(lGranularSamples):
    #lGranularSamples = lGranularSamples[:100];
    assert(config.get_bool('COLLAPSE_FIRST'));
    dConnRewards = LoadRewardsDict();
    fNegMultiplier = PrintDebugInfo(dConnRewards);
    #add the reward data to the samples themselves
    lCollapsedSamples = Sample.CollapseSamples(lGranularSamples);
    lNewSamples = [];
    for sample in lCollapsedSamples:
        dRewards = dConnRewards[sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo];
        if dRewards['iNumPos'] > 0:
            for iIter in range(dRewards['iNumPos']):
                sampleNew = copy.copy(sample);
                sampleNew._bPos = True;
                lNewSamples.append(sampleNew);
        else:
            for iIter in range(int(math.ceil(dRewards['iNumNeg']*fNegMultiplier))):
                sampleNew = copy.copy(sample);
                sampleNew._bPos = False;
                lNewSamples.append(sampleNew);
    lCollapsedSamples = lNewSamples;
    lFScores = [];
    lPrecisions = [];
    lRecalls = [];

    lTrainCollapsed, lTestCollapsed = SplitTrainTest(lCollapsedSamples);
    svm.Train(lTrainCollapsed);
    svm.Test(lTestCollapsed);
    # remove the duplicates
    setAlreadySeen = set();
    lTestNoDups = [];
    for sample in lTestCollapsed:
        tKey = (sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo);
        if tKey not in setAlreadySeen:
            setAlreadySeen.add(tKey);
            lTestNoDups.append(sample);

    fScore, fPrec, fRecall = AnalyzePredsSimple(lTestNoDups);
    Sample.CollapsedSample.WriteConnections(lTestNoDups, config.get_string('SVM_REWARD_CONNECTIONS_FILE'), 
                                            bAppend=False, bWritePredictions = True, bPosOnly = True);
    fOut = open('debug.txt', 'w');
    for sample in lTestCollapsed:
        print >> fOut, "Sample:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, sample.fPred;

    print "Precision: ", fPrec
    print "Recall: ", fRecall
    print "F-Score: ", fScore;
    

def CalcEasyHardConnections():
    sPartialDir = '/nfs2/hierarchical_planning/branavan/output/atdi1_fw_';
    dCounts = collections.defaultdict(lambda:[0,0]);
    for i in range(1, 201):
        bStartedRelevant = False;
        for sLine in open(sPartialDir + str(i) + '/run.log'):
            sLine = sLine.strip();
            if not bStartedRelevant:
                if sLine.startswith('List of solved problems'):
                    bStartedRelevant = True;
                continue;
            else:
                if sLine.startswith('----'):
                    continue;
                sName = sLine.split('.')[0];
                bNotSolved = (sLine.split()[1].startswith('[NOT'));
                if bNotSolved:
                    dCounts[sName][0] += 1;
                else:
                    #print "Not Solved:" + sLine.split()[1] + ":";
                    dCounts[sName][1] += 1;

    lFirst30 = [];
    for sName, (iFailedCount, iSolvedCount) in dCounts.items():
        if iSolvedCount == 400:
            lFirst30.append(sName);
    data.obj_to_file(lFirst30, 'first30.json');

    # sorted 
    lSortedTups = sorted(dCounts.items(), key=lambda tup:tup[1][1]);
    lSortedObjs = map(lambda x:x[0], lSortedTups);
    data.obj_to_file(lSortedObjs, 'sorted.json');
    iSplit = int(len(lSortedObjs)/2.0);
    lEasy = lSortedObjs[iSplit:];
    data.obj_to_file(lEasy, 'easy.json');
    


def CalcConnFileFScore():
    print "Calcing FScore for:", config.get_string('CONN_FILE');
    setConnTups = predicate.ReadConnectionsFileToTupSet();
    setGoldConns = LoadGoldStringConnSet();

    if config.get_bool('ANALYZE_ON_HARD'):
        lEasy = data.file_to_obj(config.get_string('EASY_CONNECTIONS_LIST_FILE'));

    iTruePos = 0;
    iFalsePos = 0;
    for sFrom, sTo in setConnTups:
        if config.get_bool('ANALYZE_ON_HARD'):
            if sTo in lEasy:
                continue;

        if (sFrom, sTo) in setGoldConns:
            iTruePos += 1;
        else:
            iFalsePos += 1;

    iFalseNeg = len(setGoldConns)-iTruePos;
    if config.get_bool('ANALYZE_ON_HARD'):
        iFalseNeg = len(setGoldConns)-iTruePos-len(lEasy);
        
    iTrueNeg = 0;
    fPrecision = float(iTruePos)/float(iTruePos+iFalsePos) if iTruePos > 0 else 0;
    fRecall = float(iTruePos)/float(iTruePos+iFalseNeg) if iTruePos > 0 else 0;
    fScore = 2*fPrecision*fRecall/(fPrecision+fRecall) if (fPrecision*fRecall) > 0 else 0;
    print "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
    print "Precision:", fPrecision;
    print "Recall:", fRecall;
    print "FScore:", fScore;
    
def TrainOnEasyTestOnHardWithGold():
    lSentences = Sentence.ReadSentencesFromTextFile();
    lGranularSamples = Sentence.GenAllGranularSamplesFromList(lSentences, 'sentences.log');
    lCollapsed = Sample.CollapseSamples(lGranularSamples);
    

def ComputeMultiplier(dConnRewards, bPos):
    iPosTotal = 0;
    iNegTotal = 0;
    for cr in dConnRewards.values():
        iPosTotal += cr.GetNumPos();
        iNegTotal += cr.GetNumNeg();
    if bPos:
        fMult = float(iNegTotal)/float(iPosTotal);
    else:
        fMult = float(iPosTotal)/float(iNegTotal);
    if config.get_float('REWARDS_NEG_MULT') != -1:
        assert(not bPos);
        fMult = config.get_float('REWARDS_NEG_MULT');
    print "fMult:", fMult;
    return fMult;

def GenerateTrainingSamplesFromRewards(dConnRewards, lCollapsedSamples):
    fNegMultiplier = ComputeMultiplier(dConnRewards, bPos = False);
    lNewSamples = [];
    for sample in lCollapsedSamples:
        cr = dConnRewards[sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo];
        #for iIter in range(int(math.ceil(cr.GetNumPos()*fPosMultiplier))):
        for iIter in range(cr.GetNumPos()):
            sampleNew = copy.copy(sample);
            sampleNew._bPos = True;
            lNewSamples.append(sampleNew);
        #for iIter in range(cr.GetNumNeg()):
        for iIter in range(int(math.ceil(cr.GetNumNeg()*fNegMultiplier))):
            sampleNew = copy.copy(sample);
            sampleNew._bPos = False;
            lNewSamples.append(sampleNew);
    return lNewSamples;
        
    

def LoadFullRewards():
    dConnRewards = reward.LoadFullRewardsDict();
    #print "Len:", len(dConnRewards);
    #for (sFrom, sTo), cr in dConnRewards.items():
    #    print sFrom, sTo, "Pos:", cr.iNumPos, "NE:", cr.iNumEarlierNeg, "NR:", cr.iNumNoReachNeg;
    #lGranularSamples = lGranularSamples[:100];
    assert(config.get_bool('COLLAPSE_FIRST'));
    #add the reward data to the samples themselves
    lSentences = Sentence.ReadSentencesFromTextFile();
    lGranularSamples = Sentence.GenAllGranularSamplesFromList(lSentences, 'sentences.log');
    lCollapsedSamples = Sample.CollapseSamples(lGranularSamples);
    setEasy = set(data.file_to_obj(config.get_string('EASY_CONNECTIONS_LIST_FILE')));
    lTrainCollapsed = filter(lambda sample: sample.pddlconn.sPddlTo in setEasy, lCollapsedSamples);
    lTestCollapsed = filter(lambda sample: sample.pddlconn.sPddlTo not in setEasy, lCollapsedSamples);
    
    lTrainingSamples = GenerateTrainingSamplesFromRewards(dConnRewards, lTrainCollapsed);
    if config.get_bool('SVM'):
        svm.Train(lTrainingSamples);
        svm.Test(lTestCollapsed);
    elif config.get_bool('LOG_LINEAR'):
        log_linear.TrainAndTestLogLinear(lTrainingSamples, lTestCollapsed);
    else:
        assert False;
    # remove the duplicates
    setAlreadySeen = set();
    lTestNoDups = [];
    for sample in lTestCollapsed:
        tKey = (sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo);
        if tKey not in setAlreadySeen:
            setAlreadySeen.add(tKey);
            lTestNoDups.append(sample);

    fScore, fPrec, fRecall = AnalyzePredsSimple(lTestNoDups);
    #Sample.CollapsedSample.WriteConnections(lTestNoDups, config.get_string('SVM_REWARD_CONNECTIONS_FILE'), 
    #                                        bAppend=False, bWritePredictions = True, bPosOnly = True);
    #fOut = open('debug.txt', 'w');
    #for sample in lTestCollapsed:
    #    print >> fOut, "Sample:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, sample.fPred;

    print "Precision: ", fPrec
    print "Recall: ", fRecall
    print "F-Score: ", fScore;


def CalcAllTextFScore(lGranularSamples):
    lCollapsedSamples = Sample.CollapseSamples(lGranularSamples);
    lSorted = data.file_to_obj(config.get_string('SORTED_CONNECTIONS_LIST_FILE'));
    lSorted.reverse();
    lPos = [0 for i in range(len(lSorted))];
    lNeg = [0 for i in range(len(lSorted))];
    iPosTot = 0;
    iNegTot = 0;
    for sample in lCollapsedSamples:
        if sample.bPos:
            iPosTot += 1;
        else:
            iNegTot += 1;
        for i in range(len(lSorted)):
            if sample.pddlconn.sPddlTo != lSorted[i]:
                continue;
            if sample.bPos:
                lPos[i] += 1;
            else:
                lNeg[i] += 1;
    for i in range(len(lSorted)):
        fPrecision = float(lPos[i])/float(lPos[i] + lNeg[i]) if (lPos[i] + lNeg[i]) != 0 else 0;
        print lSorted[i], fPrecision;
    print "Overall Precision:", float(iPosTot)/float(iNegTot);

def Run():
    if config.get_bool('CALC_CONN_FILE_FSCORE'):
        CalcConnFileFScore();
        return;
    elif config.get_bool('CALC_EASY_HARD_CONNECTIONS'):
        CalcEasyHardConnections();
        return;
    elif config.get_bool('LOAD_FULL_REWARDS'):
        LoadFullRewards();
        return;


    

    lSentences = Sentence.ReadSentencesFromTextFile();
    lGranularSamples = Sentence.GenAllGranularSamplesFromList(lSentences, 'sentences.log');

    if config.get_bool('CALC_ALL_TEXT_FSCORE'):
        CalcAllTextFScore(lGranularSamples);
    elif config.get_string('GRANULAR_SAMPLE_FILE') != '':
        Sample.GranularSample.WriteList(lGranularSamples, config.get_string('GRANULAR_SAMPLE_FILE'));
    elif config.get_string('SENTENCES_AND_FEATURES_FILE') != '':
        Sample.GranularSample.WriteDebugFromList(lGranularSamples, config.get_string('SENTENCES_AND_FEATURES_FILE'));
    elif config.get_string('SVM_CONNECTIONS_FILE') != '':
        WriteSvmConnectionsFile(lGranularSamples);
    elif config.get_string('FIRST_30_SVM_CONNECTIONS_FILE') != '':
        WriteFirst30SvmConnectionsFile(lGranularSamples);
    elif config.get_string('COLLAPSED_MANUAL_TEXT_CONNECTIONS_FILE'):
        lCollapsed = Sample.CollapseSamples(lGranularSamples);
        Sample.CollapsedSample.WriteConnections(lCollapsed, config.get_string('COLLAPSED_MANUAL_TEXT_CONNECTIONS_FILE'), bPosOnly = True);
    elif config.get_string('COLLAPSED_ALL_TEXT_CONNECTIONS_FILE'):
        lCollapsed = Sample.CollapseSamples(lGranularSamples);
        Sample.CollapsedSample.WriteConnections(lCollapsed, config.get_string('COLLAPSED_ALL_TEXT_CONNECTIONS_FILE'), bPosOnly = False);
    elif config.get_bool('TRAIN_ON_REWARD_EVAL_ON_GOLD'):
        TrainOnRewardEvalOnGold(lGranularSamples);
    else:
        Evaluate(lGranularSamples);

def Main():
    config.load_config(sys.argv);
    Run();
    #TrainOnRewardEvalOnGold(None);

Main();
