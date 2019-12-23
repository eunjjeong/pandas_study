import pandas as pd

exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

pd.options.mode.chained_assignment = None

print("inplace=False", "pd.options.mode.chained_assignment = None")
df2 = df[:]

df3 = df2.drop('우현')
print('df4', df3, sep='\n')
print()

df4 = df[:]
df5 = df4.drop(['우현', '인아'], axis=0)
print("\ndf5", df5, sep='\n')
print()

print("inplace=True", "pd.options.mode.chained_assignment = 'warn''")
pd.options.mode.chained_assignment = 'warn'
df.drop('인아', inplace=True)
print("df", df, sep='\n')

df.drop(['서준', '우현'], axis=0, inplace=True)
print("\ndf", df, sep="\n")
