@echo off
py -m ensurepip --upgrade
py -m pip install selenium
py -m pip install flask
echo ------------------------------------------------------------------------------------------------------------------------
Pause
color C
echo MAKE SURE YOU HAVE CHROMEDRIVER IN YOUR PYTHON PROGRAM DIRECTORY!!!
echo continue if you do have chromedriver
pause
color B
py "GUI Bot.py"