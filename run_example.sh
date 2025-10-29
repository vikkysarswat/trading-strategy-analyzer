#!/bin/bash

# Quick start script to run the trading analyzer with example data
# Make sure you have set up your .env file with OPENROUTER_API_KEY before running

echo "================================"
echo "Trading Strategy Analyzer"
echo "================================"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and add your OpenRouter API key."
    echo ""
    echo "Run: cp .env.example .env"
    echo "Then edit .env and add your API key."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt
echo "✅ Dependencies installed"
echo ""

# Run the analyzer with example data
echo "🚀 Running analysis with example data..."
echo ""

python trading_analyzer.py \
    --rulebook data/rulebook_example.txt \
    --trades data/trades_example.json \
    --positions data/positions_example.json \
    --output analysis_output.txt

echo ""
echo "================================"
echo "✅ Analysis complete!"
echo "Results saved to: analysis_output.txt"
echo "================================"
