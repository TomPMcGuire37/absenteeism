import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('C:/Users/Tom/git/pythonProject/absenteeism/Absenteeism_at_work.csv', index_col=False, sep=';')

print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

"""sns.set_theme(style="darkgrid")
sns.histplot(x=['Reason for absence'], data=data)
plt.show()"""

_ = plt.hist(data['Reason for absence'], bins='auto')
plt.show()