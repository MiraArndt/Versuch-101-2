import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.optimize import curve_fit

x=np.genfromtxt("Eigentraegheitsmoment.csv", delimiter=",",unpack=True,usecols=0)
y=np.genfromtxt("Eigentraegheitsmoment.csv", delimiter=",",unpack=True,usecols=1)

x = x**2
y = y**2

params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(0, 0.1)


plt.plot(x, y,'r.', label='Messwerte')
plt.plot(x_plot,x_plot * params[0] + params[1], label = 'Lineare Regression')
plt.xlabel(r'$a^2 \:/\: \si{\meter}^2$')
plt.ylabel(r'$T^2 \:/\: \si{\second}^2$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
