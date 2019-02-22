import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 20})



#Reads in file
df       = pd.read_csv("Absorption_Unir_Samples.csv", sep=",")
Waves    = df.Wavelength
#Mu_eff   = df.MuEffective
Andres_1 = df.T_andres_1
Andres_2 = df.T_andres_2
Andres2_1 = df.T_andres2_1
Andres2_2 = df.T_andres2_2
Andres3_1 = df.T_andres3_1
Andres3_2 = df.T_andres3_2
Andres4_1 = df.T_andres4_1
Andres4_2 = df.T_andres4_2
Kak_1    = df.T_kak_1
Kak_2    = df.T_kak_2
Kak2_1   = df.T_kak2_1
Kak2_2   = df.T_kak2_2
Kak3_1   = df.T_kak3_1
Kak3_2   = df.T_kak3_2
Avi_1    = df.T_avi_1
Avi_2    = df.T_avi_2
Avi2_1    = df.T_avi2_1
Avi2_2    = df.T_avi2_2
Avi3_1    = df.T_avi3_1
Avi3_2    = df.T_avi3_2

Andres1 = np.mean( np.array([ Andres_1, Andres_2 ]), axis=0 ) # set V1, 0 days aft
Andres2 = np.mean( np.array([ Andres2_1, Andres2_2 ]), axis=0 )# set V3, 14 days aft
Andres3 = np.mean( np.array([ Andres3_1, Andres3_2 ]), axis=0 ) #set V3, 28 days aft.
Andres4 = np.mean( np.array([ Andres4_1, Andres4_2 ]), axis=0 )# set V3, 159 days aft.
Kak1   = np.mean( np.array([ Kak_1, Kak_2 ]), axis=0 ) #V1, 14 days aft
Kak2   = np.mean( np.array([ Kak2_1, Kak2_2 ]), axis=0 )#V1, 28 days
Kak3   = np.mean( np.array([ Kak3_1, Kak3_2 ]), axis=0 )#V3, 2 days
Avi1   = np.mean( np.array([ Avi_1, Avi_2 ]), axis=0 )#V1, 468
Avi2   = np.mean( np.array([ Avi2_1, Avi2_2 ]), axis=0 )#V3, 154
Avi3   = np.mean( np.array([ Avi3_1, Avi3_2 ]), axis=0 )#V3, 410

stdevT = [0]*len(Waves)
stdV1  = [0]*len(Waves)
stdV3  = [0]*len(Waves)
for i in range(len(Waves)):
    pointV1 = []
    pointV3 = []
    pointV1.append(Andres1[i])
    pointV3.append(Andres2[i])
    pointV3.append(Andres3[i])
    pointV3.append(Andres4[i])
    pointV1.append(Kak1[i])
    pointV1.append(Kak2[i])
    pointV3.append(Kak3[i])
    pointV1.append(Avi1[i])
    pointV3.append(Avi2[i])
    pointV3.append(Avi3[i])
    point = pointV1 + pointV3
    stdevT[i] = np.std(point)
    stdV1[i]  = np.std(pointV1)
    stdV3[i]  = np.std(pointV3)

#Mu = list(data.Mu)
#E  = list(data.E)

#Muu = np.asarray(Mu)

#def E_fit(m):
#    return np.exp(-0.1037-10.03*m)

plt.figure(1)
#plt.plot(Waves,Mu_eff)
plt.subplot(211)
plt.plot(Waves, Andres1,'g',label='Andres (set V1)')
plt.plot(Waves, Andres2,'g', linestyle='--', label='Andres (set V3) x 3')
plt.plot(Waves, Andres3,'g', linestyle='--')
plt.plot(Waves, Andres4,'g', linestyle='-.')
plt.plot(Waves, Kak1,'r', label='Kak (set V1) x 2')
plt.plot(Waves, Kak2,'r')
plt.plot(Waves, Kak3,'r', linestyle='--', label='Kak (set V3)')
plt.plot(Waves, Avi1,'b', label='Avi (set V1)')
plt.plot(Waves, Avi2,'b', linestyle='--', label='Avi (set V3) x 2')
plt.plot(Waves, Avi3,'b', linestyle='--')
plt.ylim(86,91)
plt.xlim(400,600)
#plt.plot(Muu, E,'b.', label='Simulated Efficiency')
#plt.plot(Muu,E_fit(Muu),'r-',dashes=[6,2], label='$e^{(-0.1037-10.03)\mu}$')
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Transmission Efficiency (%)')
plt.legend(loc='lower right', ncol = 3)
plt.title('Estimation of Systematic Uncertainty in Absorption Measurements \n(Data from set V1 and V3: 10 mm Unirradiated Sample)')


plt.subplot(212)
plt.plot(Waves, stdevT,'c',label='General Standard Deviation')
#plt.plot(Waves, stdV1,'m',label='set V1 Standard Deviation')
#plt.plot(Waves, stdV3,'y',label='set V3 Standard Deviation')
#plt.plot(Waves, Kak1,'g',label='Kak 3/16/17')
#plt.plot(Waves, Kak2,'r',label='Kak 3/30/17')
#plt.plot(Waves, Avi,'b',label='Avi 6/14/18')
plt.xlabel('Wavelength($nm$)')
plt.ylabel('Standard Deviation in Transmission Efficiency (%)')
plt.legend(loc='upper right')
plt.xlim(400,600)
#plt.ylim(85,91)
plt.show()
