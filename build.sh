#!/bin/bash

echo 'Build and Installation Module'

echo 'Download source code:'

wget http://www.pjsip.org/release/2.5.5/pjproject-2.5.5.tar.bz2

tar xjvf pjproject-2.5.5.tar.bz2

cd pjproject-2.5.5

echo 'Configure and build:'

./configure CFLAGS='-O2 -fPIC'

make dep

make

make install

cd pjsip-apps/src/python

sudo python ./setup.py install

echo 'Installation module successful !'
