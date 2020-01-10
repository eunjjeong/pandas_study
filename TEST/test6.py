import pandas as pd

exam_data = {'시험': ['중간', '기말'], '수학': [95,90], '국어': [90,85], '영어': [85,80]}

df = pd.DataFrame(exam_data)
df.set_index('시험', inplace=True)
print(df)
print()

# 과목별 합계, 평균 계산하여 출력
mid = pd.Series({'수학':95, '국어':90, '영어':85})
last = pd.Series({'수학':90, '국어':85, '영어':80})

print("# 과목별 합계, 평균 계산")
add = mid + last
ave = add / 2

result = pd.DataFrame([add, ave], index=['합계', '평균'])
print(result)
