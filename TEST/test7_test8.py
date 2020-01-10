import pandas as pd

name = pd.Series({0:'Potter', 1:'Elsa', 2:'Gates', 3:'Wendy', 4:'Ben'}, name='name')
print(name, '\n')

gender = pd.Series({0:'Female', 1:'Male', 2:'Female', 3:'Male', 4:'Female'}, name='gender')
print(gender, '\n')

math = pd.Series({0:85, 1:76, 2:99, 3:88, 4:40}, name='math')
print(math, '\n')

print("# 데이터프레임 생성")
result = pd.concat([name, gender, math], axis=1)
result.set_index(name, inplace=True)
print(result, '\n')

stat = pd.Series({0:76, 1:73, 2:95, 3:10, 4:25}, name='stat')
print(stat, '\n')

score = pd.Series(math + stat, name='score')
print(score, '\n')

# score가 150 이상이면 A, 100 이상 150 미만이면 B, 70 이상 100 미만이면 C  등급, 그 외 nan을 부여하고 grade 컬럼에 저장
def rank(x):
    if x>150: return 'A'
    elif x>100: return 'B'
    elif x>70: return 'C'
    else: return 'NaN'

print("# grade")
grade = pd.Series(score.apply(rank), name='grade')
print(grade, '\n')

print("# 데이터프레임 생성")
result = pd.concat([name, gender, math, stat, score, grade], axis=1)
result.set_index(name, inplace=True)
print(result, '\n')