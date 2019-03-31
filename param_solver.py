import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# calculates Oxygen penetration depth (z), and the two absorption coefficients (u1 and u2)

plt.rcParams.update({'font.size': 22})

#Read in Effective Absorption Coefficient (u_eff) DataSet
# m = minus one sigma, p = plus one sigma.
df       = pd.read_csv("Mu_eff.csv", sep=",")
Waves    = df.Wave
u_eff10m = df.Minus_Sigma10
u_eff10p = df.Plus_Sigma10
u_eff8m  = df.Minus_Sigma8
u_eff8p  = df.Plus_Sigma8
u_eff6m = df.Minus_Sigma6
u_eff6p = df.Plus_Sigma6
u_eff4m = df.Minus_Sigma4
u_eff4p = df.Plus_Sigma4

t10 = 10
t8  = 8
t6  = 6
t4  = 4

L = len(Waves)
N = 10 # iterations
u1_m = [None]*L
u1_p = [None]*L
u2_m = np.zeros((L,N))
u2_p = np.zeros((L,N))
z_m  = np.zeros((L,N))
z_p  = np.zeros((L,N))

#RUN ZEROTH ITERATION, U2 and Z0 are calculated independent of each other!
for i in range (L):
    # Calculate u1
    u1_m[i] = u_eff4m[i]
    u1_p[i] = u_eff4p[i]
    # Calculate u2
    u2_m[i,0] = (u_eff6m[i]*t6 - u_eff10m[i]*t10) / (t6 - t10)
    u2_p[i,0] = (u_eff6p[i]*t6 - u_eff10p[i]*t10) / (t6 - t10)

    # absorption coefficient cannot be negative
    if (u1_m[i] <= 0):
        u1_m[i] = 0
    if (u1_p[i] <= 0):
        u1_p[i] = 0
    if (u2_m[i,0] <= 0):
        u2_m[i,0] = 0
    if (u2_p[i,0] <= 0):
        u2_p[i,0] = 0

    # Calculate z
    z_p[i,0]  = (t6*t10*(u_eff6p[i]-u_eff10p[i])) / (2*(u_eff6p[i]*t6 - u_eff10p[i]*t10 + u_eff4p[i]*(t10-t6)))
    z_m[i,0]  = (t6*t10*(u_eff6m[i]-u_eff10m[i])) / (2*(u_eff6m[i]*t6 - u_eff10m[i]*t10 + u_eff4m[i]*(t10-t6)))


# Now iterate
for n in range(1,N): # start at first iteration
    zm = np.nanmean(z_m[:,n-1])#Znot should be constant as a function of wavelength
    zp = np.nanmean(z_p[:,n-1])
    for i in range (L):
        z_m[i,n-1] = zm
        z_p[i,n-1] = zp

        # Calculate u2 from z's last iteration
        u2_m[i,n] = ((t10*u_eff10m[i])-(2*z_m[i,n-1]*u_eff4m[i]))/(t10-(2*z_m[i,n-1]))
        u2_p[i,n] = ((t10*u_eff10p[i])-(2*z_p[i,n-1]*u_eff4p[i]))/(t10-(2*z_p[i,n-1]))

        # absorption coefficient cannot be negative
        if (u2_m[i,n] <= 0):
            u2_m[i,n] = 0
        if (u2_p[i,n] <= 0):
            u2_p[i,n] = 0
    
        #Calculate z from the current generation u2
        zma = (t6*(u_eff6m[i] - u2_m[i,n])) / (2*(u1_m[i]-u2_m[i,n]))
        zmb = (t10*(u_eff10m[i] - u2_m[i,n])) / (2*(u1_m[i]-u2_m[i,n]))
        zpa = (t6*(u_eff6p[i] - u2_p[i,n])) / (2*(u1_p[i]-u2_p[i,n]))
        zpb = (t10*(u_eff10p[i] - u2_p[i,n])) / (2*(u1_p[i]-u2_p[i,n]))

        z_m[i,n] = np.mean([zma,zmb])
        z_p[i,n] = np.mean([zpa,zpb])


#Calculate Differences between iterations
difzm = np.zeros(N)
difzp = np.zeros(N)
difu2m = np.zeros(N)
difu2p = np.zeros(N)

for n in range(1,N):
    for i in range(L):
        difzm[n] = difzm[n] + np.abs(z_m[i,n] - z_m[i,n-1])
        difzp[n] = difzp[n] + np.abs(z_p[i,n] - z_p[i,n-1])
        difu2m[n] = difu2m[n] + np.abs(u2_m[i,n] - u2_m[i,n-1])
        difu2p[n] = difu2p[n] + np.abs(u2_p[i,n] - u2_p[i,n-1])

Its = np.arange(N)    

plt.figure(1)
plt.subplot(221)
my_plot = plt.fill_between(Waves, u1_m, u1_p, alpha=0.3, label='$\mu_1$')
my_plot2 = plt.fill_between(Waves, u2_m[:,0], u2_p[:,0], alpha=0.9, label='$\mu_2$ zeroth iteration')
plt.setp(my_plot, facecolor='g')
plt.setp(my_plot2, facecolor='b')
plt.legend(loc='upper right')
plt.xlabel('Wavelength (nm)')
plt.ylim([-0.05,0.3])

plt.subplot(222)
my_plot3 = plt.fill_between(Waves, z_m[:,0], z_p[:,0], alpha=0.3, label='$z_0$ zeroth iteration')
plt.setp(my_plot3, facecolor='g')
#plt.plot(Waves,z_m,'g')
#plt.plot(Waves,z_p,'g')
my_plot4 = plt.fill_between(Waves, z_m[:,1], z_p[:,1], alpha=0.3, label='$z_0$ first iteration')
plt.setp(my_plot4, facecolor='r')
#plt.plot(Waves,z_m2,'r')
#plt.plot(Waves,z_p2,'r')
plt.xlabel('Wavelength (nm)')
plt.legend(loc='upper right')
plt.ylim([0,5])

my_plot7 = plt.fill_between(Waves, z_m[:,2], z_p[:,2], alpha=0.3, label='$z_0$ second iteration')
plt.setp(my_plot7, facecolor='c')
#plt.plot(Waves,z_m2,'r')
#plt.plot(Waves,z_p2,'r')
plt.xlabel('Wavelength (nm)')
plt.legend(loc='upper right')
plt.ylim([0,5])

my_plot8 = plt.fill_between(Waves, z_m[:,3], z_p[:,3], alpha=0.3, label='$z_0$ second iteration')
plt.setp(my_plot8, facecolor='m')
#plt.plot(Waves,z_m2,'r')
#plt.plot(Waves,z_p2,'r')
plt.xlabel('Wavelength (nm)')
plt.legend(loc='upper right')
plt.ylim([0,5])

plt.subplot(223)
my_plot5 = plt.fill_between(Its, difzm, difzp, alpha=0.3, label='$z_0$ difference between iterations')
plt.setp(my_plot5, facecolor='k')
plt.xlabel('Iteration')
plt.ylabel('Difference between iterations')
plt.legend(loc='upper right')

plt.subplot(224)
my_plot6 = plt.fill_between(Its, difu2m, difu2p, alpha=0.3, label='$\mu_2$ difference between iterations')
plt.setp(my_plot6, facecolor='k')
plt.xlabel('Iteration')
plt.ylabel('Difference between iterations')
plt.legend(loc='upper right')

plt.show()
