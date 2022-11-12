import pandas as pd
import matplotlib.pyplot as plt
import linear_model as lm
import quadratic_model as qm

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.drop('Unnamed: 3', axis = 1)
data = data.drop('Unnamed: 4', axis = 1)
data = data.drop('Unnamed: 5', axis = 1)
data = data.drop('Unnamed: 6', axis = 1)
data = data.drop('PPM', axis=1)

print(data.to_string())

plt.xlabel('Year')
plt.ylabel('Temp')

plt.plot(data['Year'], data['Temp'], '-', label='raw data')
plt.legend(loc='lower right')
plt.savefig('./picture/temperature-year')