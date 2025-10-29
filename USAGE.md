# Trading Strategy Analyzer - Usage Guide

This guide provides detailed instructions on how to use the Trading Strategy Analyzer effectively.

## Table of Contents

- [Quick Start](#quick-start)
- [Command Line Options](#command-line-options)
- [Input File Formats](#input-file-formats)
- [Understanding the Analysis Output](#understanding-the-analysis-output)
- [Advanced Usage](#advanced-usage)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

## Quick Start

### 1. Set Up Your Environment

```bash
# Clone the repository
git clone https://github.com/vikkysarswat/trading-strategy-analyzer.git
cd trading-strategy-analyzer

# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp .env.example .env
# Edit .env and add your OpenRouter API key
```

### 2. Run with Example Data

```bash
# Linux/Mac
chmod +x run_example.sh
./run_example.sh

# Windows
run_example.bat
```

### 3. Analyze Your Own Data

```bash
python trading_analyzer.py \
    --rulebook your_rulebook.txt \
    --trades your_trades.json \
    --positions your_positions.json \
    --output my_analysis.txt
```

## Command Line Options

### Required Arguments

- `--rulebook PATH`: Path to your trading rule book file (txt format)
- `--trades PATH`: Path to your trades data file (JSON format)
- `--positions PATH`: Path to your current positions file (JSON format)

### Optional Arguments

- `--output PATH`: Output file for analysis results (default: `analysis_output.txt`)
- `--model MODEL`: OpenRouter model to use (default: `deepseek/deepseek-chat-v3.1:free`)

### Examples

**Basic usage:**
```bash
python trading_analyzer.py --rulebook data/rules.txt --trades data/trades.json --positions data/positions.json
```

**Custom output file:**
```bash
python trading_analyzer.py --rulebook rules.txt --trades trades.json --positions positions.json --output results_2025_10_29.txt
```

**Different AI model:**
```bash
python trading_analyzer.py --rulebook rules.txt --trades trades.json --positions positions.json --model anthropic/claude-3-opus
```

## Input File Formats

### Rule Book (rulebook.txt)

Plain text file describing your trading strategy, rules, and approach.

**Example:**
```
=== MY TRADING STRATEGY ===

ENTRY RULES:
1. Trade only during 9:30 AM - 3:00 PM
2. Minimum 1% price movement
3. Confirm with volume spike

STOP LOSS:
- Fixed 1% below entry for BUY
- Fixed 1% above entry for SELL

TARGET:
- 2% profit target (R:R = 1:2)
```

### Trades File (trades.json)

JSON array containing executed trades with the following fields:

**Required Fields:**
- `trade_id`: Unique identifier for the trade
- `symbol`: Stock/instrument symbol
- `side`: "BUY" or "SELL"
- `entry_time`: Entry timestamp
- `exit_time`: Exit timestamp
- `entry_price`: Entry price
- `exit_price`: Exit price
- `quantity`: Number of shares/units
- `pnl`: Profit/Loss amount

**Optional but Recommended Fields:**
- `pnl_percent`: P&L as percentage
- `stop_loss`: Stop loss price
- `target`: Target price
- `exit_reason`: Why the trade was exited
- `trade_duration_mins`: Duration in minutes

**Example:**
```json
[
  {
    "trade_id": "T001",
    "symbol": "AAPL",
    "side": "BUY",
    "entry_time": "2025-10-29 10:00:00",
    "exit_time": "2025-10-29 11:30:00",
    "entry_price": 175.50,
    "exit_price": 178.25,
    "quantity": 100,
    "pnl": 275.00,
    "pnl_percent": 1.57,
    "stop_loss": 173.00,
    "target": 180.00,
    "exit_reason": "TARGET_HIT",
    "trade_duration_mins": 90
  }
]
```

### Positions File (positions.json)

JSON array containing open positions with the following fields:

**Required Fields:**
- `position_id`: Unique identifier
- `symbol`: Stock/instrument symbol
- `side`: "BUY" or "SELL"
- `entry_time`: When position was opened
- `entry_price`: Entry price
- `current_price`: Current market price
- `quantity`: Number of shares/units
- `unrealized_pnl`: Current unrealized profit/loss

**Optional but Recommended Fields:**
- `unrealized_pnl_percent`: Unrealized P&L as percentage
- `stop_loss`: Stop loss price
- `target`: Target price
- `time_in_position_mins`: How long position has been open

**Example:**
```json
[
  {
    "position_id": "P001",
    "symbol": "GOOGL",
    "side": "BUY",
    "entry_time": "2025-10-29 14:00:00",
    "entry_price": 140.50,
    "current_price": 142.10,
    "quantity": 50,
    "unrealized_pnl": 80.00,
    "unrealized_pnl_percent": 1.14,
    "stop_loss": 139.00,
    "target": 145.00,
    "time_in_position_mins": 60
  }
]
```

## Understanding the Analysis Output

The analyzer provides six main sections:

### 1. Executive Insight Summary
- 3-5 bullet points highlighting key behavioral patterns
- Anomalies and standout behaviors
- Dominant signals of the day

### 2. Quantitative Findings
- Win rate and expectancy
- Profit factor
- Average gain/loss statistics
- Performance by time, side, and symbol
- Repeated inefficiencies

### 3. Behavioral & Executional Insights
- Psychological patterns (FOMO, revenge trading, etc.)
- Reaction to losses
- Risk aversion patterns
- Emotional biases

### 4. Strategy Improvement Opportunities
- Specific rule adjustments
- Noise trade filtering suggestions
- Data-driven recommendations

### 5. Trader Persona Profile
- Risk style assessment
- Execution consistency
- Strengths and blind spots
- Focus areas for improvement

### 6. Updated Strategy Recommendations
- Actionable refinements
- Threshold adjustments
- Timing optimizations

## Advanced Usage

### Using Different AI Models

You can use various models from OpenRouter:

```bash
# Free models
--model deepseek/deepseek-chat-v3.1:free
--model google/gemini-flash-1.5

# Paid models (higher quality)
--model anthropic/claude-3-opus
--model openai/gpt-4-turbo
```

Check [OpenRouter's model list](https://openrouter.ai/models) for more options.

### Batch Processing Multiple Days

Create a script to analyze multiple days:

```bash
#!/bin/bash
for date in 2025-10-{25..29}; do
    python trading_analyzer.py \
        --rulebook rulebook.txt \
        --trades data/trades_${date}.json \
        --positions data/positions_${date}.json \
        --output analysis_${date}.txt
done
```

### Integrating with Your Trading System

You can use the `TradingAnalyzer` class in your own Python scripts:

```python
from trading_analyzer import TradingAnalyzer

# Initialize
analyzer = TradingAnalyzer()

# Run analysis
analysis = analyzer.analyze(
    'rulebook.txt',
    'trades.json',
    'positions.json'
)

# Process results
print(analysis)
```

## Best Practices

### Data Collection

1. **Be Consistent**: Use the same format for all trades
2. **Include Context**: Add as many optional fields as possible
3. **Track Everything**: Log every trade, even losses
4. **Timestamp Accuracy**: Use precise timestamps for better time-based analysis

### Analysis Frequency

- **Daily**: Recommended for active traders
- **Weekly**: Good for swing traders
- **After Major Events**: After significant wins/losses

### Acting on Insights

1. **Review Patterns**: Look for recurring issues
2. **Test Changes**: Implement one recommendation at a time
3. **Track Progress**: Compare analyses over time
4. **Stay Objective**: Don't ignore uncomfortable truths

### Rule Book Maintenance

- Update your rule book as you refine your strategy
- Document why you made changes
- Version your rule book files

## Troubleshooting

### Common Issues

**1. API Key Error**
```
Error: OpenRouter API key not found
```
**Solution**: Make sure you've created `.env` file and added your API key.

**2. File Not Found**
```
FileNotFoundError: File not found: data/trades.json
```
**Solution**: Check the file path is correct relative to where you're running the script.

**3. JSON Parse Error**
```
json.decoder.JSONDecodeError
```
**Solution**: Validate your JSON files. Common issues:
- Missing commas between objects
- Trailing commas at the end
- Unquoted strings
- Single quotes instead of double quotes

**4. Rate Limiting**
```
Error 429: Too Many Requests
```
**Solution**: The free tier has rate limits. Wait a few minutes or upgrade to a paid plan.

### Getting Help

- Check [existing issues](https://github.com/vikkysarswat/trading-strategy-analyzer/issues)
- Open a new issue with:
  - Your command
  - Error message
  - Python version
  - Operating system

## Tips for Better Analysis

1. **Include Trade Context**: Add exit reasons and notes
2. **Consistent Timing**: Use the same timezone for all timestamps
3. **Clean Data**: Remove test trades or fix data errors
4. **Regular Reviews**: Run analysis daily or weekly for trends
5. **Act on Insights**: Implement the recommendations you receive

---

Happy Trading! 📈

For more information, see the [main README](README.md) or [contribute to the project](CONTRIBUTING.md).
