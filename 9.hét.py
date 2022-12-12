
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def get_daily_risk_free_rate():
    # https: // fred.stlouisfed.org / series / DTB3
    df = pd.read_csv('DTB3.csv')
    df.index = pd.to_datetime(df['DATE'])
    df = df[['DTB3']]
    df.columns = ['risk_free_daily']
    msk = df['risk_free_daily']!='.'
    df = df[msk]
    df = df.astype(float)
    df = df / 252
    return df
#df = get_daily_risk_free_rate()
#print(df)
"""
filename = 'BRK-B.csv'
df = pd.read_csv(filename)
df['ret_log_daily'] = np.log(
    df['Adj Close']/df['Adj Close'].shift(1))
df.index = pd.to_datetime(df['Date'])
df_risk_free = get_daily_risk_free_rate()
df = df.join(df_risk_free)
df = df.dropna()
df['ret_log_daily_exc'] = df['ret_log_daily'] - df['risk_free_daily']
t_day_in_year = 252
vol_windows_in_y = [0.25, 1, 3, 10]
cols_vol, cols_ret, cols_beta = [], [], []
for year in vol_windows_in_y:
    col_vol = 'vol_' + str(year) + 'y'
    col_ret = 'ret_yearly_' + str(year) + 'y'
    col_beta = 'beta_yearly_' + str(year) + 'y'
    cols_vol.append(col_vol)
    cols_ret.append(col_ret)
    cols_beta.append(col_beta)
    df[col_vol] = \
        np.sqrt(t_day_in_year) * \
        df['ret_log_daily_exc'].rolling(int(year * t_day_in_year)).std()
    df[col_ret] = \
        t_day_in_year * \
        df['ret_log_daily_exc'].rolling(int(year * t_day_in_year)).mean()
    df[col_beta] = df[col_ret] / df[col_vol]
df['ret_log_daily_exc'].plot()
df[cols_vol].plot()
df[['ret_log_daily', 'vol_1y', 'beta_yearly_1y', 'ret_yearly_1y']].plot()
plt.show()
print(1)
"""

import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

from np6het2sav import Option



"""
#inspect dataframe
df.describe()
print(df[:6])
"""

filename = "KO.csv"
df = pd.read_csv(filename)
print(df.describe()) # adott oszlopok mutatószámai
print(df.columns)
# Open interest: összesen mennyi kontraktot nyitottak meg
# mid : Best bid és Best offer 

# CALC time to expiry
df["date"] = pd.to_datetime(df["date"])
df["expiry"]=pd.to_datetime(df["expiry"])
df["daystoexp"]=(df.expiry-df.date).dt.days
df=df.set_index("date")

print(df[:6])


#plot forward price vs time
df.groupby(df.index).forward_price.median().plot()
plt.show()

#calc implied volatility and greeks
def calcVolaMid(row):
    opt = Option(row.cp_flag, row.strike, row.expiry, 1)
    if row.forward_price*row.daystoexp*row.mid>0:
        return opt.calcVola(row.forward_price,row.daystoexp/365,row.mid)
    else:
        return np.nan

df0 = df[df.index<"2018-03-01"]


# Calc vola: takes a few minutes
df0.loc[:, "implied_vola_mid"] = df0.apply(calcVolaMid, axis=1)
#print(df0)
# Volatility smile
dates = df0.index.unique()
# example:
df_ = df0[df0.index == dates[23]]
df_ = df0[df0.daystoexp == 102]
# Filtering out lagged data
df_ = df_[df_.last_date == "2018-02-05"]
df_.groupby(df_.strike).implied_vola_mid.median().plot()
plt.show()




