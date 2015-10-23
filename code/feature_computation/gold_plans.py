#!/usr/bin/python

import collections
import data
import pddl
import os
import sys
import predicate
import math

import SubgoalValidator;
import numpy as np;

# class deptree:
#     def __init__(self, dNodes):
#         self.lChildren = [];
#         self.dNodes = dNodes;
        


# def ReadDeps(sFilename):
#     lLines = open(sFilename).readlines();
#     for sLine in lLines


# so main question is how to get the none back
# so I 

def GenSubgoals(dDeps, sObjective, iNumNeeded, dAvailable = None, bGoal = True):
    if dAvailable == None:
        dAvailable = collections.defaultdict(lambda:0);
    #print "Calling Gen:", sObjective, iNumNeeded, 'with:', dAvailable[sObjective];
    lSubgoals = [];
    if sObjective not in dDeps:
        #print "\t", sObjective, "not in deps";
        dAvailable[sObjective] = iNumNeeded;
    else:
        #print "Found: ", sObjective, "in dDeps with dict:";
        #data.print_obj(dDeps[sObjective]);
        iNumProducedOneCopy = dDeps[sObjective]['num'];
        iNumCopies = int(math.ceil(float(iNumNeeded)/float(iNumProducedOneCopy)));
        iNumProduced = iNumProducedOneCopy*iNumCopies;
        for sPre, iNumPre in sorted(dDeps[sObjective].items()):
            if sPre == 'num':
                continue;
            iActualNumPre = iNumPre*iNumCopies if iNumPre != -1 else 1;
            if dAvailable[sPre] < iActualNumPre:
                lCurSubgoals = GenSubgoals(dDeps, sPre, iActualNumPre, dAvailable, False);
            else:
                lCurSubgoals = [];

            assert dAvailable[sPre] >= iNumPre, "Not enough: " + sPre + " " + str(dAvailable[sPre]) + \
                " instead of " + str(iNumPre);

            if iNumPre != -1:
                dAvailable[sPre] -= iActualNumPre;
            lSubgoals.extend(lCurSubgoals);
        #print "\t", sObjective, "setting available to:", iNumProduced;
        dAvailable[sObjective] += iNumProduced;
    
    #if not bGoal:
    if True:
        lSubgoals.append({sObjective:min(dAvailable[sObjective],iNumNeeded)});
    #print "Returning from:", sObjective, iNumNeeded, ' with:', dAvailable[sObjective];
    return lSubgoals;
        

def GetOneObjective(sDomainFile, sProblemFile):
    #sDomainFile = '../subgoal_learning/data/domain-no-farmland.v120.pddl';
    #sProblemFile = '../subgoal_learning/data/problems/fence.19.pddl';
    domain = pddl.Domain(sDomainFile, sProblemFile, 0);
    tObjective = domain.GetObjective();
    return tObjective;

def FixObjectives(sInFile, sOutFile):
    lOldObjectives = data.file_to_obj(sInFile);
    lNewObjectives = [];
    for tObjective in lOldObjectives:
        lObjective = [tObjective[0], tObjective[1]+1];
        lNewObjectives.append(lObjective);
    data.obj_to_file(lNewObjectives,sOutFile);

def GetAllObjectives(sDomainFile, sDir):
    #dir = open(sDir);
    lObjectives = [];
    for item in os.listdir(sDir):
        if (item.startswith('test.0.pddl') or
            item.startswith('tallgrass.34.pddl')):
            continue;
        sFullPath = sDir+item;
        print "objective for:", item;
        if os.path.isfile(sFullPath):
            tObjective = GetOneObjective(sDomainFile, sFullPath);
            print item, tObjective;
            lObjectives.append([item, tObjective[0], tObjective[1]]);
    data.obj_to_file(lObjectives, 'objectives.json');

def Run3():
    dDeps = data.file_to_obj_with_comments('dep.json');
    lSubgoals = GenSubgoals(dDeps, "fish", 1);
    data.print_obj(lSubgoals);

def TransformToValidateFormat(lSubgoals):
    lSubgoalsToValidate = [];
    for dSubgoal in lSubgoals:
        tSubgoal = dSubgoal.items()[0];
        
        if tSubgoal[1] == -1:
            iNum = 0;
        else:
            iNum = tSubgoal[1]-1;
        #for iCurNum in range(iNum+1):
        for iCurNum in range(iNum, iNum+1):
            if tSubgoal[0] == 'furnace-fuel':
                sSubgoal = '(> (furnace-fuel) ' + str(iCurNum) + ')';
            else:
                sSubgoal = '(> (thing-available ' + tSubgoal[0] + ') ' + str(iCurNum) + ')';
            lSubgoalsToValidate.append(sSubgoal);
    return lSubgoalsToValidate;


def HashStrInt(sStr, iInt):
    #return sStr + ':' + str(iInt)
    return sStr;

def FormatSubgoal(dSubgoal):
    tSubgoal = dSubgoal.items()[0];
    sThing = tSubgoal[0];
    if sThing == 'furnace-fuel':
        sStr= 'furnace-fuel';
    else:
        sStr = 'thing-available ' + tSubgoal[0];
    if tSubgoal[1] == -1:
        iNum = 0;
    else:
        iNum = tSubgoal[1]-1;
    return (sStr, iNum, HashStrInt(sThing, iNum+1));


def WriteConnectionsFile(dDeps, dPredToIndex, dIndexToPred, sFileName):
    fConnections = open(sFileName, 'w');
    for sTo, dFrom in dDeps.items():
        sToHash = HashStrInt(sTo, dFrom['num']);
        if sToHash not in dPredToIndex:
            print "Skipping:", sToHash;
            continue;
        lTo = dPredToIndex[sToHash];
        for sFrom, iNum in dFrom.items():
            if sFrom == 'num':
                continue;
            sFromHash = HashStrInt(sFrom, iNum);
            lFrom = dPredToIndex[sFromHash];
            for iTo in lTo:
                for iFrom in lFrom:
                    sOutput  = '1|' + str(iFrom) + '|' + str(iTo) + '|' + dIndexToPred[iFrom] + '|' + dIndexToPred[iTo];
                    print >> fConnections, sOutput;

def WriteConnectionsFileNew(dDeps, dPredSimpleStringToPred, sFileName):
    fConnections = open(sFileName, 'w');
    for sTo, dFrom in dDeps.items():
        predTo = predicate.Predicate();
        predTo.FromThingAvailableNameAndNum(sTo, dFrom['num']);
        if predTo.ToSimpleString() not in dPredSimpleStringToPred:
            print "Skipping:", predTo.ToSimpleString();
            continue;
        lTo = dPredSimpleStringToPred[predTo.ToSimpleString()];
        for sFrom, iNum in dFrom.items():
            if sFrom == 'num':
                continue;
            predFrom = predicate.Predicate();
            predFrom.FromThingAvailableNameAndNum(sFrom, iNum);
            lFrom = dPredSimpleStringToPred[predFrom.ToSimpleString()];
            for predCurTo in lTo:
                for predCurFrom in lFrom:
                    sOutput  = '1|' + str(predCurFrom.iIndex) + '|' + str(predCurTo.iIndex) + '|' + predCurFrom.ToString() + '|' + predCurTo.ToString();
                    print >> fConnections, sOutput;

def WriteConnectionsFileFromMatrix(lPreds, mConnDepth, sFileName):
    fConnections = open(sFileName, 'w');
    for iFrom, predFrom in enumerate(lPreds):
        for iTo, predTo in enumerate(lPreds):
            iDepth = mConnDepth[iFrom][iTo];
            if iDepth != sys.maxint:
                sOutput  = (str(int(iDepth)) + '|' + str(predFrom.iIndex) + '|' + str(predTo.iIndex) + '|' + 
                            predFrom.ToString() + '|' + predTo.ToString());
                print >> fConnections, sOutput;



def GenConnectionMatrix(dDeps, lPreds, bLoose):
    iSize = len(lPreds);
    mConnDepth = np.ones((iSize, iSize))*sys.maxint;
    for iFrom, predFrom in enumerate(lPreds):
        sFromObject = predFrom.GetObject();
        iFromNum = predFrom.fValue+1;
        for iTo, predTo in enumerate(lPreds):
            sToObject = predTo.GetObject();
            iToNum = predTo.fValue+1;
            if (sToObject in dDeps):
                dFrom = dDeps[sToObject];
                iDepTo = dFrom['num'] if dFrom['num'] != -1 else 1;
                if (sFromObject in dFrom):
                    if bLoose:
                        # loosely connected
                        mConnDepth[iFrom][iTo] = 1;
                    else:
                        iDepFrom = dFrom[sFromObject] if dFrom[sFromObject] != -1 else 1;
                        if (iDepTo == iToNum) and (iDepFrom == iFromNum):
                            # excactly connected
                            mConnDepth[iFrom][iTo] = 1;
                    
                # if (iDepTo == iToNum) and (sFromObject in dFrom):
                #     iDepFrom = dFrom[sFromObject] if dFrom[sFromObject] != -1 else 1;
                #     if (iFromNum == iDepFrom):
                #         mConnDepth[iFrom][iTo] = 1;
    return mConnDepth;

def ComputeShortestPath(mConnDepth):
    iSize = mConnDepth.shape[0];
    for k in range(iSize):
        for i in range(iSize):
            for j in range(iSize):
                mConnDepth[i][j] = min(mConnDepth[i][j], mConnDepth[i][k] + mConnDepth[k][j]);


def WriteConnectionsFromDictAndDeps(sPredDictFile, sDepsFile, sExactConnectionsFile, sLooseConnectionsFile):
    dDeps = data.file_to_obj_with_comments('dep.json');
    lPreds = predicate.PredDictFileToPredList(sPredDictFile);
    mConnDepthLoose = GenConnectionMatrix(dDeps, lPreds, bLoose = True);
    mConnDepthExact = GenConnectionMatrix(dDeps, lPreds, bLoose = False);
    #ComputeShortestPath(mConnDepth);
    WriteConnectionsFileFromMatrix(lPreds, mConnDepthLoose, sLooseConnectionsFile);
    WriteConnectionsFileFromMatrix(lPreds, mConnDepthExact, sExactConnectionsFile);
    
def GenerateIndexesFromPredDict(sPredDict, setObjectives):
    fPredDict = open(sPredDict, 'w');
    dIndexToPred = {};
    dPredToIndex = collections.defaultdict(lambda:[]);
    for iIndex, tSubgoal in enumerate(setObjectives):
        print >> fPredDict, str(iIndex) + '|' + str(tSubgoal[1]+1) + '|' + tSubgoal[0];
        dPredToIndex[tSubgoal[2]].append(iIndex);
        dIndexToPred[iIndex] = tSubgoal[2] + ':' + str(tSubgoal[1]+1);
    return dIndexToPred, dPredToIndex;


def ValidateTest():
    sDomainFile = '../subgoal_learning/data/domain-no-stone-iron-tools.v120.pddl';
    sProblemFile = '../subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources/wood.36.pddl'
    sFFPath = '/home/nkushman/hierarchical_planning/ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/lhla_v4 /home/nkushman/hierarchical_planning/model/subgoal_learning/run_compute_end_state.cfg';
    


def ValidateAll():
    sDomainFile = '../subgoal_learning/data/domain-no-stone-iron-tools.v120.pddl';
    sProblemPath = '../subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources/'
    sFFPath = '/home/nkushman/hierarchical_planning/ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/lhla_v4 /home/nkushman/hierarchical_planning/model/subgoal_learning/run_compute_end_state.cfg';
    lDicts = data.file_to_obj('subgoals_gold_augmented.json');
    for dInfo in lDicts:
        lSubgoalsToValidate1 = [];
        lSubgoalsToValidate2 = [ '(> (thing-available wood-pickaxe) 0)'];
        lSubgoalsToValidate3 = [ '(> (thing-available wood-pickaxe) 0)',
                                  '(> (thing-available stone) 7)'];
        lSubgoalsToValidate4 = [ '(> (thing-available wood-pickaxe) 0)',
                                  '(> (thing-available stone) 7)', 
                                  '(> (thing-available ironore) 2)',
                                  '(> (thing-available iron) 2)'];
        

        print >> open('test.tmp', 'w'), data.obj_to_string(dInfo);
        item = dInfo['file'];
        if (item.startswith('test.0.pddl') or
            item.startswith('tallgrass.34.pddl')):
            continue;
        #if not item.startswith('iron.30.pddl'):
        #    continue;
        sFullPath = sProblemPath+item;
        print "objective for:", item;
        sGoal = dInfo['subgoals-formatted'][-1];
        lSubgoalsToValidate1.append(sGoal);
        lSubgoalsToValidate2.append(sGoal);
        lSubgoalsToValidate3.append(sGoal);
        lSubgoalsToValidate4.append(sGoal);
        print "Goal:", sGoal;

        bSuccess1 = False;
        bSuccess2 = False;
        bSuccess3 = False;
        bSuccess4 = False;
        if os.path.isfile(sFullPath):
            sTempProblemPath = 'tmp-validate-all/' + item + '.subgoals1';
            #bSuccess1 = SubgoalValidator.TestSubgoals(sDomainFile, sFullPath, lSubgoalsToValidate1,
            #                                         sFFPath, sMainPath, sTempProblemPath, bOptimize = False);
            bSuccess1 = False;
            if not bSuccess1:
                sTempProblemPath = 'tmp-validate-all/' + item + '.subgoals2';
                bSuccess2 = SubgoalValidator.TestSubgoals(sDomainFile, sFullPath, lSubgoalsToValidate2,
                                                          sFFPath, sMainPath, sTempProblemPath, bOptimize = False,
                                                          iLimitSecs = 10);
                if not bSuccess2:
                    sTempProblemPath = 'tmp-validate-all/' + item + '.subgoals3';
                    bSuccess3 = SubgoalValidator.TestSubgoals(sDomainFile, sFullPath, lSubgoalsToValidate3,
                                                              sFFPath, sMainPath, sTempProblemPath, bOptimize = False,
                                                              iLimitSecs = 10);
                    if not bSuccess3:
                        sTempProblemPath = 'tmp-validate-all/' + item + '.subgoals4';
                        bSuccess4 = SubgoalValidator.TestSubgoals(sDomainFile, sFullPath, lSubgoalsToValidate4,
                                                                  sFFPath, sMainPath, sTempProblemPath,bOptimize = False,
                                                                  iLimitSecs = 10);
            bOverall = bSuccess1 or bSuccess2 or bSuccess3 or bSuccess4;
            print "File:", sFullPath, "Success:", bOverall, "1:", bSuccess1, "2:", bSuccess2, "3:", bSuccess3, "4:", bSuccess4;
            sys.stdout.flush();

        

def WriteNumSubgoalsFile(lOutput, sNumSubgoalsFile):
    fNumSubgoals = open(sNumSubgoalsFile, 'w');
    for dOutput in lOutput:
        sOut = dOutput['file'] + '|' + str(len(dOutput['subgoals-formatted'])-1);
        print >> fNumSubgoals, sOut;


def GetSubgoalsForAll(bValidate, bRebuildObjectives):
    sDomainFile = '../subgoal_learning/data/domain-no-stone-iron-tools-simple-furnace.v120.pddl';
    sProblemPath = '../subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources-rand2/'
    sFFPath = '/home/nkushman/hierarchical_planning/ff/metric-ff-recompiled-2011-11-24-2';
    sMainPath = '/home/nkushman/hierarchical_planning/model/subgoal_learning/lhla_v4 /home/nkushman/hierarchical_planning/model/subgoal_learning/run_compute_end_state.cfg';
    sNumSubgoalsFile = 'thing-available_max5.gold_num_subgoals';
    dDeps = data.file_to_obj_with_comments('dep.json');
    if bRebuildObjectives:
        GetAllObjectives(sDomainFile, sProblemPath);
    lObjectives = data.file_to_obj('objectives.json');
    setObjectives = set();
    lOutput = [];
    for iIndex, tObjective in enumerate(lObjectives):
        dCurOutput = {'file':tObjective[0], 'thing':tObjective[1], 'num':tObjective[2]}
        if iIndex < 0:
            print "Skipping:", iIndex, tObjective;
            continue;
        sys.stdout.flush();
        print "****Objective:", iIndex, tObjective;
        lSubgoals = GenSubgoals(dDeps, tObjective[1], tObjective[2]);
        lSubgoalsToValidate = TransformToValidateFormat(lSubgoals);
        print "Plan:";
        data.print_obj(lSubgoalsToValidate);
        sTempProblemPath = 'tmp-no-shovel/test.' + tObjective[0] + '.subgoals';
        if bValidate:
            bSuccess = SubgoalValidator.TestSubgoals(sDomainFile, sProblemPath + tObjective[0], lSubgoalsToValidate,
                                                     sFFPath, sMainPath, sTempProblemPath, bOptimize = False);
            dCurOutput['success'] = bSuccess;
            print "Success:", bSuccess;
        # include them all
        for dSubgoal in lSubgoals:
            setObjectives.add(FormatSubgoal(dSubgoal));

        dCurOutput['subgoals'] = lSubgoals;
        dCurOutput['subgoals-formatted'] = lSubgoalsToValidate;
        dCurOutput['index'] = iIndex;
        lOutput.append(dCurOutput);
        #data.print_obj(lSubgoals);
    data.obj_to_file(lOutput, 'subgoals_gold.json');
    dIndexToPred, dPredToIndex = GenerateIndexesFromPredDict('pred_gold.txt', setObjectives);
    WriteConnectionsFile(dDeps, dPredToIndex, dIndexToPred, 'pred_gold_connections.txt');
    WriteNumSubgoalsFile(lOutput, sNumSubgoalsFile);

def AnalyzePlans():
    lCompleted = map(lambda sLine: sLine.strip(), open('gold_completed.txt').readlines());
    lSubgoalDicts = data.file_to_obj('subgoals_gold.json');
    fSuccess = open('success.txt', 'w');
    fFailed = open('fail.txt', 'w');
    for dSubgoal in lSubgoalDicts:
        sName = dSubgoal['file'].split('.')[0];
        sLine = dSubgoal['file'];
        for dObj in dSubgoal['subgoals']:
            sObj = dObj.keys()[0];
            sLine += ' ' + sObj;
        if sName in lCompleted:
            print >> fSuccess, sLine;
        else:
            print >> fFailed, sLine;



def ConnFileToPairSet(sConnFile, dIndexToPred, iOffset):
    lLines = open(sConnFile).readlines();
    setConnPairs = set();
    for sLine in lLines:
        lSplit = sLine.split('|');
        predFrom = dIndexToPred[int(lSplit[iOffset])];
        predTo = dIndexToPred[int(lSplit[iOffset+1])];
        setConnPairs.add((predFrom, predTo));
    return setConnPairs;


def PairSetToConnFile(setConnPairs, sConnFile):
    fConnFile = open(sConnFile, 'w');
    for predFrom, predTo in setConnPairs:
        print >> fConnFile, '1|' + str(predFrom.iIndex) + '|' + str(predTo.iIndex) + '|' + predFrom.ToString() + '|' + predTo.ToString();



def ConnectionIntersection(sDictFile, sConnFileIn1, iOffset1, sConnFileIn2, iOffset2, sConnFileOut):
    lPreds = predicate.PredDictFileToPredList(sDictFile);
    print "ReadDict";
    dIndexToPred = {};
    for pred in lPreds:
        dIndexToPred[pred.iIndex] = pred;
    print "Genned Index"
    setConnPairsIn1 = ConnFileToPairSet(sConnFileIn1, dIndexToPred, iOffset1);
    print "Read conn1:", len(setConnPairsIn1);
    setConnPairsIn2 = ConnFileToPairSet(sConnFileIn2, dIndexToPred, iOffset2);
    print "Read conn2:", len(setConnPairsIn2);
    
    setConnPairsOut = setConnPairsIn1.intersection(setConnPairsIn2);
    print "Genned intersection:", len(setConnPairsOut);
    PairSetToConnFile(setConnPairsOut, sConnFileOut);
    print "Done";


def Run2():
    #dDeps = data.file_to_obj_with_comments('dep.json');
    #lSubgoals = GenSubgoals(dDeps, 'stone-pickaxe', 1);
    #data.print_obj(lSubgoals);
    #GetAllObjectives('../subgoal_learning/data/domain-no-shovel.v120.pddl',
    #                 '../subgoal_learning/data/problems/no-stone-iron-tools-and-extra-resources/');
    #FixObjectives('objectives.json', 'objectives-new.json');
    #GetSubgoalsForAll(bValidate=False, bRebuildObjectives=False);
    #WriteConnectionsFromDictAndDeps('../subgoal_learning/data/thing-available_max5.dict', 'deps.json', 
    #                                'thing-available_max5.gold_conn_one_hop_exact', 'thing-available_max5.gold_conn_one_hop_loose');
    #AnalyzePlans();
    #ValidateAll();
    ConnectionIntersection('../subgoal_learning/data/thing-available_max5.dict',
                           '../subgoal_learning/data/thing-available_max5.full_conn_text_features', 2,
                           '../subgoal_learning/data/thing-available_max5.gold_conn_one_hop_loose', 1,
                           'thing-available_max5.gold_loose_text_overlap_conn');


def Run():
    for action in domain.lActions:
        print action.sName;
        action.GetThingAvailablePost();
        action.GetThingAvailablePre();

def test_json():
    dNate = {};

    dNate[0] = [{1:3, 2:4},2,3];
    dNate[5] = [4,5,6];

    data.obj_to_file(dNate, "test.json");


Run2();
