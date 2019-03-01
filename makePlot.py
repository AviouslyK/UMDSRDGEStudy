import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 18})



#Reads in file
df       = pd.read_csv("training_ej260.csv", sep=",")
Waves    = df.Waves
#Mu_eff   = df.Mu_eff

# All after repair
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

#before repair - 6/14/18
Avi2_a    = df.Avi2_a
Avi2_b    = df.Avi2_b
Avi2_c    = df.Avi2_c
Avi2_d    = df.Avi2_d



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
 
stdeva = [0]*len(Waves)
stdevb = [0]*len(Waves)
stdevc = [0]*len(Waves)
stdevd = [0]*len(Waves)

stdeva_1day = [0]*len(Waves)
stdevb_1day = [0]*len(Waves)
stdevc_1day = [0]*len(Waves)
stdevd_1day = [0]*len(Waves)

#stdV1  = [0]*len(Waves)
#stdV3  = [0]*len(Waves)
for i in range(len(Waves)):
    pointa = []
    pointa_1day = []
    pointb = []
    pointb_1day = []
    pointc = []
    pointc_1day = [] 
    pointd = []
    pointd_1day = []
#    pointV3 = []
    pointa.append(Avi_a[i])
    pointa.append(Duan_a[i])
    pointa.append(Tim_a[i])
    pointa_1day.append(Avi_a[i])
    pointa_1day.append(Duan_a[i])
    pointa_1day.append(Tim_a[i])
    pointa_1day.append(Avi2_a[i])

    pointb.append(Avi_b[i])
    pointb.append(Duan_b[i])
    pointb.append(Tim_b[i])
    pointb_1day.append(Avi_b[i])
    pointb_1day.append(Duan_b[i])
    pointb_1day.append(Tim_b[i])
    pointb_1day.append(Avi2_b[i])

    pointc.append(Avi_c[i])
    pointc.append(Duan_c[i])
    pointc.append(Tim_c[i])
    pointc_1day.append(Avi_c[i])
    pointc_1day.append(Duan_c[i])
    pointc_1day.append(Tim_c[i])
    pointc_1day.append(Avi2_c[i])

    pointd.append(Avi_d[i])
    pointd.append(Duan_d[i])
    pointd.append(Tim_d[i])
    pointd_1day.append(Avi_d[i])
    pointd_1day.append(Duan_d[i])
    pointd_1day.append(Tim_d[i])
    pointd_1day.append(Avi2_d[i])

#    point = pointV1 + pointV3
    stdeva[i] = np.std(pointa)
    stdevb[i] = np.std(pointb)
    stdevc[i] = np.std(pointc)
    stdevd[i] = np.std(pointd)

    stdeva_1day[i] = np.std(pointa_1day)
    stdevb_1day[i] = np.std(pointb_1day)
    stdevc_1day[i] = np.std(pointc_1day)
    stdevd_1day[i] = np.std(pointd_1day)
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
#plt.subplot(121)
plt.plot(Waves, stdeva, 'g', label='Side A')
plt.plot(Waves, stdevb,'b',label='Side B')
plt.plot(Waves, stdevc,'r',label='Side C')
plt.plot(Waves, stdevd,'m', label='Side D')
plt.legend(loc='upper right', ncol=2)
#plt.errorbar(Waves,stdeva, yerr = err, errorevery=50, capsize = 3, ecolor= 'b', fmt = 'b') 
plt.xlabel('Wavelength ($nm$)')
plt.ylabel('Stdev in Transmission Efficiency (%)')
#plt.ylim(84,89) 
plt.xlim(400,600)
#plt.ylim(1e-06,1e02)
plt.title('Standard Deviation in Training Measurements')
plt.legend(loc ='upper right')
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
