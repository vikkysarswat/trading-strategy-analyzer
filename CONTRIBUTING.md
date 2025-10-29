# Contributing to Trading Strategy Analyzer

Thank you for considering contributing to this project! Here are some guidelines to help you get started.

## How to Contribute

### Reporting Issues

If you find a bug or have a feature request:

1. Check if the issue already exists in the [Issues](https://github.com/vikkysarswat/trading-strategy-analyzer/issues) section
2. If not, create a new issue with a clear title and description
3. Include:
   - Steps to reproduce (for bugs)
   - Expected behavior
   - Actual behavior
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

We welcome suggestions for new features! Please:

1. Open an issue with the tag "enhancement"
2. Clearly describe the feature and its benefits
3. Provide examples of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, descriptive commits
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description of your changes

#### Pull Request Guidelines

- One feature/fix per pull request
- Follow the existing code style
- Include comments for complex logic
- Update README.md if adding new features
- Add tests if applicable

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/trading-strategy-analyzer.git
cd trading-strategy-analyzer

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your OpenRouter API key
```

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Testing

Before submitting:

```bash
# Run the example to ensure everything works
python trading_analyzer.py \
    --rulebook data/rulebook_example.txt \
    --trades data/trades_example.json \
    --positions data/positions_example.json
```

## Areas for Contribution

Here are some areas where contributions would be valuable:

### Features
- Support for additional data formats (CSV, Excel)
- Visualization of trading patterns
- Multi-day analysis and trend tracking
- Export to PDF reports
- Integration with trading platforms
- Real-time analysis capabilities

### Analysis Improvements
- Advanced statistical metrics
- Machine learning pattern detection
- Sentiment analysis integration
- Risk-adjusted return calculations

### Documentation
- More usage examples
- Video tutorials
- API documentation
- Translation to other languages

### Testing
- Unit tests
- Integration tests
- Performance benchmarks

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make this project better! 🚀
