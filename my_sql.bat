@echo off
:: Disable command echoing

echo.
echo === Running SQL script on MySQL ===

:: Define your connection variables
set DB_USER=root
set DB_PASS=admin
set DB_NAME=mydatabase
set DB_HOST=localhost
set SQL_FILE=.\src\database\estrutura.sql

:: Check if SQL file exists
if not exist %SQL_FILE% (
    echo [ERROR] SQL file "%SQL_FILE%" not found.
    pause
    exit /b
)

:: Run the SQL script
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u %DB_USER% -p%DB_PASS% -h %DB_HOST% < %SQL_FILE%

if %errorlevel%==0 (
    echo [OK] SQL script executed successfully.
) else (
    echo [ERROR] Failed to execute SQL script.
)

pause
