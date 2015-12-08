######### READ ME BASELINES CONFIG #############

question_model.cfg is the initial config file 
It contains the default config settings to run
the question answering system. To change config 
file while running the system choose it in 
run_learner.sh

We provide 5 other config files that contain 
variation of the default settings that we used 
to benchmark different question scheme and techniques.

Below a description of the differences between each
of the 5 config files and the initial one :

- question_model_1.cfg contains random=1 (default 0). 
this makes the system answer the question with random extracted
from the text wiki.

- question_model_2.cfg contains ir:reward = -1 (default 0)
this makes the system rewards the completion of a question with -1

- question_model_3.cfg contains ir:reward = 1 (default 0)
this makes the system rewards the completion of a question with -1

- question_model_4.cfg contains ir:num_answers = 1 (default 5)
this makes the system caps the number of sentences returned by 1 top.

- question_model_5.cfg contains ir:action-questions = 0 (default 1)
this makes the system asks only object-related questions (making
action-related questions forbidden)