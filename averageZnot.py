import numpy

#program to calculate Znot and Mu2 Iterations for each wavelength


Waves     =[410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 
            480, 485, 490, 495, 500] 

# MuEff4 = Mu1
MuEff4  = [0.04165070, 0.02503760, 0.01973180, 0.01619190, 0.01393150, 0.0124136, 
          0.01128400, 0.01006360, 0.00911752, 0.00840986, 0.00754227, 0.00679159, 
          0.00632955, 0.00599585, 0.00560205, 0.00502454, 0.00483332, 0.00449612, 
          0.00405594]


#MuE3
# 6 mm from Python Script
MuEff6 = [0.0366739, 0.0223522, 0.0175271, 0.0144516, 0.0122924, 0.0108411, 
        0.0096307, 0.0085361, 0.0076291, 0.0069036, 0.0061815, 0.0054224, 
        0.004971, 0.0046588, 0.0041977, 0.0037511, 0.0034574, 0.0030691, 
        0.0027372]

# 10 mm from Python Script
#MuE1s
MuEff10 = [0.0282258, 0.0160772, 0.0120908, 0.0097304, 
         0.0081497, 0.0070059, 0.0061152, 0.0053619, 
         0.0046693, 0.0040584, 0.0033999, 0.0029544, 
         0.0025852, 0.0023379, 0.0020139, 0.0017133, 
         0.0015094, 0.001307, 0.0011205]



t10 = 10;
t6 = 6;
t4 = 4;

ZnotsIT0  = [2.427889359, 2.561517235, 2.581265491, 2.614503112, 2.590083237, 2.577303884, 2.525007063, 
            2.515745535, 2.497603489, 2.475734576, 2.509029113, 2.455170914, 2.443449109, 2.438159203, 
            2.386197251, 2.400069724, 2.339126982, 2.265970197, 2.261966723]
     
Mu2sIT0   = [0.01555365, 0.0066647, 0.00393635, 0.0026486, 0.00193565, 0.0012531, 0.00084195, 0.0006006, 0.0002296, 
             -0.0002094, -0.0007725, -0.0007476, -0.0009935, -0.00114345, -0.0012618, -0.0013434, -0.0014126,
             -0.00133615, -0.00130455]

Mu2sIT10   = [None]*19;
Mu2sIT2   = [None]*19;
Mu2sIT6   = [None]*19;
Mu2sIT4   = [None]*19;
Mu2sIT5   = [None]*19;
Mu2sIT6   = [None]*19;
Mu2sIT7   = [None]*19;
Mu2sIT8   = [None]*19;
Mu2sIT9   = [None]*19;
Mu2sIT100  = [None]*19;
Mu2sIT101  = [None]*19;
Mu2sIT102  = [None]*19;
Mu2sIT103  = [None]*19;
Mu2sIT104  = [None]*19;
Mu2sIT105  = [None]*19;
Mu2sIT106  = [None]*19;
Mu2sIT107  = [None]*19;
Mu2sIT108  = [None]*19;
Mu2sIT109  = [None]*19;
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
Mu2sIT60  = [None]*19;
Mu2sIT61  = [None]*19;
Mu2sIT62  = [None]*19;
Mu2sIT63  = [None]*19;

ZnotsIT10  = [None]*19;
ZnotsIT2  = [None]*19;
ZnotsIT6  = [None]*19;
ZnotsIT4  = [None]*19;
ZnotsIT5  = [None]*19;
ZnotsIT6  = [None]*19;
ZnotsIT7  = [None]*19;
ZnotsIT8  = [None]*19;
ZnotsIT9  = [None]*19;
ZnotsIT100 = [None]*19;
ZnotsIT101 = [None]*19;
ZnotsIT102 = [None]*19;
ZnotsIT103 = [None]*19;
ZnotsIT104 = [None]*19;
ZnotsIT105 = [None]*19;
ZnotsIT106 = [None]*19;
ZnotsIT107 = [None]*19;
ZnotsIT108 = [None]*19;
ZnotsIT109 = [None]*19;
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
ZnotsIT60 = [None]*19;
ZnotsIT61 = [None]*19;
ZnotsIT62 = [None]*19;
ZnotsIT63 = [None]*19;

Iterations = list(range(34));
#loop over iterations
for j in range (len(Iterations)):

    for i in range(len(Waves)):
            
        if j == 0:
            Znot = numpy.mean(ZnotsIT0);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT10[i] = 0;
            #else:
            Mu2sIT10[i] = Mu2b;
        
    
        if j == 1:
            Znot =  (ZnotsIT10[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT2[i] = 0;
            #else:
            Mu2sIT2[i] = Mu2b;
        
            
        if j == 2:
            Znot =  (ZnotsIT2[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT6[i] = 0;
            #else:
            Mu2sIT6[i] = Mu2b;
        

        if j == 3:
            Znot =  (ZnotsIT6[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT4[i] = 0;
            #else:
            Mu2sIT4[i] = Mu2b;
        

        if j == 4:
            Znot =  (ZnotsIT4[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT5[i] = 0;
            #else:
            Mu2sIT5[i] = Mu2b;
        

        if j == 5:
            Znot =  (ZnotsIT5[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT6[i] = 0;
            #else:
            Mu2sIT6[i] = Mu2b;
        

        if j == 6:
            Znot =  (ZnotsIT6[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT7[i] = 0;
            #else:
            Mu2sIT7[i] = Mu2b;
        

        if j == 7:
            Znot =  (ZnotsIT7[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT8[i] = 0;
            #else:
            Mu2sIT8[i] = Mu2b;
        

        if j == 8:
            Znot =  (ZnotsIT8[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT9[i] = 0;
            #else:
            Mu2sIT9[i] = Mu2b;
        

        if j == 9:
            Znot =  (ZnotsIT9[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT100[i] = 0;
            #else:
            Mu2sIT100[i] = Mu2b;
        
        if j == 10:
            Znot =  (ZnotsIT100[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT101[i] = Mu2b;
        
        if j == 11:
            Znot =  (ZnotsIT101[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT102[i] = Mu2b;
        
        if j == 12:
            Znot =  (ZnotsIT102[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT103[i] = Mu2b;
        
        if j == 13:
            Znot =  (ZnotsIT103[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT104[i] = Mu2b;
        
        if j == 14:
            Znot =  (ZnotsIT104[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT105[i] = Mu2b;
        
        if j == 15:
            Znot =  (ZnotsIT105[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT106[i] = Mu2b;
        
        if j == 16:
            Znot =  (ZnotsIT106[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT107[i] = Mu2b;
        
        if j == 17:
            Znot =  (ZnotsIT107[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT108[i] = Mu2b;
        
        if j == 18:
            Znot =  (ZnotsIT108[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT109[i] = Mu2b;
        
        if j == 19:
            Znot =  (ZnotsIT109[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT20[i] = Mu2b;
        
        if j == 20:
            Znot =  (ZnotsIT20[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT21[i] = Mu2b;
        
        if j == 21:
            Znot =  (ZnotsIT21[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT22[i] = Mu2b;
        
        if j == 22:
            Znot =  (ZnotsIT22[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT23[i] = Mu2b;
        
        if j == 23:
            Znot =  (ZnotsIT23[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT24[i] = Mu2b;
        
        if j == 24:
            Znot =  (ZnotsIT24[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT25[i] = Mu2b;
        
        if j == 25:
            Znot =  (ZnotsIT25[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT26[i] = Mu2b;
        
        if j == 26:
            Znot =  (ZnotsIT26[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT27[i] = Mu2b;
        
        if j == 27:
            Znot =  (ZnotsIT27[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT28[i] = Mu2b;
        
        if j == 28:
            Znot =  (ZnotsIT28[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT29[i] = Mu2b;
        
        if j == 29:
            Znot =  (ZnotsIT29[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT60[i] = Mu2b;
        
        if j == 30:
            Znot =  (ZnotsIT60[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT61[i] = Mu2b;
        
        if j == 31:
            Znot =  (ZnotsIT61[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT62[i] = Mu2b;
        
        if j == 32:
            Znot =  (ZnotsIT62[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            Mu2sIT63[i] = Mu2b;
                  
    #for i in range(len(Waves)):

        if j == 0:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT10[i]))/(2*(MuEff4[i]-Mu2sIT10[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT10[i]))/(2*(MuEff4[i]-Mu2sIT10[i]));
            #print (Mu2sIT10[i])
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT10[i] = ZnotB;

        if j == 1:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT2[i]))/(2*(MuEff4[i]-Mu2sIT2[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT2[i]))/(2*(MuEff4[i]-Mu2sIT2[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT2[i] = ZnotB;


        if j == 2:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT6[i] = ZnotB;

        if j == 3:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT4[i]))/(2*(MuEff4[i]-Mu2sIT4[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT4[i]))/(2*(MuEff4[i]-Mu2sIT4[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT4[i] = ZnotB;


        if j == 4:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT5[i]))/(2*(MuEff4[i]-Mu2sIT5[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT5[i]))/(2*(MuEff4[i]-Mu2sIT5[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT5[i] = ZnotB;

    

        if j == 5:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT6[i] = ZnotB;

            
        if j == 6:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT7[i]))/(2*(MuEff4[i]-Mu2sIT7[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT7[i]))/(2*(MuEff4[i]-Mu2sIT7[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT7[i] = ZnotB;


        if j == 7:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT8[i]))/(2*(MuEff4[i]-Mu2sIT8[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT8[i]))/(2*(MuEff4[i]-Mu2sIT8[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT8[i] = ZnotB;


        if j == 8:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT9[i]))/(2*(MuEff4[i]-Mu2sIT9[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT9[i]))/(2*(MuEff4[i]-Mu2sIT9[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT9[i] = ZnotB;


        if j == 9:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT100[i]))/(2*(MuEff4[i]-Mu2sIT100[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT100[i]))/(2*(MuEff4[i]-Mu2sIT100[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT100[i] = ZnotB;


        if j == 10:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT101[i]))/(2*(MuEff4[i]-Mu2sIT101[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT101[i]))/(2*(MuEff4[i]-Mu2sIT101[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT101[i] = ZnotB;
            
        if j == 11:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT102[i]))/(2*(MuEff4[i]-Mu2sIT102[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT102[i]))/(2*(MuEff4[i]-Mu2sIT102[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT102[i] = ZnotB;

        if j == 12:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT103[i]))/(2*(MuEff4[i]-Mu2sIT103[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT103[i]))/(2*(MuEff4[i]-Mu2sIT103[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT103[i] = ZnotB;


        if j == 13:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT104[i]))/(2*(MuEff4[i]-Mu2sIT104[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT104[i]))/(2*(MuEff4[i]-Mu2sIT104[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT104[i] = ZnotB;

        if j == 14:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT105[i]))/(2*(MuEff4[i]-Mu2sIT105[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT105[i]))/(2*(MuEff4[i]-Mu2sIT105[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT105[i] = ZnotB;


        if j == 15:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT106[i]))/(2*(MuEff4[i]-Mu2sIT106[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT106[i]))/(2*(MuEff4[i]-Mu2sIT106[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT106[i] = ZnotB;

    

        if j == 16:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT107[i]))/(2*(MuEff4[i]-Mu2sIT107[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT107[i]))/(2*(MuEff4[i]-Mu2sIT107[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT107[i] = ZnotB;

        if j == 17:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT108[i]))/(2*(MuEff4[i]-Mu2sIT108[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT108[i]))/(2*(MuEff4[i]-Mu2sIT108[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT108[i] = ZnotB;


        if j == 18:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT109[i]))/(2*(MuEff4[i]-Mu2sIT109[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT109[i]))/(2*(MuEff4[i]-Mu2sIT109[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT109[i] = ZnotB;


        if j == 19:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT20[i]))/(2*(MuEff4[i]-Mu2sIT20[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT20[i]))/(2*(MuEff4[i]-Mu2sIT20[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT20[i] = ZnotB;


        if j == 20:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT21[i]))/(2*(MuEff4[i]-Mu2sIT21[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT21[i]))/(2*(MuEff4[i]-Mu2sIT21[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT21[i] = ZnotB;


        if j == 21:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT22[i]))/(2*(MuEff4[i]-Mu2sIT22[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT22[i]))/(2*(MuEff4[i]-Mu2sIT22[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT22[i] = ZnotB;

        if j == 22:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT23[i]))/(2*(MuEff4[i]-Mu2sIT23[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT23[i]))/(2*(MuEff4[i]-Mu2sIT23[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT23[i] = ZnotB;

        if j == 23:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT24[i]))/(2*(MuEff4[i]-Mu2sIT24[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT24[i]))/(2*(MuEff4[i]-Mu2sIT24[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT24[i] = ZnotB;


        if j == 24:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT25[i]))/(2*(MuEff4[i]-Mu2sIT25[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT25[i]))/(2*(MuEff4[i]-Mu2sIT25[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT25[i] = ZnotB;

        if j == 25:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT26[i]))/(2*(MuEff4[i]-Mu2sIT26[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT26[i]))/(2*(MuEff4[i]-Mu2sIT26[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT26[i] = ZnotB;


        if j == 26:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT27[i]))/(2*(MuEff4[i]-Mu2sIT27[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT27[i]))/(2*(MuEff4[i]-Mu2sIT27[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT27[i] = ZnotB;

    

        if j == 27:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT28[i]))/(2*(MuEff4[i]-Mu2sIT28[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT28[i]))/(2*(MuEff4[i]-Mu2sIT28[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT28[i] = ZnotB;

            
        if j == 28:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT29[i]))/(2*(MuEff4[i]-Mu2sIT29[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT29[i]))/(2*(MuEff4[i]-Mu2sIT29[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT29[i] = ZnotB;


        if j == 29:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT60[i]))/(2*(MuEff4[i]-Mu2sIT60[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT60[i]))/(2*(MuEff4[i]-Mu2sIT60[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT60[i] = ZnotB;
 

        if j == 30:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT61[i]))/(2*(MuEff4[i]-Mu2sIT61[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT61[i]))/(2*(MuEff4[i]-Mu2sIT61[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT61[i] = ZnotB;


        if j == 31:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT62[i]))/(2*(MuEff4[i]-Mu2sIT62[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT62[i]))/(2*(MuEff4[i]-Mu2sIT62[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT62[i] = ZnotB;


        if j == 32:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT63[i]))/(2*(MuEff4[i]-Mu2sIT63[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT63[i]))/(2*(MuEff4[i]-Mu2sIT63[i]));

            Znot  = (ZnotB + ZnotC)/2;
            ZnotsIT63[i] = ZnotB;

#print parameter values
print 'Wavelength \t\tMu2sIT0 \t\tMu2sIT10 \t\tMu2sIT2 \t\tMu2sIT6 \t\tMu2sIT4 \t\tMu2sIT5 \t\tMu2sIT6 \t\tMu2sIT7 \t\tMu2sIT8 \t\tMu2sIT9 \t\tMu2sIT100 \t\tMu2sIT101 \t\tMu2sIT102 \t\tMu2sIT103 \t\tMu2sIT104 \t\tMu2sIT105 \t\tMu2sIT106 \t\tMu2sIT107 \t\tMu2sIT108 \t\tMu2sIT109 \t\tMu2sIT20 \t\tMu2sIT21 \t\tMu2sIT22 \t\tMu2sIT23 \t\tMu2sIT24 \t\tMu2sIT25 \t\tMu2sIT26 \t\tMu2sIT27 \t\tMu2sIT28 \t\tMu2sIT29 \t\tMu2sIT60 \t\tMu2sIT61 \t\tMu2sIT62 \t\tMu2sIT63 \t\tZnotsIT0 \t\tZnotsIT10 \t\tZnotsIT2 \t\tZnotsIT6 \t\tZnotsIT4 \t\tZnotsIT5 \t\tZnotsIT6 \t\tZnotsIT7 \t\tZnotsIT8 \t\tZnotsIT9 \t\tZnotsIT100 \t\tZnotsIT101 \t\tZnotsIT102 \t\tZnotsIT103 \t\tZnotsIT104 \t\tZnotsIT105 \t\tZnotsIT106 \t\tZnotsIT107 \t\tZnotsIT108 \t\tZnotsIT109 \t\tZnotsIT20 \t\tZnotsIT21 \t\tZnotsIT22 \t\tZnotsIT23 \t\tZnotsIT24 \t\tZnotsIT25 \t\tZnotsIT26 \t\tZnotsIT27 \t\tZnotsIT28 \t\tZnotsIT29 \t\tZnotsIT60 \t\tZnotsIT61 \t\tZnotsIT62 \t\tZnotsIT63'

for w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33 in zip(Waves,Mu2sIT0,Mu2sIT10,Mu2sIT2,Mu2sIT6,Mu2sIT4,Mu2sIT5,Mu2sIT6,Mu2sIT7,Mu2sIT8,Mu2sIT9,Mu2sIT100,Mu2sIT101,Mu2sIT102,Mu2sIT103,Mu2sIT104,Mu2sIT105,Mu2sIT106,Mu2sIT107,Mu2sIT108,Mu2sIT109,Mu2sIT20,Mu2sIT21,Mu2sIT22,Mu2sIT23,Mu2sIT24,Mu2sIT25,Mu2sIT26,Mu2sIT27,Mu2sIT28,Mu2sIT29,Mu2sIT60,Mu2sIT61,Mu2sIT62,Mu2sIT63,ZnotsIT0,ZnotsIT10,ZnotsIT2,ZnotsIT6,ZnotsIT4,ZnotsIT5,ZnotsIT6,ZnotsIT7,ZnotsIT8,ZnotsIT9,ZnotsIT100,ZnotsIT101,ZnotsIT102,ZnotsIT103,ZnotsIT104,ZnotsIT105,ZnotsIT106,ZnotsIT107,ZnotsIT108,ZnotsIT109,ZnotsIT20,ZnotsIT21,ZnotsIT22,ZnotsIT23,ZnotsIT24,ZnotsIT25,ZnotsIT26,ZnotsIT27,ZnotsIT28,ZnotsIT29,ZnotsIT60,ZnotsIT61,ZnotsIT62,ZnotsIT63):
    print "%.3f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f\t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f" % ( w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33)
