from nltk.stem.porter import PorterStemmer
from collections import defaultdict
from vocab import O, A
import random
import sys
from term_colors import q, ir, c

# Random is not really random anymore
random.seed(1)
stemmer = PorterStemmer()


def clean_word(word):
    word = unicode(word, 'utf-8')
    word = stemmer.stem(word)

    if word == 'collect' or word == 'obtain':
        word = 'harvest'

    if word in {'make', 'craft', 'made', 'build', 'built'}:
        word = 'craft-make'

    if word in {'wooden'}:
        word = 'wood'

    if word in {'fornace'}:
        word = 'furnace'

    return word


# Build the inverted index {word: [sent_id1, sentid_2]}
# wordpair = ("make-wood", ['make wood'])
def build_inverted_index(vocab_annotated, sentences, k=0, shuffle=False):
    vocab = set()
    for pddl, alternatives in vocab_annotated.iteritems():
        for alternative in alternatives:
            for word in alternative.split(' '):
                word = clean_word(word)
                vocab.add(word)

    index = defaultdict(set)
    sent_ids = sentences.keys()

    if shuffle:
        sent_id = random.shuffle(sent_ids)

    for sent_id in sent_ids:
        sentence = sentences[sent_id]
        for word in sentence:
            word = clean_word(word)
            if word in vocab:
                if k == 0 or len(index[word]) < k:
                    index[word].add(sent_id)

    return index


def search_inverted_index(vocab_annotated, index, pddl):
    alternatives = vocab_annotated[pddl]
    sentences = set()
    for alternative in alternatives:
        intersection = set.intersection(
            *[index[clean_word(w)] for w in alternative.split(' ')]
        )

        for sent_id in intersection:
            sentences.add(sent_id)

    return sentences


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

        vocab_all = O.copy()
        vocab_all.update(A)
        self.vocab = vocab_all
        self.counter = 0

        self.index = build_inverted_index(
            self.vocab,
            self.sentences,
            k,
            shuffle)

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
                self.cache[sent_id].append(l)

    # ask question to the IR engine
    def search_index(self, pddl):
        return search_inverted_index(self.vocab, self.index, pddl)

    def question(self, type, question):
        parsed = self.parse_question(question)
        self.counter = self.counter + 1
        msg = ""
        if type == "action":
            a = parsed
            msg_q = q("{}".format(a.replace('-', ' '))) + "': "
            msg = ir("IR") + c(self.counter) + " 'Tell me more about how to " + msg_q

            indexes = self.search_index(a)
        elif type == "object":
            o = parsed
            msg_q = q("{}".format(o.replace('-', ' '))) + "': "
            msg = ir("IR") + c(self.counter) + " 'Tell me more about the object " + msg_q
            indexes = self.search_index(o)
        elif type == "subgoal":
            p, o = parsed
            indexes = set.intersect(
                self.search_index(p),
                self.search_index(o))
        elif type == "subgoal_pair":
            p1, o1, p2, o2 = parsed
            p_matching = set.intersection(
                self.search_index(p1),
                self.search_index(p2))
            o_matching = set.intersection(
                self.search_index(o1),
                self.search_index(o2))
            indexes = p_matching | o_matching
        else:
            indexes = []

        answers = [self.sentence_to_features(i) for i in indexes]
        print msg, "{} response/s".format(len(answers))
        return answers

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
