from src.utils import load_yfinance, plot_equity_and_signals, performance_metrics
from src.backtest import SMACrossoverBacktest

def main():
    symbol = 'AAPL'
    df = load_yfinance(symbol, start='2015-01-01', end='2024-12-31')
    bt = SMACrossoverBacktest(df, short_window=50, long_window=200, capital=100_000, slippage=0.0005, commission=1.0)
    df_res = bt.run()
    metrics = performance_metrics(df_res['equity'])
    print('Performance:')
    for k,v in metrics.items():
        print(f'{k}: {v}')

    fig = plot_equity_and_signals(df_res, df_res['equity'], signals=df_res['signal_change'])
    fig.savefig('examples/equity_curve.png')

if __name__ == '__main__':
    main()
