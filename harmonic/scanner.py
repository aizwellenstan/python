import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

data = pd.read_csv('')

data.columns = [['Date', 'open', 'high', 'low', 'close', 'vol']]

data.Date = pd.to_datetime(data.Date, format='%d.%m.%Y %H:%M:%S.%f')

data = data.set_index(data.Date)

data = data.drop_duplicates(keep=False)

data = data[['open', 'high', 'low', 'close', 'vol']]

price = data.close.iloc[:100]

max_idx = list(argrelextrema(price.values, np.greater, order=1[0]))
min_idx = list(argrelextrema(price.values, np.less, order=1[0])

idx = max_idx + min_adx

idx.sort()

peaks = price.values[idx]

plt.plot(price.values)
plt.scatter(idx, peaks, c='r')
plt.slow()