# Data Directory

This directory contains example data files and is where you should place your trading data for analysis.

## Example Files

The following example files are provided to help you get started:

### 1. `rulebook_example.txt`
- Example trading rule book
- Demonstrates the format for documenting your trading strategy
- Includes entry rules, stop loss rules, targets, and risk management

### 2. `trades_example.json`
- Sample executed trades data
- Contains 8 example trades with realistic Indian stock data
- Shows the required JSON structure and fields

### 3. `positions_example.json`
- Sample open positions data
- Contains 3 example open positions
- Demonstrates the format for current holdings

## Using Your Own Data

### Directory Structure

You can organize your data files in this directory:

```
data/
├── rulebook_example.txt          # Example rule book
├── trades_example.json           # Example trades
├── positions_example.json        # Example positions
├── your_rulebook.txt            # Your actual rule book
├── trades_2025_10_29.json       # Your daily trades
└── positions_2025_10_29.json    # Your daily positions
```

### File Naming Conventions

We recommend using consistent naming:

**For daily files:**
```
trades_YYYY_MM_DD.json
positions_YYYY_MM_DD.json
```

**For different strategies:**
```
rulebook_momentum.txt
rulebook_scalping.txt
```

**For different accounts:**
```
trades_account1_2025_10_29.json
trades_account2_2025_10_29.json
```

## Data Format Guidelines

### Rule Book (.txt files)
- Plain text format
- Clear sections and headings
- Document your intended strategy
- Include entry/exit rules, risk management, and psychological guidelines

### Trades (.json files)
Required fields:
- `trade_id`: Unique identifier
- `symbol`: Stock symbol
- `side`: "BUY" or "SELL"
- `entry_time`: Entry timestamp
- `exit_time`: Exit timestamp
- `entry_price`: Entry price
- `exit_price`: Exit price
- `quantity`: Number of shares
- `pnl`: Profit/Loss amount

Recommended fields:
- `pnl_percent`: P&L percentage
- `stop_loss`: Stop loss price
- `target`: Target price
- `exit_reason`: Why you exited
- `trade_duration_mins`: Duration in minutes

### Positions (.json files)
Required fields:
- `position_id`: Unique identifier
- `symbol`: Stock symbol
- `side`: "BUY" or "SELL"
- `entry_time`: When opened
- `entry_price`: Entry price
- `current_price`: Current price
- `quantity`: Number of shares
- `unrealized_pnl`: Current P&L

Recommended fields:
- `unrealized_pnl_percent`: P&L percentage
- `stop_loss`: Stop loss price
- `target`: Target price
- `time_in_position_mins`: Duration

## Data Privacy

**Important:** The example files are committed to the repository for demonstration purposes.

If you're using real trading data:
1. **Never commit real trading data** to public repositories
2. Add your actual data files to `.gitignore`
3. Consider using the data directory only for local analysis

To exclude your actual trading data from git:

```bash
# Add to .gitignore
echo "data/trades_*.json" >> .gitignore
echo "data/positions_*.json" >> .gitignore
echo "data/*_rulebook.txt" >> .gitignore
```

## Data Backup

Always backup your trading data:
- Keep multiple copies in different locations
- Consider encrypted backups for sensitive data
- Regular exports from your trading platform

## Questions?

For more information on data formats, see the [USAGE.md](../USAGE.md) file.

For issues with data files, check the [troubleshooting section](../USAGE.md#troubleshooting).
