import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print()

def missing_value(series):
    return series.isnull()

print("# 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환")
result = df.apply(missing_value, axis=0)
print(result.head(), type(result), sep='\n')
