CC=	g++
RM=	rm 
SHARED_OBJECT_FLAG = -shared
INC_PATH = -I../include -I../include/antlr31
LIB_PATH = -L../../lib
BIN_PATH = ../../bin

DEBUG = -ggdb #-DNDEBUG
OPTIMIZE = -O3 -DNDEBUG
LARGE_FILE_SUPPORT = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE


# set debug & optimization flags...	----------------
CFLAGS = $(INC_PATH) \
		   -Wall \
		   $(CUSTOM_FLAGS) \
		   -fPIC \


CXXFLAGS = $(INC_PATH) \
		   -Wall \
		   $(CUSTOM_FLAGS) \
		   -fPIC \
		   -fno-rtti \
		   # $(LARGE_FILE_SUPPORT) 


# use this for performance
# CUSTOM_FLAGS = $(OPTIMIZE) \
# 			   -m64 \
# 			   -Wno-deprecated \
# 			   -ggdb #-pg

# use this for debug:
CUSTOM_FLAGS = -Wno-deprecated \
			   -ggdb 

TARGET = text_guided_planner

OBJS = Probability.o \
	   Feature.o \
	   LogLinearPolicy.o \
	   Zlib.o \
	   CompressedBuffer.o \
	   FFInterface.o \
	   Pddl.o \
	   PddlParser.o \
	   PddlLexer.o \
	   PddlInterface.o \
	   SubgoalPolicy.o \
	   Learner.o \
	   main.o \
	   Problems.o 


LIBS = -lnlp_string \
	   -lnlp_config \
	   -lnlp_filesystem \
	   -lnlp_time \
	   -lnlp_socket \
	   -lnlp_distr \
	   -lpthread \
	   -lgsl \
	   -lgslcblas \
	   -lz \
	   -lantlr3c

build: $(TARGET) install

$(TARGET): $(OBJS)
	$(CXX) $(CUSTOM_FLAGS) $(LIB_PATH) -o$(TARGET) $(OBJS) $(LIBS)

%.o: %.c
	gcc -c -o $@ $< $(CFLAGS)


clean:
	@echo "  -- cleaning out object files : " $(TARGET)  $(OBJS)
	-@$(RM) -f $(OBJS) $(TARGET)

all: clean build

install:
	install -m0644 $(TARGET) $(BIN_PATH)
