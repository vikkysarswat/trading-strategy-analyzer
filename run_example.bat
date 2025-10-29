@echo off
REM Quick start script to run the trading analyzer with example data (Windows)
REM Make sure you have set up your .env file with OPENROUTER_API_KEY before running

echo ================================
echo Trading Strategy Analyzer
echo ================================
echo.

REM Check if .env file exists
if not exist .env (
    echo Error: .env file not found!
    echo Please copy .env.example to .env and add your OpenRouter API key.
    echo.
    echo Run: copy .env.example .env
    echo Then edit .env and add your API key.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q -r requirements.txt
echo Dependencies installed
echo.

REM Run the analyzer with example data
echo Running analysis with example data...
echo.

python trading_analyzer.py --rulebook data\rulebook_example.txt --trades data\trades_example.json --positions data\positions_example.json --output analysis_output.txt

echo.
echo ================================
echo Analysis complete!
echo Results saved to: analysis_output.txt
echo ================================
pause
