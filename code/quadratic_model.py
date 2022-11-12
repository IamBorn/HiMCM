import imp
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error
import math

def objective_quadratic(x,a,b,c):
    return a*x**2 + b*x + c

def quadratic_fit(data):
    fit_paramsQ, covariances = curve_fit(objective_quadratic, data["Year"], data["carbon level"])
    a, b, c = fit_paramsQ
    y_fit = objective_quadratic(data["Year"],*fit_paramsQ)
    plt.plot(data["Year"], y_fit, '--', color='red', label='quadratic fit')
    mse = mean_squared_error(data['carbon level'], y_fit)
    rmse = math.sqrt(mse)
    print('%.5f * x^2 + %.5f * x + %.5f' % (a, b, c))
    return rmse