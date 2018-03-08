#!/usr/bin/python
import numpy as np


#This program will return a MuEffective vs. Wavelength Spectrum
#The Efficiency from the Simulation (calculated witha a fit function) is compared
#to the Transmission percentage of data to return a Mueff vs Wavelength spectrum


Waves      = [500, 495, 490, 485, 480, 475, 470, 465, 460, 455, 450, 445, 440, 435, 430, 425, 
              420, 415, 410, 405, 400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350];
                
TranData10 = [88.85736847, 88.67812347, 88.54241181, 88.37619782, 88.13978577, 87.98074723, 
              87.69673157, 87.54169083, 87.22632218, 86.80953217, 86.41916275, 85.92263413, 
              85.42676926, 84.81585312, 84.09698487, 83.06842423, 81.53116989, 78.90200806, 
              70.83247376, 45.41727639, 11.65778018, 0.880290389, 0.097448073, 0.073275082, 
              0.071407758, 0.070513714, 0.071400929, 0.069640268, 0.071769845, 0.071669124, 
              0.071280494];

TranData6  = [88.41542435, 88.25827408, 88.087883, 87.91617966, 87.71035385, 87.5097847, 
              87.32942963, 87.19142151, 86.947926, 86.57976914, 86.26733399, 85.90228272, 
              85.48829270, 85.07317734, 84.501480, 83.84502030, 82.79325104, 81.10833359, 
              75.89678955, 57.84192848, 25.161210, 4.986814499, 0.656730682, 0.140732259, 
              0.082300156, 0.075009748, 0.0738093, 0.072954465, 0.072235860, 0.068529855, 
              0.076690212];

MuResults  = [None]*31;

start = 0.0032
stop = 1.2
total = 500000000
step = (stop-start)/total
minimum = 100;

for j in range (len(Waves)):

    for i in np.arange(start,stop,step):
        #10 mm fit function
        #Eff1   = 100 * np.exp(-0.105095-10.0157*(i-step))
        #Eff2   = 100 * np.exp(-0.105095-10.0157*(i))
        
        #6 mm fit function
        Eff1   = 100 * np.exp(-0.10241-6.029*(i-step))
        Eff2   = 100 * np.exp(-0.10241-6.029*(i))
        
        Diff1  = abs(TranData6[j] - Eff1)
        Diff2  = abs(TranData6[j] - Eff2)

        if Diff2 < Diff1:
            minimum = i
            
    MuResults[j] = minimum


f = open('MUEFFECTIVEDATA.txt','w')

print>>f, 'Wavelength \t\tMuEffective'
for w,mr in zip(Waves,MuResults):
    print>>f, "%.7f \t\t%.7f" % (w, mr)

f.close()
