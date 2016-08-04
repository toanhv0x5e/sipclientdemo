#!/bin/sh
#
export CFLAGS="$CFLAGS -fPIC"

./configure


sudo apt-get install -y software-properties-common # To make add-apt-repository work
sudo add-apt-repository ppa:dennis.guse/sip-tools 
sudo apt-get update 
sudo apt-get install python-pjsua
sudo apt-get install python-pjsua2


pjsua