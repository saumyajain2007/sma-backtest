import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple

def load_yfinance(symbol: str, start: str, end: str) -> pd.DataFrame:
    import yfinance as yf
    df = yf.download(symbol, start=start, end=end, progress=False)
    df = df[['Open','High','Low','Close','Adj Close','Volume']]
    df.columns = df.columns.rename(None)
    df = df.dropna()
    return df

def compute_sma(df: pd.DataFrame, window: int, price_col: str = 'Adj Close') -> pd.Series:
    return df[price_col].rolling(window=window, min_periods=1).mean()

def performance_metrics(equity: pd.Series, periods_per_year: int = 252) -> dict:
    returns = equity.pct_change().fillna(0)
    total_return = equity.iloc[-1] / equity.iloc[0] - 1
    years = (equity.index[-1] - equity.index[0]).days / 365.25
    cagr = (equity.iloc[-1] / equity.iloc[0]) ** (1/years) - 1 if years>0 else np.nan
    ann_vol = returns.std() * np.sqrt(periods_per_year)
    sharpe = (returns.mean() * periods_per_year - 0) / ann_vol if ann_vol>0 else np.nan
    running_max = equity.cummax()
    drawdown = equity / running_max - 1
    max_dd = drawdown.min()
    return {
        'total_return': total_return,
        'cagr': cagr,
        'ann_vol': ann_vol,
        'sharpe': sharpe,
        'max_drawdown': max_dd,
    }

def plot_equity_and_signals(df: pd.DataFrame, equity: pd.Series, signals: pd.Series = None):
    fig, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)
    axes[0].plot(df.index, df['Adj Close'], label='Adj Close')
    if signals is not None:
        buys = signals[signals==1].index
        sells = signals[signals==-1].index
        axes[0].scatter(buys, df.loc[buys,'Adj Close'], marker='^', s=60)
        axes[0].scatter(sells, df.loc[sells,'Adj Close'], marker='v', s=60)
    axes[0].set_title('Price and Signals')
    axes[0].legend()

    axes[1].plot(equity.index, equity.values)
    axes[1].set_title('Equity Curve')
    plt.tight_layout()
    return fig
