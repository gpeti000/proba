import pandas as pd
'''
df_funds = pd.read_csv("fundamentals.csv")
df_prices = pd.read_csv("prices.csv")
df_psplit = pd.read_csv("prices-split-adjusted.csv")
df_secs = pd.read_csv("securities.csv")

#print(df_prices)

def process_prices(df):
    df["date"] = df["date"].apply(lambda x: x[:10])
    df_filtered = df[["date", "symbol", "close"]]
    df_pivot = pd.pivot_table(df_filtered, index=["date"], columns=["symbol"], values=["close"])
    df_pivot.columns = df_pivot.columns.droplevel()

    return df_pivot

df_prices_processed = process_prices(df_prices)
df_prices_adjusted_processed = process_prices(df_psplit)

print(df_prices_adjusted_processed)

def add_effective_return(df):
    for col in df.columns:
        df[col + '_effective_return'] = df[col] / df[col].shift(1) - 1
    return df

df_prices_processed_with_returns = add_effective_return(df_prices_processed)
df_prices_adjusted_processed_with_returns = add_effective_return(df_prices_adjusted_processed)

print(df_prices_processed_with_returns)

df_merged = df_prices_processed_with_returns.merge(df_prices_adjusted_processed_with_returns, on='date', suffixes=('_normal', '_adjusted'))

symbols = df_prices_processed.columns       #kiszedjük egy listába az oszlopneveket
splits = []
for symbol in symbols:
    df_symbol = df_merged[[symbol + '_effective_return_normal', symbol + '_effective_return_adjusted']]
    difference_array = df_symbol[symbol + '_effective_return_normal'] - df_symbol[symbol + '_effective_return_adjusted'] > 0.001
    if len(df_symbol.loc[difference_array]) > 0:
        splits.append(symbol)
print(splits, len(splits))
'''

import numpy as np
def add_log_return(df):
    df_out = pd.DataFrame()



for col in df_prices_adjusted_log_return.columns:
    col_notnull = df_prices_adjusted_log_return.loc[df_prices_adjusted_log_return[col].notnull(), col]
    yearly_return = 255 * col_notnull.mean()
    return_dict[col] = yearly_return
df_securities['yearly_return'] = df_securities['Ticker symbol'].map(return_dict)
print(df_securities)
