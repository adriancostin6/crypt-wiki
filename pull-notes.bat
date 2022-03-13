@echo off

python crypt.py -e 
git pull
python crypt.py -d
