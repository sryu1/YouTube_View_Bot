@echo off
py -m ensurepip --upgrade
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
pause