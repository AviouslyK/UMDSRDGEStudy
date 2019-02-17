import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 22})

#Reads in file
data = pd.read_csv("10mm.csv", sep=",")


Mu = list(data.Mu)
E  = list(data.E)

Muu = np.asarray(Mu)

def E_fit(m):
    return np.exp(-0.1037-10.03*m)

plt.figure(1)
plt.plot(Muu, E,'b.', label='Simulated Efficiency')
plt.plot(Muu,E_fit(Muu),'r-',dashes=[6,2], label='$e^{(-0.1037-10.03)\mu}$')
plt.xlabel('Induced Mu ($mm^{-1}$)')
plt.ylabel('Transmission Efficiency')
plt.legend(loc='upper right')
plt.title('Simulated Transmission Efficiency as a Function of the Induced Absorption Coefficient ($E_{sim}(\mu)$)')
plt.show()
