import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

auslenkung = np.array([30,60,90,120,150,180,210,240,270,300])
kraft      = np.array([0.02,0.12,0.21,0.31,0.40,0.50,0.60,0.70,0.80,0.90])
werte      = np.array([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
err        = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

for i in range(10):
    werte[i] =  kraft[i]  * 0.12 * 1/(auslenkung[i]/360*(2*np.pi)) 

y = unp.uarray(werte,err)
x = ufloat(0.0,0.0)

#for i in range(10):
#    x = x + y[i]

b = ufloat(8.064,1.870)
D = ufloat(0.117027,0.004618)
m = 1.1193
R = 0.00375
h = 0.003
I = ufloat(0.0,0.0)


print(b*D)
print( (b*D)/(4*np.pi**2) - (m*R**2)/(2) -(m*h**2)/(6) )

print(np.mean(werte))
print(np.std(werte))


