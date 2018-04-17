import pandas as pd
df1 = pd.DataFrame({'A': range(8), 'B': [2*i for i in range(8)]})
df2 = pd.DataFrame({'A': range(8), 'B': [-2*i for i in range(8)]})
print('Positive Data Set')
print(df1)
print('Negative Data Set')
print(df2)
print('Results')
print('Correlation Positive:', df1['A'].corr(df1['B']))
print('Correlation Negative:', df2['A'].corr(df2['B']))

df1.loc[2, 'B'] = 10
df2.loc[2, 'B'] = -10
print('Positive Data Set')
print(df1)
print('Negative Data Set')
print(df2)
print('Results')
print('Correlation Positive:', df1['A'].corr(df1['B']))
print('Correlation Negative:', df2['A'].corr(df2['B']))

df1.loc[3, 'B'] = 100
df2.loc[3, 'B'] = -100
print('Positive Data Set')
print(df1)
print('Negative Data Set')
print(df2)
print('Results')
print('Correlation Positive:', df1['A'].corr(df1['B']))
print('Correlation Negative:', df2['A'].corr(df2['B']))