FROM ubuntu:12.04

ENV LD_LIBRARY_PATH /extending_hierarchical_planning/lib

RUN apt-get update
RUN apt-get install git make apt-utils libgsl0-dev libc6-dev-i386 zlib1g-dev libncurses5-dev g++ bzip2 python-pip nano -y
RUN git clone https://github.com/YalaHub/extending_hierarchical_planning

WORKDIR /extending_hierarchical_planning

RUN cd code && make clean && make
RUN cd bin && chmod +x ff-plan-cache text_guided_planner

EXPOSE 5002 5001 46941 46942 46943 41551

ENTRYPOINT  ./run_cache.sh & ./run_client.sh & ./run_learner.sh & bash
