FROM python:2-onbuild
MAINTAINER shikanon <shikanon@foxmail.com>

RUN apt-get update
RUN apt-get install python-software-properties software-properties-common -y
RUN apt-add-repository ppa:python-pylinkgrammar/getsome
RUN apt-get install liblink-grammar4 liblink-grammar4-dev cmake swig enchant -y
RUN pip install pylinkgrammar pyenchant nltk pyyaml networkx

wget https://nchc.dl.sourceforge.net/project/gnuplot-py/Gnuplot-py/1.8/gnuplot-py-1.8.tar.gz
tar -zxvf gnuplot-py-1.8.tar.gz

