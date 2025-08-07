import pandas as pd

ts_data = {
    'Date': pd.date_range(start='2025-01-01', periods=6, freq='M'),
    'Sales': [2000, 2200, 2500, 2100, 2700, 3000]
}
ts_df = pd.DataFrame(ts_data)
ts_df.set_index('Date', inplace=True)
ts_df['3_Month_MA'] = ts_df['Sales'].rolling(window=3).mean()
print(ts_df)
