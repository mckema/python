import pandas as pd
import datetime
import pandas_datareader.data as web
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
from matplotlib import style
yf.pdr_override()

style.use('fivethirtyeight')

mystart = datetime.datetime(2018, 1, 7) #yyyy, d, m
myend = datetime.datetime.now()
#myticker = ["AAPL", "BAC"]
myticker = "AAPL"
style.use('fivethirtyeight')

# download dataframe
df = web.get_data_yahoo(myticker, start=mystart, end=myend)

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
#df = df.drop("Symbol", axis=1)

#print(myticker)
print(df.tail())
#print(df['High'])
df['High'].plot()
plt.legend()
plt.show()