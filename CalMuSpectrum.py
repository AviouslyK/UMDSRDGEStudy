#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#This program will return a MuEffective vs. Wavelength Spectrum
#The Efficiency from the Simulation (calculated witha a fit function) is compared
#to the Transmission percentage of data to return a Mueff vs Wavelength spectrum

plt.rcParams.update({'font.size': 22})

#Read in DataSet
df        = pd.read_csv("LDR_irr_4data.csv", sep=",")
Waves     = df.Waves
#Kak_a     = df.T_K_a
#Kak_c     = df.T_K_c # still temporary damage
#Andres_a  = df.T_A_a
#Andres_c  = df.T_A_c
Andres2_a = df.T_A2_a
Andres2_c = df.T_A2_c
Avi_a     = df.T_AV_a
Avi_c     = df.T_AV_c
Andres3_a = df.T_A3_a
Andres3_c = df.T_A3_c
Avi2_a     = df.T_AV2_a
Avi2_c     = df.T_AV2_c

#Kak   = np.mean( np.array([ Kak_a, Kak_c ]), axis=0 )
#Andres = np.mean( np.array([ Andres_a, Andres_c ]), axis=0 )
Andres2 = np.mean( np.array([ Andres2_a, Andres2_c ]), axis=0 )
Andres3 = np.mean( np.array([ Andres3_a, Andres3_c ]), axis=0 )
Avi   = np.mean( np.array([ Avi_a, Avi_c ]), axis=0 )
Avi2   = np.mean( np.array([ Avi2_a, Avi2_c ]), axis=0 )

# Plus/Minus one sigma
#Kak = Kak - 0.7
#Andres = Andres - 0.7
Andres2 = Andres2 + 0.7
Andres3 = Andres3 + 0.7
Avi = Avi + 0.7
Avi2 = Avi2 + 0.7

TransE = np.mean(np.array([Andres2, Andres3, Avi, Avi2]), axis=0)

#don't want E > 100 or < 0 from the +- sigma systematic error curves
TransE = TransE.clip(0,100) 

L = len(Waves)
MuResults  = [None]*L;
start    = 0.00001
stop     = 0.00005
total    = 100000
step     = (stop-start)/(total)
Diff     = [None]*total;
Results = [None]*total;

def Eff10(x):
    return 100 * np.exp(-0.1037-10.03*(x))
def Eff8(x):
    return 100 * np.exp(-0.1046-8.0077*(x))
def Eff6(x):
    return 100 * np.exp(-0.10241-6.029*(x))
def Eff4(x):
    return 100 * np.exp(-0.1019-4.0212*(x))


for i in range (len(Waves)):

    k = 0;
    E_Meas = TransE[i]
    for mu in np.arange(start,stop,step):
        Diff[k]  = abs(E_Meas - Eff4(mu));

        MuValue = k*step+start;
        Results[k] = MuValue;
        k = k + 1;
    mink      = Diff.index(min(Diff))
    MuResults[i] = Results[mink];
    if Diff[mink] > (E_Meas*0.0001): #comes from machine error of 0.01% (and ignored for very low values of efficiency) 
        MuResults[i] = 100; #so a quick glance shows if there was a bad match 


f = open('Mu_4_819_p_corrected.txt','w')

print>>f, 'Wavelength,MuEffective'
for w,mr in zip(Waves,MuResults):
    print>>f, "%.7f,%.7f" % (w, mr)

f.close()

