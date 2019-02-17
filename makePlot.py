import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 22})

#Reads in file
df       = pd.read_csv("10mm_LDR_data.csv", sep=",")
Waves    = df.Wave
Andres_1 = df.T_a_1
Andres_2 = df.T_a_2
Kak_1    = df.T_k_1
Kak_2    = df.T_k_2
Kak2_1   = df.T_k2_1
Kak2_2   = df.T_k2_2
Avi_1    = df.T_av_1
Avi_2    = df.T_av_2

Andres = np.mean( np.array([ Andres_1, Andres_2 ]), axis=0 )
Kak1   = np.mean( np.array([ Kak_1, Kak_2 ]), axis=0 )
Kak2   = np.mean( np.array([ Kak2_1, Kak2_2 ]), axis=0 )
Avi   = np.mean( np.array([ Avi_1, Avi_2 ]), axis=0 )

#Mu = list(data.Mu)
#E  = list(data.E)

#Muu = np.asarray(Mu)

#def E_fit(m):
#    return np.exp(-0.1037-10.03*m)

plt.figure(1)
plt.subplot(211)
plt.plot(Waves, Andres,'y',label='Andres 0 days aft. irradiation')
plt.plot(Waves, Kak1,'g',label='Kak 14 days aft. irradiation')
plt.plot(Waves, Kak2,'r',label='Kak 28 days aft. irradiation')
plt.plot(Waves, Avi,'b',label='Avi 468 days aft. irradiation')
#plt.plot(Muu, E,'b.', label='Simulated Efficiency')
#plt.plot(Muu,E_fit(Muu),'r-',dashes=[6,2], label='$e^{(-0.1037-10.03)\mu}$')
#plt.xlabel('Wavelength(nm)')
plt.ylabel('Transmission Efficiency')
plt.legend(loc='upper right')
plt.title('10mm Absorption Measurement Data Consistency (Set V1)')

plt.subplot(212)
plt.plot(Waves, Andres,'y',label='Andres 3/2/17')
plt.plot(Waves, Kak1,'g',label='Kak 3/16/17')
plt.plot(Waves, Kak2,'r',label='Kak 3/30/17')
plt.plot(Waves, Avi,'b',label='Avi 6/14/18')
plt.xlabel('Wavelength(nm)')
plt.ylabel('Transmission Efficiency')
#plt.legend(loc='upper right')
plt.xlim(400,600)
plt.ylim(85,91)
plt.show()
