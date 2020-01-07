import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# 파일 불러오기
df_2015_2019 = pd.read_csv('전국 전체 분양가격(2015_2019).csv', encoding='utf-8')
print(df_2015_2019.shape, '\n', df_2015_2019.head(), '\n', df_2015_2019.tail())

df_2013_2015 = pd.read_csv('전국 평균 분양가격(2015년 9월까지).csv',
                           encoding='euc-kr',
                           skiprows=1,
                           header=0, engine='python')
print(df_2013_2015.shape, '\n', df_2013_2015.head(), '\n', df_2013_2015.tail())

print(df_2013_2015.columns)

# 24열 이후 삭제(통계정보)
df_2013_2015 = df_2013_2015.drop(columns=df_2013_2015.columns[24:])
print(df_2013_2015.columns)

year = df_2013_2015.iloc[0]
# 결측치를 전의 값으로 채워줌
year = year.fillna(method='ffill')
year

month = df_2013_2015.iloc[1]
print(year, '\n', month)

for i, y in enumerate(year):
    if i > 1:
        year[i] = ' '.join([str(year[i]), '{:,.0f}'.format(month[i])])
year[1] = '시군구'

print(year)

df_2013_2015.columns = year
print(df_2013_2015)

# 통계정보 제거
df_2013_2015 = df_2013_2015.drop(df_2013_2015.index[[0,1,2,10,12,22]])
print(df_2013_2015)

df_2013_2015.loc[4, '구분'] = ''
df_2013_2015.loc[14, '구분'] = ''
print(df_2013_2015)

# 지역 컬럼을 새로 만들어 시도와 시군구를 병합
# 결측치 빈문자로
df_2013_2015['구분'] = df_2013_2015['구분'].fillna('')
df_2013_2015.시군구 = df_2013_2015.시군구.fillna('')
print(df_2013_2015)
df_2013_2015['지역명'] = df_2013_2015.구분 + df_2013_2015.시군구
print(df_2013_2015)

print(df_2013_2015.drop(['구분','시군구'], axis=1))

melt_columns = df_2013_2015.columns.copy()
print(melt_columns)
print()
df_2013_2015 = pd.melt(df_2013_2015, id_vars=['지역명'],
                       value_vars=['2013 12', '2014 1', '2014 2', '2014 3', '2014 4',
                                   '2014 5', '2014 6', '2014 7', '2014 8', '2014 9', '2014 10', '2014 11',
                                   '2014 12', '2015 1', '2015 2', '2015 3', '2015 4', '2015 5', '2015 6',
                                   '2015 7', '2015 8', '2015 9'])
print(df_2013_2015.head())

df_2013_2015.columns = ['지역명', '기간', '분양가']
print(df_2013_2015.head())
print()

df_2013_2015['연도'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[0])
df_2013_2015['월'] = df_2013_2015['기간'].apply(lambda year_month: year_month.split(' ')[1])

print(df_2013_2015.head())
print(df_2015_2019.head(), '\n')

print(df_2013_2015.info(), '\n\n')
df_2013_2015.연도 = df_2013_2015.연도.astype(int)
df_2013_2015.월 = df_2013_2015.월.astype(int)
print(df_2013_2015.info(), '\n\n')