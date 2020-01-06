import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

x = np.array([0.92,1.16,0.96,1.12,1.00])

print(np.mean(x))
print(np.std(x))

y = np.array([2.23,1.95,2.01,2.02,1.95])

print(np.mean(y))
print(np.std(y))
#2.032 \pm 0.0515