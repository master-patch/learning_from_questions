# Learning a plan by asking questions

The aim of this research effort is to extend the work by [Branavan et al. (2012)](http://people.csail.mit.edu/regina/my_papers/planning12.pdf). Our work will introduce the actions of asking questions as part of the agent planning process.

## Run

This assumes you have `docker` installed on your machine.

```
$ sh ./start.sh
```

---

### Changelog / Updates

#### Week 3

- (issue) There is no space left on the physical machine given by Karthik
- (success) Discover how to augment the policy with information goals
  - (code) We model our questions as PDDL predicates, and load it to the same "possible next subgoal" vector as regular subgoals.    
- (theory) Investigating the policy for predicting the next subgoal
- (code) After deciding that a subgoal is a question, we need to execute the question, update C before continuing to sample
  - (code/theory) For a trivial retrieval system, we can load all the answers in memory
- (success) 42 million new actions are now down to 517 thanks to Nicola's hardcoding of questions and Adam's hate for thresholds.

- (success) We found three type of questions:
  1. Objects (T)
  2. Subgoal (P*T)
  3. Comparing two subgoals in the sampled sequence
  4. Actions (A)

```
T=50
A=72
P=7
```

#### Week 2
- Finalizing where to add questions and planning how to do so
- Finally getting Branavan's code running
- Setting up the machine given for computation by Regina/Karthik
- Write `Dockerfile` that would compile the code & prepare the environment to run the agent
- Setting up `GDB` to simplify C++ debugging

#### Week 1
- Understanding the paper and the problem
- Trying to get Branavan's code to work
- Researching on where to add questions

---


## Credits
This work is being actively research by Adam Yala, Nicola Greco, and Sebastien Boyer
