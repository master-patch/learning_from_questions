# Fix path issues for importing parent path
import sys
sys.path.append('../')

from ir import BagOfWords
from feature_computation.Sentence import ReadSentencesFromTextFileSimple

if __name__ == '__main__':
    # Load sentences using Branavan's code
    sSentenceFile = '../../data/minecraft_text.raw'
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)

    # Run BagOfWords passing the sentences and the ids
    sentences = [sentence.lWords for sentence in lSentences]
    ids = [sentence.iIndex for sentence in lSentences]
    bags = BagOfWords(sentences, ids)

    # Random tests
    print len(bags.vocab.items())
    notmatching = 0
    for key, val in bags.vocab.iteritems():
        matches = [ans[0] for ans in bags.question("object", key)]
        if len(matches) == 0:
            print "no matches", key
            notmatching = notmatching + 1
    print notmatching
