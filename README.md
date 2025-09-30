# 📊 SMA Backtest – Moving Average Crossover Strategy

## Project Overview
This repository demonstrates a **Simple Moving Average (SMA) Crossover Strategy** with a lightweight Python backtest engine.  
The goal is to provide a compact, educational implementation that is easy to extend for more advanced quantitative trading research.

The project covers:
- Fetching market data
- Implementing SMA crossover logic
- Running backtests with realistic assumptions
- Evaluating strategy performance with key metrics
- Visualizing results (equity curve, buy/sell signals)

---

## 🧠 Theoretical Background

### 1. Simple Moving Average (SMA)
A **moving average** smooths out price data by creating a constantly updated average price over a given time window.  
For a time series of prices \( P_t \):

\[
SMA_n(t) = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}
\]

- **Short SMA** (e.g., 20 days): reacts quickly to price changes, capturing short-term trends.  
- **Long SMA** (e.g., 50 or 200 days): reacts slowly, capturing long-term trends.  

### 2. SMA Crossover Strategy
The **crossover strategy** generates trading signals when two moving averages cross:
- **Bullish Signal (Buy):** Short SMA crosses **above** Long SMA → Uptrend expected.
- **Bearish Signal (Sell):** Short SMA crosses **below** Long SMA → Downtrend expected.

This method attempts to ride major price trends while avoiding whipsaws (false signals).

### 3. Backtesting
**Backtesting** is the process of simulating a strategy on historical data to evaluate its performance before live trading.  
Key aspects include:
- **Position sizing:** Determines how much capital to allocate per trade.
- **Transaction costs:** Incorporates realistic slippage/commission.
- **Performance metrics:**
  - **CAGR (Compound Annual Growth Rate)** – annualized portfolio return.
  - **Max Drawdown** – largest peak-to-trough equity decline.
  - **Sharpe Ratio** – risk-adjusted return measure.
- **Visualization:** Equity curve, trade signals, and SMA overlays.

---

## ✨ Features
- Fetch historical price data with **yfinance** (or load from local CSVs)
- Implement SMA crossover (short vs long) strategy
- Simple backtest engine with:
  - Position sizing
  - Transaction cost support
- Performance metrics:
  - Returns
  - CAGR
  - Max Drawdown
  - Sharpe Ratio
- Basic plots of equity curve and buy/sell signals

---

## 🚀 Quickstart

### 1. Setup Environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\activate    # Windows PowerShell

pip install -r requirements.txt
```

### 2. Run Example
```bash
python examples/run_example.py
```

- The script runs a sample backtest on **AAPL** with configurable SMA windows.
- Results include performance metrics and plots.

---

## 📈 Example Output
- **Equity Curve** showing portfolio value over time.
- **Price Chart** with SMA overlays and buy/sell markers.
- **Summary Table** of performance metrics.

---

## 🛠️ Next Steps / Extensions
- Experiment with different SMA windows.
- Add **Exponential Moving Average (EMA)** strategies.
- Test multiple assets and portfolios.
- Implement stop-loss / take-profit rules.
- Extend performance metrics (Sortino ratio, volatility).

---

## 📜 License
MIT License – feel free to use and modify for educational or research purposes.
