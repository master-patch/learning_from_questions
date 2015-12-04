#!/bin/sh
./run_cache.sh &
./run_client.sh &
cgdb bin/text_guided_planner
