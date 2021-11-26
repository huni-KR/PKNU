import pandas as pd

file = 'countries.csv'
countires_df = pd.read_csv(file, index_col='Unnamed: 0')
print(countires_df.sort_values('area', ascending=False))
