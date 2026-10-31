@echo off
title MeetingAutopsy AI Local Server
echo ========================================================
echo   Starting MeetingAutopsy AI Server...
echo   Speech-to-Text ^& Intelligent Video Classifier
echo   Open http://localhost:8000 in your browser
echo ========================================================
cd /d "%~dp0"
if exist venv\Scripts\python.exe (
    venv\Scripts\python.exe server.py
) else (
    py server.py 2>nul || python server.py
)
pause
