# Trading Strategy Analyzer

AI-powered trading strategy analysis tool using OpenRouter API for behavioral insights and performance optimization.

## Overview

This tool analyzes trading performance using AI to provide:
- **Data-driven insights** from trade execution patterns
- **Behavioral analysis** of trader psychology and decision-making
- **Strategy improvement recommendations** based on quantitative findings
- **Evolving trader persona profiles** to track performance trends

## Features

- 📊 **Quantitative Analysis**: Win rate, expectancy, profit factor, drawdown analysis
- 🧠 **Behavioral Insights**: Detect patterns like FOMO, revenge trading, loss aversion
- 🎯 **Strategy Optimization**: AI-derived actionable recommendations
- 📈 **Performance Metrics**: Time-based, symbol-based, and side-based analysis
- 🔄 **Daily Evolution**: Build dynamic trader profiles over time

## Prerequisites

- Python 3.8+
- OpenRouter API key (get it from [openrouter.ai](https://openrouter.ai))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vikkysarswat/trading-strategy-analyzer.git
cd trading-strategy-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
cp .env.example .env
```
Edit `.env` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
SITE_URL=your_site_url  # Optional
SITE_NAME=your_site_name  # Optional
```

## Usage

### Basic Analysis

```bash
python trading_analyzer.py --rulebook data/rulebook.txt --trades data/trades.json --positions data/positions.json
```

### Command Line Options

```bash
python trading_analyzer.py --help
```

Options:
- `--rulebook`: Path to rule book file (txt format)
- `--trades`: Path to trades file (JSON format)
- `--positions`: Path to positions file (JSON format)
- `--output`: Output file for analysis results (default: analysis_output.txt)
- `--model`: OpenRouter model to use (default: deepseek/deepseek-chat-v3.1:free)

## Input File Formats

### Trades File (trades.json)
```json
[
  {
    "trade_id": "T001",
    "symbol": "RELIANCE",
    "side": "BUY",
    "entry_time": "2025-10-29 09:45:00",
    "exit_time": "2025-10-29 10:15:00",
    "entry_price": 2850.50,
    "exit_price": 2865.75,
    "quantity": 10,
    "pnl": 152.50,
    "stop_loss": 2840.00,
    "target": 2870.00
  }
]
```

### Positions File (positions.json)
```json
[
  {
    "position_id": "P001",
    "symbol": "TCS",
    "side": "BUY",
    "entry_time": "2025-10-29 13:30:00",
    "entry_price": 3450.25,
    "current_price": 3462.80,
    "quantity": 5,
    "unrealized_pnl": 62.75,
    "stop_loss": 3435.00,
    "target": 3475.00
  }
]
```

### Rule Book (rulebook.txt)
Plain text file describing your trading rules and strategy framework.

## Analysis Output

The tool generates comprehensive reports including:

1. **Executive Insight Summary**: 3-5 key behavioral patterns
2. **Quantitative Findings**: Win rate, profit factor, performance metrics
3. **Behavioral & Executional Insights**: Psychological patterns and biases
4. **Strategy Improvement Opportunities**: Data-driven recommendations
5. **Trader Persona Profile**: Dynamic risk and execution style assessment
6. **Updated Strategy Recommendations**: Actionable refinements

## Example Output

```
=== EXECUTIVE INSIGHT SUMMARY ===
• Momentum-chasing behavior observed with 72% of entries within first 30 mins
• Strong performance on BUY side (Win rate: 68%) vs SELL side (Win rate: 42%)
• Early exits reducing profit potential - average winner held for 18 mins vs 45 min target

=== QUANTITATIVE FINDINGS ===
Win Rate: 58.3%
Profit Factor: 1.85
Average Gain: ₹245.50 | Average Loss: ₹180.25
Best Time Cluster: 10:00-11:00 (75% win rate)

[... detailed analysis continues ...]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Support

For issues or questions, please open an issue on GitHub.

## Acknowledgments

- Powered by [OpenRouter](https://openrouter.ai)
- Uses DeepSeek Chat v3.1 for AI analysis
