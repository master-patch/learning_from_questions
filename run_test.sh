#!/bin/sh
./run_cache.sh &
./run_client.sh &
./run_ir.sh &
sleep 5 &&
bin/text_guided_planner cfg/question_model.cfg run=t1 2>&1 | tee output/t1/learner_all.log
