            import numpy

#program to calculate Znot and Mu2 Iterations for each wavelength


Waves     =[410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 
            480, 485, 490, 495, 500] 

# a from 410 - 500 nm

a      = [0.04165070, 0.02503760, 0.01973180, 0.01619190, 0.01393150, 0.0124136, 
          0.01128400, 0.01006360, 0.00911752, 0.00840986, 0.00754227, 0.00679159, 
          0.00632955, 0.00599585, 0.00560205, 0.00502454, 0.00483332, 0.00449612, 
          0.00405594]


#MuE3
# 6 mm from Python Script
b    = [0.0366739, 0.0223522, 0.0175271, 0.0144516, 0.0122924, 0.0108411, 
        0.0096307, 0.0085361, 0.0076291, 0.0069036, 0.0061815, 0.0054224, 
        0.004971, 0.0046588, 0.0041977, 0.0037511, 0.0034574, 0.0030691, 
        0.0027372]

# 10 mm from Python Script
#MuE1s
c     = [0.0282258, 0.0160772, 0.0120908, 0.0097304, 
         0.0081497, 0.0070059, 0.0061152, 0.0053619, 
         0.0046693, 0.0040584, 0.0033999, 0.0029544, 
         0.0025852, 0.0023379, 0.0020139, 0.0017133, 
         0.0015094, 0.001307, 0.0011205]



t1 = 10;
t2 = 8;
t3 = 6;
t4 = 4;

ZnotsIT0  = [2.427889359, 2.561517235, 2.581265491, 2.614503112, 2.590083237, 2.577303884, 2.525007063, 
            2.515745535, 2.497603489, 2.475734576, 2.509029113, 2.455170914, 2.443449109, 2.438159203, 
            2.386197251, 2.400069724, 2.339126982, 2.265970197, 2.261966723]
     
Mu2sIT0   = [0.01555365, 0.0066647, 0.00393635, 0.0026486, 0.00193565, 0.0012531, 0.00084195, 0.0006006, 0.0002296, 
             -0.0002094, -0.0007725, -0.0007476, -0.0009935, -0.00114345, -0.0012618, -0.0013434, -0.0014126,
             -0.00133615, -0.00130455]
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
Mu2sIT12   = [None]*19;
Mu2sIT13  = [None]*19;
Mu2sIT14  = [None]*19;
Mu2sIT15  = [None]*19;
Mu2sIT16  = [None]*19;
Mu2sIT17  = [None]*19;
Mu2sIT18  = [None]*19;
Mu2sIT19  = [None]*19;
Mu2sIT20  = [None]*19;
Mu2sIT20  = [None]*19;
Mu2sIT21  = [None]*19;
Mu2sIT22  = [None]*19;
Mu2sIT23  = [None]*19;
Mu2sIT24  = [None]*19;
Mu2sIT25  = [None]*19;
Mu2sIT26  = [None]*19;
Mu2sIT27  = [None]*19;
Mu2sIT28  = [None]*19;
Mu2sIT29  = [None]*19;
Mu2sIT30  = [None]*19;
Mu2sIT31  = [None]*19;
Mu2sIT32  = [None]*19;
Mu2sIT33  = [None]*19;

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
ZnotsIT12 = [None]*19;
ZnotsIT13 = [None]*19;
ZnotsIT14 = [None]*19;
ZnotsIT15 = [None]*19;
ZnotsIT16 = [None]*19;
ZnotsIT17 = [None]*19;
ZnotsIT18 = [None]*19;
ZnotsIT19 = [None]*19;
ZnotsIT20 = [None]*19;
ZnotsIT21 = [None]*19;
ZnotsIT22 = [None]*19;
ZnotsIT23 = [None]*19;
ZnotsIT24 = [None]*19;
ZnotsIT25 = [None]*19;
ZnotsIT26 = [None]*19;
ZnotsIT27 = [None]*19;
ZnotsIT28 = [None]*19;
ZnotsIT29 = [None]*19;
ZnotsIT30 = [None]*19;
ZnotsIT31 = [None]*19;
ZnotsIT32 = [None]*19;
ZnotsIT33 = [None]*19;

Iterations = list(range(34));
#loop over iterations
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
        
        if j == 11:
            Znot = numpy.mean(ZnotsIT11);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT12[i] = Mu2;
        
        if j == 12:
            Znot = numpy.mean(ZnotsIT12);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT13[i] = Mu2;
        
        if j == 13:
            Znot = numpy.mean(ZnotsIT13);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT14[i] = Mu2;
        
        if j == 14:
            Znot = numpy.mean(ZnotsIT14);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT15[i] = Mu2;
        
        if j == 15:
            Znot = numpy.mean(ZnotsIT15);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT16[i] = Mu2;
        
        if j == 16:
            Znot = numpy.mean(ZnotsIT16);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT17[i] = Mu2;
        
        if j == 17:
            Znot = numpy.mean(ZnotsIT17);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT18[i] = Mu2;
        
        if j == 18:
            Znot = numpy.mean(ZnotsIT18);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT19[i] = Mu2;
        
        if j == 19:
            Znot = numpy.mean(ZnotsIT19);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT20[i] = Mu2;
        
        if j == 20:
            Znot = numpy.mean(ZnotsIT20);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT21[i] = Mu2;
        
        if j == 21:
            Znot = numpy.mean(ZnotsIT21);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT22[i] = Mu2;
        
        if j == 22:
            Znot = numpy.mean(ZnotsIT22);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT23[i] = Mu2;
        
        if j == 23:
            Znot = numpy.mean(ZnotsIT23);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT24[i] = Mu2;
        
        if j == 24:
            Znot = numpy.mean(ZnotsIT24);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT25[i] = Mu2;
        
        if j == 25:
            Znot = numpy.mean(ZnotsIT25);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT26[i] = Mu2;
        
        if j == 26:
            Znot = numpy.mean(ZnotsIT26);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT27[i] = Mu2;
        
        if j == 27:
            Znot = numpy.mean(ZnotsIT27);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT28[i] = Mu2;
        
        if j == 28:
            Znot = numpy.mean(ZnotsIT28);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT29[i] = Mu2;
        
        if j == 29:
            Znot = numpy.mean(ZnotsIT29);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT30[i] = Mu2;
        
        if j == 30:
            Znot = numpy.mean(ZnotsIT30);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT31[i] = Mu2;
        
        if j == 31:
            Znot = numpy.mean(ZnotsIT31);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT32[i] = Mu2;
        
        if j == 32:
            Znot = numpy.mean(ZnotsIT32);
            Mu2c = ((t1*c[i])-(2*Znot*a[i]))/(t1-(2*Znot));

            Mu2b = ((t3*b[i])-(2*Znot*a[i]))/(t3-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT11[i] = 0;
            #else:
            Mu2sIT33[i] = Mu2;
                 
    for i in range(len(Waves)):

        if j == 0:
            ZnotB = (t3*(b[i]-Mu2sIT1[i]))/(2*(a[i]-Mu2sIT1[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT1[i]))/(2*(a[i]-Mu2sIT1[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT1[i] = Znot;

        if j == 1:
            ZnotB = (t3*(b[i]-Mu2sIT2[i]))/(2*(a[i]-Mu2sIT2[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT2[i]))/(2*(a[i]-Mu2sIT2[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT2[i] = Znot;


        if j == 2:
            ZnotB = (t3*(b[i]-Mu2sIT3[i]))/(2*(a[i]-Mu2sIT3[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT3[i]))/(2*(a[i]-Mu2sIT3[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT3[i] = Znot;

        if j == 3:
            ZnotB = (t3*(b[i]-Mu2sIT4[i]))/(2*(a[i]-Mu2sIT4[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT4[i]))/(2*(a[i]-Mu2sIT4[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT4[i] = Znot;


        if j == 4:
            ZnotB = (t3*(b[i]-Mu2sIT5[i]))/(2*(a[i]-Mu2sIT5[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT5[i]))/(2*(a[i]-Mu2sIT5[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT5[i] = Znot;

    

        if j == 5:
            ZnotB = (t3*(b[i]-Mu2sIT6[i]))/(2*(a[i]-Mu2sIT6[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT6[i]))/(2*(a[i]-Mu2sIT6[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT6[i] = Znot;

            
        if j == 6:
            ZnotB = (t3*(b[i]-Mu2sIT7[i]))/(2*(a[i]-Mu2sIT7[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT7[i]))/(2*(a[i]-Mu2sIT7[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT7[i] = Znot;


        if j == 7:
            ZnotB = (t3*(b[i]-Mu2sIT8[i]))/(2*(a[i]-Mu2sIT8[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT8[i]))/(2*(a[i]-Mu2sIT8[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT8[i] = Znot;


        if j == 8:
            ZnotB = (t3*(b[i]-Mu2sIT9[i]))/(2*(a[i]-Mu2sIT9[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT9[i]))/(2*(a[i]-Mu2sIT9[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT9[i] = Znot;


        if j == 9:
            ZnotB = (t3*(b[i]-Mu2sIT10[i]))/(2*(a[i]-Mu2sIT10[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT10[i]))/(2*(a[i]-Mu2sIT10[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT10[i] = Znot;


        if j == 10:
            ZnotB = (t3*(b[i]-Mu2sIT11[i]))/(2*(a[i]-Mu2sIT11[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT11[i]))/(2*(a[i]-Mu2sIT11[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT11[i] = Znot;
            
        if j == 11:
            ZnotB = (t3*(b[i]-Mu2sIT12[i]))/(2*(a[i]-Mu2sIT12[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT12[i]))/(2*(a[i]-Mu2sIT12[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT12[i] = ZnotC;

        if j == 12:
            ZnotB = (t3*(b[i]-Mu2sIT13[i]))/(2*(a[i]-Mu2sIT13[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT13[i]))/(2*(a[i]-Mu2sIT13[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT13[i] = Znot;


        if j == 13:
            ZnotB = (t3*(b[i]-Mu2sIT14[i]))/(2*(a[i]-Mu2sIT14[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT14[i]))/(2*(a[i]-Mu2sIT14[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT14[i] = Znot;

        if j == 14:
            ZnotB = (t3*(b[i]-Mu2sIT15[i]))/(2*(a[i]-Mu2sIT15[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT15[i]))/(2*(a[i]-Mu2sIT15[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT15[i] = Znot;


        if j == 15:
            ZnotB = (t3*(b[i]-Mu2sIT16[i]))/(2*(a[i]-Mu2sIT16[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT16[i]))/(2*(a[i]-Mu2sIT16[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT16[i] = Znot;

    

        if j == 16:
            ZnotB = (t3*(b[i]-Mu2sIT17[i]))/(2*(a[i]-Mu2sIT17[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT17[i]))/(2*(a[i]-Mu2sIT17[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT17[i] = Znot;

        if j == 17:
            ZnotB = (t3*(b[i]-Mu2sIT18[i]))/(2*(a[i]-Mu2sIT18[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT18[i]))/(2*(a[i]-Mu2sIT18[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT18[i] = Znot;


        if j == 18:
            ZnotB = (t3*(b[i]-Mu2sIT19[i]))/(2*(a[i]-Mu2sIT19[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT19[i]))/(2*(a[i]-Mu2sIT19[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT19[i] = Znot;


        if j == 19:
            ZnotB = (t3*(b[i]-Mu2sIT20[i]))/(2*(a[i]-Mu2sIT20[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT20[i]))/(2*(a[i]-Mu2sIT20[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT20[i] = Znot;


        if j == 20:
            ZnotB = (t3*(b[i]-Mu2sIT21[i]))/(2*(a[i]-Mu2sIT21[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT21[i]))/(2*(a[i]-Mu2sIT21[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT21[i] = Znot;


        if j == 21:
            ZnotB = (t3*(b[i]-Mu2sIT22[i]))/(2*(a[i]-Mu2sIT22[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT22[i]))/(2*(a[i]-Mu2sIT22[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT22[i] = Znot;

        if j == 22:
            ZnotB = (t3*(b[i]-Mu2sIT23[i]))/(2*(a[i]-Mu2sIT23[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT23[i]))/(2*(a[i]-Mu2sIT23[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT23[i] = Znot;

        if j == 23:
            ZnotB = (t3*(b[i]-Mu2sIT24[i]))/(2*(a[i]-Mu2sIT24[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT24[i]))/(2*(a[i]-Mu2sIT24[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT24[i] = Znot;


        if j == 24:
            ZnotB = (t3*(b[i]-Mu2sIT25[i]))/(2*(a[i]-Mu2sIT25[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT25[i]))/(2*(a[i]-Mu2sIT25[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT25[i] = Znot;

        if j == 25:
            ZnotB = (t3*(b[i]-Mu2sIT26[i]))/(2*(a[i]-Mu2sIT26[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT26[i]))/(2*(a[i]-Mu2sIT26[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT26[i] = Znot;


        if j == 26:
            ZnotB = (t3*(b[i]-Mu2sIT27[i]))/(2*(a[i]-Mu2sIT27[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT27[i]))/(2*(a[i]-Mu2sIT27[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT27[i] = Znot;

    

        if j == 27:
            ZnotB = (t3*(b[i]-Mu2sIT28[i]))/(2*(a[i]-Mu2sIT28[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT28[i]))/(2*(a[i]-Mu2sIT28[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT28[i] = Znot;

            
        if j == 28:
            ZnotB = (t3*(b[i]-Mu2sIT29[i]))/(2*(a[i]-Mu2sIT29[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT29[i]))/(2*(a[i]-Mu2sIT29[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT29[i] = Znot;


        if j == 29:
            ZnotB = (t3*(b[i]-Mu2sIT30[i]))/(2*(a[i]-Mu2sIT30[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT30[i]))/(2*(a[i]-Mu2sIT30[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT30[i] = Znot;
 

        if j == 30:
            ZnotB = (t3*(b[i]-Mu2sIT31[i]))/(2*(a[i]-Mu2sIT31[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT31[i]))/(2*(a[i]-Mu2sIT31[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT31[i] = Znot;


        if j == 31:
            ZnotB = (t3*(b[i]-Mu2sIT32[i]))/(2*(a[i]-Mu2sIT32[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT32[i]))/(2*(a[i]-Mu2sIT32[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT32[i] = Znot;


        if j == 32:
            ZnotB = (t3*(b[i]-Mu2sIT33[i]))/(2*(a[i]-Mu2sIT33[i]));
   
            ZnotC = (t1*(c[i]-Mu2sIT33[i]))/(2*(a[i]-Mu2sIT33[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT33[i] = Znot;

#print parameter values
print 'Wavelength \t\tMu2sIT0 \t\tMu2sIT1 \t\tMu2sIT2 \t\tMu2sIT3 \t\tMu2sIT4 \t\tMu2sIT5 \t\tMu2sIT6 \t\tMu2sIT7 \t\tMu2sIT8 \t\tMu2sIT9 \t\tMu2sIT10 \t\tMu2sIT11 \t\tMu2sIT12 \t\tMu2sIT13 \t\tMu2sIT14 \t\tMu2sIT15 \t\tMu2sIT16 \t\tMu2sIT17 \t\tMu2sIT18 \t\tMu2sIT19 \t\tMu2sIT20 \t\tMu2sIT21 \t\tMu2sIT22 \t\tMu2sIT23 \t\tMu2sIT24 \t\tMu2sIT25 \t\tMu2sIT26 \t\tMu2sIT27 \t\tMu2sIT28 \t\tMu2sIT29 \t\tMu2sIT30 \t\tMu2sIT31 \t\tMu2sIT32 \t\tMu2sIT33 \t\tZnotsIT0 \t\tZnotsIT1 \t\tZnotsIT2 \t\tZnotsIT3 \t\tZnotsIT4 \t\tZnotsIT5 \t\tZnotsIT6 \t\tZnotsIT7 \t\tZnotsIT8 \t\tZnotsIT9 \t\tZnotsIT10 \t\tZnotsIT11 \t\tZnotsIT12 \t\tZnotsIT13 \t\tZnotsIT14 \t\tZnotsIT15 \t\tZnotsIT16 \t\tZnotsIT17 \t\tZnotsIT18 \t\tZnotsIT19 \t\tZnotsIT20 \t\tZnotsIT21 \t\tZnotsIT22 \t\tZnotsIT23 \t\tZnotsIT24 \t\tZnotsIT25 \t\tZnotsIT26 \t\tZnotsIT27 \t\tZnotsIT28 \t\tZnotsIT29 \t\tZnotsIT30 \t\tZnotsIT31 \t\tZnotsIT32 \t\tZnotsIT33'

for w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33 in zip(Waves,Mu2sIT0,Mu2sIT1,Mu2sIT2,Mu2sIT3,Mu2sIT4,Mu2sIT5,Mu2sIT6,Mu2sIT7,Mu2sIT8,Mu2sIT9,Mu2sIT10,Mu2sIT11,Mu2sIT12,Mu2sIT13,Mu2sIT14,Mu2sIT15,Mu2sIT16,Mu2sIT17,Mu2sIT18,Mu2sIT19,Mu2sIT20,Mu2sIT21,Mu2sIT22,Mu2sIT23,Mu2sIT24,Mu2sIT25,Mu2sIT26,Mu2sIT27,Mu2sIT28,Mu2sIT29,Mu2sIT30,Mu2sIT31,Mu2sIT32,Mu2sIT33,ZnotsIT0,ZnotsIT1,ZnotsIT2,ZnotsIT3,ZnotsIT4,ZnotsIT5,ZnotsIT6,ZnotsIT7,ZnotsIT8,ZnotsIT9,ZnotsIT10,ZnotsIT11,ZnotsIT12,ZnotsIT13,ZnotsIT14,ZnotsIT15,ZnotsIT16,ZnotsIT17,ZnotsIT18,ZnotsIT19,ZnotsIT20,ZnotsIT21,ZnotsIT22,ZnotsIT23,ZnotsIT24,ZnotsIT25,ZnotsIT26,ZnotsIT27,ZnotsIT28,ZnotsIT29,ZnotsIT30,ZnotsIT31,ZnotsIT32,ZnotsIT33):
    print "%.3f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f\t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f" % ( w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33)
