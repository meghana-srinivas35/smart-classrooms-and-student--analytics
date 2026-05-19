@echo off
echo ========================================
echo  Smart Classrooms Analytics
echo  Restructured Full-Stack Application
echo ========================================
echo.

echo [1/2] Starting Backend Server (Flask)...
start "Backend API - Port 5000" cmd /k "cd /d "%~dp0backend" && py app.py"
timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend Server (React)...
start "Frontend UI - Port 3000" cmd /k "cd /d "%~dp0client" && npm start"

echo.
echo ========================================
echo  Servers Started Successfully!
echo ========================================
echo  Backend API:  http://localhost:5000
echo  Frontend UI:  http://localhost:3000
echo  Health Check: http://localhost:5000/health
echo ========================================
echo.
echo Keep both terminal windows open!
echo Press any key to exit this window...
pause >nul
