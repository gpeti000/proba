import pandas as pd

df_tlt = pd.read_csv("TLT.csv")
df_voo = pd.read_csv("VOO.csv")
'''
#df_test = pd.read_excel("teszt.xlsx", sheet_name="Sheet1")
# excel file-ból csinál csv-t
#df_test.to_csv("df_test_output.csv")

df = pd.DataFrame(data={"A": [3, 4, "a"],
                        "B": ["dafd", 3, 5]})

# print(df_tlt, df_voo)
# # debug, "view as dataframe"
# print(df_test)

# print(df)

# adattábla első n sora (head), és utolsó n sora (tail)

# print(df_voo.head(3))
# print(df_voo.tail(3))
# print(df_voo.columns)
# print(df_voo.index)
# print(df_voo.dtypes)

# print(df["B"])
# df["C"] = ""
# print(df)
# del df["C"]
# print(df)

# debugger, evaluate expression parancsok
# df[["A", "B"]]
# df_voo.loc[0:5, "Adj Close"]
# df_voo.iloc[-5:-1]["Adj Close"]

# df_voo_copy = df_voo.copy()
# df_voo_copy.index = df_voo_copy["Date"]
# print(df_voo_copy)
# del df_voo_copy["Date"]
# print(df_voo_copy)

df_voo["Volume in thousands"] = df_voo["Volume"] / 1000
df_voo["Open Close Difference"] = df_voo["Open"] - df_voo["Close"]
#print(df_voo)

df_merged = df_voo.merge(df_tlt, how="inner", on="Date", suffixes=['_voo', '_tlt']) # a suffiexes-zel toldalékolom az oszlopok nevét

df_merged_filtered = df_merged[['Date', 'Adj Close_voo', 'Adj Close_tlt']]
print(df_merged_filtered)

df_prop = pd.read_csv('property data.csv')
print(df_prop.shape)

#evaluate parancs
df_prop_berkeley = df_prop.loc[df_prop['ST_NAME'] == 'BERKELEY']

print(df_prop.loc[df_prop['ST_NAME'] == 'BERKELEY', 'ST_NAME'])

#ha több elemre akarunk szűrni az ST_NAME oszlopban, akkor az isin kell használni
msk = df_prop['ST_NAME'].isin(['BERKELEY', 'LEXINGTON'])
print(df_prop.loc[msk, ])

#msk = df_prop['ST_NUM'] < 200
msk = (df_prop['ST_NUM'] < 200) & (df_prop['ST_NAME'] == "LEXINGTON")
print(df_prop.loc[msk])
print(msk)

msk = df_prop["ST_NUM"].notnull()
print(df_prop.loc[msk])

df_prop["PID"] = df_prop["PID"].fillna("UNKNOWN") # a NaN-t kicseréli UNKNOWN-ra
print(df_prop)

df_prop_copy = df_prop.copy()
df_prop_copy = df_prop_copy.fillna("UNKNOWN")
print(df_prop_copy)
'''

df_voo['effective_return'] = df_voo['Adj Close'] / df_voo['Adj Close'].shift(1) - 1
print(df_voo)

import numpy as np
df_voo['log_return'] = np.log(df_voo['Adj Close'] / df_voo['Adj Close'].shift(1))
df_voo['cumsum_log_return'] = df_voo['log_return'].cumsum()
print(df_voo)


