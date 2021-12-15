import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Finals/data.csv', encoding='euc-kr')
data = data.groupby('시간')['풍속(m/s)'].mean()

data.plot(color='r')
plt.xlabel('time')
plt.ylabel('mean_wind_speed(m/s)')
plt.show()
