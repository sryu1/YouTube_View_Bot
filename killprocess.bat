@echo off
color C
echo WARNING!!!
echo THIS WILL CLOSE ALL CHROME INSTANCES (INCLUDING CHROME BROWSER)
pause
taskkill /F /IM chrome.exe
taskkill /F /IM chromedriver.exe
echo All chrome processes has been terminated.
pause