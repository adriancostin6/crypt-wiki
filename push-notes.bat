@echo off

python crypt.py -e 
git add .
git commit -m "Add notes"
git push
python crypt.py -d
