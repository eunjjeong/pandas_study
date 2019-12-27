import pandas as pd

print("# Timestamp의 배열 만들기 - 월, 간격, 월의 시작일 기준")
ts_ms = pd.date_range(start='2019-01-01', end = None, periods = 6, freq = 'MS', tz = 'Asia/Seoul')

print(ts_ms, '\n')

print("# 월 간격, 월의 마지막 날 기준")
ts_me = pd.date_range('2019-01-01', periods=6, freq='M', tz='Asia/Seoul')
print(ts_me, '\n')

print("# 분기(3개월) 간격, 월의 마지막 날 기준")
ts_3m = pd.date_range('2019-01-01', periods=6, freq='3M', tz='Asia/Seoul')
print(ts_3m)

print('# Period 배열 만들기 - 1개월 길이')
pr_m = pd.period_range(start='2019-01-01', end=None, periods=3, freq='M')
print(pr_m, '\n')

print('# Period 배열 만들기 - 1시간 길이')
pr_h = pd.period_range(start='2019-01-01', end=None, periods=3, freq='H')
print(pr_h, '\n')

print('# Period 배열 만들기 - 2시간 길이')
pr_2h = pd.period_range(start='2019-01-01', end=None, periods=3, freq='2H')
print(pr_2h)
