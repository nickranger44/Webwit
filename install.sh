#!/bin/bash
# Assign f to be equal to the directory of "Webwit-master"
f=$(find ~/ -type d -name "Webwit-master")
# Change directory to the location of "Webwit-master"
cd $f
# Use pip to install both requests and random, just in case the user doesn't already have them.
pip install requests
pip install random
