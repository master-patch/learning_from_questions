
import math;
import sys;
from stemmer import PorterStemmer;
import data;
import itertools;

inputFile = None;
outputFile = None;
windowSize = 1;
infoFile = 'minecraft_unit.txt'

unitDict = {};

def splitToken(token,isStem=True):
    toks = token.split('_')
    word = toks[0].lower()
    tag = toks[1]
    if not word.isalnum():
        tag = 'PUNC'
    if isStem:
        # simple post stem
        p = PorterStemmer()
        #word = p.stem1(word,0,len(word)-1)
        word = p.stem(word,0,len(word)-1)

    return (word, tag)

def isNounTag(tag):
    isNoun =  (tag == 'NN' or tag == 'NNS' or tag == 'NNP' or tag == 'NNPS');
    if tag.startswith('NN') and not isNoun:
        print 'warning: tag=%s' % tag;
    return isNoun;

def ReadInfoFile(infoFile):
    global text2pddl;

    fin = open(infoFile)
    lines = fin.readlines()
    fin.close()
    lines = [ line.strip() for line in lines ];

    unitDict = {}
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
        for word in words:
            unitDict[word] = True

    #print unitDict.keys()

    return unitDict

def isUnitPhrase(phrase,unitDict):
    words = phrase.split();
    l = len(words);
    if words[l-1] != 'block':
        return (unitDict.get(words[l-1],None) != None);
    else:
        return (l > 1 and unitDict.get(words[l-2],None) != None);

def getOriginalSentence(sid):
    sentence = ' '.join(sentences[sid:sid+windowSize]);
    words = sentence.split();
    res = '';
    for word in words:
        tkn, tag = splitToken(word,False);
        res = res+' '+tkn;
    return res;

if len(sys.argv)>1:
    inputFile = sys.argv[1]
if len(sys.argv)>2:
    windowSize = int(sys.argv[2]);

unitDict = ReadInfoFile(infoFile)

fin = open(inputFile)
sentences = fin.readlines()
fin.close()


for sid in range(0,len(sentences)):
    sentence = ' '.join(sentences[sid:sid+windowSize]);
    #print sentence
    words = sentence.split()
    wlen = len(words)
    phrs = {}
    lstKeywords = [];
    setKeywords = set();
    i = 0
    while i < wlen:
        word, tag = splitToken(words[i])
        if isNounTag(tag):
            phr = word
            lastWord = splitToken(words[i],False)[0];
            lastIndex = i;
            if i>0:
                nword, ntag = splitToken(words[i-1]);
            for j in range(i+1,wlen):
                word2, tag2 = splitToken(words[j])
                if not isNounTag(tag2):
                    i = j
                    break
                else:
                    phr = phr + ' ' + word2
                    if word2 != 'block':
                        lastWord = splitToken(words[j],False)[0];
                        lastIndex = j;
                    #phr = word2
            if isUnitPhrase(phr,unitDict):
                lstKeywords.append('%s:%d' % (lastWord, lastIndex));
                setKeywords.add(lastWord);
        i = i + 1
    if len(setKeywords)>1:
        print 'No.%d' % sid;
        sys.stdout.write(' Connections:');
        for u in lstKeywords:
            for v in lstKeywords:
                uw = u[:u.find(':')];
                vw = v[:v.find(':')];
                if uw==vw:continue;
                sys.stdout.write(' %s|%s' % (u,v));
        sys.stdout.write('\n');
        line = getOriginalSentence(sid);
        print ' Text:%s' % line;
        print '';

