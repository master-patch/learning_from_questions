#!/usr/bin/python

#ToDo:
# 1. read in the gold data and generate samples from this
# 2. handle the output
# 3. try generating individual features as well?
# 4. Evaluation
#   - all I care about is the problem Id

import pddl
import data
import subprocess
import shlex
import os.path
import collections
import nltk.classify.maxent as maxent

REVERSE = True;
USENUMERICS = False;
SVM = True;
#MAXNUMPROBLEMS = 2;
MAXNUMPROBLEMS = 1000000;
USE_NON_CONNECTION_FEATURES = True;
USE_TEXT_CONNECTIONS = False
PREDICT_ONLY_LAST = True

iMaxFeature = 1;


class Predicate:
    def __init__(self):
        self.bFunc = False;
        self.sName = 'thing-available';
        self.lArgs = [];
        self.sType = 'NOTYPE';
        self.fValue = -10000;
        self._iIndex = -1;
        self.sString = '';

    def ToStringInternal(self):
        sOut = '';
        if self.bFunc:
            sOut += '(' + self.sType + ' ';
        sOut += '(' + self.sName;
        for sArg in self.lArgs:
            sOut += ' ' + sArg;
        sOut += ')';
        if self.bFunc:
            sOut += ' ' + str(self.fValue) + ')';
        return sOut;

    def ToSimpleStringInternal(self):
        sOut = '';
        if self.bFunc:
            sOut += '(> ';
        sOut += '(' + self.sName;
        for sArg in self.lArgs:
            sOut += ' ' + sArg;
        sOut += ')';
        if self.bFunc:
            sOut += ' 0)';
        return sOut;

    def ToString(self):
        if self.sString == '':
            if USENUMERICS:
                self.sString = self.ToStringInternal();
            else:
                self.sString = self.ToSimpleStringInternal();
        return self.sString;

    def FromPrecondition(self, precondition):
        assert(precondition.sType == 'COMPARISON_GD');
        comparison = precondition.comparison;
        self.sType = comparison.sDir;
        self.fValue = int(comparison.sTo);
        self.FromPredInst(comparison.FromFunctionInst, bFunc = True);

    def FromEffect(self, effect):
        self.sName = effect.sText;
        if effect.assign != None:
            assert(effect.predicate_inst == None);
            self.FromAssign(effect.assign);
        elif effect.predicate_inst != None:
            self.FromPredInst(effect.predicate_inst, bFunc = False);
        else:
            assert False;

    def get_iIndex(self):
        if self._iIndex == -1:
            if self.ToString() in dStringToPred:
                self._iIndex = dStringToPred[self.ToString()].iIndex;
            else:
                self._iIndex = -1000;
            
        return self._iIndex;

    def set_iIndex(self, iIndex):
        self._iIndex = iIndex;

    def FromPredInst(self, predinst, bFunc):
        self.bFunc = bFunc;
        self.sName = predinst.sName
        for arg in predinst.lArgs:
            self.lArgs.append(arg.sName);

    def FromAssign(self, assign):
        self.sType = '=';
        self.fValue = int(assign.To);
        self.FromPredInst(assign.From, bFunc = True);


    def FromDict(self, dPredicate):
        assert(len(dPredicate) == 1);
        self.bFunc = True;
        self.sType = '>';
        self.fValue = dPredicate.values()[0]-1 if dPredicate.values()[0] != -1 else 0;
        #self.fValue = 0;
        sName = dPredicate.keys()[0];
        if sName == 'furnace-fuel':
            self.sName = 'furnace-fuel';
        else:
            self.sName = 'thing-available';
            self.lArgs.append(sName);

    iIndex = property(get_iIndex, set_iIndex);

    @staticmethod
    def GetInitPredList(domain):
        lInitEffects = domain.lInit;
        lInitPreds = [];
        for effect in lInitEffects:
            pred = Predicate();
            pred.FromEffect(effect);
            lInitPreds.append(pred);
        return lInitPreds;

    @staticmethod
    def GetGoalPredList(domain):
        lGoalPreconditions = domain.lGoals;
        lGoalPreds = [];
        for precondition in lGoalPreconditions:
            pred = Predicate();
            pred.FromPrecondition(precondition);
            lGoalPreds.append(pred);
        return lGoalPreds;
    
    @staticmethod
    def GetSubgoalPredList(lSubgoals):
        lSubgoalPreds = [];
        for dSubgoal in lSubgoals:
            pred = Predicate();
            pred.FromDict(dSubgoal);
            lSubgoalPreds.append(pred);
        return lSubgoalPreds;
    


# def make_joint_feature_func(iMaxFeature):
#     def dummy_joint_features(dFeatures, sLabel):
#         lFeatures = [];
#         for iFeatureIndex, fFeatureVal in dFeatures.items():
#             if sLabel == '-1':
#                 iFeatureIndex += iMaxFeature;
#             tFeature = (iFeatureIndex, fFeatureVal);
#             lFeatures.append(tFeature);
#         return lFeatures;

#         return dFeatures.items();
#     return dummy_joint_features;

def dummy_joint_features(dFeatures, sLabel):
    lFeatures = [];
    for iFeatureIndex, fFeatureVal in dFeatures.items():
        if sLabel == '-1':
            iFeatureIndex += iMaxFeature;
        tFeature = (iFeatureIndex, fFeatureVal);
        lFeatures.append(tFeature);
    return lFeatures;

    return dFeatures.items();

def TrainAndTestLogLinear(lSamples):
    lFeatureTups = Sample.SamplesToFeatureTups(lSamples);
    iNumFeatures = len(lFeatureTups[0][0]);
    encoder = maxent.FunctionBackedMaxentFeatureEncoding(dummy_joint_features,
                                                         iMaxFeature*2,
                                                         ['-1','1']);
    #lFeatureTupsPruned = lFeatureTups[0:1000];
    classifier = maxent.MaxentClassifier.train(lFeatureTups, 
                                               encoding = encoder,
                                               algorithm = 'LBFGSB');
    lPreds = [];
    for (dFeatures, sLabel) in lFeatureTups:
        fProb = classifier.prob_classify(dFeatures).prob('1');
        lPreds.append(fProb);
    return lPreds;



class FeatureGen:
    def __init__(self):
        self.dFeatures = {};
        # svm light requires feature indexes to start at 1
        self.iIndex = 1;

    def FeatureIndex(self, sFeature):
        global iMaxFeature;
        if sFeature in self.dFeatures:
            return self.dFeatures[sFeature];
        else:
            self.dFeatures[sFeature] = self.iIndex;
            self.iIndex += 1;
            iMaxFeature = self.iIndex;
            return self.iIndex-1;

fgen = FeatureGen();

class Sample:
    def __init__(self, pred, lInitPreds, lPrevPreds, lGoalPreds, sProblemFile, bPositive, iSubgoalIndex):
        self.pred = pred;
        self.bPositive = bPositive;
        #self.lFeatureIndexes = [];
        #self.lFeatureValues = [];
        self.lInitPreds = lInitPreds;
        self.lPrevPreds = lPrevPreds;
        self.lGoalPreds = lGoalPreds;
        self.dFeatures = {};
        self.sProblemFile = sProblemFile;
        self.GenFeatures();
        self.iSubgoalIndex = iSubgoalIndex;

    def GenFeatures(self):
        self.GenFeaturesAllPreds('INIT', self.lInitPreds, bSelfIsFrom = False);
        self.GenFeaturesAllPreds('PREV', self.lPrevPreds, bSelfIsFrom = REVERSE);
        self.GenFeaturesAllPreds('GOAL', self.lGoalPreds, bSelfIsFrom = True);

    def GenFeaturesAllPreds(self, sFeature, lPreds, bSelfIsFrom):
        for pred in lPreds:
            self.GenFeaturesOnePred(sFeature, pred, bSelfIsFrom);

    def GenFeaturesOnePred(self, sFeature, pred, bSelfIsFrom):
        if USE_NON_CONNECTION_FEATURES:
            # name feature
            sName1 = self.pred.sName;
            sName2 = pred.sName;
            self.AddBinaryTwoStrings(sFeature + ':NAME:',  self.pred.sName, pred.sName);
            # arg features
            for sArg1 in self.pred.lArgs:
                for sArg2 in self.pred.lArgs:
                    self.AddBinaryTwoStrings(sFeature + ':ARG:', sArg1, sArg2);
        # connection features
        if bSelfIsFrom:
            iFrom = self.pred.iIndex;
            iTo = pred.iIndex;
            sFrom = self.pred.ToString();
            sTo = pred.ToString();
        else:
            iFrom = pred.iIndex;
            iTo = self.pred.iIndex;
            sFrom = pred.ToString();
            sTo = self.pred.ToString();
            
        if iTo in dConnections[iFrom]:
            iDepth = dConnections[iFrom][iTo];
            self.AddBinary(fgen.FeatureIndex(sFeature + ":DEPTH:" + str(iDepth)));

    def AddBinaryTwoStrings(self, sFeatureName, s1, s2):
        self.AddBinary(fgen.FeatureIndex(sFeatureName + s1 + ':' + s2));

    def AddBinary(self, iIndex):
        self.dFeatures[iIndex] = 1;
        #self.lFeatureIndexes.append(iIndex);
        #self.lFeatureValues.append(1);
        

    def ToSvmLightString(self):
        lFeatureIndexes = sorted(self.dFeatures.keys());
        sSvmLight = '+1 ' if self.bPositive else '-1 ';
        for iIndex in lFeatureIndexes:
            sSvmLight += ' ' + str(iIndex) + ':1';
        sSvmLight += '  #' + self.sProblemFile + '#' + str(self.iSubgoalIndex) + '#' + self.pred.ToString();
        return sSvmLight;

    def ToFeatureTup(self):
        sIsPositive = "1" if self.bPositive else "-1";
        return (self.dFeatures, sIsPositive);
    @staticmethod
    def SamplesToFeatureTups(lSamples):
        lFeatureTups = [];
        for sample in lSamples:
            lFeatureTups.append(sample.ToFeatureTup());
        return lFeatureTups;


    @staticmethod
    def WriteSamplesToSvmLightFile(lSamples, fOut):
        for sample in lSamples:
            print >> fOut, sample.ToSvmLightString();


def GenSamplesOneSubgoal(predGold, lInitPreds, lPrevPreds, lGoalPreds, sProblemFile, iSubgoalIndex, lSamples, bLast):
    bFoundPositive = False;
    print "GenSubgoal:", str(iSubgoalIndex);
    for pred in lPossiblePreds:
        bPositive = predGold.ToString() == pred.ToString();
        if PREDICT_ONLY_LAST:
            bPositive &= bLast;
        bFoundPositive |= bPositive;
        sample = Sample(pred, lInitPreds, lPrevPreds, lGoalPreds, sProblemFile, bPositive, iSubgoalIndex);
        lSamples.append(sample);
    assert PREDICT_ONLY_LAST or bFoundPositive,"Gold: " + predGold.ToString() + " First: " + lPossiblePreds[0].ToString();

        
def GenSamplesOneProblem(dGold, lSamples):
    lGoldPreds = Predicate.GetSubgoalPredList(dGold['subgoals'][:-1]);
    lInitPreds = dGold['init'];
    lGoalPreds = dGold['goal'];
    print "GoldPreds:", len(lGoldPreds);
    for iSubgoalIndex, predGold in enumerate(lGoldPreds):
        if REVERSE:
            lPrevPreds = lGoldPreds[iSubgoalIndex+1:];
        else:
            lPrevPreds = lGoldPreds[:iSubgoalIndex];
        GenSamplesOneSubgoal(predGold, lInitPreds, lPrevPreds, lGoalPreds, dGold['file'],
                             iSubgoalIndex, lSamples, bLast = (iSubgoalIndex == (len(lGoldPreds)-1)));


# making this a global because I'm lazy
dConnections = collections.defaultdict(lambda:{});
def ReadConnections(sFileName):
    lLines = open(sFileName).readlines();
    for sLine in lLines:
        sLine = sLine.strip();
        lSplitLine = sLine.split('|');
        iDepth = int(lSplitLine[0]);
        iFrom = int(lSplitLine[1]);
        iTo = int(lSplitLine[2]);
        dConnections[iFrom][iTo] = iDepth;
        sFrom = dIndexToPred[iFrom].ToString() if (iFrom in dIndexToPred) else 'BAD INDEX';
        sTo = dIndexToPred[iTo].ToString() if (iTo in dIndexToPred) else 'BAD INDEX';
        print "Init Connection:", iFrom, iTo, sFrom, sTo;
    return dConnections;

lPossiblePreds = [];
dStringToPred = {};
dIndexToPred = {};
def ReadPreds(sFileName):
    lLines = open(sFileName).readlines();
    for sLine in lLines:
        sLine = sLine.strip();
        lSplitLine = sLine.split('|');
        pred = Predicate();
        iIndex = int(lSplitLine[0]);
        pred.bFunc = (lSplitLine[1] != '0');
        lSplitName = lSplitLine[2].split(' ');
        pred.sName = lSplitName[0];
        pred.fValue = int(lSplitLine[1])-1;
        pred.sType = '>';
        pred.iIndex = iIndex;
        for sArg in lSplitName[1:]:
            pred.lArgs.append(sArg);
        if pred.ToString() in dStringToPred:
            print "Skipping Pred:", iIndex, pred.ToString();
            continue;
        print "Adding Pred:", iIndex, pred.ToString();
        lPossiblePreds.append(pred);
        dStringToPred[pred.ToString()] = pred;
        dIndexToPred[iIndex] = pred;


def PrintPredList(lPreds):
    for pred in lPreds:
        print "Pred:", pred.ToString();


def GenTrainingSamples(sAugmentedGoldSubgoalsFile, sTrainingFile):
    lGold = data.file_to_obj(sAugmentedGoldSubgoalsFile);
    iSubgoalIndex = 0;
    lSamples = [];
    for iIndex, dGold in enumerate(lGold[:min(len(lGold), MAXNUMPROBLEMS)]):
        # skip the ones without the right answer
        print "Running on:", dGold['file'], iIndex, "out of", len(lGold);
        data.print_obj(dGold['subgoals']);
        if ('success' in dGold) and (not dGold['success']):
            continue;
        if len(dGold['subgoals']) < 2:
            print "Skipping:", dGold['file'], 'because no subgoals';
            # if there's no read "sub"-goals, then just skip this one
            continue;
        GenSamplesOneProblem(dGold, lSamples);

    return lSamples;


def PrintAndRun(sCommand, bPrint = True):
    if bPrint:
        print "Running:", sCommand;
    iRetVal= subprocess.call(shlex.split(sCommand));
    print "RetVal is:", iRetVal;
    return iRetVal;

def GetRank(fGoldScore, lScores):
    iRank = 0;
    iTies = 0;
    for fCurScore in lScores:
        if fCurScore > fGoldScore:
            iRank+= 1;
        if fCurScore == fGoldScore:
            iTies += 1;
    return iRank, iTies;


def Evaluate(lSamples, lPreds):
    assert(len(lSamples) == len(lPreds));
    iNumTruePos = 0;
    iNumFalsePos = 0;
    iNumTrueNeg = 0;
    iNumFalseNeg = 0;
    tPrevId = None;
    lScores = [];
    fScoreGold = None;
    iTotalTies = 0;
    iTotalRank = 0;
    iTotalRank0 = 0;
    iTotalNum = 0;
    for iIndex, (sample, fPred) in enumerate(zip(lSamples, lPreds)):
        bGoldPositive = sample.bPositive;
        tId = (sample.sProblemFile, sample.iSubgoalIndex);
        if (not PREDICT_ONLY_LAST) and (tId != tPrevId) and (tPrevId != None):
            assert fScoreGold != None, "Badness at line:" + str(iIndex);
            iRank, iTies = GetRank(fScoreGold, lScores);
            print "Rank:", iRank, "Ties:", iTies, "Num:", len(lScores), "Id:", tPrevId, "Score:", fScoreGold,
            print "Pred:", sGoldPred;
            if iRank == 0:
                iTotalRank0 += 1;
            iTotalTies += iTies;
            iTotalRank += iRank;
            iTotalNum += 1;
            fScoreGold = None;
            lScores = [];
        tPrevId = tId;
        if (not PREDICT_ONLY_LAST) and bGoldPositive:
            assert fScoreGold == None, "Badness at line:" + str(iIndex);
            fScoreGold = fPred;
            sGoldPred = sample.pred.ToString();
        else:
            lScores.append(fPred);

        if fPred > 0:
            if bGoldPositive:
                iNumTruePos += 1;
            else:
                iNumFalsePos += 1;
        else:
            if bGoldPositive:
                iNumFalseNeg += 1;
            else:
                iNumTrueNeg += 1;

    fAvgRank0 = float(iTotalRank0)/float(iTotalNum) if iTotalNum > 0 else 0;
    fAvgRank = float(iTotalRank)/float(iTotalNum) if iTotalNum > 0 else 0;
    fAvgTies = float(iTotalTies)/float(iTotalNum) if iTotalNum > 0 else 0;
    print "Avg Rank:", fAvgRank, "Ties:", fAvgTies, "Avg Rank 0:", fAvgRank0;
    fPrecision = float(iNumTruePos)/(iNumTruePos+iNumFalsePos) if (iNumTruePos > 0) else 0;
    fRecall = float(iNumTruePos)/(iNumTruePos+iNumFalseNeg) if (iNumTruePos > 0) else 0;
    print "Precision:", fPrecision, "Recall:", fRecall, "Nums: tp:", iNumTruePos, "fp:", iNumFalsePos, 
    print "tn:", iNumTrueNeg, "fn:", iNumFalseNeg;

def TrainSvm(lSamples, sTrainFile, sModelFile):
    Sample.WriteSamplesToSvmLightFile(lSamples, open(sTrainFile, 'w'));
    iRetVal = PrintAndRun("../../bin/svm_perf_learn -c 10 -w 3 -l 1 -b 0 " + sTrainFile + " " + "model.svm");

def TestSvm(sTestFile, sModelFile, sPredFile):
    iRetVal = PrintAndRun("../../bin/svm_perf_classify " + sTestFile + " " + sModelFile + " " + sPredFile);
    sPredLines = open(sPredFile).readlines();
    lPreds  = map(lambda x:float(x), sPredLines);
    return lPreds;

def ExtractInitGoalPreds(sProblemPath, sDomainFile, sGoldSubgoalsFile, sAugmentedGoldSubgoalsFile):
    lGold = data.file_to_obj(sGoldSubgoalsFile);
    for dGold in lGold[:min(len(lGold), MAXNUMPROBLEMS)]:
        sProblemFile = sProblemPath + dGold['file'];
        domain = pddl.Domain(sDomainFile, sProblemFile, 0);
        lInitPreds = Predicate.GetInitPredList(domain);
        lGoalPreds = Predicate.GetGoalPredList(domain);
        dGold['init'] = lInitPreds;
        dGold['goal'] = lGoalPreds;
    data.obj_to_file(lGold, sAugmentedGoldSubgoalsFile);

def Main():
    # generate features for each prediate
    #GenFeatures(fgen);
    sPredicateFile = '../subgoal_learning/data/pred_gold.fixed';
    if USE_TEXT_CONNECTIONS:
        sConnectionFile = '../subgoal_learning/data/pred_text_connections.fixed_to_gold';
    else:
        sConnectionFile = '../subgoal_learning/data/pred_gold_connections.fixed';
    sGoldSubgoalsFile = 'subgoals_gold.json';
    sAugmentedGoldSubgoalsFile = 'subgoals_gold_augmented.json';
    sProblemPath = '../subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources/';
    sDomainFile = '../subgoal_learning/data/domain-no-stone-iron-tools.v120.pddl';
    sSamplesFile = 'samples.json';

    ReadPreds(sPredicateFile);
    ReadConnections(sConnectionFile);

    sTrainFile = 'train.svm';
    sModelFile = 'model.svm';
    sPredFile = 'pred.svm';
    #ExtractInitGoalPreds(sProblemPath, sDomainFile, sGoldSubgoalsFile, sAugmentedGoldSubgoalsFile);
    lSamples = GenTrainingSamples(sAugmentedGoldSubgoalsFile, sTrainFile);
    #data.obj_to_file(lSamples, sSamplesFile);
    #lSamples = data.file_to_obj(sSamplesFile);
    if SVM:
        TrainSvm(lSamples, sTrainFile, sModelFile);
        lPreds = TestSvm(sTrainFile, sModelFile, sPredFile);
    else:
        # log-linear
        lPreds = TrainAndTestLogLinear(lSamples);

    Evaluate(lSamples, lPreds);
    

Main();
