#!/usr/bin/env python3
"""
Trading Strategy Analyzer
AI-powered analysis tool using OpenRouter API
"""

import os
import json
import argparse
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TradingAnalyzer:
    """Main class for trading strategy analysis"""
    
    def __init__(self, api_key=None, model=None, site_url=None, site_name=None):
        """
        Initialize the Trading Analyzer
        
        Args:
            api_key (str): OpenRouter API key
            model (str): Model to use for analysis
            site_url (str): Site URL for OpenRouter rankings
            site_name (str): Site name for OpenRouter rankings
        """
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        self.model = model or os.getenv('MODEL', 'deepseek/deepseek-chat-v3.1:free')
        self.site_url = site_url or os.getenv('SITE_URL', '')
        self.site_name = site_name or os.getenv('SITE_NAME', '')
        
        if not self.api_key:
            raise ValueError("OpenRouter API key not found. Set OPENROUTER_API_KEY in .env file")
        
        # Initialize OpenAI client with OpenRouter
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )
        
        # System prompt for trading analysis
        self.system_prompt = self._get_system_prompt()
    
    def _get_system_prompt(self):
        """Return the system prompt for trading analysis"""
        return """Role: You are a Quantitative Trading Analyst and Behavioral Finance AI Model specialized in analyzing trading performance and improving probabilistic strategy edge. You are given three key inputs daily:

Rule Book (reference only) — defines what the trader intends to do.
Trades File (main data) — executed trades with P&L, time, direction, etc.
Positions File (current state) — open trades, unrealized gains/losses, exposure.

Your goal is to generate findings not found in the text, but inferred, discovered, and derived from the data. You must tell what the trader is actually doing, what can be improved, and how the system can evolve.

🎯 Core Objective

Deliver data-driven, LLM-inferred insights that:

Explain what patterns and behaviors are emerging in the trades.
Identify inefficiencies, biases, and edge leaks in the system.
Suggest practical, rule-level adjustments backed by the patterns found in the trades and positions.
Reflect on how the trader's psychology and execution discipline align or conflict with the Rule Book.

🔍 Analysis Structure

1. Executive Insight Summary

Give a concise, insight-based overview in 3–5 bullet points:

What kind of trader behavior or market adaptation is visible today?
Any anomaly or standout behavior (e.g., exiting too early, overtrading at one time of day, bias toward specific sectors)?
What signals or patterns dominated the day?

2. Quantitative Findings

Derive and report the findings, not the definitions:

Win rate, expectancy, average gain/loss per trade
Profit factor and drawdown distribution
Performance by time, side (BUY/SELL), symbol, and trade duration
Identify repeated inefficiencies — e.g., "trades taken before 10:15 hit SL 68% of the time"
Detect top profitable symbols, time clusters, and side biases

3. Behavioral & Executional Insights

Use the data to infer the trader's psychological and decision-making traits:

Signs of impatience, fear of missing out, revenge trading, or hesitation
Reactions to losses (e.g., quick reversal or withdrawal)
Overconfidence or risk aversion patterns
Quantify emotional bias (e.g., average loss larger than average gain = loss aversion)

4. Strategy Improvement Opportunities

Data-based, non-redundant recommendations:

Specific points to tighten or relax rules (e.g., "avoid entries before X minutes from open" or "increase position size on 3 consecutive valid setups")
Suggestions to filter noise trades (based on time, volatility, or performance clusters)
Identify which rules may be hurting performance statistically
Suggest a small list (3–5) of tangible actions for next day's iteration

5. Trader Persona Profile (Evolving)

Build a short, dynamic profile based on the trader's daily behavior:

Risk style (aggressive / cautious / momentum chaser / range player)
Execution consistency (measured by adherence to expected timing or size pattern)
Strengths and blind spots emerging from current data
Behavioral focus area for tomorrow

6. Updated Strategy Recommendations

Present a list of AI-derived actionable refinements (not reworded rules).
Focus only on what the data suggests needs change, such as thresholds, stop-loss ratios, trade holding time, or market timing.
Example outputs:

"Tighten SL for early entries by 0.4% based on drawdown curve."
"Avoid re-entries within 8 mins of a stopped-out trade."
"Increase exposure by 20% on high-volume momentum trades above VWAP."

⚙️ Guidelines for Response Generation

Never restate or paraphrase the Rule Book content.
Only derive from Trades + Positions + inferred logic.
Treat the Rule Book as a lens, not a script.
Output should feel like an analyst's report, not a mirror of input data.
Prefer findings and recommendations over summaries.
Prioritize new learning, predictive behavioral cues, and tactical refinement."""
    
    def load_file(self, filepath):
        """
        Load file content based on extension
        
        Args:
            filepath (str): Path to the file
            
        Returns:
            str or dict: File content
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            if filepath.endswith('.json'):
                return json.load(f)
            else:
                return f.read()
    
    def prepare_user_message(self, rulebook, trades, positions):
        """
        Prepare the user message with all trading data
        
        Args:
            rulebook (str): Rule book content
            trades (list): Trades data
            positions (list): Positions data
            
        Returns:
            str: Formatted message for analysis
        """
        message = f"""Please analyze the following trading data:

=== RULE BOOK ===
{rulebook}

=== TRADES FILE ===
{json.dumps(trades, indent=2)}

=== POSITIONS FILE ===
{json.dumps(positions, indent=2)}

Please provide a comprehensive analysis following the structure defined in your system prompt."""
        
        return message
    
    def analyze(self, rulebook_path, trades_path, positions_path):
        """
        Perform trading analysis
        
        Args:
            rulebook_path (str): Path to rule book file
            trades_path (str): Path to trades file
            positions_path (str): Path to positions file
            
        Returns:
            str: Analysis result
        """
        print("Loading files...")
        rulebook = self.load_file(rulebook_path)
        trades = self.load_file(trades_path)
        positions = self.load_file(positions_path)
        
        print("Preparing analysis request...")
        user_message = self.prepare_user_message(rulebook, trades, positions)
        
        print(f"Sending request to OpenRouter ({self.model})...")
        
        extra_headers = {}
        if self.site_url:
            extra_headers["HTTP-Referer"] = self.site_url
        if self.site_name:
            extra_headers["X-Title"] = self.site_name
        
        try:
            completion = self.client.chat.completions.create(
                extra_headers=extra_headers,
                extra_body={},
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ]
            )
            
            result = completion.choices[0].message.content
            print("\n✅ Analysis completed successfully!\n")
            return result
            
        except Exception as e:
            print(f"\n❌ Error during analysis: {str(e)}\n")
            raise
    
    def save_analysis(self, analysis, output_path):
        """
        Save analysis to file
        
        Args:
            analysis (str): Analysis content
            output_path (str): Output file path
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"Trading Strategy Analysis\n")
            f.write(f"Generated: {timestamp}\n")
            f.write(f"{'=' * 80}\n\n")
            f.write(analysis)
        
        print(f"Analysis saved to: {output_path}")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Trading Strategy Analyzer - AI-powered trading analysis using OpenRouter'
    )
    
    parser.add_argument(
        '--rulebook',
        type=str,
        required=True,
        help='Path to rule book file (txt format)'
    )
    
    parser.add_argument(
        '--trades',
        type=str,
        required=True,
        help='Path to trades file (JSON format)'
    )
    
    parser.add_argument(
        '--positions',
        type=str,
        required=True,
        help='Path to positions file (JSON format)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='analysis_output.txt',
        help='Output file for analysis results (default: analysis_output.txt)'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default=None,
        help='OpenRouter model to use (default: from .env or deepseek/deepseek-chat-v3.1:free)'
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize analyzer
        analyzer = TradingAnalyzer(model=args.model)
        
        # Perform analysis
        analysis = analyzer.analyze(
            args.rulebook,
            args.trades,
            args.positions
        )
        
        # Display analysis
        print("\n" + "=" * 80)
        print(analysis)
        print("=" * 80 + "\n")
        
        # Save to file
        analyzer.save_analysis(analysis, args.output)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
