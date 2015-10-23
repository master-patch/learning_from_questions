#===================================================
# GNUmakefile for GCC 4.01							
# S.R.K. Branavan									
# Massachusetts Institute of Technology				
#===================================================


# flags --------------------------------------------
CC=	g++
RM=	rm 
SHARED_OBJECT_FLAG = -shared
INC_PATH = ../include
LIB_PATH = ../../lib
BIN_PATH = ../../bin

DEBUG = -ggdb -pg
OPTIMIZE = -fno-rtti -O3 -pg -DNDEBUG
LARGE_FILE_SUPPORT = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE



# set debug & optimization flags...	----------------
CXXFLAGS = -I$(INC_PATH) \
		   -Wall \
		   $(OPTIMIZE) \
		   $(LARGE_FILE_SUPPORT) \
		   -fPIC \
		   -DHAVE_INLINE \
		   -Wno-deprecated \
		   -fno-rtti \
		   -m64 \




# build targets  -----------------------------------
# the default build target here is lib				

TARGET = ff-plan-cache
OBJS = Zlib.o \
	   CompressedBuffer.o \
	   Cache.o \
	   CacheInterface.o \
	   EnvInterface.o \
	   Server.o \
	   main.o

LIBS = -lnlp_string \
	   -lnlp_config \
	   -lnlp_socket \
	   -lnlp_filesystem \
	   -lnlp_time \
	   -lz \
	   -lpthread


# build commands -----------------------------------
.PHONY : all auto build clean install test

auto: build install

all: clean build

build: $(OBJS)
	$(CXX) -L$(LIB_PATH) -o$(TARGET) $(OBJS) $(LIBS)
	# $(CXX) -L$(LIB_PATH) -o$(TARGET) $(DEBUG) $(SHARED_OBJECT_FLAG) $(OBJS) $(LIBS)

install:
	install -m0644 $(TARGET) $(BIN_PATH)

clean:
	@echo "  -- cleaning out object files : " $(TARGET)  $(OBJS)
	-@$(RM) -f $(OBJS) $(TARGET)

