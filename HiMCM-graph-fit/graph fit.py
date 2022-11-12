import imp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import curve_fit

def objective_quadratic(x,a,b,c):
    return a*x**2 + b*x + c

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.drop('Unnamed: 3', axis = 1)
data = data.drop('Unnamed: 4', axis = 1)
data = data.drop('Unnamed: 5', axis = 1)
data = data.drop('Unnamed: 6', axis = 1)
data = data.rename(columns={"PPM": "carbon level"})

print(data.to_string())

fit_paramsQ, covariances = curve_fit(objective_quadratic, data["Year"], data["carbon level"])
a, b, c = fit_paramsQ
print('Parameter values: ')
print('y = %.5f * x^2 + %.5f * x + %.5f' % (a, b, c))
y_fit = objective_quadratic(data["Year"],*fit_paramsQ)

plt.xlabel('Year')
plt.ylabel('Carbon dioxide level[PPM]')
plt.plot(data["Year"], y_fit, '--', color='red')
plt.plot(data["Year"], data["carbon level"])
plt.savefig('carbon dioxide level quadratic fit.png')