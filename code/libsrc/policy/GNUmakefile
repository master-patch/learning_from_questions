CC=	g++
RM=	rm 
SHARED_OBJECT_FLAG = -shared
INC_PATH = ../../include
LIB_PATH = ../../../lib

DEBUG = -ggdb
OPTIMIZE = -fno-rtti -O3
LARGE_FILE_SUPPORT = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE

INTEL_OPT_FLAGS = -mtune=native -march=native -mfpmath=sse -msse2
INTEL64_OPT_FLAGS = -mtune=native -march=native -mfpmath=sse -msse4 -m64 -fPIC
AMD_OPT_FLAGS = -mtune=opteron -march=opteron -mfpmath=sse -m3dnow -fPIC

# set debug & optimization flags...	----------------
CXXFLAGS = -I$(INC_PATH) \
		   -Wall \
		   $(OPTIMIZE) \
		   $(INTEL_OPT_FLAGS) \
		   $(LARGE_FILE_SUPPORT) \
		   -fPIC


ENABLE_SOURCE_DUMP = 1

# build targets  -----------------------------------
test: clean build

ARCH_FLAGS = -mfpmath=sse -msse -msse2 -msse3 -mssse3 -msse4 -msse4.1 -msse4.2
PERF_FLAGS = ${ARCH_FLAGS} -DHAVE_INLINE 


# use this for performance:
# CUSTOM_FLAGS = -Wno-deprecated \
			   -fopenmp \
			   ${PERF_FLAGS} \
			   -DNDEBUG \

# use this for debug:
CUSTOM_FLAGS = -Wno-deprecated \
			   -fopenmp \
			   ${PERF_FLAGS} \
			   -ggdb \
			   -DNAN_CHECK

TARGET = <name of program>

OBJS = main.o *.o

LIBS = -lgsl_intel64 \
	   -lgslcblas_intel64 \
	   -lnlp_string \
	   -lnlp_config \
	   -lnlp_time \
	   -lnlp_socket \
	   -lnlp_filesystem \
	   -lnlp_distr \
	   -lpthread


# OBJECTS_TO_CLEAN = $(OBJS) $(TARGET_NAME)
.PHONY : all auto build clean install test

build: $(OBJS)
	$(CXX) -L$(LIB_PATH) -o$(TARGET) $(SHARED_OBJECT_FLAG) $(OBJS) $(LIBS)

clean:
	@echo "  -- cleaning out object files : " $(TARGET)  $(OBJS)
	-@$(RM) -f $(OBJS) $(TARGET)

install:
	cp $(EXE_DIR)/$(RSLVD_TARGET) <installation location>
