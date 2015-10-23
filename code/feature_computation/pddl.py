#!/usr/bin/python
import data
import collections
import copy

import sys
import antlr3
import antlr3.tree
from PddlLexer import PddlLexer
from PddlParser import PddlParser
#from Eval import Eval
import pddl
import data

bPostToPre = False;
bPosOnly = True;
#bRemoveInit = True;
bRemoveInit = False;
lAllowedPredicates = ['placed-thing-at-map',
                       'resource-at-craft',
                       'thing-available','duration-need',
                       'furnace-fuel','placed-thing-at-map','thing-at-map','craft-empty'];
lAllowedPredicates = [];
#lDisallowedPredicates = ['player-at','craft-empty','connect','crafting'];
lDisallowedPredicates = [];

def IsThingAvailable(sPred):
    return sPred.find('thing-available') != -1;
        

def CalcDeeperPredGraph(dCurPredGraph, dOneStepPredGraph):
    dDeeperPredGraph = collections.defaultdict(lambda:{});
    for sPost, dPre in dCurPredGraph.items():
        dNewPre = {};
        for sPre, (sAction, iNumThingAvailables, setPredicates) in dPre.items():
            if iNumThingAvailables >= 2:
                continue;
            # if IsThingAvailable(sPost) and IsThingAvailable(sPre):
            #     # once we've connected thing available's, then stop
            #     continue;
            for sNewPre, (sNewAction, iNewNumThingAvailables, setPredicatesNew) in dCurPredGraph[sPre].items():
                if iNewNumThingAvailables >= 2:
                    continue;
                if len(setPredicates.intersection(setPredicatesNew)) != 0:
                    #there's a loop in here
                    continue;
                # if IsThingAvailable(sPre) and IsThingAvailable(sNewPre):
                #     # once we've connected thing available's, then stop
                #     continue
                if sNewPre == sPost:
                    continue;
                #if sAction.startswith('make-farmland') and sNewAction.endswith('make-farmland'):
                #    continue;
                if sNewPre not in dPre:
                    dNewPre[sNewPre] = (sAction + ',' + sNewAction, iNumThingAvailables+iNewNumThingAvailables,setPredicates.union(setPredicatesNew));
                    
        dDeeperPredGraph[sPost] = dNewPre;
    return dDeeperPredGraph;


class Domain:
    def __init__(self, sDomainFile, sProblemFile, setObjects, iDepth = 10):
        self.lPredicates = [];
        self.lFunctions = [];
        self.lActions = [];
        self.lTypes = [];
        self.lObjects = [];
        self.lInit = [];
        self.lGoals = [];
        self.bPreprocessed = False;
        self.iDepth = iDepth;
        self.setObjects = setObjects;

        domain_char_stream = antlr3.ANTLRInputStream(open(sDomainFile));
        domain_lexer = PddlLexer(domain_char_stream)
        domain_tokens = antlr3.CommonTokenStream(domain_lexer)
        domain_parser = PddlParser(domain_tokens)
        treeDomain = domain_parser.getdomain();

        problem_char_stream = antlr3.ANTLRInputStream(open(sProblemFile));
        problem_lexer = PddlLexer(problem_char_stream)
        problem_tokens = antlr3.CommonTokenStream(problem_lexer)
        problem_parser = PddlParser(problem_tokens)
        treeProblem = problem_parser.getproblem();


        #print "Parsing Domain";
        sys.stdout.flush();
        for iChild in range(treeDomain.getChildCount()):
            node = treeDomain.getChild(iChild)
            sNodeType = node.toString();
            if sNodeType == 'PREDICATES':
                self.ParsePredicates(node);
            elif sNodeType == 'FUNCTIONS':
                self.ParseFunctions(node);
            elif sNodeType == 'TYPES':
                self.ParseTypes(node);
            elif sNodeType == 'ACTION':
                self.lActions.append(Action(node));

        #print "Parsing Problem";
        sys.stdout.flush();
        for iChild in range(treeProblem.getChildCount()):
            node = treeProblem.getChild(iChild)
            sNodeType = node.toString();
            if sNodeType == 'OBJECTS':
                self.ParseObjects(node);
            elif sNodeType == 'INIT':
                self.ParseInit(node);
            elif sNodeType == 'GOAL':
                self.ParseGoal(node);
            else:
                #print "Parsing:", sNodeType;
                pass;
        self.PreProcess();

    def PreProcess(self):
        if not self.bPreprocessed:
            self.bPreprocessed = True;
            self.GenTypeTree();
            self.GenTypeDict();
            self.GenInitSet();
            self.GenPredicateDict();
            self.GenPredGraph();

    def GenInitSet(self):
        self.setInit = set();
        for effect in self.lInit:
            self.setInit.update(effect.GetAllInstances({}));

    def GenTypeDict(self):
        self.dOneHopTypeToObjects = collections.defaultdict(lambda:[]);
        for obj in self.lObjects:
            self.dOneHopTypeToObjects[obj.sType].append(obj.sName);
        self.dTypeToObjects = {};
        #walk type tree, for each type add all it's children
        for sType in self.typetree.dNodes.keys():
            ttn = self.typetree.dNodes[sType];
            self.dTypeToObjects[sType] = \
                ttn.GetAllChildrenObjects(self.dOneHopTypeToObjects);




    def GenTypeTree(self):
        self.typetree = TypeTree(self.lTypes);

    def GenPredGraph(self, bIncludeInits = False):
        assert(not bIncludeInits);
        self.PreProcess();
        self.dOneHopPostToPre = collections.defaultdict(lambda:{});
        for action in self.lActions:
            dCurPostToPre = action.GetFullPostToPre(self.dTypeToObjects,
                                                    self.setInit);
            # gen all postpred to pre pred
            sAction = action.sName;
            for sPost, setPre in dCurPostToPre.items():
                for sPre in setPre:
                    self.dOneHopPostToPre[sPost][sPre] = (sAction, int(IsThingAvailable(sPre))+int(IsThingAvailable(sPost)), 
                                                          set([sPre + "::" + sPost]));

            dCurPostToPre = action.GetObjectPostToPre(self.setObjects);
            # gen all postpred to pre pred
            sAction = action.sName;
            for sPost, setPre in dCurPostToPre.items():
                for sPre in setPre:
                    self.dOneHopPostToPre[sPost][sPre] = (sAction+"-LOOSE", int(IsThingAvailable(sPre))+int(IsThingAvailable(sPost)), 
                                                          set([sPre + "::" + sPost]));

    def WriteConnectionGraph(self, sFilename, dStringToPredIndexList):
        fOut = open(sFilename, 'w');
        # first write out the one hop
        self.WriteOneConnectionGraph(self.dOneHopPostToPre, fOut, 1, dStringToPredIndexList);
        # gen deeper pred graphs
        dCurPredGraph = self.dOneHopPostToPre;
        for iCurDepth in range(2, self.iDepth):
            dCurPredGraph = pddl.CalcDeeperPredGraph(dCurPredGraph, self.dOneHopPostToPre);
            self.WriteOneConnectionGraph(dCurPredGraph, fOut, iCurDepth, dStringToPredIndexList);
        fOut.flush ()
        fOut.close ()
        print 'WriteOneConnectionGraph done.'


    def WriteOneConnectionGraph(self, dCurPredGraph, fOut, iDepth, dStringToPredIndexList):
        for sPost, dPre in dCurPredGraph.items():
            for sPre, (sAction, iNumThingAvailables, setPredicates) in dPre.items():
                if sPre == sPost:
                    continue;
                if None == self.dPredToInt.get (sPost, None):
                    print self.dPredToInt.get (sPost, "pred_to_int ("+sPost+") failed")
                    continue
                if None == self.dPredToInt.get (sPre, None):
                    print self.dPredToInt.get (sPre, "pred_to_int ("+sPre+") failed")
                    continue
                if not sPost.startswith('thing-available') or not sPre.startswith('thing-available'):
                    continue;
                assert iNumThingAvailables == 2;
                lFrom = dStringToPredIndexList[sPost];
                lTo = dStringToPredIndexList[sPre];
                for iFrom in lFrom:
                    for iTo in lTo:
                        #print >> fOut, str(iDepth) + '|' + str(iFrom) + '|' + str(iTo) + '|' + sPost + '|' + sPre + '|' + sAction;
                        print >> fOut, '1|' + str(iFrom) + '|' + str(iTo) + '|' + sPost + '|' + sPre + '|' + sAction;


    def GenPredicateDict(self):
        self.dIntToPred = {};
        self.dPredToInt = {};

        lAllPreds = [];
        #for pred in (self.lPredicates + self.lFunctions):
        for pred in self.lPredicates:
            lCurPreds = pred.GetAllInstances(self.dTypeToObjects);
            lCurPreds = [ ('0', p) for p in lCurPreds ];
            lAllPreds.extend(lCurPreds);
        for pred in self.lFunctions:
            lCurPreds = pred.GetAllInstances(self.dTypeToObjects);
            lCurPreds = [ ('1', p) for p in lCurPreds ];
            lAllPreds.extend(lCurPreds);

        iCurIndex = 0;
        for sType, sPred in lAllPreds:
            self.dIntToPred[iCurIndex] = (sPred, sType);
            self.dPredToInt[sPred] = iCurIndex;
            iCurIndex += 1;

    def GetObjective(self):
        assert(len(self.lGoals) == 1);
        precondition = self.lGoals[0];
        #print "PRECONDITION:", precondition.sText;
        assert(precondition.sType == 'COMPARISON_GD');
        assert(precondition.comparison.sDir == '>');
        assert(precondition.comparison.FromFunctionInst.sName == 'thing-available');
        sObjective = precondition.comparison.FromFunctionInst.lArgs[0].sName;
        iNum = int(precondition.comparison.sTo);
        #print "Found:", sObjective, " num:", iNum;
        return (sObjective, iNum+1);


    def WritePredDict(self, sFileName):
        self.PreProcess();
        fOut = open(sFileName, 'w');
        for iKey, (sPred, sType) in self.dIntToPred.items():
            print >> fOut, str(iKey) + '|' + sType + '|' + sPred;

    def ParseObjects(self, node):
        for iChild in range(node.getChildCount()):
            self.lObjects.append(Object(node.getChild(iChild)));


    def ParsePredicates(self, node):
        for iChild in range(node.getChildCount()):
            self.lPredicates.append(Predicate(node.getChild(iChild),
                                              bFunction = False));

    def ParseFunctions(self, node):
        for iChild in range(node.getChildCount()):
            self.lFunctions.append(Predicate(node.getChild(iChild),
                                             bFunction = True));

    def ParseTypes(self, node):
        for iChild in range(node.getChildCount()):
            self.lTypes.append(Type(node.getChild(iChild)));

    def ParseInit(self, node):
        for iChild in range(node.getChildCount()):
            nodeChild = node.getChild(iChild);
            self.lInit.append(Effect(nodeChild));

    def ParseGoal(self, node):
        assert node.getChildCount() == 1;
        #for iChild in range(node.getChildCount()):
        nodeChild = node.getChild(0);
        self.lGoals = Precondition.GenPreconditionList(nodeChild);




class Object:
    def __init__(self, node):
        self.sName = node.toString();
        self.sType = node.getChild(0).toString();


class Type:
    def __init__(self, node):
        self.sName = node.toString();
        if node.getChildCount() > 0:
            self.sParent = node.getChild(0).toString();
        else:
            self.sParent = None;

class TypeTree:
    def __init__(self, lTypes):
        self.lRoots = [];
        self.dNodes = {};
        # add all the nodes
        for typeCur in lTypes:
            if typeCur.sName not in self.dNodes:
                ttn = TypeTreeNode(typeCur.sName);
                self.dNodes[ttn.sName] = ttn;
            # also add the parent just in case
            if typeCur.sParent != None and typeCur.sParent not in self.dNodes:
                ttnParent = TypeTreeNode(typeCur.sParent);
                self.dNodes[ttnParent.sName] = ttnParent;

        #add all the connections
        for typeCur in lTypes:
            if typeCur.sParent == None:
                self.lRoots.append(self.dNodes[typeCur.sName]);
            else:
                ttnCur = self.dNodes[typeCur.sName];
                ttnParent = self.dNodes[typeCur.sParent];
                ttnParent.lChildren.append(ttnCur);
                ttnCur.parent = ttnParent;


class TypeTreeNode:
    def __init__(self, sName):
        self.sName = sName
        self.lChildren = [];
        self.parent = None;

    def GetAllChildrenObjects(self, dTypeToObjects):
        lObjects = dTypeToObjects[self.sName];
        for ttnChild in self.lChildren:
            lObjects.extend(ttnChild.GetAllChildrenObjects(dTypeToObjects));
        return lObjects;


def ConcatAllPairsStrings(lPrefix, lSuffix):
    lPairs = [];
    for sPrefix in lPrefix:
        for sSuffix in lSuffix:
            lPairs.append(sPrefix + ' ' + sSuffix);
    return lPairs;

class Predicate:
    def __init__(self, node, bFunction):
        self.sName = node.toString();
        self.lArgs = Arg.GenArgList(node);
        self.bFunction = bFunction;

    def GetAllInstances(self, dTypeToObjects):
        lInstances = [self.sName];
        for arg in self.lArgs:
            lInstances = ConcatAllPairsStrings(lInstances,
                                               dTypeToObjects[arg.sType]);
            iCur = len(dTypeToObjects[arg.sType]);
        #lInstances = ConcatAllPairsStrings(lInstances, '|' + self.bFunction);
        return lInstances;


class PredicateInst:
    def __init__(self, node):
        assert ((node.toString() == 'PRED_HEAD') or
                (node.toString() == 'PRED_INST'));
        self.sName = node.getChild(0).toString();
        self.lArgs = Arg.GenArgList(node);
        # remove the first since it will be a dup
        del self.lArgs[0];

    def ToString():
        sOut = self.sName;
        for arg in lArgs:
            sOut += ' ' + arg.sName;
        

    def GetAllInstances(self, dParamToObjects):
        if (((lAllowedPredicates != []) and
             (self.sName not in lAllowedPredicates)) or
            ((lDisallowedPredicates != []) and
             (self.sName in lDisallowedPredicates))):
            return [];
        sOutput = self.sName;
        for arg in self.lArgs:
            sArg = arg.sName;
            if sArg.startswith('?'):
                sArg = dParamToObjects[sArg];
            sOutput += " " + sArg;
        return [sOutput];
    
    def GetAllObjects(self, setObjects):
        setCurObjects = set();
        for arg in self.lArgs:
            sArg = arg.sName;
            if sArg in setObjects:
                setCurObjects.add(sArg);
        return setCurObjects;


# class Function:
#     def __init__(self, node):
#         self.sName = node.toString();
#         self.lArgs = Arg.GenArgList(node);

#     def GetNumInstances(self, dTypeToObjects):
#         iNumInstances = 1;
#         for arg in self.lArgs:
#             iNumInstances *= len(dTypeToObjects[arg.sType]);
#         return iNumInstances;



class FunctionInst:
    def __init__(self, node):
        assert node.toString() == 'FUNC_HEAD', "BadFuncInst:" + node.toString();
        self.sText = node.toStringTree();
        self.sName = node.getChild(0).toString();
        self.lArgs = Arg.GenArgList(node);
        # remove the first since it will be a dup
        del self.lArgs[0];

    def GetAllInstances(self, dParamToObjects):
        if (self.sName not in lAllowedPredicates) and (lAllowedPredicates != []):
            return [];
        sOutput = self.sName;
        for arg in self.lArgs:
            sArg = arg.sName;
            if sArg.startswith('?'):
                sArg = dParamToObjects[sArg];
            sOutput += " " + sArg;
        return [sOutput];


    def GetAllObjects(self, setObjects):
        setCurObjects = set();
        for arg in self.lArgs:
            sArg = arg.sName;
            if sArg in setObjects:
                setCurObjects.add(sArg);
        return setCurObjects;


class Arg:
    def __init__(self, node):
        self.sName = node.toString();
        if node.getChildCount() > 0:
            self.sType = node.getChild(0).toString();
            assert node.getChildCount() == 1;
        else:
            self.sType = None;

    @staticmethod
    def GenArgList(node):
        lArgs = [];
        for iChild in range(node.getChildCount()):
            lArgs.append(Arg(node.getChild(iChild)));
        return lArgs;


def ConcatAllPairs(lCurDicts, sArg, lObjects):
    lOutput = [];
    for dDict in lCurDicts:
        for sObject in lObjects:
            dNew = copy.deepcopy(dDict);
            dNew[sArg] = sObject;
            lOutput.append(dNew);
    return lOutput;



class Action:
    def __init__(self, node):
        self.sName = node.getChild(0).toString();
        self.lArgs = [];
        self.lPreconditions = [];
        self.lEffects = [];
        for iChild in range(1, node.getChildCount()):
            nodeChild = node.getChild(iChild);
            sType = nodeChild.toString();
            if sType == 'PARAMETERS':
                self.lArgs = Arg.GenArgList(nodeChild);
            elif sType == 'PRECONDITION':
                self.lPreconditions = \
                    Precondition.GenPreconditionList(nodeChild);
            elif sType == 'EFFECT':
                self.lEffects = Effect.GenEffectList(nodeChild);
            else:
                print "   ***BadChild:", nodeChild.toString(), nodeChild.toStringTree();

    def GetThingAvailablePost(self):
        dThingAvailable = {};
        for effect in self.lEffects:
            tIncrease = effect.GetThingAvailable(bIncrease = True);
            if tIncrease != None:
                dThingAvailable[tIncrease[0]]= tIncrease[1];

    def GetThingAvailablePre(self):
        dThingAvailable = {};
        for precondition in self.lPreconditions:
            tIncrease = precondition.GetThingAvailable(bGreaterThan = True);
            if tIncrease != None:
                dThingAvailable[tIncrease[0]]= tIncrease[1];
        data.print_obj(dThingAvailable);

    def ParamToObjDictList(self, dTypeToObjects):
        lParamToObjDicts = [{}];
        for arg in self.lArgs:
            #print "Types:", dTypeToObjects.keys();
            lParamToObjDicts = ConcatAllPairs(lParamToObjDicts, arg.sName,
                                              dTypeToObjects[str(arg.sType)]);
        return lParamToObjDicts;

    def GetFullPostToPre(self, dTypeToObjects, setInit):
        dPostToPre = collections.defaultdict(lambda: set());
        lParamToObjects = self.ParamToObjDictList(dTypeToObjects);
        for dParamToObjects in lParamToObjects:
            lPrePreds = self.GetFullPrePredList(dParamToObjects, setInit);
            lPostPreds = self.GetFullPostPredList(dParamToObjects, setInit);
            # now remove all the predicates in init in both
            if bRemoveInit:
                lPrePreds = list(set(lPrePreds).difference(setInit));
                lPostPreds = list(set(lPostPreds).difference(setInit));
            if bPostToPre:
                for sPostPreds in lPostPreds:
                    dPostToPre[sPostPreds].update(lPrePreds);
            else:
                for sPrePreds in lPrePreds:
                    dPostToPre[sPrePreds].update(lPostPreds);
        return dPostToPre;

    def GetObjectPostToPre(self, setObjects):
        dPostToPre = collections.defaultdict(lambda: set());
        setPreObjects = self.GetFullPreObjectSet(setObjects);
        setPostObjects = self.GetFullPostObjectSet(setObjects);
        for sPreObj in setPreObjects:
            sPrePred = 'thing-available '+ sPreObj;
            for sPostObj in setPostObjects:
                sPostPred = 'thing-available '+ sPostObj;
                print "Action:", self.sName, 'Pre:', sPreObj, 'Post:', sPostObj;
                dPostToPre[sPrePred].add(sPostPred);
        return dPostToPre;

    def GetFullPreObjectSet(self, setObjects):
        setPreObjs = set();
        for pre in self.lPreconditions:
            setPreObjs.update(pre.GetAllObjects(setObjects));
        return setPreObjs;

    def GetFullPrePredList(self, dParamToObjects, setInit):
        assert bPosOnly, "Haven't coded Negative Preds yet";
        lPrePreds = [];
        for pre in self.lPreconditions:
            lPrePreds.extend(pre.GetAllInstances(dParamToObjects));
        return lPrePreds;

    def GetFullPostPredList(self, dParamToObjects, setInit):
        assert bPosOnly, "Haven't coded Negative Preds yet";
        lPostPreds = [];
        for post in self.lEffects:
            lPostPreds.extend(post.GetAllInstances(dParamToObjects));
        return lPostPreds;

    def GetFullPostObjectSet(self, setObjects):
        setPostObjs = set();
        for post in self.lEffects:
            setPostObjs.update(post.GetAllObjects(setObjects));
        return setPostObjs;
        



class Precondition:
    def __init__(self, node):
        self.sText = node.toStringTree();
        self.bNot = False;
        self.predicate_inst = None;
        self.comparison = None;
        if node.toString() == 'NOT_GD':
            self.bNot = True;
            node = node.getChild(0);
        self.sType = node.toString();
        if self.sType == 'PRED_HEAD':
            self.predicate_inst = PredicateInst(node);
        elif self.sType == 'COMPARISON_GD':
            self.comparison = Comparison(node);
        else:
            assert False, 'Havent coded precondition:' + self.sType;

    def GetThingAvailable(self, bGreaterThan = True):
        print "Predicate:", self.sType + ": " + self.sText;
        assert bGreaterThan
        if self.sType != 'COMPARISON_GD':
            "Skipping because not comparison";
            return None;
        if self.comparison.sDir != '>':
            "Skipping because dir is:", self.comparison.sDir;
            return None;
        print self.comparison.FromFunctionInst.sText, self.comparison.sTo;

    def GetAllInstances(self, dParamToObjects):
        assert(bPosOnly);
        if self.bNot:
            return [];
        if self.predicate_inst != None:
            return self.predicate_inst.GetAllInstances(dParamToObjects);
        elif self.comparison != None:
            return self.comparison.GetAllInstances(dParamToObjects);
        else:
            assert False;

    def GetAllObjects(self, setObjects):
        if self.bNot:
            return set();
        if self.predicate_inst != None:
            return self.predicate_inst.GetAllObjects(setObjects);
        elif self.comparison != None:
            return self.comparison.GetAllObjects(setObjects);
        else:
            assert False;
        



    @staticmethod
    def GenPreconditionList(node):
        lPreconditions = [];
        nodeList = node.getChild(0);
        lChildNodes = [];
        if nodeList.toString() == 'AND_GD':
            for iChild in range(nodeList.getChildCount()):
                nodeChild = nodeList.getChild(iChild);
                if nodeChild.toString() == 'OR_GD':
                    print "WARNING: HACKING OR_GD to be same as AND_GD";
                    for iOrChild in range(nodeChild.getChildCount()):
                        nodeOrChild = nodeChild.getChild(iOrChild);
                        lPreconditions.append(Precondition(nodeOrChild));
                        print "OR_CHILD:", nodeOrChild.ToStringTree();
                else:
                    lPreconditions.append(Precondition(nodeChild));
        else:
            #assert False, 'Havent coded non-AND preconditions: ' + nodeList.toString();
            lPreconditions.append(Precondition(nodeList));

        return lPreconditions;

class Comparison:
    def __init__(self, node):
        assert node.getChildCount() == 3;
        self.sDir = node.getChild(0).toString();
        self.FromFunctionInst = FunctionInst(node.getChild(1));
        self.sTo = node.getChild(2).toString();
        self.sToTree = node.getChild(2).toStringTree();

    def GetAllInstances(self, dParamToObjects):
        assert(bPosOnly);
        # return only positive instances
        if self.sDir == '<':
            return [];
        assert self.sDir == '>' or self.sDir == '=', 'Dir is:' + self.sDir;
        return self.FromFunctionInst.GetAllInstances(dParamToObjects);

    def GetAllObjects(self, setObjects):
        assert(bPosOnly);
        # return only positive instances
        if self.sDir == '<':
            return set();
        assert self.sDir == '>' or self.sDir == '=', 'Dir is:' + self.sDir;
        setCurObjects = self.FromFunctionInst.GetAllObjects(setObjects);
        lTree = self.sToTree.rstrip(')').split();
        for sObj in setObjects:
            if sObj in lTree:
                setCurObjects.add(sObj);
        return setCurObjects;



class Assign:
    def __init__(self, node):
        if node.getChildCount() == 2:
            self.sType = node.toString();
            iFirstChild = 0;
        elif node.getChildCount() == 3:
            self.sType = node.getChild(0).toString();
            iFirstChild = 1;
        else:
            assert False;
        self.From = FunctionInst(node.getChild(iFirstChild));
        nodeSecondChild = node.getChild(iFirstChild+1);
        if nodeSecondChild.getChildCount() > 0:
            self.To = FunctionInst(nodeSecondChild);
        else:
            self.To = nodeSecondChild.toString();

    def GetAllInstances(self, dParamToObjects):
        if self.sType == 'decrease':
            return [];
        if ((self.sType == 'assign' or self.sType == 'INIT_EQ') and
            isinstance(self.To, basestring) and (self.To == '0')):
            return [];
        assert ((self.sType == 'increase') or (self.sType == 'assign') or
                (self.sType == 'INIT_EQ'));
        lInst = self.From.GetAllInstances(dParamToObjects);
        #if not isinstance(self.To, basestring):
        #    lInst.extend(self.To.GetAllInstances(dParamToObjects));
        return lInst;

    def GetAllObjects(self, setObjects):
        if self.sType == 'decrease':
            return set();
        if ((self.sType == 'assign' or self.sType == 'INIT_EQ') and
            isinstance(self.To, basestring) and (self.To == '0')):
            return set();
        assert ((self.sType == 'increase') or (self.sType == 'assign') or
                (self.sType == 'INIT_EQ'));
        setObjects = self.From.GetAllObjects(setObjects);
        #if not isinstance(self.To, basestring):
        #    lInst.extend(self.To.GetAllInstances(dParamToObjects));
        return setObjects;

class Effect:
    def __init__(self, node):
        self.sText = node.toStringTree();
        self.bNot = False;
        self.predicate_inst = None;
        self.assign = None;
        if node.toString() == 'NOT_EFFECT':
            self.bNot = True;
            node = node.getChild(0);
        self.sType = node.toString();
        if (self.sType == 'PRED_HEAD') or (self.sType == 'PRED_INST'):
            self.predicate_inst = PredicateInst(node);
        elif (self.sType == 'ASSIGN_EFFECT') or (self.sType == 'INIT_EQ'):
            self.assign = Assign(node);
        else:
            assert False, 'Havent coded effect:' + self.sType + ':';

    def GetThingAvailable(self, bIncrease):
        assert bIncrease;
        if self.sType != 'ASSIGN_EFFECT':
            return None;
        if self.assign.sType != 'increase':
            return None;
        if self.assign.From.sName != 'thing-available':
            if self.assign.From.sName == 'furnace-fuel':
                return ('furnace-fuel', self.assign.To);
            return None;
        return (self.assign.From.lArgs[0].sName, self.assign.To);
            

    def GetAllInstances(self, dParamToObjects):
        assert(bPosOnly);
        if self.bNot:
            return [];
        if self.predicate_inst != None:
            return self.predicate_inst.GetAllInstances(dParamToObjects);
        elif self.assign != None:
            return self.assign.GetAllInstances(dParamToObjects);
        else:
            assert False;

    def GetAllObjects(self, setObjects):
        assert(bPosOnly);
        if self.bNot:
            return set();
        if self.predicate_inst != None:
            return self.predicate_inst.GetAllObjects(setObjects);
        elif self.assign != None:
            return self.assign.GetAllObjects(setObjects);
        else:
            assert False;


    @staticmethod
    def GenEffectList(node):
        lEffects = [];
        nodeList = node.getChild(0);
        if nodeList.toString() == 'AND_EFFECT':
            for iChild in range(nodeList.getChildCount()):
                nodeChild = nodeList.getChild(iChild);
                lEffects.append(Effect(nodeChild));
        else:
            assert False, 'Havent coded non-AND preconditions';

        return lEffects;

def ReadPredDictFile(sFile):
    dStringToPredIndexList = collections.defaultdict(lambda:[]);
    setObjects = set();
    for sLine in open(sFile).readlines():
        sLine = sLine.strip();
        lSplit = sLine.split('|');
        dStringToPredIndexList[lSplit[2]].append(int(lSplit[0]));
        lPredSplit = lSplit[2].split();
        if len(lPredSplit) > 1:
            assert len(lPredSplit) ==  2, str(len(lPredSplit)) + ':' + lPredSplit;
            setObjects.add(lPredSplit[1]);
    return dStringToPredIndexList, setObjects;

def main():
    if len(sys.argv) < 3:
        #sDomainFile = "domain.v120.pddl";
        #sProblemFile = "problem1.pddl";
        sDomainFile = "../subgoal_learning/data/domain-no-stone-iron-tools-simple-furnace.v120.pddl";
        sProblemFile = "../subgoal_learning/data/problems/identical_init_rand2/coal.14.pddl";
        sDictFile = "../subgoal_learning/data/thing-available_max5.dict";
        #sDomainFile = "domain-non-numeric.v4.pddl";
        #sProblemFile = "coal.30.pddl";
    else:
        sDomainFile = sys.argv[1];
        sProblemFile = sys.argv[2];

    dStringToPredIndexList, setObjects = ReadPredDictFile(sDictFile);
    # comment in this line for loose
    #domain = pddl.Domain(sDomainFile, sProblemFile, setObjects, iDepth = 10);
    # comment in this line for tight
    domain = pddl.Domain(sDomainFile, sProblemFile, set(), iDepth = 10);
    domain.WritePredDict('pred_dict.txt');
    print "objects:", setObjects;
    domain.WriteConnectionGraph('pddl_connections.txt', dStringToPredIndexList);
    #print domain.ComputeNumPredicateValues();



if __name__ == '__main__':
    main();
