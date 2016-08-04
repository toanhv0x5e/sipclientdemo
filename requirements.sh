#!/bin/sh

#
# Requirements
#

sudo apt-get install -y software-properties-common # To make add-apt-repository work
sudo add-apt-repository ppa:dennis.guse/sip-tools 
sudo apt-get update 
sudo apt-get install python-pjsua
sudo apt-get install python-pjsua2


# export CFLAGS="$CFLAGS -fPIC"
# ./configure
