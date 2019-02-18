#!/usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#This program will return a MuEffective vs. Wavelength Spectrum
#The Efficiency from the Simulation (calculated witha a fit function) is compared
#to the Transmission percentage of data to return a Mueff vs Wavelength spectrum

plt.rcParams.update({'font.size': 22})

#Read in DataSet
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

TransE = np.mean(np.array([Andres, Kak1, Kak2, Avi]), axis=0)
L = len(Waves)
MuResults  = [None]*L;
start    = 0.0003
stop     = 0.1
total    = 4000000
step     = (stop-start)/total
minimum  = 100;
Diff     = [None]*total;
Results = [None]*total;

for i in range (len(Waves)):

    k = 0;

    for mu in np.arange(start,stop,step):
         #10 mm fit function
        Eff     = 100 * np.exp(-0.1037-10.03*(mu));
        Diff[k]  = abs(TransE[i] - Eff);

        #6 mm fit function
        #Eff   = 100 * np.exp(-0.10241-6.029*(i))
        #Diff[k]  = abs(TranData6[j] - Eff);

        #4 mm fit function
        #Eff   = 100 * np.exp(-0.1019-4.0212*(i))
        #Diff[k]  = abs(TranData4[j] - Eff);

        MuValue = k*step+start;
        Results[k] = MuValue;
        k = k + 1;
    mink      = Diff.index(min(Diff))
    MuResults[i] = Results[mink];
    if Diff[mink] < 0.0001:
        MuResults[i] = 100;#so a quick glance shows if there was a bad match 


f = open('Muspec_10mm_LDR_V2.txt','w')

print>>f, 'Wavelength,MuEffective'
for w,mr in zip(Waves,MuResults):
    print>>f, "%.7f,%.7f" % (w, mr)

f.close()
