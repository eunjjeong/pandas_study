import pandas as pd

exam_data = {'수학':[90, 80, 70], '영어':[98, 89, 95], '음악':[85,95,100], '체육':[100,90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print("df", df, sep='\n')
print()

pd.options.mode.chained_assignment = None
print("inplace=False", " pd.options.mode.chained_assignment = None")

df4 = df[:]
sub_df4 = df4.drop('수학', axis = 1)
print("sub_df4", sub_df4, sep='\n')
print('\n')

df5 = df[:]
sub_db5 = df5.drop(['영어', '음악'], axis = 1)
print("sub_db5", sub_db5, sep='\n')

pd.options.mode.chained_assignment = 'warn'
print("inplace=True", " pd.options.mode.chained_assignment = 'warn'")

df.drop('수학', axis=1, inplace=True)
print("df", df, sep='\n')
print('\n')

df.drop(['영어', '음악'], axis=1, inplace=True)
print("df", df, sep='\n')



