import config
import Sample
import subprocess;
import shlex;
import sys
import collections
import math
import os

def PrintAndRun(sCommand, bSuppress = False):
    if not bSuppress:
        print "Running:", sCommand;
        iRetVal= subprocess.call(shlex.split(sCommand));
        print "RetVal is:", iRetVal;
    else:
        iRetVal = os.system(sCommand + ' > /tmp/tmp.out');
    return iRetVal;


def Train(lSamples, j = 1, bSuppress = False):
    sTrainFile = config.get_string('SVM_TRAIN');
    sModelFile = config.get_string('SVM_MODEL');

    Sample.WriteSvmFile(lSamples, sTrainFile);
    if config.get_bool('USE_SVM_PERF'):
        # version used for good svm results
        iRetVal = PrintAndRun("../../bin/svm_perf_learn -c 10 -w 3 -l 1 -b 0 " + sTrainFile + " " + "model.svm", bSuppress = bSuppress);
        #iRetVal = PrintAndRun("../../bin/svm_perf_learn -c 1 -w 3 -l 1 -b 0 " + sTrainFile + " " + "model.svm");
    else:
        iRetVal = PrintAndRun("../../bin/svm_learn -c 10 -b 0 -m 1000 -j " + str(j) + ' ' + sTrainFile + " " + "model.svm", bSuppress = bSuppress);

def Test(lSamples, bSuppress = False):
    sTestFile = config.get_string('SVM_TEST');
    sModelFile = config.get_string('SVM_MODEL');
    sPredFile = config.get_string('SVM_PRED');

    Sample.WriteSvmFile(lSamples, sTestFile);
    if config.get_bool('USE_SVM_PERF'):
        iRetVal = PrintAndRun("../../bin/svm_perf_classify " + sTestFile + " " + sModelFile + " " + sPredFile, bSuppress = bSuppress);
    else:
        iRetVal = PrintAndRun("../../bin/svm_classify " + sTestFile + " " + sModelFile + " " + sPredFile, bSuppress = bSuppress);
    sPredLines = open(sPredFile).readlines();
    lPreds  = map(lambda x:float(x), sPredLines);
    assert (len(lPreds) == len(lSamples));
    for pred, sample in zip(lPreds, lSamples):
        sample.fPred = float(pred);


def AnalyzePreds(lSamples, lPreds, lFeatureWeights = None, sOutFile = None, fThreshold=0.0, bPrintExtraThresholds = True, sDebugFile = None,
                 bConsiderMultipleThresholds = False):
    assert(((lFeatureWeights == None) and (sDebugFile == None)) or ((lFeatureWeights != None) and (sDebugFile != None)));
    assert len(lSamples) == len(lPreds);
    mResults = np.zeros((NUM_CLASSES, NUM_CLASSES));
    if sOutFile != None:
        fOut = open(sOutFile, 'w');
    if sDebugFile != None:
        fDebug = open(sDebugFile, 'w');
    fPrevThreshold = 1.0;
    if SVM:
        lThres = [0.0];
    else:
        lThres = [0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001]

    fMaxFScore = 0.0;
    fMaxPrec = 0.0;
    fMaxRecall = 0.0;
    for iIter, fThreshold in enumerate(lThres):
        iNumTotal = 0;
        iNumCorrect = 0;
        iTruePos = 0;
        iFalsePos = 0;
        iTrueNeg = 0;
        iFalseNeg = 0;
        if sDebugFile != None:
            print >> fDebug, 'Threshold:', fThreshold, 'Prev:', fPrevThreshold;
        for sample, fPred in zip(lSamples, lPreds):
            if fPred > fThreshold and fPred <= fPrevThreshold and sDebugFile != None:
                if sample.bPos:
                    print >> fDebug, '******POSITIVE SAMPLE****** Pred:', fPred;
                else:
                    print >> fDebug, '******NEG SAMPLE****** Pred:', fPred;
                    
                sample.PrintDebugInfo(fDebug, lFeatureWeights);
            if sOutFile != None and iIter == 0:
                print >> fOut, sample.bPos, fPred;
            iPredType = TYPE_GOOD if float(fPred) > fThreshold else TYPE_BAD;
            iActualType = sample.GetType();
            mResults[iPredType, iActualType] += 1;
            iNumTotal += 1;
            if iPredType == iActualType:
                iNumCorrect += 1;
            if iPredType == TYPE_GOOD:
                if iActualType == TYPE_GOOD:
                    iTruePos += 1;
                else:
                    iFalsePos += 1;
            else:
                if iActualType == TYPE_GOOD:
                    iFalseNeg += 1;
                else:
                    iTrueNeg += 1;
        fPrevThreshold = fThreshold;
            
        fPrecision = float(iTruePos)/float(iTruePos+iFalsePos) if iTruePos > 0 else 0;
        fRecall = float(iTruePos)/float(iTruePos+iFalseNeg) if iTruePos > 0 else 0;
        fScore = 2*fPrecision*fRecall/(fPrecision+fRecall) if (fPrecision*fRecall) > 0 else 0;
        #fMaxFScore = max(fMaxFScore, fScore);
        if fMaxFScore < fScore:
            fMaxFScore, fMaxPrec, fMaxRecall = (fScore, fPrecision, fRecall);
        print "FScore:", fScore, fPrecision, fRecall;
        print "Frac Correct:", float(iNumCorrect)/float(iNumTotal), iNumCorrect, iNumTotal;
        print "Threshold:", fThreshold, "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
        print_matrix(mResults);
#   return fMaxFScore;
    return (fMaxFScore, fMaxPrec, fMaxRecall);


def GetNormalizedWeights():
    fThreshold, dFeatureWeights = GetWeights();
    dNormalizedFeatureWeights = collections.defaultdict(lambda:0);
    fNorm = math.sqrt(reduce(lambda x, y: x + math.pow(y,2), dFeatureWeights.values(), 0));
    
    for iFeature, fWeight in dFeatureWeights.items():
        dNormalizedFeatureWeights[iFeature] = float(fWeight)/fNorm;
        
    return (fThreshold, dNormalizedFeatureWeights);

def GetWeights():
    sModelFile = 'model.svm';
    sLines = open(sModelFile).readlines();
    # get the highest feature index from line 7(8)                              
    iMaxFeature = int(sLines[7].split()[0]);
    #iMaxFeature = GetNumFeatures(sLines[11]);                                  
    fThreshold = float(sLines[10].split()[0]);
    dFeatureWeights = collections.defaultdict(lambda:0);
    #lFeatureWeights = [0 for i in range(iMaxFeature+1)];
    # the first few lines are just metadata so skip them                        
    for sLine in sLines[11:]:
        lLine = sLine.split();
        fMult = float(lLine[0]);
        for sFeature in lLine[1:]:
            # check if we've hit the comment                                    
            if "#" == sFeature:
                break;
            (iFeature, fWeight) = sFeature.split(':');
            dFeatureWeights[int(iFeature)] += fMult*float(fWeight);

    # the 0th feature and max feature don't really exist                        
    #lFeatureWeights = lFeatureWeights[1:iMaxFeature-1];
    return (fThreshold, dFeatureWeights);



# def AnalyzePredsSimple(lSamples):
#     if config.get_bool('FORCE_SINGLE_DIR'):
#         dSamples = {};
#         for sample in lSamples:
#             tKey = (sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo);
#             assert(tKey not in dSamples);
#             dSamples[tKey] = sample;

#     iNumTotal = 0;
#     iNumCorrect = 0;
#     iTruePos = 0;
#     iFalsePos = 0;
#     iTrueNeg = 0;
#     iFalseNeg = 0;
#     iThres = 0;
#     if config.get_bool('SVM'):
#         fThres = 0;
#     elif config.get_bool('LOG_LINEAR'):
#         fThres = 0.5
#     else:
#         assert False;

#     for sample in lSamples:
#         bActual = sample.GetPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_EVAL'));
#         if config.get_bool('FORCE_SINGLE_DIR'):
#             fPred = sample.fPred;
#             tReverseKey = (sample.pddlconn.sPddlTo, sample.pddlconn.sPddlFrom);
#             fReversePred = dSamples[tReverseKey].fPred if tReverseKey in dSamples else -sys.maxint;
#             bNormalPred = (float(sample.fPred) > fThres);
#             bPred = ((float(sample.fPred) > fThres) and (float(fPred) >= float(fReversePred)));
#             if tReverseKey not in dSamples:
#                 print "FORCE-MISSING";
#             elif (bNormalPred == bActual) and (bPred != bActual):
#                 print "FORCE-BAD:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
#             elif  (bNormalPred != bActual) and (bPred == bActual):
#                 print "FORCE-GOOD:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
#             else:
#                 print "FORCE-NEITHER:", sample.pddlconn.sPddlFrom, sample.pddlconn.sPddlTo, fPred, fReversePred;
#         else:
#             bPred = sample.GetPredPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_EVAL'));
                

#         iNumTotal += 1;
#         if bPred == bActual:
#             iNumCorrect += 1;
#         if bPred:
#             if bActual:
#                 iTruePos += 1;
#             else:
#                 iFalsePos += 1;
#         else:
#             if bActual:
#                 iFalseNeg += 1;
#             else:
#                 iTrueNeg += 1;
#     fPrecision = float(iTruePos)/float(iTruePos+iFalsePos) if iTruePos > 0 else 0;
#     fRecall = float(iTruePos)/float(iTruePos+iFalseNeg) if iTruePos > 0 else 0;
#     fScore = 2*fPrecision*fRecall/(fPrecision+fRecall) if (fPrecision*fRecall) > 0 else 0;
#     print "FScore:", fScore, fPrecision, fRecall;
#     print "Frac Correct:", float(iNumCorrect)/float(iNumTotal), iNumCorrect, iNumTotal;
#     print "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
#     return fScore, fPrecision, fRecall;



def GenFeatureWeightsFile(sModelFile, sWeightsFile):
    fWeights = open(sWeightsFile, 'w');
    fThreshold, lFeatureWeights = GetWeightsFromSvmModel(sModelFile);
    lFeatureWeightTups = [];
    dFeatureWeights = {};
    print >> fWeights, "NUM Features:", len(lFeatureWeights);
    for iFeature, iFeatureWeight in enumerate(lFeatureWeights):
        if (iFeature == 0) or (iFeature == len(lFeatureWeights)-1) or (iFeature >= feature.fgen.iIndex):
            continue;
        lFeatureWeightTups.append((iFeature, iFeatureWeight));
    lSortedFeatureWeightTups = sorted(lFeatureWeightTups, key=lambda tup: tup[1]);
    for iFeature, iFeatureWeight in lSortedFeatureWeightTups:
        sFeature = feature.fgen.dIndexToFeature[iFeature];
        print >> fWeights, "Feature:", iFeature, sFeature, '-->', iFeatureWeight;
        dFeatureWeights[sFeature] = iFeatureWeight;
    return dFeatureWeights;
