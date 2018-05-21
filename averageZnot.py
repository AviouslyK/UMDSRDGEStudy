import numpy

#program to calculate iterations of Znot and Mu2 for each wavelength

# NUMBER 1
#Waves   = [350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 
#           420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 
#           490, 495, 500]

# NUMBER 2
#Waves    = [380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445] 

# NUMBER 3
#Waves    = [350, 355, 360, 365, 370, 375, 380, 385, 390, 393, 395, 396, 397, 398, 
#            399, 400, 401, 402, 403, 404, 405, 406, 407, 410, 415, 420, 425, 430, 
#            435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 
#            505, 510, 515, 520, 525, 530]             

Waves     =[410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 
            480, 485, 490, 495, 500] 
#Mu1s from Set V3
#a        = [1.746, 1.594, 1.22, 0.718, 0.315, 0.108, 0.04, 0.024, 0.018, 0.015, 
#           0.013, 0.011, 0.01, 0.009, 0.008] 



################################ Set V1 ######################################

#6mm and 10mm MuEffective values for each wavelength
#MuE3
#b        = [1.1610785, 1.0720943, 0.8165934, 0.4803388, 0.2118853, 0.0738176, 
#            0.0287586, 0.0177433, 0.014333, 0.0122392, 0.0109456, 0.0098272, 
#            0.0090199, 0.0082186] 
#MuE1
#c        = [0.7128232, 0.7102459, 0.6817807, 0.4620325, 0.2040897, 0.068311, 
#            0.0239382, 0.0131662, 0.0098934, 0.0080284, 0.0067998, 0.0059499, 
#            0.0052333, 0.0046555] 

##############################################################################


#4 mm mueffective values for each  wavelength
#MuE4
#a       = [1.78837, 1.76991, 1.77515, 1.77419, 1.77252, 1.77515, 1.74603,
#           1.59420, 1.21951, 0.91852, 0.71836, 0.62381, 0.53662, 0.45450, 
#           0.38012, 0.31500, 0.25916, 0.20958, 0.16910, 0.13522, 0.10846, 
#           0.08669, 0.07012, 0.04044, 0.02381, 0.01850, 0.01500, 0.01274, 
#           0.01121, 0.01004, 0.00885, 0.00789, 0.00722, 0.00637, 0.00562, 
#           0.00515, 0.00482, 0.00442, 0.00383, 0.00361, 0.00326, 0.00282, 
#           0.00268, 0.00239, 0.00216, 0.00200, 0.00186, 0.00162]

#MuE4 for waves NUMBER 3
#a      = [1.788370, 1.7699100, 1.775150, 1.7741900, 1.7725200, 1.7751500, 1.74603000, 
#          1.594200, 1.2195100, 0.918518, 0.7183600, 0.6238070, 0.5366160, 0.45450400, 
#          0.380117, 0.3150030, 0.259155, 0.2095760, 0.1691030, 0.1352170, 0.10846000, 
#          0.086686, 0.0701190, 0.040436, 0.0238070, 0.0185000, 0.0149970, 0.01274500, 
#          0.011213, 0.0100360, 0.008846, 0.0078910, 0.0072230, 0.0063690, 0.00562025,
#          0.005151, 0.0048156, 0.004415, 0.0038289, 0.0036098, 0.0032584, 0.002822, 
#          0.0026763, 0.002388, 0.0021583, 0.00200397, 0.00185635, 0.0016179]
#MuE4 from python script
#a      = [1.7797904, 1.7656896, 1.7696128, 1.7680112, 1.7665264, 1.7696, 
#          1.741416, 1.6035952, 1.2185968, 0.917056, 0.7174416, 0.6226864, 
#          0.5351504, 0.4538304, 0.3808432, 0.3154544, 0.2587616, 0.210032, 
#          0.1696656, 0.1360352, 0.1092614, 0.0877509, 0.0713063, 0.0417182, 
#          0.0251847, 0.0198121, 0.0163027, 0.0140263, 0.0124507, 0.0112945, 
#          0.010107, 0.0091719, 0.0084832, 0.007637, 0.0068645, 0.0063814, 
#          0.0060377, 0.0056443, 0.0050479, 0.0048375, 0.004506, 0.0040604, 
#         0.0039327, 0.0036304, 0.0033979, 0.0032411, 0.0030768, 0.0028384]

# a from 410 - 500 nm

a      = [0.04165070, 0.02503760, 0.01973180, 0.01619190, 0.01393150, 0.0124136, 
          0.01128400, 0.01006360, 0.00911752, 0.00840986, 0.00754227, 0.00679159, 
          0.00632955, 0.00599585, 0.00560205, 0.00502454, 0.00483332, 0.00449612, 
          0.00405594]


# 6 mm

#MuE3s
#b       = [1.19009, 1.17853, 1.19590, 1.18628, 1.19094, 1.19174, 1.19163, 
#           1.15872, 0.98492, 0.76041, 0.60098, 0.52316, 0.44934, 0.38198,
#           0.32017, 0.26492, 0.21749, 0.17736, 0.14317, 0.11497, 0.09243,
#           0.07445, 0.06037, 0.03532, 0.02104, 0.01612, 0.01309, 0.01093,
#           0.00947, 0.00830, 0.00723, 0.00629, 0.00556, 0.00484, 0.00409, 
#           0.00365, 0.00335, 0.00289, 0.00245, 0.00214, 0.00175, 0.00142,
#           0.00123, 0.00095, 0.00070, 0.00056, 0.00036, 0.00016]

#MuE3
# 6 mm from Python Script
b    = [0.0366739, 0.0223522, 0.0175271, 0.0144516, 0.0122924, 0.0108411, 
        0.0096307, 0.0085361, 0.0076291, 0.0069036, 0.0061815, 0.0054224, 
        0.004971, 0.0046588, 0.0041977, 0.0037511, 0.0034574, 0.0030691, 
        0.0027372]

#MuE1s
#c       = [0.72051, 0.71382, 0.71334, 0.71556, 0.71628, 0.71916, 0.71628, 
#           0.71502, 0.69708, 0.61230, 0.49971, 0.43698, 0.37726, 0.32051, 
#           0.26911, 0.22290, 0.18299, 0.14840, 0.11959, 0.09562, 0.07652, 
#           0.06130, 0.04950, 0.02832, 0.01619, 0.01221, 0.00986, 0.00828, 
#           0.00713, 0.00625, 0.00549, 0.00480, 0.00419, 0.00353, 0.00309, 
#           0.00272, 0.00247, 0.00215, 0.00185, 0.00165, 0.00144, 0.00126, 
#           0.00112, 0.00099, 0.00087, 0.00077, 0.00066, 0.00054]

# 10 mm from Python Script
#MuE1s
c     = [0.0282258, 0.0160772, 0.0120908, 0.0097304, 
         0.0081497, 0.0070059, 0.0061152, 0.0053619, 
         0.0046693, 0.0040584, 0.0033999, 0.0029544, 
         0.0025852, 0.0023379, 0.0020139, 0.0017133, 
         0.0015094, 0.001307, 0.0011205]



#from simulation (not equations)
#0.69643, 0.69791, 0.69643, 0.69272, 0.69768, 0.70000, 0.70000,
#           0.70000, 0.69930, 0.69272, 0.66102, 0.60937, 0.54379, 0.46941,
#           0.39484, 0.32608, 0.26449, 0.21056, 0.16525, 0.12785, 0.09814,
#           0.07427, 0.05607, 0.02389, 0.00765, 0.00399, 0.00265, 0.00202,
#           0.00169, 0.00161, 0.00161, 0.00173, 0.00176, 0.00172, 0.00171,
#           0.00176, 0.00172, 0.00159, 0.00142, 0.00129, 0.00115, 0.00098,
#           0.00092, 0.00082, 0.00075, 0.00072, 0.00071, 0.00070

# Mu2 Iteration 1 (410-500 nm)
#Mu2s   = [0.019465, 0.011505, 0.00836, 0.006825, 0.005385, 0.004345, 
#          0.00327, 0.002725, 0.002085, 0.00143, 0.00105, 0.000555, 
#          0.0002, 0, 0, 0, 0, 0, 0]

t1 = 10;
t2 = 8;
t3 = 6;
t4 = 4;

ZnotsIT0  = [2.427889359, 2.561517235, 2.581265491, 2.614503112, 2.590083237, 2.577303884, 2.525007063, 
            2.515745535, 2.497603489, 2.475734576, 2.509029113, 2.455170914, 2.443449109, 2.438159203, 
            2.386197251, 2.400069724, 2.339126982, 2.265970197, 2.261966723]
     
Mu2sIT0   = [0.01555365, 0.0066647, 0.00393635, 0.0026486, 0.00193565, 0.0012531, 0.00084195, 0.0006006, 0.0002296, 
             0, 0, 0, 0, 0, 0, 0, 0, 0, 
             0]

#ZnotsB    = [None]*19;
#ZnotsC    = [None]*19;
#Mu1s      = [None]*19;
#Mu2sC    = [None]*19;
#Mu2sB    = [None]*19;
Mu2sIT1   = [None]*19;
Mu2sIT2   = [None]*19;
Mu2sIT3   = [None]*19;
Mu2sIT4   = [None]*19;
Mu2sIT5   = [None]*19;
Mu2sIT6   = [None]*19;
Mu2sIT7   = [None]*19;
Mu2sIT8   = [None]*19;
Mu2sIT9   = [None]*19;
Mu2sIT10  = [None]*19;
Mu2sIT11  = [None]*19;
ZnotsIT1  = [None]*19;
ZnotsIT2  = [None]*19;
ZnotsIT3  = [None]*19;
ZnotsIT4  = [None]*19;
ZnotsIT5  = [None]*19;
ZnotsIT6  = [None]*19;
ZnotsIT7  = [None]*19;
ZnotsIT8  = [None]*19;
ZnotsIT9  = [None]*19;
ZnotsIT10 = [None]*19;
ZnotsIT11 = [None]*19;


Iterations = list(range(12));
#loop over iteration
for j in range (len(Iterations)):

    for i in range(len(Waves)):
            
        if j == 0:
            Znot = numpy.mean(ZnotsIT0);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT1[i] = 0;
            #else:
            Mu2sIT1[i] = Mu2;
        
    
        if j == 1:
            Znot = numpy.mean(ZnotsIT1);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT2[i] = 0;
            #else:
            Mu2sIT2[i] = Mu2;
        
            
        if j == 2:
            Znot = numpy.mean(ZnotsIT2);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT3[i] = 0;
            #else:
            Mu2sIT3[i] = Mu2;
        

        if j == 3:
            Znot = numpy.mean(ZnotsIT3);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT4[i] = 0;
            #else:
            Mu2sIT4[i] = Mu2;
        

        if j == 4:
            Znot = numpy.mean(ZnotsIT4);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT5[i] = 0;
            #else:
            Mu2sIT5[i] = Mu2;
        

        if j == 5:
            Znot = numpy.mean(ZnotsIT5);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT6[i] = 0;
            #else:
            Mu2sIT6[i] = Mu2;
        

        if j == 6:
            Znot = numpy.mean(ZnotsIT6);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT7[i] = 0;
            #else:
            Mu2sIT7[i] = Mu2;
        

        if j == 7:
            Znot = numpy.mean(ZnotsIT7);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT8[i] = 0;
            #else:
            Mu2sIT8[i] = Mu2;
        

        if j == 8:
            Znot = numpy.mean(ZnotsIT8);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT9[i] = 0;
            #else:
            Mu2sIT9[i] = Mu2;
        

        if j == 9:
            Znot = numpy.mean(ZnotsIT9);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT10[i] = 0;
            #else:
            Mu2sIT10[i] = Mu2;
        
        if j == 10:
            Znot = numpy.mean(ZnotsIT10);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT11[i] = Mu2;
        
    for i in range(len(Waves)):
            
    #Mu2s[i]   = (t3*b[i]-2*Znot*a[i])/(t3-2*Znot);
    #correct equations
 #   Mu2      = (t3*b[i]-t1*c[i])/(t3-t1);        
 #   Mu2s[i]  = Mu2;

        if j == 0:
            ZnotB = (t3*(b[i]-Mu2sIT0[i]))/(2*(a[i]-Mu2sIT0[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT0[i]))/(2*(a[i]-Mu2sIT0[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT1[i] = ZnotC;

        if j == 1:
            ZnotB = (t3*(b[i]-Mu2sIT1[i]))/(2*(a[i]-Mu2sIT1[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT1[i]))/(2*(a[i]-Mu2sIT1[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT2[i] = Znot;


        if j == 2:
            ZnotB = (t3*(b[i]-Mu2sIT2[i]))/(2*(a[i]-Mu2sIT2[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT2[i]))/(2*(a[i]-Mu2sIT2[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT3[i] = Znot;

        if j == 3:
            ZnotB = (t3*(b[i]-Mu2sIT3[i]))/(2*(a[i]-Mu2sIT3[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT3[i]))/(2*(a[i]-Mu2sIT3[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT4[i] = Znot;


        if j == 4:
            ZnotB = (t3*(b[i]-Mu2sIT4[i]))/(2*(a[i]-Mu2sIT4[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT4[i]))/(2*(a[i]-Mu2sIT4[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT5[i] = Znot;

    

        if j == 5:
            ZnotB = (t3*(b[i]-Mu2sIT5[i]))/(2*(a[i]-Mu2sIT5[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT5[i]))/(2*(a[i]-Mu2sIT5[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT6[i] = Znot;

            
        if j == 6:
            ZnotB = (t3*(b[i]-Mu2sIT6[i]))/(2*(a[i]-Mu2sIT6[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT6[i]))/(2*(a[i]-Mu2sIT6[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT7[i] = Znot;


        if j == 7:
            ZnotB = (t3*(b[i]-Mu2sIT7[i]))/(2*(a[i]-Mu2sIT7[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT7[i]))/(2*(a[i]-Mu2sIT7[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT8[i] = Znot;


        if j == 8:
            ZnotB = (t3*(b[i]-Mu2sIT8[i]))/(2*(a[i]-Mu2sIT8[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT8[i]))/(2*(a[i]-Mu2sIT8[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT9[i] = Znot;


        if j == 9:
            ZnotB = (t3*(b[i]-Mu2sIT9[i]))/(2*(a[i]-Mu2sIT9[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT9[i]))/(2*(a[i]-Mu2sIT9[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT10[i] = Znot;


        if j == 10:
            ZnotB = (t3*(b[i]-Mu2sIT10[i]))/(2*(a[i]-Mu2sIT10[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT10[i]))/(2*(a[i]-Mu2sIT10[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT11[i] = Znot;

#############old equations##############
  #  Mu1 = a[i];
  #  Mu1s[i] = Mu1;

   # Mu2 = (b[i]*t3 - a[i]*t1)/(t3-t1);
   # Mu2s[i] = Mu2;

   # Znot = 0.5*t3*(b[i]-Mu2)/(c[i]-Mu2);
   # Znots[i] = Znot;




#print to a file
#f1=open('./testfile', 'w+')

#ZnotAvg = sum(Znots)/len(Znots);
#Mu1Avg  = sum(Mu1s)/len(Mu1s);
#Mu2Avg  = sum(Mu2s)/len(Mu2s);

#print parameter values
print 'Wavelength \t\tMu2sIT0 \t\tMu2sIT1 \t\tMu2sIT2 \t\tMu2sIT3 \t\tMu2sIT4 \t\tMu2sIT5 \t\tMu2sIT6 \t\tMu2sIT7 \t\tMu2sIT8 \t\tMu2sIT9 \t\tMu2sIT10 \t\tMu2sIT11 \t\tZnotsIT0 \t\tZnotsIT1 \t\tZnotsIT2 \t\tZnotsIT3 \t\tZnotsIT4 \t\tZnotsIT5 \t\tZnotsIT6 \t\tZnotsIT7 \t\tZnotsIT8 \t\tZnotsIT9 \t\tZnotsIT10 \t\tZnotsIT11'
 
for w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11 in zip(Waves,Mu2sIT0,Mu2sIT1,Mu2sIT2,Mu2sIT3,Mu2sIT4,Mu2sIT5,Mu2sIT6,Mu2sIT7,Mu2sIT8,Mu2sIT9,Mu2sIT10,Mu2sIT11,ZnotsIT0,ZnotsIT1,ZnotsIT2,ZnotsIT3,ZnotsIT4,ZnotsIT5,ZnotsIT6,ZnotsIT7,ZnotsIT8,ZnotsIT9,ZnotsIT10,ZnotsIT11):
    print "%.3f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f" % (w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11)
#print Znot values
#print 'Wavelength \t\tZnot \t\tMu1 \t\tMu2' 
#for w,z,m1,m2 in zip(Waves,Znots,a,Mu2s):
#    print "%.3f \t\t%.3f \t\t%.3f \t\t%.3f" % (w, z, m1, m2)
