import collections
import config

USENUMERICS = True;

class Predicate:
    def __init__(self):
        self.bFunc = False;
        self.sName = 'thing-available';
        self.lArgs = [];
        self.sType = 'NOTYPE';
        self.fValue = -10000;
        self._iIndex = -1;
        self.sString = '';
        self.sSimpleString = '';

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

    def ToSimpleString(self):
        if self.sSimpleString == '':
            self.sSimpleString = self.ToSimpleStringInternal();
        return self.sSimpleString;


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
                assert False;
                #self._iIndex = -1000;
            
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

    def FromPredDictLine(self, sLine):
        lSplitLine = sLine.split('|');
        self.iIndex = int(lSplitLine[0]);
        self.bFunc = (lSplitLine[1] != '0');
        lSplitName = lSplitLine[2].split(' ');
        self.sName = lSplitName[0];
        self.fValue = int(lSplitLine[1])-1;
        self.sType = '>';
        for sArg in lSplitName[1:]:
            self.lArgs.append(sArg);
    
    def GetObject(self):
        if self.sName == 'furnace-fuel':
            return self.sName;
        else:
            assert(self.sName == 'thing-available')
            assert(len(self.lArgs) == 1);
            return self.lArgs[0];

    def FromThingAvailableNameAndNum(self, sName, iNum):
        self.bFunc = True;
        self.sType = '>';
        if sName == 'furnace-fuel':
            self.sName = 'furnace-fuel';
        else:
            self.sName = 'thing-available';
            self.lArgs.append(sName);
        
        if iNum == -1:
            self.fValue = 0;
        else:
            self.fValue = iNum-1;
    
    def FromPddlLine(self, sLine):
        sLine = sLine.strip();
        lSplitLine = sLine.split();
        assert lSplitLine[0] == '(>', 'Bad Start:' + lSplitLine[0];
        self.sType = '>';
        self.bFunc = True;
        if lSplitLine[1] == '(thing-available':
            self.sName = 'thing-available';
        elif lSplitLine[1] == '(furnace-fuel)':
            self.sName = 'furnace-fuel';
        else:
            assert False, 'Bad Name:' + lSplitLine[1];
        iNumIndex = 2;
        if self.sName == 'thing-available':
            # add an arg
            self.lArgs.append(lSplitLine[2].rstrip(')'));
            iNumIndex = 3;
        assert iNumIndex < len(lSplitLine), 'BadNum: ' + str(iNumIndex) + ' len: ' + str(len(lSplitLine));
        self.fValue = int(lSplitLine[iNumIndex].rstrip(')'));
       
        

def PredDictFileToPredListDict(sFileName, fKeyFunc):
    lPreds = PredDictFileToPredList(sFileName);
    print "NumPreds:", len(lPreds);
    dPredKeyToPred = collections.defaultdict(lambda:[]);
    for pred in lPreds:
        dPredKeyToPred[fKeyFunc(pred)].append(pred);
    return dPredKeyToPred;


def PredDictFileToPredList(sFileName):
    lLines = open(sFileName).readlines();
    lPreds = [];
    for sLine in lLines:
        sLine = sLine.strip();
        pred = Predicate();
        pred.FromPredDictLine(sLine);
        lPreds.append(pred);
    return lPreds;

def PredDictFileToPredDict(sFileName, fKeyFunc):
    lPreds = PredDictFileToPredList(sFileName);
    print "NumPreds:", len(lPreds);
    dPredKeyToPred = {};
    for pred in lPreds:
        key = fKeyFunc(pred);
        assert(key not in dPredKeyToPred);
        dPredKeyToPred[key] = pred;
    return dPredKeyToPred;


def ReadConnectionsFileToTupSet():
    dIndexToPred = PredDictFileToPredDict(config.get_string('PRED_DICT_FILE'), lambda x:x.iIndex);
    setConnTups = set();
    for sLine in open(config.get_string('CONN_FILE')):
        sLine = sLine.strip();
        lSplit = sLine.split('|');
        setConnTups.add((dIndexToPred[int(lSplit[1])].GetObject(), dIndexToPred[int(lSplit[2])].GetObject())); 
    return setConnTups;


def LoadPredStringSet():
    lPreds = PredDictFileToPredList(config.get_string('PRED_DICT_FILE'));
    setPreds = set();
    for pred in lPreds:
        setPreds.add(pred.GetObject());
    print "NumPreds:", len(setPreds);
    return setPreds;

# def PredListToPredDict(lPreds):
#     dPredStringToPred = {};
#     for pred in lPreds:
#         dPredStringToPred[pred.ToString()] = pred;
#         print "Adding:", pred.ToString(), ':';
#     return dPredStringToPred;
