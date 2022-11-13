import pandas as pd
import matplotlib.pyplot as plt
import linear_model as lm
import quadratic_model as qm

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.drop('Temp', axis=1)
data = data.rename(columns={"PPM": "carbon level"})

print(data.to_string())

plt.xlabel('Year')
plt.ylabel('Carbon dioxide concentration level(ppm)')

plt.plot(data["Year"], data["carbon level"], '-', label='raw data')
lm.linear_fit(data)
plt.legend(loc = 'lower right')
#plt.title("Model of relationship between Year and carbon dioxed level\n using quadratic regression")
plt.savefig('./picture/carbon dioxide level linear fit.png')