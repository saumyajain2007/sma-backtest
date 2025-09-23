import numpy as np
import pandas as pd
from typing import Tuple
from .utils import compute_sma

class SMACrossoverBacktest:
    def __init__(self, df: pd.DataFrame, short_window: int = 20, long_window: int = 50,
                 capital: float = 100_000.0, slippage: float = 0.0, commission: float = 0.0):
        self.df = df.copy()
        self.short_window = short_window
        self.long_window = long_window
        self.capital = capital
        self.slippage = slippage
        self.commission = commission
        self._prepare()

    def _prepare(self):
        self.df['sma_short'] = compute_sma(self.df, self.short_window)
        self.df['sma_long'] = compute_sma(self.df, self.long_window)
        self.df['signal'] = 0
        self.df.loc[self.df['sma_short'] > self.df['sma_long'], 'signal'] = 1
        self.df.loc[self.df['sma_short'] < self.df['sma_long'], 'signal'] = 0
        self.df['signal_change'] = self.df['signal'].diff().fillna(0)

    def run(self) -> pd.DataFrame:
        cash = self.capital
        position = 0
        position_price = 0
        equity_curve = []
        positions = []

        for idx, row in self.df.iterrows():
            price = row['Adj Close']
            sig = row['signal_change']

            if sig > 0 and position == 0:
                qty = (cash * (1 - self.slippage)) // price
                if qty > 0:
                    cost = qty * price + self.commission
                    cash -= cost
                    position = qty
                    position_price = price
            elif sig < 0 and position > 0:
                proceeds = position * price - self.commission
                cash += proceeds
                position = 0
                position_price = 0

            total_equity = cash + position * price
            equity_curve.append(total_equity)
            positions.append(position)

        self.df['position'] = positions
        self.df['equity'] = equity_curve
        return self.df
