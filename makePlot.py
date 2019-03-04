import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})



#Reads in file
df       = pd.read_csv("Mu_spec_10mm_LDR.csv", sep=",")
Waves    = df.Wave
Mu_eff   = df.Mu_eff
#Mu = list(df.Mu_eff)
#E  = list(df.E)
#Eff = np.asarray(E)
#Muu = np.asarray(Mu)

#Diff = [0]*len(Mu)
#Abslength = [0]*len(Mu)

#def E_fit(m):
#    return np.exp(-0.1037-10.03*m)

#for i in range(len(Mu)):
#    Abslength[i] = (1 / Mu[i])/10
#    Diff[i] = np.abs(100*(E_fit(Mu[i]) - Eff[i])/(E_fit(Mu[i]) + Eff[i])/2)

err = 0.4

plt.figure(1)
#plt.plot(Waves,Mu_eff)
#plt.subplot(121)
plt.plot(Waves, Mu_eff, 'g')
#plt.legend(loc='upper right')
#plt.errorbar(Waves,stdeva, yerr = err, errorevery=50, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Effective Absorption Coefficient, $\mu_{eff}$ ($mm^{-1}$)')
#plt.ylim(84,89) 
#plt.ylim(1e-06,1e02)
plt.title('EJ200PVT Absorption Spectrum')
#plt.legend(loc ='upper right')
#plt.subplot(122)
#plt.plot(Waves, stdeva, 'g', label='Avi')
#plt.plot(Waves, stdevb,'b',label='Duan')
#plt.plot(Waves, stdevc,'r',label='Tim')
#plt.plot(Waves, stdevd,'g', label='Avi - 2018')
#plt.legend(loc='upper right', ncol=2)
#plt.errorbar(Waves,stdeva, yerr = err, errorevery=15, capsize = 3, ecolor= 'b', fmt = 'b') 
#plt.xlabel('Wavelength ($nm$)', fontsize='x-small')
#plt.ylabel('Stdev in Transmission Efficiency')
#plt.suptitle('EJ260-1X1P-N1 Training Measurements: ')
#plt.title('Standard Deviation including 2018 measurement')

plt.show()
