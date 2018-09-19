import pandas as pd

#this gets the historical data into pandas df
df = pd.read_csv('GBP_USD_Historical_Data.csv')

print(df.head)
