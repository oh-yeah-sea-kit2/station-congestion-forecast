#!/bin/bash
echo "Start script 'realize.sh'"
source ~/.bashrc

export GO111MODULE=off
cd ~/
go get github.com/golang/dep/cmd/dep
go get github.com/oxequa/realize

RV=$(realize --version)
echo "Realize installed @: $RV"

# Realize Downgrade
# cd /go/src/github.com/oxequa/realize && \
#   git fetch && \
#   git checkout v2.0.2 && \
# 	go install  && \
#   # go get github.com/oxequa/realize
# RV=$(realize --version)
# echo "Realize installed @: $RV"
# export GO111MODULE=on

which realize
goenv global 1.9.5
go version
cd /go/src
pwd

realize start
