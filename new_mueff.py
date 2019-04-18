import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Program to calculate an effective Mu for any dose rate. This spectra can than be input into teh EJ200
#material in GEANT to simulate an absorption measurement

#Read in solved u1, u2, and z parameter values, based off of set V3 (8.19 krad/h)
# m = minus one sigma, p = plus one sigma.
df    = pd.read_csv("LDR_params_withbounds_corrected.csv", sep=",")
Wave  = df.Waves
z_m   = df.zm
z_p   = df.zp
u1_m  = df.u1m
u1_p  = df.u1p
u2_m  = df.u2m
u2_p  = df.u2p

L = len(Wave)
zm = z_m[0] # can take z at any wavelength, it's a constant
zp = z_p[0]
R = 8.19 * 1e3 # Dose rate in rad/hr

# Calculate the Dose Constant
Gm = R * zm**2 
Gp = R * zp**2 

R_new = 0.3 * 1e3 # We will eventually compare to set GV2 which was irradiated at 0.3 krad/hr 

#Calculate the new z
zm_new = np.sqrt(Gm/R_new)
zp_new = np.sqrt(Gp/R_new)

# the u1 and u2 spectra remain the same, regardless of dose rate - they are an inherent property of the material

#Now calculate new U_eff spectra, which will be input into the Geant4 source code under the EJ200 material
ueff10_m = np.zeros(L)
ueff6_m = np.zeros(L)
ueff4_m = np.zeros(L)

ueff10_p = np.zeros(L)
ueff6_p = np.zeros(L)
ueff4_p = np.zeros(L)

t10 = 10
t8 = 8
t6 = 6
t4 = 4
for i in range(L):
    ueff10_m[i] = u2_m[i] + 2*(zm_new/t10)*(u1_m[i]-u2_m[i])
    ueff6_m[i] = u2_m[i] + 2*(zm_new/t6)*(u1_m[i]-u2_m[i])
    ueff4_m[i] = u2_m[i] + 2*(zm_new/t4)*(u1_m[i]-u2_m[i])

    ueff10_p[i] = u2_p[i] + 2*(zp_new/t10)*(u1_p[i]-u2_p[i])
    ueff6_p[i] = u2_p[i] + 2*(zp_new/t6)*(u1_p[i]-u2_p[i])
    ueff4_p[i] = u2_p[i] + 2*(zp_new/t4)*(u1_p[i]-u2_p[i])
f = open('new_muspec_withbounds_corrected.txt','w')

print>>f, 'Wavelength,ueff10_m,ueff6_m,ueff4_m,ueff10_p,ueff6_p,ueff4_p'
for w,u10m,u6m,u4m,u10p,u6p,u4p in zip(Wave,ueff10_m,ueff6_m,ueff4_m,ueff10_p,ueff6_p,ueff4_p):
        print>>f, "%.7f,%.7f,%.7f,%.7f,%.7f,%.7f,%.7f" % (w,u10m,u6m,u4m,u10p,u6p,u4p)

f.close()
