#!/bin/sh
./run_cache.sh &
./run_client.sh &
bin/text_guided_planner cfg/test.cfg run=t1 2>&1 > output/t1/learner_all.log
