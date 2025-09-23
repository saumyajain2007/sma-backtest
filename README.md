# SMA Backtest

A compact repository demonstrating a simple moving-average crossover strategy and a small backtest engine in Python. This repo is suitable for educational use, quick experimentation, and as a starting point for more advanced quant development.

## Features
- Fetch historical price data with `yfinance` (or use local CSVs)
- Implement SMA crossover (short vs long) strategy
- Simple backtest engine with position sizing, transaction cost support
- Performance metrics (returns, CAGR, max drawdown, Sharpe)
- Basic plots of equity curve and signals

## Quickstart
1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\activate  # Windows PowerShell
pip install -r requirements.txt
```

2. Run `examples/run_example.py` to execute a sample backtest on `AAPL`.

3. Inspect results and tweak SMA windows.

## License
MIT
