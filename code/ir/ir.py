from collections import defaultdict
from vocab import P, O, A
import sys
import random

# Random is not really random anymore
random.seed(1)


# Build the inverted index {word: [sent_id1, sentid_2]}
def build_inverted_index(vocab, sentences, k=0, shuffle=False):
    index = defaultdict(list)
    sent_ids = sentences.keys()

    if shuffle:
        sent_id = random.shuffle(sent_ids)

    for sent_id in sent_ids:
        sentence = sentences[sent_id]
        for word in sentence:
            if word in vocab:
                if k == 0 or len(index[word]) < k:
                    index[word].append(sent_id)
    return index


# Abstract implementation of the IR system
class AbstractIR:
    def __init__(self, name, sentences, ids=None):
        if ids is None:
            ids = range(0, len(sentences))
        self.sentences = {
            ids[i]: sentences[i]
            for i in range(len(sentences))
        }
        self.name = name

    # Subclasses will implement this
    def question(self, type, question):
        pass

    # Parsing a question is just about separating the words
    # TODO here some more intelligent hack will make sure
    # we can map `make-sugar` to `make sugar` or similar to
    # increase recall
    def parse_question(self, question):
        question.split(" ")
        return question

    def sentence_to_features(self, sent_id):
        # TODO parse the sentence
        # TODO extract the features
        sentence = " ".join(self.sentences[sent_id])
        return sent_id, sentence, ''


# Bag of Words IR
# It matches all the sentences with a specific set of words
class BagOfWords(AbstractIR):

    def __init__(
        self, sentences,
        ids=None, use_cache=True, k=0, shuffle=False
    ):

        AbstractIR.__init__(
            self,
            str(k) + "-Matches",
            sentences,
            ids)

        self.vocab = P | O | A
        self.index = build_inverted_index(
            self.vocab,
            self.sentences,
            k,
            shuffle)

        # # print ids

        # build up a cache
        self.cache = dict()
        if use_cache:
            self._build_cache()

    # build a cache by reading the already generated feature file
    # the last number in each line of the file has the ID of the sentence
    def _build_cache(self):
        valid_predicates = sys.path[0]
        valid_predicates += '/../../data/valid_predicates.text_features'
        with open(valid_predicates) as f:
            lines = f.readlines()
            for l in lines:
                split = l.split("|")
                sent_id = int(split[len(split) - 1])
                if sent_id not in self.cache:
                    self.cache[sent_id] = []
                    # # print sent_id, l
                self.cache[sent_id].append(l)
            # # print sorted(self.cache.keys()), len(self.cache.keys())

    # ask question to the IR engine
    def question(self, type, question):
        parsed = self.parse_question(question)

        if type == "action":
            a = parsed
            indexes = self.index[a]
        elif type == "object":
            o = parsed
            indexes = self.index[o]
        elif type == "subgoal":
            p, o = parsed
            indexes = set.intersect(
                self.index[p],
                self.index[o])
        elif type == "subgoal_pair":
            p1, o1, p2, o2 = parsed
            p_matching = set.intersect(
                self.index[p1],
                self.index[p2])
            o_matching = set.intersect(
                self.index[o1],
                self.index[o2])
            indexes = p_matching | o_matching
        else:
            indexes = []

        return [self.sentence_to_features(i) for i in indexes]

    # convert a sentence to its features
    # it returns ((int)sent_id, (string)sentence, (string)features)
    # features are listed line by line, hence separated by \n
    def sentence_to_features(self, sent_id):
        sentence = " ".join(self.sentences[sent_id])

        # check if features are in cache
        if sent_id in self.cache:
            features = self.cache[sent_id]
            return sent_id, sentence, "".join(features)

        # otherwise use the default option:
        # generate features on runtime and store in cache
        return AbstractIR.sentence_to_features(
            self,
            sent_id)
