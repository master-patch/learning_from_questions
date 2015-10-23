#!/usr/bin/python
import data;
import feature;
import subprocess;
import shlex;
import numpy as np;
import random
from nltk.stem.porter import PorterStemmer
import load_parse
import sys
import predicate
import collections
import obj_extract
import string
import nltk.classify.maxent as maxent
import math
import os
import os.path
import draw_dep

# Things to do:
# High level:
#  1.  I want to train on the solutions that I can get out of the gate? so basically I want to train on a set of samples that say that the 
#      gold connections I see are correct and then see how many of the other connections I get right
#      by other connections, I mean other connections that we would predict from the svm
# Low-level:
# 1.  I need to produce a set of samples that includes all the features that are true for a given connection
# 2.  So what I'd like is a matrix of possible connections - generated from the dict
# 3.  for each one I'll list all features associated with it and whether it's positive or not
# 4.  so I think we'll just have a sample for each one
# 1.  read gold data
# 2.  
# 1. Thing to do is to figure out which connections are in the set of 31 that we solve immediately
# 2. let's assume I have a file containing those file names
# 3. no... i don't need subgoals.gold because I don't need that complexit
# 4. I just need objectives.json, which will tell me the objective and then I walk backwards

# things to do:
# 1.  gen the file with the filenames
# 2.  read the file in and walk backwards
# 3.  for each connection, I'll mark it as found in the solutions that we have
# 4.  then when training, I'll randomly split the negatives half train and half test


#####GOLDMAT CONFIG#######

TRAIN_ON_GOLD_DEP = True;
TRAIN_ON_MANUAL_ANNOT = False;
TRAIN_ON_RANDOM_ANNOT = False;
assert(TRAIN_ON_GOLD_DEP + TRAIN_ON_MANUAL_ANNOT + TRAIN_ON_RANDOM_ANNOT == 1);

EVAL_TRAIN_FIRST_30 = True;
EVAL_RANDOM_HALF_HALF = False;
assert(EVAL_TRAIN_FIRST_30 + EVAL_RANDOM_HALF_HALF == 1);

IGNORE_CONNECTION_DIR = False;

SVM = False;
LOG_LINEAR = True;
assert(SVM+LOG_LINEAR == 1);

USE_SVM_PERF = False;

GEN_FEATURE_FREQ_FILE = False;
GEN_CONN_FILE = False;
DONT_GEN_FEATURES_WITH_PDDL_OBJECT_WORDS = True;
#GEN_CONN_FROM_HALF = True;
GEN_CONN_FROM_HALF = False;
GEN_FEATURE_FILE = True;
REMOVE_DUPLICATE_CONNS = False;
POS_FEATURE_WEIGHT_THRES = 1.0;
NEG_FEATURE_WEIGHT_THRES = -1.0;
CROSS_VALIDATE = False;


#########END GOLDMAT CONFIG#################


USE_GOLD_SAMPLES = True

SIMPLE_INPUTS = False;

NUM_ITER = 30;

GEN_FEATURE_WEIGHTS_FILE = True;

ADD_TERMINAL_WORDS = True;
USE_SENTENCE_DIR = True;
USE_NON_SENTENCE_DIR_TOO = True;


TRAIN_AND_TEST_ON_ALL = True;
#TRAIN_AND_TEST_ON_ALL = True;
#TRAIN_ON_HALF_TEST_ON_ALL = True;
TRAIN_ON_HALF_TEST_ON_ALL = False;

USE_STEMMER = False
USE_DEPS = True

USE_POS_TAGS = False
USE_WORD_FEATURES = False

USE_END_WORD_FEATURES = False


USE_PATH_DIR = False;
USE_PATH_DEP_TYPES = True;
USE_PATH_WORDS = True;

ASTERIX_IS_BAD = False;

Stemmer = PorterStemmer();

class GoldSample:
    def __init__(self, predFrom, predTo):
        self.predFrom = predFrom;
        self.predTo = predTo;
        self.bPos = False;
        self.bNoSubgoal = False;
        self.setFeatures = set();
        self.dFeatureCounts = collections.defaultdict(lambda:0);
        self.iNumSentences = 0;
        self.lSentenceFeatureConnTups = [];
        self.lSentences = [];

    def PrintDebugInfo(self, fDebug, lFeatureWeights):
        print >> fDebug, "Features:", self.iNumSentences, self.predFrom.ToString(), '-->', self.predTo.ToString();

        fPosScoreTotal = 0;
        fNegScoreTotal = 0;
        for iIndex, fValue in self.dFeatureCounts.items():
            fWeight = lFeatureWeights[iIndex];
            print >> fDebug, "\t", feature.fgen.dIndexToFeature[iIndex], ':', fValue, ':', fWeight, ':', fValue*fWeight;
            fPosScoreTotal += fValue*fWeight;
            fNegScoreTotal += lFeatureWeights[iIndex+feature.fgen.iIndex]*fValue;
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
                print >> fDebug, "\t", feature.fgen.dIndexToFeature[iFeature], ':', fWeight;
                fPosScoreTotal += fWeight;
                fNegScoreTotal += lFeatureWeights[iFeature+feature.fgen.iIndex];
            fPosPow = math.pow(2,fPosScoreTotal);
            fNegPow = math.pow(2,fNegScoreTotal);
            fDenom = fPosPow + fNegPow;
            print >> fDebug, "Calced Sentence Pred:", float(fPosPow)/float(fDenom);

        
    def GetType(self):
        return TYPE_GOOD if self.bPos else TYPE_BAD;
    
    def AddFeatures(self, setFeatures, sentence, conn):
        self.lSentences.append(sentence);
        self.lSentenceFeatureConnTups.append((sentence, setFeatures, conn));
        #self.setFeatures.update(setFeatures);
        for iFeature in setFeatures:
            self.dFeatureCounts[iFeature] += 1;
        self.iNumSentences += 1;
        
    def GetFeatureTupList(self):
        #return sorted(list(self.setFeatures));
        return sorted(map(lambda (x,y):(x, float(y)/float(self.iNumSentences)), self.dFeatureCounts.items()), key=lambda tup:tup[0]);

    def ToFeatureTup(self):
        sIsPositive = "1" if self.bPos else "-1";
        return (self.GetFeatureTupList(), sIsPositive);

    def GetSvmLine(self):
        sLine = '+1' if self.bPos else '-1'; #str(self.GetType());
        lFeatureTups = self.GetFeatureTupList();
        sFeatureComment = '';
        for iFeatureIndex, iFeatureValue in lFeatureTups:
            sLine += ' ' + str(iFeatureIndex) + ':' + str(iFeatureValue);
            sFeatureComment += ' ' + str(iFeatureIndex) + '->' + feature.fgen.dIndexToFeature[iFeatureIndex];
        sLine += '# ' + self.predFrom.ToString() + ' --> ' + self.predTo.ToString();
        return sLine;


class Sample:
    def __init__(self):
        pass;

    def FromSentence(self, bPos, conn, sComment):
        self.setFeatures = set();
        self.bPos = bPos;
        self.sComment = sComment;
        self.conn = conn;

    def GetType(self):
        return TYPE_GOOD if self.bPos else TYPE_BAD;

    def AddFeature(self, sWord):
        iFeature = feature.fgen.FeatureIndex(sWord);
        self.setFeatures.add(iFeature);

    def GetFeatureIndexList(self):
        return sorted(list(self.setFeatures));

    def GetFeatureWordList(self):
        return map(lambda x:feature.fgen.dIndexToFeature[x], sorted(list(self.setFeatures)));

    def GetSvmLine(self):
        sLine = '+1' if self.bPos else '-1'; #str(self.GetType());
        lFeatures = self.GetFeatureIndexList();
        sFeatureComment = '';
        for iFeature in lFeatures:
            sLine += ' ' + str(iFeature) + ':1';
            sFeatureComment += ' ' + str(iFeature) + '->' + feature.fgen.dIndexToFeature[iFeature];
        sLine += '# conn:' + self.conn.sText + ' Features: ' + sFeatureComment + ' ***Sentence--> ' + self.sComment;
        return sLine;
    
    @staticmethod
    def WriteSvmFile(lSamples, sFile):
        fOut = open(sFile, 'w');
        print "Length:", len(lSamples);
        for sample in lSamples:
            sLine = sample.GetSvmLine();
            fOut.write(sLine + '\n');

    @staticmethod
    def SamplesToFeatureTups(lSamples):
        lFeatureTups = [];
        for sample in lSamples:
            lFeatureTups.append(sample.ToFeatureTup());
        return lFeatureTups;


        

class Dep:
    def __init__(self, tDep):
        self.sType = tDep[0];
        # this is the way the stanford parser labels it
        # self.iFrom = tDep[1];
        # self.iTo = tDep[2];
        # self.sFrom = tDep[3];
        # self.sTo = tDep[4];
        # I'm calling from and to going up the tree
        self.iFrom = tDep[2];
        self.iTo = tDep[1];
        self.sFrom = tDep[4];
        self.sTo = tDep[3];
        self.depParent = None;

    def ToString(self):
        return "Dep:"+' '+str(self.iFrom) + ' --> ' + str(self.iTo) + '  :  ' + str(self.sFrom) + ' --> ' + str(self.sTo) + '        Type: ' + self.sType; 



class DepTree:
    def __init__(self, lDepTups, sentence):
        self.bUseMatrix = False;
        self.lDeps = map(lambda x:Dep(x), lDepTups);
        self.sentence = sentence;
        # index them
        self.dIndexToDep = {};
        self.dIndexToWord = {};
        for dep in self.lDeps:
            self.dIndexToWord[dep.iFrom] = dep.sFrom;
            self.dIndexToWord[dep.iTo] = dep.sTo;
            self.dIndexToDep[dep.iFrom] = dep;
            if dep.iTo not in self.dIndexToDep:
                # this is might be the root so add a dep for it which will be overwritten later if it's not the root
                depNew = Dep(('ROOT', dep.iTo, dep.iTo, dep.sTo, dep.sTo));
                #self.lDeps.append(depNew);
                self.dIndexToDep[dep.iTo] = depNew;
                
        # and now put the parents in place
        for dep in self.lDeps:
            assert(dep.iTo in self.dIndexToDep);
            dep.depParent = self.dIndexToDep[dep.iTo] if dep.iTo in self.dIndexToDep else None;

    def PrintDeps(self, sPrefix = ''):
        for dep in self.lDeps:
            print sPrefix + dep.ToString();

    def GetDepList(self, iIndex):
        lDeps = [];
        depCur = self.dIndexToDep[iIndex];
        setSeen = set();
        while True:
            if depCur in setSeen:
                # found a loop
                #print "Bad Sentence:", self.sentence.sText;
                #for dep in setSeen:
                #    print "\tDep:", dep.iFrom, '-->', dep.iTo, '   :    ', dep.sFrom, '-->', dep.sTo, dep.sType;
                return None;
            setSeen.add(depCur);
            lDeps.append(depCur);
            if depCur.sType == 'ROOT':
                break;
            depCur = depCur.depParent;
        return lDeps;

    def GenShortestPath(self):
        iSize = self.mDist.shape[0];
        for k in range(iSize):
            for i in range(iSize):
                for j in range(iSize):
                    if self.mDist[i,k] + self.mDist[k,j] < self.mDist[i,j]:
                        self.mDist[i,j] = self.mDist[i,k] + self.mDist[k,j];
                        self.mNext[i,j] = k;

    def GetShortestPath(self, i, j):
        if self.mDist[i,j] == sys.maxint:
            assert False;
            return None;
        iInter = self.mNext[i,j];
        if iInter == -1:
            return [];   #/* there is an edge from i to j, with no vertices between */
        else:
            lPrefix = self.GetShortestPath(i,iInter);
            lCur = [iInter];
            lPostfix = self.GetShortestPath(iInter,j);
            if (lPrefix == None) or (lPostfix == None):
                return None;
            return  lPrefix + lCur + lPostfix;

    def BuildMatrix(self):
        lNumWords = len(self.sentence.sText.split());
        self.mDist = np.ones((lNumWords, lNumWords))*sys.maxint;
        self.mNext = np.ones((lNumWords, lNumWords))*-1;
        self.dTupToDep = {};
        for dep in self.lDeps:
            self.dTupToDep[(dep.iFrom,dep.iTo)] = dep;
            self.mDist[dep.iFrom, dep.iTo] = 1;
            self.mDist[dep.iTo, dep.iFrom] = 1;
        self.GenShortestPath();
            

    def FindLeastCommonDepFromMatrix(self, iFrom, iTo):
        self.bUseMatrix = True;
        if not hasattr(self, 'mDist'):
            self.BuildMatrix();
        lPath = self.GetShortestPath(iFrom, iTo);
        if lPath == None:
            print "BadMatrix:", iFrom, iTo;
            print "\tSentence:", self.sentence.sText;
            self.PrintDeps('\t');
            return None;
        # add ifrom and ito
        if ADD_TERMINAL_WORDS:
            lPath = [iFrom] + lPath + [iTo];
        if len(lPath) == 0:
            return iFrom, [];
        for iIndex in range(len(lPath)-1):
            if (lPath[iIndex], lPath[iIndex+1]) not in self.dTupToDep:
                return lPath[iIndex], lPath;
        return lPath[-1], lPath;

    def FindLeastCommonDep(self, iFrom, iTo):
        return self.FindLeastCommonDepFromMatrix(iFrom, iTo);

    # def FindLeastCommonDep(self, iFrom, iTo):
    #     if iFrom == iTo:
    #         return iFrom;
    #     if self.bUseMatrix:
    #         return self.FindLeastCommonDepFromMatrix(iFrom, iTo);
    #     lDepsFrom = self.GetDepList(iFrom);
    #     lDepsTo = self.GetDepList(iTo);
    #     if (lDepsFrom == None) or (lDepsTo == None):
    #         # we found a loop so we're not going to generate a sample
    #         return self.FindLeastCommonDepFromMatrix(iFrom, iTo);
    #     if lDepsFrom[-1].iTo != lDepsTo[-1].iTo:
    #         print "Dict:";
    #         self.PrintDeps('\t');
    #         print "From:",
    #         for dep in lDepsFrom:
    #             print dep.iTo,
    #         print;
    #         print "To:",
    #         for dep in lDepsTo:
    #             print dep.iTo,
    #         print;
    #     assert lDepsFrom[-1].iTo == lDepsTo[-1].iTo;
    #     for i in range(max(len(lDepsFrom), len(lDepsTo))):
    #         if i >= len(lDepsFrom) or i >= len(lDepsTo):
    #             break;
    #         if lDepsFrom[-(i+1)].iTo != lDepsTo[-(i+1)].iTo:
    #             break;
    #     assert lDepsFrom[-i].iTo == lDepsTo[-i].iTo, 'badness:' + str(lDepsFrom[-i].iTo)+' '+str(lDepsTo[-i].iTo);
    #     assert(lDepsFrom[-i].sTo == lDepsTo[-i].sTo);
    #     return lDepsFrom[-i].iTo;

     



class Connection:
    def __init__(self, sTextIn):
        self.bIrrelevant = False;
        self.sText = sTextIn;
        if self.sText.startswith('+'):
            self.bPos = True;
            # skip first char
            self.sText = self.sText[1:]
        else:
            self.bPos = False;
        if self.sText.startswith('*'):
            if ASTERIX_IS_BAD:
                self.bIrrelevant = True;
            else:
                self.bPos = True;
            self.sText = self.sText[1:];

        lSplit = self.sText.split('|');
        assert(len(lSplit) == 2);
        self.sFrom, self.iFrom = lSplit[0].split(':');
        self.sTo, self.iTo = lSplit[1].split(':');
        self.iFrom = int(self.iFrom);
        self.iTo = int(self.iTo);
                

class Sentence:
    def __init__(self):
        pass;

    def AddDeps(self, lDepTups):
        self.deptree = DepTree(lDepTups, self);

    def FromInfoLine(self, sLine):
        lSplit = sLine.split();
        self.iIndex = int(lSplit[0].split('.')[1]);
    
    def FromAnnotationLine(self, sLine):
        assert(sLine[0] == '[');
        if sLine == '[transfered]':
            return;
        elif sLine == '[not transfered]':
            return;
        else:
        # sType = sLine.split()[0];
        # if sType == '[irrelevant]':
        #     self.type = TYPE_IRRELEVANT;
        # elif sType == '[good]':
        #     self.type = TYPE_GOOD;
        # elif sType == '[bad]':
        #     self.type = TYPE_BAD;
        # elif sType == '[coref]':
        #     self.type = TYPE_COREF;
        # elif sType == '[?:related]':
        #     self.type = TYPE_COREF;
        # elif sType == '[?:not]':
        #     self.type = TYPE_BAD;
        # elif sType == '[?:and]':
        #     self.type = TYPE_COREF;
        # elif sType == '[?:weird]':
        #     self.type = TYPE_BAD;
        # elif sType == '[?:location]':
        #     self.type = TYPE_BAD;
        # elif sType == '[?:badgrounding]':
        #     self.type = TYPE_BAD;
        # elif sType == '[?:precon]':
        #     self.type = TYPE_COREF;
        # else:
            assert False, 'Bad annotation:' + sLine;

    def FromConnectionsLine(self, sLine):
        lConnectionLines = sLine.split()[1:];
        self.lConnections = map(lambda sLine:Connection(sLine), lConnectionLines);
        if IGNORE_CONNECTION_DIR:
            # for all pos connections we 
            dTupToConn = {};
            for conn in self.lConnections:
                dTupToConn[(conn.iFrom, conn.iTo)] = conn;
            for conn in self.lConnections:
                if conn.bPos:
                    if (conn.iTo, conn.iFrom) not in dTupToConn:
                        if conn.sFrom == conn.sTo:
                            continue;
                        assert False;
                    dTupToConn[(conn.iTo, conn.iFrom)].bPos = True;

    def CheckConnections(self):
        if self.iIndex in [6281]:
            return;
        for conn in self.lConnections:
            if self.deptree.dIndexToWord[conn.iTo] != conn.sTo:
                print "Index:", self.iIndex;
                print "Dep:"
                data.print_obj(self.deptree.dIndexToWord);
                print "Conn:";
                data.print_obj(conn);
            assert(self.deptree.dIndexToWord[conn.iFrom] == conn.sFrom);
            assert(self.deptree.dIndexToWord[conn.iTo] == conn.sTo);

    def FromTextLine(self, sLine):
        assert sLine[:5] == 'Text:';
        self.sText = sLine[6:]; 
        #self.lWords = self.sText.split();

    def FromLine(self, sLine):
        if sLine.startswith('No.'):
            self.FromInfoLine(sLine);
        elif sLine.startswith('['):
            self.FromAnnotationLine(sLine);
        elif sLine.startswith('Connections:'):
            self.FromConnectionsLine(sLine);
        elif sLine.startswith('Text:'):
            self.FromTextLine(sLine);
        else:
            assert False, 'Bad Line:' + sLine;

            
    def GenSample(self, conn):
        self.lWords = self.sText.split();
        sample = Sample();
        sample.FromSentence(bPos = conn.bPos, conn = conn, sComment = self.sText);
        if USE_WORD_FEATURES:
            for sWord in self.lWords:
                if USE_STEMMER:
                    sample.AddFeature('Word::' + Stemmer.stem_word(sWord));
                else:
                    sample.AddFeature(sWord);
        # if hasattr(self, 'sPosTaggedWords'):
        #     self.lPosWords = self.sPosTaggedWords.split();
        #     for sPosWord in self.lPosWords:
        #         sample.AddFeature(sPosWord);

        if USE_SENTENCE_DIR:
            sSentenceDir = 'SentForw::' if conn.iFrom < conn.iTo else 'SentBack::';
        else:
            sSentenceDir = '';
        
        if hasattr(self, 'deptree') and USE_DEPS:
            iCommonDep, lPath = self.deptree.FindLeastCommonDep(conn.iFrom, conn.iTo);
            if iCommonDep == None:
                return None;
            sCommonDep = self.deptree.dIndexToWord[iCommonDep]
            if DONT_GEN_FEATURES_WITH_PDDL_OBJECT_WORDS and not obj_extract.IsPddlWord(sCommonDep):
                sample.AddFeature('FDep::' + sSentenceDir + sCommonDep);
                if USE_NON_SENTENCE_DIR_TOO:
                    sample.AddFeature('FDep::' + sCommonDep);
            if USE_PATH_WORDS:
                # add features for all words along path
                for iPath in lPath:
                    sWord = self.deptree.dIndexToWord[iPath];
                    if DONT_GEN_FEATURES_WITH_PDDL_OBJECT_WORDS and obj_extract.IsPddlWord(sWord):
                        continue;
                    sample.AddFeature('PathWord::' + sSentenceDir + sWord);
                    if USE_NON_SENTENCE_DIR_TOO:
                        sample.AddFeature('PathWord::' + sWord);
            
            if USE_PATH_DEP_TYPES and len(lPath) > 0:
                # add features for dep types along the path
                
                iPrev = lPath[0];
                for iPathCur in lPath[1:]:
                    sPathDirFor = 'Forw::' if USE_PATH_DIR else '';
                    sPathDirBack = 'Back::' if USE_PATH_DIR else '';
                        
                    if (iPrev, iPathCur) in self.deptree.dTupToDep:
                        sample.AddFeature('PathDepType::' +sPathDirFor + sSentenceDir + 
                                          self.deptree.dTupToDep[(iPrev, iPathCur)].sType);
                        if USE_NON_SENTENCE_DIR_TOO:
                            sample.AddFeature('PathDepType::' +sPathDirFor + 
                                              self.deptree.dTupToDep[(iPrev, iPathCur)].sType);
                    if (iPathCur, iPrev) in self.deptree.dTupToDep:
                        sample.AddFeature('PathDepType::' + sPathDirBack + sSentenceDir + 
                                          self.deptree.dTupToDep[(iPathCur, iPrev)].sType);
                        if USE_NON_SENTENCE_DIR_TOO:
                            sample.AddFeature('PathDepType::' + sPathDirBack + 
                                              self.deptree.dTupToDep[(iPathCur, iPrev)].sType);
                    iPrev = iPathCur;
        return sample;


    def GenAllSamples(self, fLog = None):
        if self.iIndex == 6281:
            # this sentence has the weird 1 1/2 thing which is screwing up the indexes
            return 0, [];
        iNumLoopy = 0;
        lSamples = [];
        if fLog != None:
            print >> fLog, "Sentence:", self.sText;
        for connection in self.lConnections:
            if fLog != None:
                print >> fLog, "\tConn:", connection.sFrom, '-->', connection.sTo, '   ::   ', 
                print >> fLog, obj_extract.GetPddlObj(connection.sFrom), '-->', obj_extract.GetPddlObj(connection.sTo);
            sample = self.GenSample(connection);
            if sample == None:
                iNumLoopy += 1;
            else:
                lSamples.append(sample);
                if fLog != None:
                    for sFeature in sample.GetFeatureWordList():
                        print >> fLog, '\t\t', sFeature
        return iNumLoopy, lSamples;
                        
    @staticmethod
    def GenAllSamplesFromList(lSentences, sLogFileName):
        fLog = open(sLogFileName, 'w');
        lSamples = [];
        iNumLoopy = 0;
        for sentence in lSentences:
            iCurNumLoopy, lCurSamples = sentence.GenAllSamples(fLog);
            lSamples.extend(lCurSamples);
            iNumLoopy += iCurNumLoopy;
        return iNumLoopy, lSamples;

    @staticmethod
    def ReadSentencesFromTextFile(sFileName):
        lLines = map(lambda x: x.strip(), open(sFileName).readlines());
        sentence = None;
        lSentences = [];
        for sLine in lLines:
            if sLine.startswith('#') or sLine == '':
                continue;
            if sLine.startswith('No.'):
                sentence = Sentence();
                lSentences.append(sentence);
            sentence.FromLine(sLine);
        return lSentences;



def PrintAndRun(sCommand, bPrint = True):
    if bPrint:
        print "Running:", sCommand;
    iRetVal= subprocess.call(shlex.split(sCommand));
    print "RetVal is:", iRetVal;
    return iRetVal;


#TYPE_IRRELEVANT = 1
#TYPE_GOOD = 2
#TYPE_BAD = 3
#TYPE_COREF = 4
TYPE_BAD = 0;
TYPE_GOOD = 1;
NUM_CLASSES = 2;


def IsError(iRetVal):
    if isinstance(iRetVal, int) and iRetVal < 0:
        return True;
    else:
        return False;
                
def print_matrix(mMat):
    iSizeX, iSizeY = mMat.shape;
    
    for x in range(iSizeX):
        for y in range(iSizeY):
            print mMat[x,y],;
        print;

def GetWeightsFromSvmModel(sModelFile):
    sLines = open(sModelFile).readlines();
    # get the highest feature index from line 7(8)                              
    iMaxFeature = int(sLines[7].split()[0]);
    #iMaxFeature = GetNumFeatures(sLines[11]);                                  
    fThreshold = float(sLines[10].split()[0]);
    lFeatureWeights = [0 for i in range(iMaxFeature+1)];
    lFeatureWeightsNorm = [0 for i in range(iMaxFeature+1)];
    # the first few lines are just metadata so skip them                        
    for sLine in sLines[11:]:
        lLine = sLine.split();
        fMult = float(lLine[0]);
        for sFeature in lLine[1:]:
            # check if we've hit the comment                                    
            if "#" == sFeature:
                break;
            (iFeature, fWeight) = sFeature.split(':');
            lFeatureWeights[int(iFeature)] += fMult*float(fWeight);

    # the 0th feature and max feature don't really exist                        
    #lFeatureWeights = lFeatureWeights[1:iMaxFeature-1];
    return (fThreshold, lFeatureWeights);


def AnalyzePredsSimple(lSamples, lPreds):
    iNumTotal = 0;
    iNumCorrect = 0;
    iTruePos = 0;
    iFalsePos = 0;
    iTrueNeg = 0;
    iFalseNeg = 0;
    iThres = 0;
    if SVM:
        iThres = 0;
    elif LOG_LINEAR:
        iThres = 0.5
    else:
        assert False;

    for sample, fPred in zip(lSamples, lPreds):
        iPredType = TYPE_GOOD if float(fPred) > iThres else TYPE_BAD;
        iActualType = sample.GetType();
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
    fPrecision = float(iTruePos)/float(iTruePos+iFalsePos) if iTruePos > 0 else 0;
    fRecall = float(iTruePos)/float(iTruePos+iFalseNeg) if iTruePos > 0 else 0;
    fScore = 2*fPrecision*fRecall/(fPrecision+fRecall) if (fPrecision*fRecall) > 0 else 0;
    print "FScore:", fScore, fPrecision, fRecall;
    print "Frac Correct:", float(iNumCorrect)/float(iNumTotal), iNumCorrect, iNumTotal;
    print "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
    return fScore;
    


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
        print "FScore:", fScore, fPrecision, fRecall;
        print "Frac Correct:", float(iNumCorrect)/float(iNumTotal), iNumCorrect, iNumTotal;
        print "Threshold:", fThreshold, "TP:", iTruePos, "FP:", iFalsePos, "TN:", iTrueNeg, "FN:", iFalseNeg;
        print_matrix(mResults);
    return fScore;


def TrainSvm(lSamples, sTrainFile, sModelFile):
    Sample.WriteSvmFile(lSamples, sTrainFile);
    if USE_SVM_PERF:
        # version used for good svm results
        iRetVal = PrintAndRun("../../bin/svm_perf_learn -c 100 -w 3 -l 1 -b 0 " + sTrainFile + " " + "model.svm");
        #iRetVal = PrintAndRun("../../bin/svm_perf_learn -c 1 -w 3 -l 1 -b 0 " + sTrainFile + " " + "model.svm");
    else:
        iRetVal = PrintAndRun("../../bin/svm_learn -c 10 -b 0 " + sTrainFile + " " + "model.svm");

def TestSvm(lSamples, sTestFile, sModelFile, sPredFile):
    Sample.WriteSvmFile(lSamples, sTestFile);
    if USE_SVM_PERF:
        iRetVal = PrintAndRun("../../bin/svm_perf_classify " + sTestFile + " " + sModelFile + " " + sPredFile);
    else:
        iRetVal = PrintAndRun("../../bin/svm_classify " + sTestFile + " " + sModelFile + " " + sPredFile);
    sPredLines = open(sPredFile).readlines();
    lPreds  = map(lambda x:float(x), sPredLines);
    return lPreds;

def CalcFracGood(lSamples):
    iNumGood = 0;
    for sample in lSamples:
        if sample.bPos:
            iNumGood += 1;
    print "NumGood:", float(iNumGood)/float(len(lSamples));


def AddPosTagFeatures(lSentences, sPosTagsFile):
    lPosTags = open(sPosTagsFile).readlines();
    for sentence in lSentences:
        sentence.sPosTaggedWords = lPosTags[sentence.iIndex]; #+ ' ' + str(sentence.type);

def AddDepFeatures(lSentences, sDepFile):
    lDeps = load_parse.load_deps(sDepFile);
    assert len(lDeps) == len(lSentences), "Not Same Len: " + str(len(lSentences)) + ' ' + str(len(lDeps));
    for dep, sentence in zip(lDeps, lSentences):
        lDeps = dep[0];
        sentence.AddDeps(lDeps);

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

def TextToPred(sTextName):
    # this is Taos function:
    #return sTextName;
    return ['wood-pickaxe','stone-pickaxe'];


def GenConnectionDicts(lSamples, sPredDictFile):
    dPredicateNamePairs = {};
    lPredNameTups = [];
    # get the predicate names from the samples
    for sample in lSamples:
        sFromText = sample.conn.sFrom;
        sToText = sample.conn.sTo;
        lFromName = obj_extract.GetPddlObj(sFromText);
        lToName = obj_extract.GetPddlObj(sToText);
        for sFromName in lFromName:
            for sToName in lToName:
                lPredNameTups.append((sFromName, sToName, sample));
                #if ((sFromName, sToName) not in dPredicateNamePairs) or (not dPredicateNamePairs[(sFromName, sToName)].bPos):
                #    dPredicateNamePairs[(sFromName, sToName)] = sample;


    lPredicates = predicate.PredDictFileToPredList(sPredDictFile);
    dNameToPredList = collections.defaultdict(lambda:[]);
    for pred in lPredicates:
        dNameToPredList[pred.GetObject()].append(pred);

    # generate tups (iFrom, iTo, sample)
    lConnectionDicts = [];
    setSendNamePairs = set();
    for (sFromName, sToName, sample) in lPredNameTups:
        if REMOVE_DUPLICATE_CONNS:
            assert False;
            if (sFromName, sToName) in setSeenNamePairs:
                continue;
            setSeenNamePairs.add((sFromName, sToName));
        #lFromIndexes = filter(lambda pred: pred.iIndex, dNameToPredList[sFromName]);
        lFromIndexes = [];
        for pred in dNameToPredList[sFromName]:
            lFromIndexes.append(pred.iIndex);
        #lToIndexes = filter(lambda pred: pred.iIndex, dNameToPredList[sToName]);
        lToIndexes = [];
        for pred in dNameToPredList[sToName]:
            lToIndexes.append(pred.iIndex);
        
        for iFromIndex in lFromIndexes:
            for iToIndex in lToIndexes:
                lConnectionDicts.append({'iFromIndex':iFromIndex, 'iToIndex':iToIndex, 'sample':sample, 'sFromName':sFromName, 'sToName':sToName});

    return lConnectionDicts;

def CheckForChicken(lSamples, bAssert = True):
    # check for chicken
    for sample in lSamples:
        lWords = sample.GetFeatureWordList();
        for word in lWords:
            assert (not bAssert) or (not word.endswith('chicken')), 'Found Feature:' + word;
            if word.endswith('chicken'):
                print "Found:", word, sample.conn.sFrom, sample.conn.sTo;

def GenConnFile(lSamples, lPredictions, dFeatureWeights, sConnPosPredFile, sConnGoldFile, sConnFeatureFile, sConnTopFeatureFile, sPredDictFile):
    # stick the predictions into the sample
    assert(len(lPredictions) == len(lSamples));
    for fPred, sample in zip(lPredictions, lSamples):
        sample.fPred = fPred;

    lConnectionDicts = GenConnectionDicts(lSamples, sPredDictFile);

    # gen the normal conn file
    fConnsPosPred = open(sConnPosPredFile, 'w');
    fConnsGold = open(sConnGoldFile, 'w');
    for dConn in lConnectionDicts:
        sample = dConn['sample'];
        sLine = '1|' + str(dConn['iFromIndex']) + '|' + str(dConn['iToIndex']) + '|' + dConn['sFromName'] + '|' + dConn['sToName'] + \
            '|Text:' + sample.conn.sFrom + '|Text:' + sample.conn.sTo + '|Pos:' + str(sample.bPos) + '|Pred:' + str(sample.fPred);
        if dConn['sample'].fPred > 0:
            print >> fConnsPosPred, sLine;
        if dConn['sample'].bPos:
            print >> fConnsGold, sLine;

    # gen the feature file
    if GEN_FEATURE_FILE:
        assert not REMOVE_DUPLICATE_CONNS;
        fConnsFeatures = open(sConnFeatureFile, 'w');
        fConnsTopFeatures = open(sConnTopFeatureFile, 'w');
        for dConn in lConnectionDicts:
            sample = dConn['sample'];
            lFeatures = sample.GetFeatureWordList();
            for sFeature in lFeatures:
                # if DONT_GEN_FEATURES_WITH_PDDL_OBJECT_WORDS:
                #     lFeatureSplit = sFeature.split('::');
                #     bSkip = False;
                #     for sSplit in lFeatureSplit:
                #         if len(obj_extract.GetPddlObj(sSplit)) != 0:
                #             bSkip = True;
                #     if bSkip:
                #         print "Skipping:", sFeature;
                #         continue;
                sLine = sFeature + '|1|' + str(dConn['iFromIndex']) + '|' + str(dConn['iToIndex']) + '|' + dConn['sFromName'] + '|' + \
                    dConn['sToName'] + \
                    '|Text:' + sample.conn.sFrom + '|Text:' + sample.conn.sTo + '|Pos:' + str(sample.bPos) + '|Pred:' + str(sample.fPred);
                print >> fConnsFeatures, sLine;
                fFeatureWeight = dFeatureWeights[sFeature];
                if (fFeatureWeight > POS_FEATURE_WEIGHT_THRES) or (fFeatureWeight < NEG_FEATURE_WEIGHT_THRES):
                    print >> fConnsTopFeatures, sLine;


def WriteFeatureFrequencies(lSamples, sPosFeatureFreqFile, sNegFeatureFreqFile):
    dPosFeatureCount = collections.defaultdict(lambda:0);
    dNegFeatureCount = collections.defaultdict(lambda:0);
    for sample in lSamples:
        for sFeature in sample.GetFeatureWordList():
            if sample.bPos:
                dPosFeatureCount[sFeature] += 1;
            else:
                dNegFeatureCount[sFeature] += 1;
                

    lPosTupsSorted = sorted(dPosFeatureCount.items(), key=lambda tup: tup[1], reverse=True);
    fPosFeatureFreqFile = open(sPosFeatureFreqFile, 'w');
    for sFeature, iCount in lPosTupsSorted:
        print >> fPosFeatureFreqFile, sFeature + ' ' + str(iCount) + ' Neg: ' + str(dNegFeatureCount[sFeature]);

    lNegTupsSorted = sorted(dNegFeatureCount.items(), key=lambda tup: tup[1], reverse=True);
    fNegFeatureFreqFile = open(sNegFeatureFreqFile, 'w');
    for sFeature, iCount in lNegTupsSorted:
        print >> fNegFeatureFreqFile, sFeature + ' ' + str(iCount) + ' Pos: ' + str(dPosFeatureCount[sFeature]);


class SampleMatrix:
    def __init__(self, lPredicates):
        self.dObjectToPredIndexList = collections.defaultdict(lambda:[]);
        for pred in lPredicates:
            assert len(self.dObjectToPredIndexList[pred.GetObject()]) == 0;
            self.dObjectToPredIndexList[pred.GetObject()].append(pred.iIndex);

        iNumPredicates = len(self.dObjectToPredIndexList);
        self.mSamples = np.empty((iNumPredicates, iNumPredicates), dtype=object);
        for iFrom, predFrom in enumerate(lPredicates):
            assert(iFrom == predFrom.iIndex);
            for iTo, predTo in enumerate(lPredicates):
                assert(iTo == predTo.iIndex);
                self.mSamples[iFrom,iTo] = GoldSample(predFrom, predTo);

    def AddRandomAnnotations(self):
        iSize = self.mSamples.shape[0];
        for i in range(iSize):
            for j in range(iSize):
                if random.random() < .5:
                    self.mSamples[i,j].bPos = True;
                
            
    def AddGoldDepInfo(self, dDeps):
        self.dDeps = dDeps;
        if not TRAIN_ON_GOLD_DEP:
            return;
        for sTo, dFrom in dDeps.items():
            lTo = self.dObjectToPredIndexList[sTo];
            for sFrom in dFrom.keys():
                lFrom = self.dObjectToPredIndexList[sFrom];
                for iTo in lTo:
                    for iFrom in lFrom:
                        # set all these as valid connections
                        self.mSamples[iFrom, iTo].bPos = True;

    def AddSentenceInfo(self, lSentences):
        for sentence in lSentences:
            iNumLoopy, lSamples = sentence.GenAllSamples();
            for sample in lSamples:
                lPddlFrom = obj_extract.GetPddlObj(sample.conn.sFrom);
                lPddlTo = obj_extract.GetPddlObj(sample.conn.sTo);
                for sFrom in lPddlFrom:
                    lFromIndexes = self.dObjectToPredIndexList[sFrom];
                    for sTo in lPddlTo:
                        lToIndexes = self.dObjectToPredIndexList[sTo];
                        for iFrom in lFromIndexes:
                            for iTo in lToIndexes:
                                self.mSamples[iFrom,iTo].AddFeatures(sample.setFeatures, sentence, sample.conn);
                                # if we're using manual annotations then set pos based on this
                                if TRAIN_ON_MANUAL_ANNOT and sample.bPos:
                                    self.mSamples[iFrom,iTo].bPos = True;
    def SetNoSubgoalConns(self, sCurObj):
        if sCurObj not in self.dDeps:
            return;
        
        lCurObjPredIndexes = self.dObjectToPredIndexList[sCurObj];
        for sPrevObj in self.dDeps[sCurObj].keys():
            if sPrevObj == 'num':
                continue;
            lPrevObjPredIndexes = self.dObjectToPredIndexList[sPrevObj];
            for iCurObjPredIndex in lCurObjPredIndexes:
                for iPrevObjPredIndex in lPrevObjPredIndexes:
                    self.mSamples[iPrevObjPredIndex, iCurObjPredIndex].bNoSubgoal = True;
            self.SetNoSubgoalConns(sPrevObj);
                    
    def AddNoSubgoalInfo(self, lNoSubgoalsObjs):
        assert(self.dDeps != None);
        for sNoSubgoalObj in lNoSubgoalsObjs:
            self.SetNoSubgoalConns(sNoSubgoalObj);


def GenSampleMatrix(sNoSubgoalsFile, sDepsFile, sPredicateDictFile, lSentences):
    lPredicates = predicate.PredDictFileToPredList(sPredicateDictFile);
    dDeps = data.file_to_obj_with_comments(sDepsFile);
    iNumPredicates = len(lPredicates);
    mSamp = SampleMatrix(lPredicates);

    mSamp.AddGoldDepInfo(dDeps);
                    
    mSamp.AddSentenceInfo(lSentences);

    if TRAIN_ON_RANDOM_ANNOT:
        assert((not TRAIN_ON_GOLD_DEP) and (not TRAIN_ON_MANUAL_ANNOT));
        mSamp.AddRandomAnnotations();

    lNoSubgoalsObjs = map(string.strip, open(sNoSubgoalsFile).readlines());

    mSamp.AddNoSubgoalInfo(lNoSubgoalsObjs);
    
    return mSamp;



def GetTrainFirst30(smat):
    iNumPredicates = smat.mSamples.shape[0];
    # now grab all the samples which have features
    lTest = [];
    lTrain = [];
    lNeg = [];
    for i in range(iNumPredicates):
        for j in range(iNumPredicates):
            # skip the self connections
            if i == j:
                continue;
            sample = smat.mSamples[i,j];
            if len(sample.dFeatureCounts) == 0:
                continue;
            if sample.bPos:
                if sample.bNoSubgoal:
                    lTrain.append(sample);
                else:
                    lTest.append(sample);
            else:
                assert(not sample.bNoSubgoal);
                lNeg.append(sample);
    print "***NUMS*** Train:", len(lTrain), "Test:", len(lTest), "Neg:", len(lNeg);

    # randomize the negs and then split them in half
    random.shuffle(lNeg);
    iSplit = len(lNeg)/2;
    lTrain.extend(lNeg[:iSplit]);
    lTest.extend(lNeg[iSplit:]);

    # now shuffle the order of train and test although I don't think that should make a difference
    random.shuffle(lTrain);
    random.shuffle(lTest);

    return lTrain,lTest;


def GetAllSamples(smat):
    iNumPredicates = smat.mSamples.shape[0];
    lSamp = [];
    for i in range(iNumPredicates):
        for j in range(iNumPredicates):
            # skip the self connections
            if i == j:
                continue;
            sample = smat.mSamples[i,j];
            if len(sample.dFeatureCounts) == 0:
                continue;
            lSamp.append(sample);
    return lSamp;
    


def dummy_joint_features(lFeatureTups, sLabel):
    if sLabel == '-1':
        return map(lambda (iIndex, iValue):(iIndex+feature.fgen.iIndex, iValue), lFeatureTups);
    else:
        return lFeatureTups;

def TrainAndTestLogLinear(lTrain, lTest):
    lTrainFeatureTups = Sample.SamplesToFeatureTups(lTrain);
    encoder = maxent.FunctionBackedMaxentFeatureEncoding(dummy_joint_features,
                                                         feature.fgen.iIndex*2,
                                                         ['-1','1']);
    #lFeatureTupsPruned = lFeatureTups[0:1000];
    classifier = maxent.MaxentClassifier.train(lTrainFeatureTups, 
                                               encoding = encoder,
                                               algorithm = 'LBFGSB');
    lPreds = [];
    lTestFeatureTups = Sample.SamplesToFeatureTups(lTest);
    for (lFeatures, sLabel) in lTestFeatureTups:
        fProb = classifier.prob_classify(lFeatures).prob('1');
        lPreds.append(fProb);
    
    lAllFeatureWeights = classifier.weights();
    return lPreds, lAllFeatureWeights;



def GenDepGraph(sDir):
    try:
        os.makedirs(sDir);
    except:
        pass;
    if SIMPLE_INPUTS:
        lSentences = Sentence.ReadSentencesFromTextFile(\
            '../../annotations/test_sentence.txt');
        AddDepFeatures(lSentences, '../../annotations/test-parsed.txt');
    else:
        lSentences = Sentence.ReadSentencesFromTextFile('../../pages_text/noparen/all.text_conn_annotated');
        #lSentences = Sentence.ReadSentencesFromTextFile('../../annotations/12.26_connection_sentences_annotated.txt');
        # lSentences.extend(Sentence.ReadSentencesFromTextFile('../../annotations/new_connection_sentence.2.txt'));
        AddDepFeatures(lSentences, '../../pages_text/noparen/all.parsed');

    for sentence in lSentences:
        sCurFile = sDir + '/' + str(sentence.iIndex) + '.dep';
        fCur = open(sCurFile, 'w');
        for iIndex, sWord in enumerate(sentence.sText.split()):
            print >> fCur, str(iIndex) + ':' + sWord,
        print >> fCur, str(iIndex+1) + ':#/#';
        sLine = '';
        for dep in sentence.deptree.lDeps:
            sLine += ' ' + str(dep.iFrom) + '\x01' + str(dep.iTo) + '\x01' + str(dep.sType)
        print >> fCur, 'gold:' + sLine;
        # print >> fCur, 'pred:' + sLine;
        fCur.close();
        sTexFileName = sCurFile[:-4] + '.tex';
        draw_dep.draw_tex(sCurFile, sTexFileName);
        os.system('cd ' + sDir + '; pdflatex ' + os.path.basename(sTexFileName));
        os.unlink (sCurFile [:-4] + '.log')
        os.unlink (sCurFile [:-4] + '.aux')
        #os.system('mv ' + sTexFileName + ' dep_graphs/' + sTexFileName);

def PrintTextConns(smat):
    iSize = smat.mSamples.shape[0];
    for i in range(iSize):
        for j in range(iSize):
            if i == j:
                continue;
            sample = smat.mSamples[i,j];
            if len(sample.dFeatureCounts) == 0:
                continue;
            print "MATCH:", sample.predFrom.GetObject(), sample.predTo.GetObject();
            print "Sentence:", sample.lSentences[0].sText;
    sys.exit(-1);

def GoldMain():
    if SIMPLE_INPUTS:
        lSentences = Sentence.ReadSentencesFromTextFile('../../annotations/test_sentence.txt');
        AddDepFeatures(lSentences, '../../annotations/test-parsed.txt');
    else:
        lSentences = Sentence.ReadSentencesFromTextFile('../../annotations/new_connection_sentence.1.txt');
        lSentences.extend(Sentence.ReadSentencesFromTextFile('../../annotations/new_connection_sentence.2.txt'));
        AddDepFeatures(lSentences, '../../annotations/new_sentences.parsed.txt');

    smat = GenSampleMatrix('../subgoal_learning/data/thing-available_max5.no_subgoals_needed', 'dep.json', 
                        '../subgoal_learning/data/thing-available_max1.dict', lSentences);
    #PrintTextConns(smat);
    if EVAL_TRAIN_FIRST_30:
        assert(LOG_LINEAR);
        lTrain, lTest = GetTrainFirst30(smat);

        lFeatureWeights = [];
        if SVM:
            TrainSvm(lTrain, 'train.svm', 'model.svm');
            lPreds = TestSvm(lTest, 'test.svm', 'model.svm', 'pred.svm');
        else:
            lPreds, lFeatureWeights = TrainAndTestLogLinear(lTrain, lTest);
        fScore = AnalyzePreds(lTest, lPreds, lFeatureWeights, 'analysis.svm', fThreshold=0.5, bPrintExtraThresholds=True, sDebugFile = 'debug.svm');
        print "FScore is:", fScore;
    elif EVAL_RANDOM_HALF_HALF:
        lSamples = GetAllSamples(smat);
        lFScores = [];
        for i in range(NUM_ITER):
            lRandomIndexes = range(len(lSamples));
            random.shuffle(lRandomIndexes);
            iSplit = len(lSamples)/2;
            lTrainIndexes = lRandomIndexes[:iSplit];
            lTestIndexes = lRandomIndexes[iSplit:];
            lTrain = map(lambda x:lSamples[x], lTrainIndexes);
            lTest = map(lambda x:lSamples[x], lTestIndexes);
            if SVM:
                TrainSvm(lTrain, 'train.svm', 'model.svm');
                lPreds = TestSvm(lTest, 'test.svm', 'model.svm', 'pred.svm');
                dFeatureWeights = GenFeatureWeightsFile('model.svm', 'feature_weights.svm');
            elif LOG_LINEAR:
                lPreds, lFeatureWeights = TrainAndTestLogLinear(lTrain, lTest);
            else:
                assert False;
            fScore = AnalyzePredsSimple(lTest, lPreds);
            lFScores.append(fScore);
        print "Num Samples:", len(lSamples), "Pos:", len(filter(lambda x:x.bPos, lSamples)), "Neg:", len(filter(lambda x:not x.bPos, lSamples));
        for fScore in lFScores:
            print "FScore is:", fScore;
        print "Average F-Score:", np.average(lFScores);
    else:
        assert False;
        




def Classifier():
    if SIMPLE_INPUTS:
        lSentences = Sentence.ReadSentencesFromTextFile('../../annotations/test_sentence.txt');
    else:
        lSentences = Sentence.ReadSentencesFromTextFile('../../annotations/new_connection_sentence.1.txt');
        lSentences.extend(Sentence.ReadSentencesFromTextFile('../../annotations/new_connection_sentence.2.txt'));
    

    if USE_POS_TAGS:
        AddPosTagFeatures(lSentences, '../../annotations/whole.tagged.txt');
        
    if SIMPLE_INPUTS:
        AddDepFeatures(lSentences, '../../annotations/test-parsed.txt');
    else:
        AddDepFeatures(lSentences, '../../annotations/new_sentences.parsed.txt');
        
    #for sentence in lSentences:
    #    sentence.CheckConnections();

    if USE_GOLD_SAMPLES:
        lSamples = GenGoldSamples('dep.json', '../subgoal_learning/data/thing-available_max5.dict', lSentences);
    else:
        iNumLoopy, lSamples = Sentence.GenAllSamplesFromList(lSentences, 'sentences.log');
        print "Num Loopy:", iNumLoopy, 'NonLoopy:', len(lSamples);
    data.obj_to_file(lSamples, 'test.json');
    if GEN_FEATURE_FREQ_FILE:
        WriteFeatureFrequencies(lSamples, 'feature_frequencies_pos.txt', 'feature_frequencies_neg.txt');
    lFScores = [];
    for i in range(NUM_ITER):
        lRandomIndexes = range(len(lSamples));
        random.shuffle(lRandomIndexes);
        iSplit = len(lSamples)/2;
        if TRAIN_AND_TEST_ON_ALL:
            assert(not TRAIN_ON_HALF_TEST_ON_ALL);
            lTrainIndexes = range(len(lSamples));
            lTestIndexes = range(len(lSamples));
        elif TRAIN_ON_HALF_TEST_ON_ALL:
            lTrainIndexes = lRandomIndexes[:iSplit];
            lTestIndexes = range(len(lSamples));
        else:
            lTrainIndexes = lRandomIndexes[:iSplit];
            lTestIndexes = lRandomIndexes[iSplit:];
        lTrain = map(lambda x:lSamples[x], lTrainIndexes);
        lTest = map(lambda x:lSamples[x], lTestIndexes);
        TrainSvm(lTrain, 'train.svm', 'model.svm');
        lPreds = TestSvm(lTest, 'test.svm', 'model.svm', 'pred.svm');
        lGenFileSamples = lTest;
        lGenFilePreds = lPreds;
        if CROSS_VALIDATE:
            TrainSvm(lTest, 'train.svm', 'model.svm');
            lTrainPreds = TestSvm(lTrain, 'test.svm', 'model.svm', 'pred.svm');
            lGenFileSamples = lTest + lTrain;
            lGenFilePreds = lPreds + lTrainPreds;
        fScore = AnalyzePreds(lTest, lPreds);
        lFScores.append(fScore);
        if GEN_CONN_FILE:
            assert(TRAIN_ON_HALF_TEST_ON_ALL or TRAIN_AND_TEST_ON_ALL or CROSS_VALIDATE or GEN_CONN_FROM_HALF);
            assert(NUM_ITER==1);
            dFeatureWeights = GenFeatureWeightsFile('model.svm', 'feature_weights.svm');
            GenConnFile(lGenFileSamples, lGenFilePreds, dFeatureWeights, 'thing-available_max5.conn_text_svm_pred','thing-available_max5.conn_text_gold', 'thing-available_max5.conn_text_features', 'thing-available_max5.conn_top_text_features', '../subgoal_learning/data/thing-available_max5.dict');

    
    CalcFracGood(lSamples);
    for fScore in lFScores:
        print "FScore is:", fScore;
    print "Average F-Score:", np.average(lFScores);


def Test():
    lSentences = Sentence.ReadSentencesFromTextFile('test_sentence.txt');
    AddDepFeatures(lSentences, 'test_sentence_parsed.txt');
    assert(len(lSentences) == 1);
    sentence = lSentences[0];
    iNumLoopy, lSamples = lSentences[0].GenAllSamples();
    iCommonDep, lPath = sentence.deptree.FindLeastCommonDep(29, 21);
    lSplit = sentence.sText.split();
    for iPath in lPath:
        iPath = int(iPath);
        print "iPath:", iPath;
        print "Path:", lSplit[iPath];
    # for sample in lSamples:
    #     if sample.conn.iFrom == 29 and sample.conn.iTo == 21:
    #         sentence.GenSample(sample.conn);
    #         print "SAMPLE";
    #         data.print_obj(sample.conn);
    #         print "Features:", sample.GetFeatureWordList();

def Main():
    #GoldMain();
    #Classifier();
    GenDepGraph('dep_graphs_noparen');
    #Test();

Main();
