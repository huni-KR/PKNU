from tabulate import tabulate
import pandas as pd

data = pd.read_csv('Finals/data.csv', encoding='euc-kr')
wind_speed_check = data['풍속(m/s)'] >= 10
humidity_check = data['습도(%)'] >= 95
data = data[wind_speed_check & humidity_check]

print(tabulate(data, headers='keys', tablefmt='psql'))
