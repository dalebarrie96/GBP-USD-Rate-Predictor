import pandas as pd

#this gets the historical data into pandas df
df = pd.read_csv('GBP_USD_Historical_Data.csv')

#this calculates the high low percentage
df['HL_PCT'] = (df['High'] - df['Low']) / df['Low'] * 100.0


# this again modifies the datafield with our own fields
df = df[['Price','Open','HL_PCT', 'Change %']]

print(df.head())
