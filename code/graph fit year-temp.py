import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import math

def objective_quadratic(x,a,b,c):
    return a*x**2 + b*x + c

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.drop('PPM', axis=1)

data['Year'] = data['Year'].astype(float)

print(data.to_string())

plt.xlabel('Year')
plt.ylabel('Temp')

plt.plot(data['Year'], data['Temp'], '-', label='raw data')
fit_paramsQ, covariances = curve_fit(objective_quadratic, data["Year"], data["Temp"], p0=(0.01, 0.01, 0.01))
a, b, c = fit_paramsQ
print("%f * x^2 + %f * x + %f" % (a, b, c))
y_fit = objective_quadratic(data["Year"], a, b, c)
mse = mean_squared_error(data['Temp'], y_fit)
rmse = math.sqrt(mse)
print(rmse)
plt.plot(data["Year"], y_fit, '--', color='red', label='quadratic fit')
plt.legend(loc='lower right')
#plt.savefig('./picture/temperature-year')
plt.show()