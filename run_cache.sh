# ---------------------------------------------------------------- #
# There are three cache configuration settings that are critical   #
# to the performance of the cache.  These are listed below with    #
# the configuration value listed in cfg/cache.cfg                  #
#                                                                  #
#   cache_file_name = env.cache                                    #
#   temp_cache_path = /tmp/                                        #
#   cache_save_period = 7200                                       #
#                                                                  #
# The cache process writes the contents of the in-memory cache to  #
# the file given under 'cache_file_name', which is path relative   #
# to the directory location from where the cache binary is run.    #
# On startup, if a cache file exists, the in-memory cache is       #
# populated from the contents of that file.  The cache_save_period #
# configuration specifies how often the cache should be saved to   #
# file.  When saving the cache to disk, a new cache file is        #
# written at the path given under temp_cache_path, and if the save #
# was successful, the old file is replaced with this new one.      #
#                                                                  #
# During a typical series of experiments, the cache file can grow  #
# to several Giga Bytes in size.  For this reason, the two file    #
# locations need to have a couple of 10's of Giga Bytes of free    #
# space.  Also note that once it has grown large, saving the cache #
# can take some time (depending on disk write speeds). For this    #
# reason, keeping the cache_save_period large is recommended.      #
#                                                                  #
# ---------------------------------------------------------------- #
bin/ff-plan-cache cfg/cache.cfg 
