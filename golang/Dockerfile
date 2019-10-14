FROM centos:7

RUN yum update -y
RUN yum install -y wget git which vim

# goenv install
RUN git clone https://github.com/syndbg/goenv.git -b 1.23.3 ~/.goenv
RUN echo 'export GOENV_ROOT=$HOME/.goenv' >> ~/.bashrc
RUN echo 'export PATH=$GOENV_ROOT/bin:$PATH' >> ~/.bashrc
RUN echo 'eval "$(goenv init -)"' >> ~/.bashrc
RUN exec $SHELL

ENV GOPATH $HOME/go
ENV GOBIN $GOPATH/bin
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin

RUN ~/.goenv/bin/goenv install 1.9.5
RUN ~/.goenv/bin/goenv install 1.10.7
RUN ~/.goenv/bin/goenv global 1.10.7

WORKDIR /go/src

# realize
COPY ./endpoint.sh /go/src/
COPY ./realize.yaml /go/src/.realize.yaml
CMD ["/go/src/endpoint.sh"]
