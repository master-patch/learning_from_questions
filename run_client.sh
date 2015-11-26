# ---------------------------------------------------------------- #
#  Command line parameters:                                        #
#  1. Number of base planners to run in parallel - e.g., 4 below.  #
#     Ideally this should be set to the number of unused           #
#     processors available on the machine.                         #
#  2. Path to the base planner (bin/metric-ff)                     #
#  3. Name or IP of host where ff-plan-cache is being run.         #
#  4. TCP/IP port on which ff-plan-cache is configured to listen   #
#     for client connections.                                      #
#                                                                  #
#  Note the you can run as many clients as you want against a      #
#  single cache.  One of the purposes of the cache is to allow     #
#  distribution of clients across multiple servers.  During our    #
#  experiments, the client count has gone as high as 200.          #
# ---------------------------------------------------------------- #
python bin/client.py 16 bin/metric-ff localhost 5001 2>&1 | tee output/t1/clients_all.log
