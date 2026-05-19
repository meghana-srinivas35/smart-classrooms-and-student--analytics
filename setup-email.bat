@echo off
echo ========================================
echo  Email Configuration Setup
echo ========================================
echo.

if exist ".env" (
    echo .env file already exists!
    echo.
    choice /C YN /M "Do you want to overwrite it"
    if errorlevel 2 goto :end
)

echo Creating .env file from template...
copy .env.example .env

echo.
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Open .env file in a text editor
echo 2. Update email credentials:
echo    - SENDER_EMAIL=your-email@gmail.com
echo    - SENDER_PASSWORD=your-app-password
echo.
echo For Gmail setup instructions:
echo See docs\EMAIL_SETUP_GUIDE.md
echo.
echo ========================================

:end
pause
