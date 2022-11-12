import imp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import curve_fit
from scipy import stats

def objective_linear(x, a, b):
    return a*x + b

def objective_quadratic(x,a,b,c):
    return a*x**2 + b*x + c

data = pd.read_csv('2022_HiMCM_Data.csv')
data = data.drop('Unnamed: 3', axis = 1)
data = data.drop('Unnamed: 4', axis = 1)
data = data.drop('Unnamed: 5', axis = 1)
data = data.drop('Unnamed: 6', axis = 1)
data = data.rename(columns={"PPM": "carbon level"})

print(data.to_string())

def quadratic_fit(data):
    fit_paramsQ, covariances = curve_fit(objective_quadratic, data["Year"], data["carbon level"])
    a, b, c = fit_paramsQ
    y_fit = objective_quadratic(data["Year"],*fit_paramsQ)
    plt.plot(data["Year"], y_fit, '--', color='red', label='q fit')
    slope, intercept, r_value, p_value, std_err = stats.linregress(data["Year"],y_fit)
    return r_value


def linear_fit(data):
    fit_paramsl, covariances = curve_fit(objective_linear, data["Year"], data["carbon level"])
    a, b = fit_paramsl
    y_fit = objective_linear(data["Year"],*fit_paramsl)
    plt.plot(data["Year"], y_fit, '--', color='red', label='linear fit')
    slope, intercept, r_value, p_value, std_err = stats.linregress(data["Year"],y_fit)
    return r_value


plt.xlabel('Year')
plt.ylabel('Carbon dioxide level[PPM]')

plt.plot(data["Year"], data["carbon level"])
print(linear_fit(data))
plt.show()