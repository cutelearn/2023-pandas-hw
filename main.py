import pandas as pd

course = ['Chinese', 'English', 'Math', 'Natural', 'Society']
chinese = [14, 12, 13, 10, 13]
eng = [13, 14, 11, 10, 15]
math = [15, 9, 12, 8, 15]
nature = [15, 10, 13, 10, 15]
social = [12, 11, 14, 9, 14]

df = pd.DataFrame([chinese, eng, math, nature, social],
                  columns=course, index=range(1, 6))

# 計算每位學生的總分
total = [df.iloc[i].sum() for i in range(5)]  # 列出每位學生總成績
df['total'] = total

# 根據總分對學生進行降序排序
df = df.sort_values(by='total', ascending=False)

print(df)

# 增加排名欄位
df['rank'] = df['total'].rank(ascending=False, method='min').astype('int')

print(df)
