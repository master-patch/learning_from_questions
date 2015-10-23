import config
import load_parse
import obj_extract
import Sample
import numpy as np;
import sys
import data
import predicate
import collections

class Dep(object):
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



class DepTree(object):
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
            #assert False;
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
            #self.PrintDeps('\t');
            return None, None;
        # add ifrom and ito
        if config.get_bool('FEATURES:ADD_TERMINAL_WORDS'):
            lPath = [iFrom] + lPath + [iTo];
        if len(lPath) == 0:
            return iFrom, [];
#        print '----------';
#        print self.sentence.sText;
#        print map(lambda x:self.dIndexToWord[x], lPath);
        for iIndex in range(len(lPath)-1):
            if (lPath[iIndex], lPath[iIndex+1]) not in self.dTupToDep:
#                print self.dIndexToWord[lPath[iIndex]]; 
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

     
class PddlConn(object):
    def __init__(self, sPddlFrom, sPddlTo, textconn):
        self.sPddlFrom = sPddlFrom;
        self.sPddlTo = sPddlTo;
        self.textconn = textconn;


class TextConn(object):
    def __init__(self, sConnText, sentence):
        self.sentence = sentence;
        self.bIrrelevant = False;
        self.sText = sConnText;
        if self.sText.startswith('+'):
            self.bPos = True;
            # skip first char
            self.sText = self.sText[1:]
        else:
            self.bPos = False;
        if self.sText.startswith('*'):
            if config.get_bool('ASTERIX_IS_BAD'):
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

    def ComputePddlConns(self):
        #print self.sentence.lPosTags;
        #sys.exit(-1);
        self.lPddlFrom = obj_extract.GetPddlObjByIndex(self.sentence.lPosTags, self.iFrom);
        self.lPddlTo = obj_extract.GetPddlObjByIndex(self.sentence.lPosTags, self.iTo);
        self.lPddlConns = [];
        for sPddlFrom in self.lPddlFrom:
            for sPddlTo in self.lPddlTo:
                if sPddlFrom == sPddlTo:
                    continue;
                self.lPddlConns.append(PddlConn(sPddlFrom, sPddlTo, self));
        
class Sentence(object):
    def __init__(self):
        self.deptree = None;
        self.lWords = None;
        self.iIndex = None;
        self.lTextConns = None;
        self.sText = None;
        self.bBad = False;
        self.bIsInOld = False;

    def ComputePddlConns(self):
        for textconn in self.lTextConns:
            textconn.ComputePddlConns();
        # set the reverse connections in the pddlconns
        dPddlConns = {};
        for textconn in self.lTextConns:
            for pddlconn in textconn.lPddlConns:
                tKey = (pddlconn.sPddlFrom, pddlconn.sPddlTo, pddlconn.textconn.iFrom, pddlconn.textconn.iTo);
                assert tKey not in dPddlConns;
                dPddlConns[tKey] = pddlconn;

        for textconn in self.lTextConns:
            for pddlconn in textconn.lPddlConns:
                tReverseKey = (pddlconn.sPddlTo, pddlconn.sPddlFrom, pddlconn.textconn.iTo, pddlconn.textconn.iFrom);
                assert tReverseKey in dPddlConns;
                pddlconn.pddlconnReverse = dPddlConns[tReverseKey];

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
        else:
            assert False, 'Bad annotation:' + sLine;

    def FromConnectionsLine(self, sLine):
        lConnectionLines = sLine.split()[1:];
        self.lTextConns = map(lambda sLine:TextConn(sLine, self), lConnectionLines);

        

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
        self.lWords = self.sText.split();

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

            
    def GenAllGranularSamples(self, fLog = None):
        #if self.iIndex == 6281:
            # this sentence has the weird 1 1/2 thing which is screwing up the indexes
        #    return 0, [];
        if self.bBad:
            return 0, [];
        iNumLoopy = 0;
        lSamples = [];
        if fLog != None:
            print >> fLog, "Sentence:", self.sText;
        for textconn in self.lTextConns:
            if fLog != None:
                print >> fLog, "\tConn:", textconn.sFrom, '-->', textconn.sTo, '   ::   ';
            for pddlconn in textconn.lPddlConns:
                sample = Sample.GranularSample(pddlconn);
                pddlconn.sample = sample;
                if sample.features.bLoopy:
                    iNumLoopy += 1;
                else:
                    lSamples.append(sample);
                    if fLog != None:
                        for sFeature in sample.features.GetFeatureWordList():
                            print >> fLog, '\t\t', sFeature
        return iNumLoopy, lSamples;
                        
    @staticmethod
    def AddDepFeatures(lSentences, sDepFile):
        lDeps = load_parse.load_deps(sDepFile);
        llPosTags = load_parse.load_tags(sDepFile);
        assert len(lDeps) == len(lSentences), "Not Same Len: " + str(len(lSentences)) + ' ' + str(len(lDeps));
        assert len(llPosTags) == len(lSentences), "Not Same Len: " + str(len(lSentences)) + ' ' + str(len(lDeps));
        for dep, lPosTags, sentence in zip(lDeps, llPosTags, lSentences):
            if sentence.iIndex == 6281:
                # this sentence has the weird 1 1/2 thing which is screwing up the indexes
                sentence.bBad = True;
                continue;
            lDeps = dep[0];
            sentence.AddDeps(lDeps);
            sentence.lPosTags = lPosTags;
            if len(sentence.lWords) != len(sentence.lPosTags):
                print "WARNING: skipping sentence -- Length Mismatch -- Sentence: " + str(len(sentence.lWords)) + ' ' + str(len(sentence.lPosTags));
                sentence.bBad = True;
                continue;
            sentence.ComputePddlConns();
            #assert(len(sentence.lWords) == len(sentence.lPosTags)), 
    
    @staticmethod
    def AddOldSentenceFeatures(lSentences, lOldSentences):
        dOldSentenceStrings = {};
        for sentence in lOldSentences:
            dOldSentenceStrings[sentence.sText] = 0;
        print "Num Sentences: New:", len(lSentences), " old:", len(lOldSentences);
        for sentence in lSentences:
            if sentence.sText in dOldSentenceStrings:
                dOldSentenceStrings[sentence.sText] = 1;
                sentence.bIsInOld = True;
            else:
                print "New Sentence:", sentence.sText;
        for sText, iCount in dOldSentenceStrings.items():
            if iCount == 0:
                print "MISSING:", sText;


def GenAllGranularSamplesFromList(lSentences, sLogFileName):
    sSentenceLogFile = config.get_string('SENTENCE_LOG_FILE');
    fLog = open(sSentenceLogFile, 'w');
    lSamples = [];
    iNumLoopy = 0;
    for sentence in lSentences:
        iCurNumLoopy, lCurSamples = sentence.GenAllGranularSamples(fLog);
        lSamples.extend(lCurSamples);
        iNumLoopy += iCurNumLoopy;

    if iNumLoopy > 0:
        print "NUM LOOPY:", iNumLoopy;
    assert iNumLoopy < config.get_int('NUM_ALLOWED_LOOPY'), 'Too Many Loopy: ' + str(iNumLoopy) + ' NonLoopy: ' + str(len(lSamples));

    sGoldDepFile = config.get_string('GOLD_DEP_FILE');
    if sGoldDepFile != '':
        dGoldDeps = data.file_to_obj_with_comments(sGoldDepFile);
        # add the gold dep info
        for sample in lSamples:
            if (sample.pddlconn.sPddlTo in dGoldDeps) and (sample.pddlconn.sPddlFrom in dGoldDeps[sample.pddlconn.sPddlTo]):
                sample.bGoldPos = True;

    sPredDictFile = config.get_string('PRED_DICT_FILE');
    if sPredDictFile != '':
        lPredicates = predicate.PredDictFileToPredList(sPredDictFile);
        dObjToPredList = collections.defaultdict(lambda:[]);
        for predCur in lPredicates:
            dObjToPredList[predCur.GetObject()].append(predCur);
        for sample in lSamples:
            sample.pddlconn.lFromPreds = dObjToPredList[sample.pddlconn.sPddlFrom];
            sample.pddlconn.lToPreds = dObjToPredList[sample.pddlconn.sPddlTo];
    else:
        assert False;
    #prune the unecessary features
    dFeatureCounts = collections.defaultdict(lambda:0);
    for sample in lSamples:
        for iFeature in sample.features.GetFeatureIndexList():
            dFeatureCounts[iFeature] += 1;
    iMinFeatureCount = config.get_int('MIN_FEATURE_OCCURANCE_COUNT');
    for sample in lSamples:
        for iFeature in sample.features.GetFeatureIndexList():
            if dFeatureCounts[iFeature] < iMinFeatureCount:
                sample.features.RemoveFeature(iFeature);
    return lSamples;


def ReadSentencesFromTextFileSimple(sSentenceFile):
    lLines = map(lambda x: x.strip(), open(sSentenceFile).readlines());
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



def ReadSentencesFromTextFile():
    sSentenceFile = config.get_string('SENTENCE_FILE');
    sOldSentenceFile = config.get_string('OLD_SENTENCE_FILE');
    sDepFile = config.get_string('DEPENDANCY_FILE');
    
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile);

    if sDepFile != '':
        Sentence.AddDepFeatures(lSentences, sDepFile);
    if sOldSentenceFile != '':
        lOldSentences = ReadSentencesFromTextFileSimple(sOldSentenceFile);
        Sentence.AddOldSentenceFeatures(lSentences, lOldSentences);

    return lSentences;
