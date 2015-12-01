FROM ubuntu:12.04

ENV LD_LIBRARY_PATH /learning_interactive_planning/lib

RUN apt-get update && apt-get install python2.7-dbg git make apt-utils libgsl0-dev libc6-dev-i386 zlib1g-dev libncurses5-dev g++ bzip2 python-pip nano emacs vim gdb cgdb -y && pip install jsonpickle colout && pip install -U nltk
RUN apt-get install python-dev -y && pip install numpy pdb
COPY . /learning_interactive_planning

WORKDIR /learning_interactive_planning

RUN cd code/model && make clean && cd ../ && make
RUN cd bin && chmod +x ff-plan-cache text_guided_planner

EXPOSE 5002 5001 46941 46942 46943 41551
