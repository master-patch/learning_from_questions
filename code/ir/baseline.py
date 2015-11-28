import sys
sys.path.append('../')

from ir import BagOfWords

from feature_computation.Sentence import ReadSentencesFromTextFileSimple

if __name__ == '__main__':
    sSentenceFile = '../../data/minecraft_text.raw'
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)
    sentences = [sentence.lWords for sentence in lSentences]
    ids = [sentence.iIndex for sentence in lSentences]

    bags = BagOfWords(sentences, ids)
    print bags.question("object", "bed")[0]
