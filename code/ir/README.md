# IR systems

- **AbstractIR**
  An abstract class for parsers, it has the default methods that other IRs can call

- **BagOfWords**
  It build an inverted index for the words in the vocabulary. To answer each question, we intersect different inverted index postings for the words we want to match.

## API
- **ir = IRSystemOfYourChoice(sentences, ids)**
  - *sentences*: the list of sentences (each sentence is a list of words)
  - *ids*: the list of ids of each sentence

- **ir.question(type, question)
  - e.g. ir.question("object", "wood")

## Files

- **test.py**: only used for test purposes
- **rpc.py**: long running process that will run an IR system and listen to a socket for changes
- **ir.py**: implementation of the IR systems
- **vocab.py**: vocabulary of the Learner when asking questions