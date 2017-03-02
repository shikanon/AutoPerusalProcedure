FROM python:2-onbuild

RUN apt-add-repository ppa:python-pylinkgrammar/getsome
RUN apt-get install liblink-grammar4 liblink-grammar4-dev cmake swig enchant -y
RUN pip install pylinkgrammar pyenchant nltk pyyaml networkx


