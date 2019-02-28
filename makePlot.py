import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})



#Reads in file
df       = pd.read_csv("EJ260.csv", sep=",")
Waves    = df.Waves
#Mu_eff   = df.MuEffective
Avi_a    = df.Avi_a
Avi_b    = df.Avi_b
Avi_c    = df.Avi_c
Avi_d    = df.Avi_d

Duan_a    = df.Duan_a
Duan_b    = df.Duan_b
Duan_c    = df.Duan_c
Duan_d    = df.Duan_d

Tim_a    = df.Tim_a
Tim_b    = df.Tim_b
Tim_c    = df.Tim_c
Tim_d    = df.Tim_d

Avi2_a    = df.Avi2_a
Avi2_b    = df.Avi2_b
Avi2_c    = df.Avi2_c
Avi2_d    = df.Avi2_d

Avi3_a    = df.Avi3_a
Avi3_b    = df.Avi3_b
Avi3_c    = df.Avi3_c
Avi3_d    = df.Avi3_d

Kak_a     = df.Kak_a
Kak_b     = df.Kak_b
Kak_c     = df.Kak_c
Kak_d     = df.Kak_d

#Andres1 = np.mean( np.array([ Andres_1, Andres_2 ]), axis=0 ) # set V1, 0 days aft
#Andres2 = np.mean( np.array([ Andres2_1, Andres2_2 ]), axis=0 )# set V3, 14 days aft
#Andres3 = np.mean( np.array([ Andres3_1, Andres3_2 ]), axis=0 ) #set V3, 28 days aft.
#Andres4 = np.mean( np.array([ Andres4_1, Andres4_2 ]), axis=0 )# set V3, 159 days aft.
#Kak1   = np.mean( np.array([ Kak_1, Kak_2 ]), axis=0 ) #V1, 14 days aft
#Kak2   = np.mean( np.array([ Kak2_1, Kak2_2 ]), axis=0 )#V1, 28 days
#Kak3   = np.mean( np.array([ Kak3_1, Kak3_2 ]), axis=0 )#V3, 2 days
#Avi1   = np.mean( np.array([ Avi_1, Avi_2 ]), axis=0 )#V1, 468
#Avi2   = np.mean( np.array([ Avi2_1, Avi2_2 ]), axis=0 )#V3, 154
#Avi3   = np.mean( np.array([ Avi3_1, Avi3_2 ]), axis=0 )#V3, 410

#stdevT = [0]*len(Waves)
#stdV1  = [0]*len(Waves)
#stdV3  = [0]*len(Waves)
#for i in range(len(Waves)):
#    pointV1 = []
#    pointV3 = []
#    pointV1.append(Andres1[i])
#    pointV3.append(Andres2[i])
#    pointV3.append(Andres3[i])
#    pointV3.append(Andres4[i])
#    pointV1.append(Kak1[i])
#    pointV1.append(Kak2[i])
#    pointV3.append(Kak3[i])
#    pointV1.append(Avi1[i])
#    pointV3.append(Avi2[i])
#    pointV3.append(Avi3[i])
#    point = pointV1 + pointV3
#    stdevT[i] = np.std(point)
#    stdV1[i]  = np.std(pointV1)
#    stdV3[i]  = np.std(pointV3)

#Mu = list(df.Mu)
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
plt.subplot(221)
plt.plot(Waves, Kak_a,'g',label='March 2017')
plt.plot(Waves, Avi3_a,'b',label='April 2018')
plt.plot(Waves, Avi2_a,'r',label='June 2018')
plt.plot(Waves, Avi_a, 'm',linestyle='dashed', label='February 2019 (After repair)')
plt.legend(loc='upper right', ncol=2)
plt.errorbar(Waves,Avi_a, yerr = err, errorevery=15, capsize = 3, ecolor= 'm', fmt = 'm',ls='-.') 
plt.errorbar(Waves,Avi3_a, yerr = err, errorevery=15, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Transmission Efficiency')
plt.ylim(84,90) 
plt.xlim(500,600)
#plt.ylim(1e-06,1e02)
plt.title('EJ260-1X1P-N1 Reference Measurements: Side A')

plt.subplot(222)
#plt.plot([], [], ' ', label="Repaired Febuary 2019")
plt.plot(Waves, Kak_b,'g',label='March 2017')
plt.plot(Waves, Avi3_b,'b',label='April 2018')
plt.plot(Waves, Avi2_b,'r',label='June 2018')
plt.plot(Waves, Avi_b, 'm',linestyle='dashed', label='February 2019 (After repair)')
plt.legend(loc='upper right',ncol = 2)
plt.errorbar(Waves,Avi_b, yerr = err, errorevery=15, capsize = 3, ecolor= 'm', fmt = 'm',ls='-.') 
plt.errorbar(Waves,Avi3_b, yerr = err, errorevery=15, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Transmission Efficiency')
plt.ylim(82,88) 
plt.xlim(500,600)
#plt.ylim(1e-06,1e02)
plt.title('EJ260-1X1P-N1 Reference Measurements: Side B')

plt.subplot(223)
#plt.plot([], [], ' ', label="Repaired Febuary 2019")
plt.plot(Waves, Kak_c,'g',label='March 2017')
plt.plot(Waves, Avi3_c,'b',label='April 2018')
plt.plot(Waves, Avi2_c,'r',label='June 2018')
plt.plot(Waves, Avi_c, 'm',linestyle='dashed', label='February 2019 (After repair)')
plt.legend(loc='upper right',ncol = 2)
plt.errorbar(Waves,Avi_c, yerr = err, errorevery=15, capsize = 3, ecolor= 'm', fmt = 'm',ls='-.') 
plt.errorbar(Waves,Avi3_c, yerr = err, errorevery=15, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Transmission Efficiency')
plt.ylim(84,90) 
plt.xlim(500,600)
#plt.ylim(1e-06,1e02)
plt.title('EJ260-1X1P-N1 Reference Measurements: Side C')

plt.subplot(224)
#plt.plot([], [], ' ', label="Repaired Febuary 2019")
plt.plot(Waves, Kak_d,'g',label='March 2017')
plt.plot(Waves, Avi3_d,'b',label='April 2018')
plt.plot(Waves, Avi2_d,'r',label='June 2018')
plt.plot(Waves, Avi_d, 'm',linestyle='dashed', label='February 2019 (After repair)')
plt.legend(loc='upper right',ncol = 2)
plt.errorbar(Waves,Avi_d, yerr = err, errorevery=15, capsize = 3, ecolor= 'm', fmt = 'm',ls='-.') 
plt.errorbar(Waves,Avi3_d, yerr = err, errorevery=15, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Transmission Efficiency')
plt.ylim(82,88) 
plt.xlim(500,600)
#plt.ylim(1e-06,1e02)
plt.title('EJ260-1X1P-N1 Reference Measurements: Side D')

plt.show()
