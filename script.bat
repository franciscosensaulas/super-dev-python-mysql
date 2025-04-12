@echo off
:: Disable command echoing

echo.
echo === Step 1: Creating virtual environment ===
py -m venv env

if exist env\Scripts\activate (
    echo ✅ Virtual environment created successfully.
) else (
    echo ✗ Failed to create virtual environment.
    pause
    exit /b
)

echo.
echo === Step 2: Activating virtual environment ===
call env\Scripts\activate

if defined VIRTUAL_ENV (
    echo ✓ Virtual environment activated.
) else (
    echo ! Warning: Could not confirm activation. Make sure you're using a supported terminal.
)

echo.
echo === Step 3: Installing dependencies from requirements.txt ===
if exist requirements.txt (
    pip install -r requirements.txt
    if %errorlevel%==0 (
        echo ✓ Dependencies installed successfully.
    ) else (
        echo ✗ Error occurred during package installation.
    )
) else (
    echo ✗ requirements.txt not found in current directory.
)

echo.
echo === Setup Complete ===
pause
