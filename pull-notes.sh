#!/bin/sh

git checkout .
git pull
python crypt.py -d
