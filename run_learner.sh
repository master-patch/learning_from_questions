# ---------------------------------------------------------------- #
#  Command line parameters:                                        #
#  1. Path to configuration file for learner (e.g., cfg/text.cfg.) #
#                                                                  #
#  Any of the parameters specified in the config file can be       #
#  overriden on the command line.  For example, the 'run'          #
#  parameter has been overriden below to the value 't1' via the    #
#  'run=t1' switch.  Note there is no whitespace around the '='.   #
#                                                                  #
#  Configuration parameters can be specified either in the config  #
#  file or on the command line.  If a parameter is given both in   #
#  the config file and the command line, the value on the command  #
#  line takes priority.                                            #
#                                                                  #
#  Packaged configuration files :                                  #
#                                                                  #
#  cfg/text.cfg                                                    #
#      Full text-guided learner.                                   #
#                                                                  #
#  cfg/svm_text.cfg                                                #
#      Hierarchical planner operating on preconditions predicted   #
#      by a SVM trained on manual annotations.                     #
#                                                                  #
#  cfg/all_text.cfg                                                #
#      Hierarchical planner operating on preconditions             #
#      heuristically extracted from the text.  Each                #
#      precondition-effect pair where the corresponding grounding  #
#      words co-occur in a single sentence are extracted as valid  #
#      preconditions.                                              #
#                                                                  #
#  cfg/manual_text.cfg                                             #
#      Hierarchical planner operating on preconditions manually    #
#      extracted from the text.                                    #
#                                                                  #
#  cfg/gold_full.cfg                                               #
#      Hierarchical planner operating on manually specified        #
#      gold-standard preconditions.  Note that this is a superset  #
#      of the preconditions manually extracted from the text.      #
#                                                                  #
#  cfg/none_full.cfg                                               #
#      Hierarchical planner operating without any preconditions.   #
#                                                                  #
# ---------------------------------------------------------------- #

bin/text_guided_planner cfg/question_model.cfg run=t1 2>&1 | tee output/t1/learner_all.log
#bin/text_guided_planner cfg/text.cfg run=t1 2>&1 | tee output/t1/learner_all.log
# bin/text_guided_planner cfg/svm_text.cfg run=s1
# bin/text_guided_planner cfg/all_text.cfg run=a1
# bin/text_guided_planner cfg/manual_text.cfg run=m1
# bin/text_guided_planner cfg/gold_full.cfg run=g1
# bin/text_guided_planner cfg/none_full.cfg run=n1

