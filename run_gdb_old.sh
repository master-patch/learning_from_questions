#!/bin/sh
./run_cache.sh &
./run_client.sh &
gdb bin/text_guided_planner cfg/text.cfg run=t1 2>&1
