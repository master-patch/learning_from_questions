from nltk.stem.porter import PorterStemmer
import config
import obj_extract
import FeatureSpace

Stemmer = PorterStemmer();

def isVerbTag(sTag):
    return sTag.startswith('VB') or sTag.startswith('vb');

def isSubjObjDepType(sType):
    return ('subj' in sType) or ('obj' in sType);

def IsSubjDepType(sType):
    return ('subj' in sType);

def IsObjDepType(sType):
    return ('obj' in sType);

def IsPrepObjDepType(sType):
    return ('obj' in sType) or ('prep' in sType);


class TextFeatures:
    def __init__(self, sample):
        self.bLoopy = False;
        self.sample = sample;
        self.setFeatures = set();
        self.GenFeatures();

    def CalcDisToTerminals(self, iIndex, iLen):
        iWindowSize = config.get_int('FEATURES:WINDOW_SIZE');
        iLeftDis = iIndex;
        iRightDis = iLen - iIndex - 1;
        if iLeftDis > iWindowSize: iLeftDis = iWindowSize + 1;
        if iRightDis > iWindowSize: iRightDis = iWindowSize + 1;
        return iLeftDis, iRightDis;

    def GetWordAndDistance(self, iPathIndex, iWordIndex, iPathLen, depTree):
        iLeftDis, iRightDis = self.CalcDisToTerminals(iPathIndex, iPathLen);
        sWord = depTree.dIndexToWord[iWordIndex];
        if config.get_bool('FEATURES:DONT_GEN_FEATURES_WITH_PDDL_OBJECT_WORDS') \
                and obj_extract.IsPddlWord(sWord):
            sWord = 'OBJ_WORD';
        if sWord != 'OBJ_WORD' and config.get_bool('FEATURES:USE_STEMMER'):
            sWord = Stemmer.stem_word(sWord);
        return sWord, iLeftDis, iRightDis;
 
    def GenFeatures(self):
        sample = self.sample;
        pddlconn = sample.pddlconn;
        textconn = pddlconn.textconn;
        sentence = textconn.sentence;
        
        bUseStemmer = config.get_bool('FEATURES:USE_STEMMER');

        if (config.get_bool('FEATURES:OLD_SENTENCE') and 
            not sentence.bIsInOld):
            self.AddFeature('NEW_SENTENCE');

        if config.get_bool('FEATURES:USE_SENTENCE_DIR'):
            sSentenceDir = 'SentForw::' if textconn.iFrom < textconn.iTo else 'SentBack::';
        else:
            sSentenceDir = '';
        
        if config.get_bool('FEATURES:USE_DEPS'):
            iCommonDep, lPath = sentence.deptree.FindLeastCommonDep(textconn.iFrom, textconn.iTo);
            
            if iCommonDep == None:
                self.bLoopy = True;
                return None;
            
            iPathLen = len(lPath);

            if config.get_bool('FEATURES:USE_PATH_WORDS'):
                # add features for all words along path
                for i in range(iPathLen):
                    iPath = lPath[i];
                    sWord, iLeftDis, iRightDis = self.GetWordAndDistance(i, iPath, \
                            iPathLen, sentence.deptree);
                    if sWord == 'OBJ_WORD': 
                        continue;
                    sFeatureStr = 'PathWord::%s::%d::%d::%s' \
                            % (sWord, iLeftDis, iRightDis, sSentenceDir);
                    self.AddFeature(sFeatureStr);
                    if config.get_bool('FEATURES:USE_NON_SENTENCE_DIR_TOO'):
                        sFeatureStr = 'PathWord::%s::%d::%d' \
                            % (sWord, iLeftDis, iRightDis);
                        self.AddFeature(sFeatureStr);
            
            if config.get_bool('FEATURES:USE_PATH_DEP_TYPES') and len(lPath) > 0:
                # add features for dep types along the path

                sPathDirFor = 'Forw::' if config.get_bool('FEATURES:USE_PATH_DIR') else '';
                sPathDirBack = 'Back::' if config.get_bool('FEATURES:USE_PATH_DIR') else '';
 
                iPrev = lPath[0];
                bContainsSubj = False;
                bContainsObj = False;
                bContainsPrepObj = False;
                for i in range(1,len(lPath)):
                    iPathCur = lPath[i];
                    dep = None;
                    sPathDir = '';

                    if (iPrev, iPathCur) in sentence.deptree.dTupToDep:
                        sPathDir = sPathDirFor;
                        dep = sentence.deptree.dTupToDep[(iPrev, iPathCur)];
                        sDepType = dep.sType;
                        bContainsSubj |= IsSubjDepType(sDepType);
                        bContainsObj |= IsObjDepType(sDepType);
                        bContainsPrepObj |= IsPrepObjDepType(sDepType);
                            
                    if (iPathCur, iPrev) in sentence.deptree.dTupToDep:
                        sPathDir = sPathDirBack;
                        dep = sentence.deptree.dTupToDep[(iPathCur, iPrev)];
                        sDepType = dep.sType
                        bContainsSubj |= IsSubjDepType(sDepType);
                        bContainsObj |= IsObjDepType(sDepType);
                        bContainsPrepObj |= IsPrepObjDepType(sDepType);
                    
                    if dep != None:
                        sLWord, iLLDis, iLRDis = self.GetWordAndDistance(i-1, iPrev, \
                                iPathLen, sentence.deptree);
                        sRWord, iRLDis, iRRDis = self.GetWordAndDistance(i, iPathCur, \
                                iPathLen, sentence.deptree);

                        # dep feature
                        sFeatureStr = 'PathDep::%s::%d::%d::%s::%s' \
                                % (sDepType, iLLDis, iRRDis, sPathDir, sSentenceDir);
                        self.AddFeature(sFeatureStr);
                        if config.get_bool('FEATURES:USE_NON_SENTENCE_DIR_TOO'):
                            sFeatureStr = 'PathDep::%s::%d::%d::%s::%s' \
                                    % (sDepType, iLLDis, iRRDis, sPathDir, sSentenceDir);
                            self.AddFeature(sFeatureStr);

                        # dep*word / word*dep feature
                        if config.get_bool('FEATURES:USE_WORD_CROSS_DEPTYPE_FEATURES'):

                            sFeatureStr = 'PathWordXDep::%s::%s::%d::%d::%s::%s' \
                                    % (sLWord, sDepType, iLLDis, iRRDis, sPathDir, sSentenceDir);
                            self.AddFeature(sFeatureStr);

                            sFeatureStr = 'PathDepXWord::%s::%s::%d::%d::%s::%s' \
                                % (sDepType, sRWord, iLLDis, iRRDis, sPathDir, sSentenceDir);
                            self.AddFeature(sFeatureStr); 
                             
                    iPrev = iPathCur;
                    
                if config.get_bool('FEATURES:CHECK_CONTAINS_BOTH_SUBJ_AND_OBJ'):
                    if bContainsObj and bContainsSubj:
                        self.AddFeature('CONTAINS_BOTH_SUBJ_AND_OBJ');
                    else:
                        self.AddFeature('DOESNT_CONTAIN_BOTH_SUBJ_AND_OBJ');
                    if bContainsPrepObj and bContainsSubj:
                        self.AddFeature('CONTAINS_BOTH_SUBJ_AND_PREP_OBJ');
                    else:
                        self.AddFeature('DOESNT_CONTAIN_BOTH_SUBJ_AND_PREP_OBJ');
    def RemoveFeature(self, iFeature):
        self.setFeatures.remove(iFeature);

    def AddFeature(self, sWord):
        iFeature = FeatureSpace.FeatureIndex(sWord);
        self.setFeatures.add(iFeature);

    def GetFeatureIndexList(self):
        return sorted(list(self.setFeatures));

    def GetFeatureWordList(self):
        return map(lambda x:FeatureSpace.FeatureString(x), sorted(list(self.setFeatures)));
