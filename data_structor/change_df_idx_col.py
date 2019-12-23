import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])

print(df, df.index, df.columns, sep='\n')
print()

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df, df.index, df.columns, sep='\n')
print()

df.rename(columns = {'연령':'나이', '남녀':'성별', '소속':'학교'}, inplace=True)
print(df, df.index, df.columns, sep='\n')
print()

df.rename(index={'학생1':'준서', '학생2':'예은'}, inplace=True)
print(df, df.index, df.columns, sep='\n')
