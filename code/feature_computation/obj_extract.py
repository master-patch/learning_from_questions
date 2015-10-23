
from stemmer import PorterStemmer;

minecraftDictFile = 'minecraft_unit.txt';
text2pddl = None;
setPddl = None;

def ReadMinecraftDict(infoFile):
    global text2pddl;

    fin = open(infoFile)
    lines = fin.readlines()
    fin.close()
    lines = [ line.strip() for line in lines ];

    text2pddl = {}
    p = PorterStemmer()
    for line in lines:
        if len(line)==0: continue;
        parts = line.split(':');
        textName = parts[0];
        words = [ p.stem(w.lower(),0,len(w)-1) for w in textName.split() ]
        textName = ' '.join(words);
        if len(parts)>1:
            pddlName = parts[1];
        else:
            pddlName = parts[0];
        assert(pddlName!='');
        assert(textName!='');
        text2pddl[textName] = pddlName;


def GenMinecraftSet():
    global text2pddl;
    global setPddl;
    if text2pddl == None:
        ReadMinecraftDict(minecraftDictFile);
    setPddl = set();
    for sTextName in text2pddl.keys():
        lstWords = sTextName.split(' ');
        for sWord in lstWords:
            setPddl.add(sWord);

stemmer = PorterStemmer();

def IsPddlWord(sWord):
    assert sWord.find(' ') == -1;
    sWord = stemmer.stem(sWord.lower(), 0, len(sWord)-1);
    global setPddl
    if setPddl == None:
        GenMinecraftSet();
    return (sWord in setPddl);

def IsNounTag(_sTag):
    _sTag = _sTag.lower();
    return _sTag == 'nn' or _sTag == 'nns' or _sTag == 'nnp' or _sTag == 'nnps';

def GetPddlObjByIndex(_lWordTagTuples, _iIndex):
    global text2pddl;
    global setPddl;
    if text2pddl == None:
        ReadMinecraftDict(minecraftDictFile);
    if setPddl == None:
        GenMinecraftSet();

    iLen = len(_lWordTagTuples);
    assert(_iIndex >= 0 and _iIndex < iLen), 'GetPddlObj: argument index out of list';

    # use old heuristics if the word is not tagged as noun.
    sCurTag, sCurWord = _lWordTagTuples[_iIndex];
    if not IsNounTag(sCurTag):
        print 'GetPddlObj: specified word \"%s\" is not a noun in sentence, its a \"%s\"' % (sCurWord, sCurTag);
        return GetPddlObj(sCurWord);

    # get the noun phrase
    sPhrase = stemmer.stem(sCurWord.lower(), 0, len(sCurWord)-1);
    iStart = _iIndex;
    iEnd = _iIndex;
    while (iStart > 0):
        sTag, sWord = _lWordTagTuples[iStart - 1];
        if not IsNounTag(sTag): break;
        sPhrase = stemmer.stem(sWord.lower(), 0, len(sWord)-1) + ' ' + sPhrase;
        iStart -= 1;
    while (iEnd + 1 < iLen):
        sTag, sWord = _lWordTagTuples[iEnd + 1];
        if not IsNounTag(sTag): break;
        sPhrase = sPhrase + ' ' + stemmer.stem(sWord.lower(), 0, len(sWord)-1);
        iEnd += 1;

    # if there is a full match, return the matched pddl obj only.

    # deal with phrases like "wooden_JJ pickaxe_NN", "cooked_VBN fish_NN" and "cooked_JJ fish_NN"
    sPhr = sPhrase;
    while (iStart > 0):
        sTag, sWord = _lWordTagTuples[iStart - 1];
        if sTag != 'JJ' and sTag != 'jj' and sTag != 'vbn' and sTag != 'VBN': break;
        sPhr = stemmer.stem(sWord.lower(), 0, len(sWord)-1) + ' ' + sPhr;
        if sPhr in text2pddl:
            sPddl = text2pddl[sPhr];
            if sPddl == 'NULL':
                return [];
            else:
                return [ sPddl ];
        iStart -= 1;

    if sPhrase in text2pddl:
        sPddl = text2pddl[sPhrase];
        if sPddl == 'NULL':
            return [];
        else:
            return [ sPddl ];
 
    # use old heuristics otherwise
    return GetPddlObj(sCurWord);

#
def GetPddlObj(_sWord):
    global text2pddl;
    if text2pddl == None:
        ReadMinecraftDict(minecraftDictFile);

    setObjs = set();
    p = PorterStemmer();
    sLastWord = p.stem(_sWord.lower(), 0, len(_sWord)-1);
    if sLastWord == 'block': return setObjs;
    #print sLastWord;
    for sTextName in text2pddl.keys():
        if text2pddl[sTextName] == 'NULL': continue;
        lstWords = sTextName.split(' ');
        sLastTextWord = lstWords[len(lstWords)-1];
        if sLastTextWord == 'block':
            if len(lstWords) == 1: continue;
            sLastTextWord = lstWords[len(lstWords)-2];
        if sLastTextWord == sLastWord:
            setObjs.add(text2pddl[sTextName]);
    return list(setObjs);

def ExtractObjPairs(_sText):
    global text2pddl;
    if text2pddl == None:
        ReadMinecraftDict(minecraftDictFile);

    iPos = _sText.find('|');
    assert(iPos!=-1);
    sFrom = _sText[:iPos];
    sTo = _sText[iPos+1:];
    lstFrom = GetPddlObj(sFrom);
    lstTo = GetPddlObj(sTo);

    lstObjPairs = [];
    for sObjFrom in lstFrom:
        for sObjTo in lstTo:
            if sObjFrom != sObjTo:
                lstObjPairs.append('%s|%s' % (sObjFrom, sObjTo));
    return lstObjPairs;

