#!/bin/bash
sudo easy_install pip
fl=$(find ~/Desktop/ -name "Webwit-master")
cd $fl
pip install requests
pip install pycurl

