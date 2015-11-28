import sys
sys.path.append('../')

from ir import BagOfWords

from feature_computation.Sentence import ReadSentencesFromTextFileSimple

if __name__ == '__main__':
    sSentenceFile = '../../data/minecraft_text.raw'
    lSentences = ReadSentencesFromTextFileSimple(sSentenceFile)
    sentences = [sentence.lWords for sentence in lSentences]

    bags = BagOfWords(sentences)
    print bags.question(1, "wood")