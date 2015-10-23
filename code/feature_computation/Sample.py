import FeatureSpace
import Features;
import config
import collections
import sys
import random

class Sample(object):
    def __init__(self):
        pass;

def CalcAllTextPosNeg(lCollapsedSamples):
    iNumPos = reduce(lambda iNum,samp:iNum+1 if samp.bPos else iNum, lCollapsedSamples, 0);
    return iNumPos, len(lCollapsedSamples)-iNumPos;


def WriteSvmFile(lSamples, sFile):
    fOut = open(sFile, 'w');
    for sample in lSamples:
        sLine = sample.GetSvmLine();
        print >> fOut, sLine;

def SamplesToFeatureTups(lSamples):
    lFeatureTups = [];
    for sample in lSamples:
        lFeatureTups.append(sample.ToFeatureTup());
    return lFeatureTups;
    

def CollapseSamples(lGranularSamples):
    dCollapsedSamples = {};
    for gransamp in lGranularSamples:
        key = gransamp.GetCollapsedSampleKey();
        if key not in dCollapsedSamples:
            colsamp = CollapsedSample(gransamp.pddlconn);
            dCollapsedSamples[key] = colsamp;
        dCollapsedSamples[key].AddGranularSample(gransamp);
    return dCollapsedSamples.values();


class CollapsedSample(object):
    def __init__(self, pddlconn):
        self.sPddlFrom = pddlconn.sPddlFrom;
        self.sPddlTo = pddlconn.sPddlTo;
        self.pddlconn = pddlconn;
        self.lGranularSamples = [];
        self.iNumPosReward = 0;
        self.iNumNegReward = 0;
        

    def GetPos(self, bIgnoreDir = False):
        if hasattr(self, '_bPos'):
            return self._bPos;
        # if any one of the granular are pos this is pos
        self._bPos = False;
        for gransamp in self.lGranularSamples:
            if gransamp.GetPos(bIgnoreDir):
                self._bPos = True;
                break;
        return self._bPos;

    def GetGoldPos(self, bIgnoreDir = False):
        if hasattr(self, '_bGoldPos'):
            return self._bGoldPos;
        # if any one of the granular are pos this is pos
        self._bGoldPos = False;
        for gransamp in self.lGranularSamples:
            if gransamp.GetGoldPos(bIgnoreDir):
                self._bGoldPos = True;
                break;
        return self._bGoldPos;

    def GetManualPos(self, bIgnoreDir = False):
        if hasattr(self, '_bManualPos'):
            return self._bManualPos;
        # if any one of the granular are pos this is pos
        self._bManualPos = False;
        for gransamp in self.lGranularSamples:
            if gransamp.GetManualPos(bIgnoreDir):
                self._bManualPos = True;
                break;
        return self._bManualPos;

    def GetPred(self, bIgnoreDir = False):
        if hasattr(self, '_fPred'):
            return self._fPred;
        # if any one of the granular are pos this is pos
        self._fPred = -sys.maxint;
        for gransamp in self.lGranularSamples:
            if gransamp.GetfPred(bIgnoreDir) > self._fPred:
                self._fPred = gransamp.GetfPred(bIgnoreDir);
        return self._fPred;
    
    def SetPred(self, fPred):
        self._fPred = fPred;

    def GetPredPos(self, bIgnoreDir = False):
        if config.get_bool('SVM'):
            fThres = config.get_int('SVM_THRESHOLD');
        elif config.get_bool('LOG_LINEAR'):
            fThres = 0.5
        else:
            assert False;
        return (self.GetPred(bIgnoreDir) > fThres);

    def AssertFalse(self, fNewVal):
        assert False, "This should never be set directly";
    bPos = property(GetPos, AssertFalse);
    fPred = property(GetPred, SetPred);
    bPredPos = property(GetPredPos, AssertFalse);
    bGoldPos = property(GetGoldPos, AssertFalse);
    bManualPos = property(GetManualPos, AssertFalse);


    def PrintDebugInfo(self, fDebug, lFeatureWeights):
        print >> fDebug, "Features:", self.iNumSentences, self.predFrom.ToString(), '-->', self.predTo.ToString();

        fPosScoreTotal = 0;
        fNegScoreTotal = 0;
        for iIndex, fValue in self.dFeatureCounts.items():
            fWeight = lFeatureWeights[iIndex];
            print >> fDebug, "\t", FeatureSpace.FeatureString(iIndex), ':', fValue, ':', fWeight, ':', fValue*fWeight;
            fPosScoreTotal += fValue*fWeight;
            fNegScoreTotal += lFeatureWeights[iIndex+FeatureSpace.MaxIndex()]*fValue;
        fPosPow = math.pow(2,fPosScoreTotal);
        fNegPow = math.pow(2,fNegScoreTotal);
        fDenom = fPosPow + fNegPow;
        print >> fDebug, "CalcedPred:", float(fPosPow)/float(fDenom);
            
        for sentence, setFeatures, conn in self.lSentenceFeatureConnTups:
            fPosScoreTotal = 0;
            fNegScoreTotal = 0;
            print >> fDebug, "Sentence:", conn.iFrom, '-->', conn.iTo, sentence.iIndex, sentence.sText;
            for iFeature in setFeatures:
                fWeight = lFeatureWeights[iFeature];
                print >> fDebug, "\t", FeatureSpace.FeatureString(iFeature), ':', fWeight;
                fPosScoreTotal += fWeight;
                fNegScoreTotal += lFeatureWeights[iFeature+FeatureSpace.MaxIndex()];
            fPosPow = math.pow(2,fPosScoreTotal);
            fNegPow = math.pow(2,fNegScoreTotal);
            fDenom = fPosPow + fNegPow;
            print >> fDebug, "Calced Sentence Pred:", float(fPosPow)/float(fDenom);

    def AddGranularSample(self, gransamp):
        self.lGranularSamples.append(gransamp);

    def GetFeatureCounts(self):
        dFeatureCounts = collections.defaultdict(lambda:0);
        for gransamp in self.lGranularSamples:
            for iFeature in gransamp.features.GetFeatureIndexList():
                dFeatureCounts[iFeature] += 1;
        return dFeatureCounts.items();
    
    def GetFeatureTupList(self):
        #return sorted(list(self.setFeatures));
        if config.get_bool('FEATURES:WEIGHT_COLLAPSE_FIRST_BY_NUM_SENTENCES'):
            return sorted(map(lambda (x,y):(x, float(y)/float(len(self.lGranularSamples))), self.GetFeatureCounts()), key=lambda tup:tup[0]);
        else:
            return sorted(map(lambda (x,y):(x, 1), self.GetFeatureCounts()), key=lambda tup:tup[0]);
            

    def ToFeatureTup(self):
        sIsPositive = "1" if self.bPos else "-1";
        return (self.GetFeatureTupList(), sIsPositive);

    def GetRewardSvmLines(self):
        lLines = [];
        sFeatures = self.GetFeatureString();
        sPosLine = '+1 ' + sFeatures;
        sNegLine = '-1 ' + sFeatures;
        for iIter in range(self.iNumPosReward):
            lLines.append(sPosLine);
        for iIter in range(self.iNumNegReward):
            lLines.append(sNegLine);

    def GetFeatureString(self):
        sLine = '';
        lFeatureTups = self.GetFeatureTupList();
        sFeatureComment = '';
        for iFeatureIndex, iFeatureValue in lFeatureTups:
            sLine += ' ' + str(iFeatureIndex) + ':' + str(iFeatureValue);
            sFeatureComment += ' ' + str(iFeatureIndex) + '->' + FeatureSpace.FeatureString(iFeatureIndex);
        sLine += '# ' + self.sPddlFrom + ' --> ' + self.sPddlTo;
        return sLine;
        
    def GetSvmLine(self):
        sLine = '+1' if self.GetPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_TRAINING')) else '-1'; #str(self.GetType());
        sLine += self.GetFeatureString();
        return sLine;

    def WritePddlConnections(self, fOut):
        for predFrom in self.pddlconn.lFromPreds:
            for predTo in self.pddlconn.lToPreds:
                print >> fOut, '1|' + str(predFrom.iIndex) + '|' + str(predTo.iIndex) + '|' + predFrom.ToString() + '|' + predTo.ToString();

    @staticmethod
    def WriteConnections(lCollapsedSamples, sCollapsedSampleFile, bAppend = False, bWritePredictions = False, bPosOnly = True):
        if not bPosOnly and config.get_float('ALL_TEXT_PRECISION') != 0:
            fAllTextPrecision = config.get_float('ALL_TEXT_PRECISION');
            iPos, iNeg = CalcAllTextPosNeg(lCollapsedSamples);
            fFracNegToWrite = (float(1-fAllTextPrecision)/float(fAllTextPrecision))*float(iPos)/float(iNeg);
            print "Writing All Text with Precision:", fAllTextPrecision, "Raw Precision:", iPos/float(iPos+iNeg), "FracNeg:", fFracNegToWrite;
        else:
            fFracNegToWrite = 1.0;

        print "Writing Positive Collapsed To:", sCollapsedSampleFile;
        if bAppend:
            fOut = open(sCollapsedSampleFile, 'a');
        else:
            fOut = open(sCollapsedSampleFile, 'w');
        for colsamp in lCollapsedSamples:
            if not bPosOnly:
                # write all connections if ALL_TEXT_PRECISION == 0 else write all pos and fFracToWrite fraction of the negs
                if colsamp.bPos or (random.random() <= fFracNegToWrite):
                    colsamp.WritePddlConnections(fOut);
            elif bWritePredictions:
                if colsamp.bPredPos:
                    colsamp.WritePddlConnections(fOut);
            else:        
                if colsamp.bPos:
                    colsamp.WritePddlConnections(fOut);




class GranularSample(object):
    def __init__(self, pddlconn):
        self._bGoldPos = False;
        self.pddlconn = pddlconn;
        self.features = Features.TextFeatures(self);
        self._fPred = -sys.maxint;

    def GetPos(self, bIgnoreDir = False):
        # don't allow same from/to
        if self.pddlconn.textconn.sFrom == self.pddlconn.textconn.sTo:
            return False;
        if bIgnoreDir:
            return self.bPos or self.pddlconn.pddlconnReverse.sample.bPos;
            
        if config.get_bool('TRAIN_ON_GOLD_DEP'):
            assert (not config.get_bool('TRAIN_ON_MANUAL_TEXT_ANNOT'));
            return self.bGoldPos;
        elif config.get_bool('TRAIN_ON_MANUAL_TEXT_ANNOT'):
            return self.bManualPos;
        else:
            assert False;

    def GetGoldPos(self, bIgnoreDir = False):
        # don't allow same from/to
        if self.pddlconn.textconn.sFrom == self.pddlconn.textconn.sTo:
            return False;
        if bIgnoreDir:
            return self.bGoldPos or self.pddlconn.pddlconnReverse.sample.bGoldPos;
        
        return self._bGoldPos;

    def SetGoldPos(self, bGoldPos):
        self._bGoldPos = bGoldPos;

    def GetManualPos(self, bIgnoreDir = False):
        # don't allow same from/to
        if self.pddlconn.textconn.sFrom == self.pddlconn.textconn.sTo:
            return False;
        if bIgnoreDir:
            return self.bManualPos or self.pddlconn.pddlconnReverse.sample.bManualPos;

        return self.pddlconn.textconn.bPos;

    def GetPredPos(self, bIgnoreDir = False):
        if bIgnoreDir:
            return self.bPredPos or self.pddlconn.pddlconnReverse.sample.bPredPos;

        if config.get_bool('SVM'):
            fThres = config.get_int('SVM_THRESHOLD');
        elif config.get_bool('LOG_LINEAR'):
            fThres = 0.5
        else:
            assert False;
        return (self.fPred > fThres);

    def GetfPred(self, bIgnoreDir = False):
        if bIgnoreDir:
            fRetVal =  max(self._fPred, self.pddlconn.pddlconnReverse.sample._fPred);
            assert fRetVal != -sys.maxint;
            return fRetVal;
        
        assert(self._fPred != -sys.maxint);
        return self._fPred;

    def SetfPred(self, fPred):
        assert(fPred != -sys.maxint);
        self._fPred = fPred;

    def AssertFalse(self, fNewVal):
        assert False, "This should never be set directly";

    bPos = property(GetPos, AssertFalse);
    bGoldPos = property(GetGoldPos, SetGoldPos);
    bManualPos = property(GetManualPos, AssertFalse);
    bPredPos = property(GetPredPos, AssertFalse);
    fPred = property(GetfPred, SetfPred);

    def GetCollapsedSampleKey(self):
        return (self.pddlconn.sPddlFrom, self.pddlconn.sPddlTo);

    def GetFeatureTupList(self):
        return sorted(map(lambda x:(x, 1), self.features.GetFeatureIndexList()), key=lambda tup:tup[0]);

    def ToFeatureTup(self):
        sIsPositive = "1" if self.bPos else "-1";
        return (self.GetFeatureTupList(), sIsPositive);

    def GetSvmLine(self):
        sLine = '+1' if self.GetPos(bIgnoreDir = config.get_bool('IGNORE_DIR_FOR_TRAINING')) else '-1'; #str(self.GetType());
        lFeatures = self.features.GetFeatureIndexList();
        sFeatureComment = '';
        for iFeature in lFeatures:
            sLine += ' ' + str(iFeature) + ':1';
            sFeatureComment += ' ' + str(iFeature) + '->' + FeatureSpace.FeatureString(iFeature);
        sLine += ('# conn:' + self.pddlconn.textconn.sText + ' Features: ' + sFeatureComment + 
                  ' ***Sentence--> ' + self.pddlconn.textconn.sentence.sText);
        return sLine;

    def Write(self, fOut, bCollapse = False):
        iSentenceId = self.pddlconn.textconn.sentence.iIndex;
        for sWord in self.features.GetFeatureWordList():
            for predFrom in self.pddlconn.lFromPreds:
                for predTo in self.pddlconn.lToPreds:
                    #print >> fOut, sWord + '|1|' + str(predFrom.iIndex) + '|' + str(predTo.iIndex) + '|' + predFrom.ToString() + '|' + predTo.ToString(); 
                    if bCollapse:
                        sLine = '%s|1|%d|%d' % (sWord, predFrom.iIndex, predTo.iIndex);
                    else:
                        sLine = '%s|1|%d|%d|%d' % (sWord, predFrom.iIndex, predTo.iIndex, iSentenceId);
                    print >> fOut, sLine;

    def WriteDebug(self, fOut):
        print >> fOut, "***********", self.pddlconn.sPddlFrom, '-->', self.pddlconn.sPddlTo, '  ::  ', \
            self.pddlconn.textconn.iFrom, '-->', self.pddlconn.textconn.iTo, '  ::  ', self.pddlconn.textconn.sentence.iIndex;
        print >> fOut, self.pddlconn.textconn.sentence.sText;
        sampleReverse = self.pddlconn.pddlconnReverse.sample;
        print >> fOut, "Manual: ", str(self.bManualPos), "Gold:", str(self.bGoldPos), "ReverseManual: ", \
            sampleReverse.bManualPos, "ReverseGold:", sampleReverse.bGoldPos;
        bHasSubj = False;
        bHasConjAnd = False;
        for iFeature in self.features.GetFeatureIndexList():
            sFeature = FeatureSpace.FeatureString(iFeature);
            print >> fOut, '\t', sFeature;
            bHasSubj |= (sFeature.find('nsubj') != -1);
            bHasConjAnd |= (sFeature.find('conj_and') != -1);
        if (self.bManualPos or sampleReverse.bManualPos) and bHasConjAnd:
            print >> fOut, '\tBADNESS-TYPE1';
        if (self.bManualPos or sampleReverse.bManualPos) and (not bHasSubj):
            print >> fOut, '\tBADNESS-TYPE2';

    @staticmethod
    def WriteList(lGranularSamples, sGranularSampleFile, bCollapse = False):
        print "Writing granular features to:", sGranularSampleFile;
        fOut = open(sGranularSampleFile, 'w');
        for gransamp in lGranularSamples:
            gransamp.Write(fOut, bCollapse);

    @staticmethod
    def WriteDebugFromList(lGranularSamples, sFile):
        print "Writing debug data for granular features to:", sFile;
        fOut = open(sFile, 'w');
        for gransamp in lGranularSamples:
            gransamp.WriteDebug(fOut);

