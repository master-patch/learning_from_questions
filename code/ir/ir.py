from collections import defaultdict
from vocab import P, T, A


def build_inverted_index(vocab, data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            if token in vocab:
                index[token].append(i)
    return index


class AbstractIR:
    def __init__(self, name, sentences):
        self.sentences = sentences
        self.name = name

    def question(self, type, question):
        # this is just empty
        pass

    def parse_question(self, question):
        question.split(" ")
        return question

    def sentence_to_features(self, sentece_id):
        # TODO parse the sentence
        # TODO extract the features
        pass


class BagOfWords(AbstractIR):

    def __init__(self, sentences, use_cache=True):
        AbstractIR.__init__(
            self,
            "BagOfWords",
            sentences)

        # using cache is the equivalent of looking up files
        self.use_cache = use_cache
        self.vocab = P | T | A
        self.index = build_inverted_index(
            self.vocab,
            self.sentences)

    def question(self, type, question):
        parsed = self.parse_question(question)

        if type == 1:
            t = parsed
            indexes = self.index[t]
        elif type == 2:
            p, t = parsed
            indexes = set.intersect(
                self.index[p],
                self.index[t])
        elif type == 3:
            p1, t1, p2, t2 = parsed
            p_matching = set.intersect(
                self.index[p1],
                self.index[p2])
            t_matching = set.intersect(
                self.index[t1],
                self.index[t2])
            indexes = p_matching | t_matching

        return [self.sentence_to_features(i) for i in indexes]

    def sentence_to_features(self, sentence_id):
        if not self.use_cache:
            return super(BagOfWords, self).sentence_to_features(sentence_id)

        # TODO read feature of the sentence from the cache