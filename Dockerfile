FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install git make apt-utils libgsl0-dev libc6-dev-i386 zlib1g-dev libncurses5-dev g++ bzip2 python-pip nano -y
RUN git clone https://github.com/YalaHub/extending_hierarchical_planning
RUN export LD_LIBRARY_PATH=/extending_hierarchical_planning/lib
RUN cd extending_hierarchical_planning/code && make
RUN cd extending_hierarchical_planning/bin && chmod +x ff-plan-cache text_guided_planner

ENTRYPOINT bash
