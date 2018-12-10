#!/bin/bash
f=$(find ~/ -type d -name "Webwit-master")
cd $f
pip3 install requests
