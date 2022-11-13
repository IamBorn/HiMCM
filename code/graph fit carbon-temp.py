import pandas as pd
import matplotlib.pyplot as plt
import linear_model as lm
import quadratic_model as qm

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.rename(columns={'PPM': 'carbon level'})

print(data.to_string())

plt.xlabel('Carbon level [PPM]')
plt.ylabel('Temp')

plt.plot(data['carbon level'], data['Temp'], '-', label='raw data')
plt.legend(loc='lower right')
plt.savefig('./picture/carbon-temperature.png')