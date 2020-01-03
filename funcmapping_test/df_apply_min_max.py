import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())
print()

def min_max(x): # 최대값 - 최소값
    return x.max() - x.min()

# 사용자 정의 함수
def add_two_obj(a,b):
    return a+b

print("# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환")
result = df.apply(min_max)
print(result, type(result), sep='\n')
print()

print("# 데이터프레임의 2개 열을 선택하여 적용")
print("# x=df, a=df['age'], b=df['ten']")
df['add'] = df.apply(lambda x:add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())




