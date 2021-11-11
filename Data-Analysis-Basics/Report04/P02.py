import pandas as pd

file_path = 'D:\\Code\\Github\\PKNU\\Data-Analysis-Basics\\Report04\\weather.csv'
data = pd.read_csv(
    file_path, encoding='euc-kr', index_col='일시')

print('1) 2020년 3월 1일의 평균기온, 최대풍속, 평균풍속 출력하기')
target_data = data.loc[['2020-03-01'], :]
print(target_data)
print('\n')

max_wind = data['평균 풍속(m/s)'].max()
print('2) 데이터에 기록된 날중에서 평균풍속의 최대 값 : ' + str(max_wind) + 'm/s\n\n')

print('3) 평균풍속이 최대인 날의 평균기온, 최대풍속, 평균풍속 출력하기')
print(data[data['평균 풍속(m/s)'] == max_wind])
