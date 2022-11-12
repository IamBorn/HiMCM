import imp
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import math

def objective_linear(x, a, b):
    return a*x + b

def linear_fit(data):
    fit_paramsl, covariances = curve_fit(objective_linear, data["Year"], data["carbon level"])
    a, b = fit_paramsl
    y_fit = objective_linear(data["Year"],*fit_paramsl)
    plt.plot(data["Year"], y_fit, '--', color='red', label='linear fit')
    mse = mean_squared_error(data['carbon level'], y_fit)
    rmse = math.sqrt(mse)
    return rmse