import numpy

#program to calculate Znot and Mu2 Iterations for each wavelength


#Waves     =[410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 
#            480, 485, 490, 495, 500] 

Waves = [410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 
         425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 
         440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 
         455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 
         470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 
         485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 
         500]


# MuEff4 = Mu1
#MuEff4  = [0.04165070, 0.02503760, 0.01973180, 0.01619190, 0.01393150, 0.0124136, 
#          0.01128400, 0.01006360, 0.00911752, 0.00840986, 0.00754227, 0.00679159, 
#          0.00632955, 0.00599585, 0.00560205, 0.00502454, 0.00483332, 0.00449612, 
#          0.00405594]


#MuE3
# 6 mm from Python Script
#MuEff6 = [0.0366739, 0.0223522, 0.0175271, 0.0144516, 0.0122924, 0.0108411, 
#        0.0096307, 0.0085361, 0.0076291, 0.0069036, 0.0061815, 0.0054224, 
#        0.004971, 0.0046588, 0.0041977, 0.0037511, 0.0034574, 0.0030691, 
#        0.0027372]

# 10 mm from Python Script
#MuE1s

#410-500 by 5s
#MuEff10 = [0.0282258, 0.0160772, 0.0120908, 0.0097304, 
#         0.0081497, 0.0070059, 0.0061152, 0.0053619, 
#         0.0046693, 0.0040584, 0.0033999, 0.0029544, 
#         0.0025852, 0.0023379, 0.0020139, 0.0017133, 
#         0.0015094, 0.001307, 0.0011205]

#410-500 By 1s
MuEff10 = [0.028226, 0.024328, 0.021375, 0.019167, 0.017387, 0.016077, 0.014917, 0.013974, 0.013285, 
           0.012714, 0.012091, 0.011490, 0.010968, 0.010555, 0.010084, 0.009730, 0.009322, 0.008977, 
           0.008675, 0.008438, 0.008150, 0.007914, 0.007659, 0.007419, 0.007218, 0.007006, 0.006836, 
           0.006658, 0.006509, 0.006341, 0.006115, 0.006009, 0.005843, 0.005670, 0.005528, 0.005362, 
           0.005249, 0.005058, 0.004943, 0.004774, 0.004669, 0.004610, 0.004480, 0.004397, 0.004165, 
           0.004058, 0.003921, 0.003840, 0.003719, 0.003520, 0.003400, 0.003289, 0.003197, 0.003130, 
           0.003019, 0.002954, 0.002854, 0.002769, 0.002692, 0.002607, 0.002585, 0.002573, 0.002508, 
           0.002428, 0.002362, 0.002338, 0.002217, 0.002172, 0.002138, 0.002037, 0.002014, 0.001946, 
           0.001902, 0.001848, 0.001797, 0.001713, 0.001695, 0.001613, 0.001601, 0.001568, 0.001509, 
           0.001482, 0.001422, 0.001389, 0.001326, 0.001307, 0.001248, 0.001244, 0.001186, 0.001119, 
           0.001121]

MuEff6  = [0.0366738, 0.0321248, 0.0286518, 0.0260489, 0.0239853, 0.0223522, 0.0209863, 0.0199977, 
           0.0190547, 0.0182269, 0.0175272, 0.0167423, 0.0161555, 0.0154983, 0.0148799, 0.0144515, 
           0.0140043, 0.0135646, 0.0131084, 0.0126823, 0.0122924, 0.0120846, 0.0117350, 0.0115156, 
           0.0111555, 0.0108412, 0.0105926, 0.0104133, 0.0100504, 0.0098623, 0.0096308, 0.0094138, 
           0.0092119, 0.0089787, 0.0088447, 0.0085361, 0.0084374, 0.0082489, 0.0081004, 0.0078835, 
           0.0076291, 0.0074730, 0.0073652, 0.0071945, 0.0070813, 0.0069036, 0.0067137, 0.0066347, 
           0.0064375, 0.0063338, 0.0061815, 0.0060076, 0.0057921, 0.0056466, 0.0055909, 0.0054224, 
           0.0053061, 0.0052778, 0.0051125, 0.0050674, 0.0049710, 0.0049340, 0.0048759, 0.0048408, 
           0.0047369, 0.0046589, 0.0045485, 0.0044162, 0.0043683, 0.0042806, 0.0041976, 0.0041697, 
           0.0040102, 0.0039172, 0.0038630, 0.0037512, 0.0037720, 0.0036531, 0.0035709, 0.0035162, 
           0.0034573, 0.0032945, 0.0032748, 0.0032201, 0.0031166, 0.0030692, 0.0030276, 0.0029801, 
           0.0029569, 0.0028283, 0.0027373]

MuEff4  = [0.0417183, 0.0365294, 0.0323840, 0.0294381, 0.0270232, 0.0251845, 0.0237868, 0.0225038, 
           0.0213937, 0.0205423, 0.0198121, 0.0189109, 0.0180933, 0.0174223, 0.0168671, 0.0163028, 
           0.0158757, 0.0154212, 0.0148903, 0.0144647, 0.0140264, 0.0137422, 0.0133512, 0.0130857, 
           0.0127867, 0.0124506, 0.0122579, 0.0120792, 0.0116991, 0.0115318, 0.0112945, 0.0109628, 
           0.0107462, 0.0105387, 0.0103830, 0.0101070, 0.0100000, 0.0097802, 0.0096912, 0.0094213, 
           0.0091721, 0.0089545, 0.0089539, 0.0087901, 0.0086016, 0.0084831, 0.0082715, 0.0081375, 
           0.0080012, 0.0078491, 0.0076369, 0.0074671, 0.0071711, 0.0071056, 0.0069807, 0.0068646, 
           0.0066920, 0.0066394, 0.0064723, 0.0064198, 0.0063813, 0.0062802, 0.0062780, 0.0062763, 
           0.0061289, 0.0060378, 0.0059156, 0.0057764, 0.0057505, 0.0056735, 0.0056442, 0.0055003, 
           0.0053892, 0.0052645, 0.0052862, 0.0050478, 0.0051540, 0.0050377, 0.0049728, 0.0048753, 
           0.0048374, 0.0046926, 0.0046816, 0.0046050, 0.0044732, 0.0045060, 0.0044491, 0.0043446, 
           0.0043423, 0.0042267, 0.0040603]


t10 = 10;
t6 = 6;
t4 = 4;

Mu2sIT0   = [None]*91;
Mu2sIT1   = [None]*91;
Mu2sIT2   = [None]*91;
Mu2sIT3   = [None]*91;
Mu2sIT4   = [None]*91;
Mu2sIT5   = [None]*91;
Mu2sIT6   = [None]*91;
Mu2sIT7   = [None]*91;
Mu2sIT8   = [None]*91;
Mu2sIT9   = [None]*91;
Mu2sIT10  = [None]*91;
Mu2sIT11  = [None]*91;
Mu2sIT12  = [None]*91;
Mu2sIT13  = [None]*91;
Mu2sIT14  = [None]*91;
Mu2sIT15  = [None]*91;
Mu2sIT16  = [None]*91;
Mu2sIT17  = [None]*91;
Mu2sIT18  = [None]*91;
Mu2sIT19  = [None]*91;
Mu2sIT20  = [None]*91;
Mu2sIT20  = [None]*91;
Mu2sIT21  = [None]*91;
Mu2sIT22  = [None]*91;
Mu2sIT23  = [None]*91;
Mu2sIT24  = [None]*91;
Mu2sIT25  = [None]*91;
Mu2sIT26  = [None]*91;
Mu2sIT27  = [None]*91;
Mu2sIT28  = [None]*91;
Mu2sIT29  = [None]*91;
Mu2sIT30  = [None]*91;
Mu2sIT31  = [None]*91;
Mu2sIT32  = [None]*91;
Mu2sIT33  = [None]*91;

ZnotsIT0  = [None]*91
ZnotsIT1  = [None]*91;
ZnotsIT2  = [None]*91;
ZnotsIT3  = [None]*91;
ZnotsIT4  = [None]*91;
ZnotsIT5  = [None]*91;
ZnotsIT6  = [None]*91;
ZnotsIT7  = [None]*91;
ZnotsIT8  = [None]*91;
ZnotsIT9  = [None]*91;
ZnotsIT10 = [None]*91;
ZnotsIT11 = [None]*91;
ZnotsIT12 = [None]*91;
ZnotsIT13 = [None]*91;
ZnotsIT14 = [None]*91;
ZnotsIT15 = [None]*91;
ZnotsIT16 = [None]*91;
ZnotsIT17 = [None]*91;
ZnotsIT18 = [None]*91;
ZnotsIT19 = [None]*91;
ZnotsIT20 = [None]*91;
ZnotsIT21 = [None]*91;
ZnotsIT22 = [None]*91;
ZnotsIT23 = [None]*91;
ZnotsIT24 = [None]*91;
ZnotsIT25 = [None]*91;
ZnotsIT26 = [None]*91;
ZnotsIT27 = [None]*91;
ZnotsIT28 = [None]*91;
ZnotsIT29 = [None]*91;
ZnotsIT30 = [None]*91;
ZnotsIT31 = [None]*91;
ZnotsIT32 = [None]*91;
ZnotsIT33 = [None]*91;

for i in range (len(Waves)):
    ZnotsIT0[i] = (t6*t10*(MuEff6[i]-MuEff10[i]))/(2*((MuEff6[i]*t6-MuEff10[i]*t10+MuEff4[i]*(t10-t6))));
    Mu2sIT0[i]  = (MuEff6[i]*t6-MuEff10[i]*t10)/(t6-t10);
    
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
            #Mu2sIT1[i] = Mu2;
            
            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT0, Mu2)
            #Mu2sIT1[i] = numpy.average(temp, axis=0)
            Mu2sIT1[i] = numpy.average([Mu2sIT0[i], Mu2])
    
        if j == 1:
            Znot =  (ZnotsIT1[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT2[i] = 0;
            #else:
            #Mu2sIT2[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT1, Mu2)
            #Mu2sIT2[i] = numpy.average(temp, axis=0)
            Mu2sIT2[i] = numpy.average([Mu2sIT1[i], Mu2])

            
        if j == 2:
            Znot =  (ZnotsIT2[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));


            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT6[i] = 0;
            #else:
            #Mu2sIT3[i] = Mu2;
        
            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT2, Mu2)
            #Mu2sIT3[i] = numpy.average(temp, axis=0)
            Mu2sIT3[i] = numpy.average([Mu2sIT2[i], Mu2])

        if j == 3:
            Znot =  (ZnotsIT3[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT4[i] = 0;
            #else:
            #Mu2sIT4[i] = Mu2;
        
            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT3, Mu2)
            #Mu2sIT4[i] = numpy.average(temp, axis=0)
            Mu2sIT4[i] = numpy.average([Mu2sIT3[i], Mu2])
            
        if j == 4:
            Znot =  (ZnotsIT4[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT5[i] = 0;
            #else:
            #Mu2sIT5[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT4, Mu2)
            #Mu2sIT5[i] = numpy.average(temp, axis=0)
            Mu2sIT5[i] = numpy.average([Mu2sIT4[i], Mu2])

        if j == 5:
            Znot =  (ZnotsIT5[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT6[i] = 0;
            #else:
            #Mu2sIT6[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT5, Mu2)
            #Mu2sIT6[i] = numpy.average(temp, axis=0)
            Mu2sIT6[i] = numpy.average([Mu2sIT5[i], Mu2])

        if j == 6:
            Znot =  (ZnotsIT6[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT7[i] = 0;
            #else:
            #Mu2sIT7[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT6, Mu2)
            #Mu2sIT7[i] = numpy.average(temp, axis=0)
            Mu2sIT7[i] = numpy.average([Mu2sIT6[i], Mu2])

        if j == 7:
            Znot =  (ZnotsIT7[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT8[i] = 0;
            #else:
            #Mu2sIT8[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT7, Mu2)
            #Mu2sIT8[i] = numpy.average(temp, axis=0)
            Mu2sIT8[i] = numpy.average([Mu2sIT7[i], Mu2])

        if j == 8:
            Znot =  (ZnotsIT8[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT9[i] = 0;
            #else:
            #Mu2sIT9[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT8, Mu2)
            #Mu2sIT9[i] = numpy.average(temp, axis=0)
            Mu2sIT9[i] = numpy.average([Mu2sIT8[i], Mu2])

        if j == 9:
            Znot =  (ZnotsIT9[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT100[i] = 0;
            #else:
            #Mu2sIT10[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT9, Mu2)
            #Mu2sIT0[i] = numpy.average(temp, axis=0)
            Mu2sIT10[i] = numpy.average([Mu2sIT9[i], Mu2])
        
        if j == 10:
            Znot =  (ZnotsIT10[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT11[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT10, Mu2)
            #Mu2sIT11[i] = numpy.average(temp, axis=0)
            Mu2sIT11[i] = numpy.average([Mu2sIT10[i], Mu2])
        
        if j == 11:
            Znot =  (ZnotsIT11[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT12[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT11, Mu2)
            #Mu2sIT12[i] = numpy.average(temp, axis=0)
            Mu2sIT12[i] = numpy.average([Mu2sIT11[i], Mu2])
        
        if j == 12:
            Znot =  (ZnotsIT12[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT13[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT12, Mu2)
            #Mu2sIT13[i] = numpy.average(temp, axis=0)
            Mu2sIT13[i] = numpy.average([Mu2sIT12[i], Mu2])
        
        if j == 13:
            Znot =  (ZnotsIT13[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT14[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT13, Mu2)
            #Mu2sIT14[i] = numpy.average(temp, axis=0)
            Mu2sIT14[i] = numpy.average([Mu2sIT13[i], Mu2])
        
        if j == 14:
            Znot =  (ZnotsIT14[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT15[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT14, Mu2)
            #Mu2sIT15[i] = numpy.average(temp, axis=0)
            Mu2sIT15[i] = numpy.average([Mu2sIT14[i], Mu2])
        
        if j == 15:
            Znot =  (ZnotsIT15[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT16[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT15, Mu2)
            #Mu2sIT16[i] = numpy.average(temp, axis=0)
            Mu2sIT16[i] = numpy.average([Mu2sIT15[i], Mu2])
        
        if j == 16:
            Znot =  (ZnotsIT16[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT17[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT16, Mu2)
            #Mu2sIT17[i] = numpy.average(temp, axis=0)
            Mu2sIT17[i] = numpy.average([Mu2sIT16[i], Mu2])
        
        if j == 17:
            Znot =  (ZnotsIT17[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT18[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT17, Mu2)
            #Mu2sIT18[i] = numpy.average(temp, axis=0)
            Mu2sIT18[i] = numpy.average([Mu2sIT17[i], Mu2])
        
        if j == 18:
            Znot =  (ZnotsIT18[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT19[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT18, Mu2)
            #Mu2sIT19[i] = numpy.average(temp, axis=0)
            Mu2sIT19[i] = numpy.average([Mu2sIT18[i], Mu2])
        
        if j == 19:
            Znot =  (ZnotsIT19[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT20[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT19, Mu2)
            #Mu2sIT20[i] = numpy.average(temp, axis=0)
            Mu2sIT20[i] = numpy.average([Mu2sIT19[i], Mu2])
        
        if j == 20:
            Znot =  (ZnotsIT20[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT21[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT20, Mu2)
            #Mu2sIT21[i] = numpy.average(temp, axis=0)
            Mu2sIT21[i] = numpy.average([Mu2sIT20[i], Mu2])
        
        if j == 21:
            Znot =  (ZnotsIT21[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT22[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT21, Mu2)
            #Mu2sIT22[i] = numpy.average(temp, axis=0)
            Mu2sIT22[i] = numpy.average([Mu2sIT21[i], Mu2])
        
        if j == 22:
            Znot =  (ZnotsIT22[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT23[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT22, Mu2)
            #Mu2sIT23[i] = numpy.average(temp, axis=0)
            Mu2sIT23[i] = numpy.average([Mu2sIT22[i], Mu2])
        
        if j == 23:
            Znot =  (ZnotsIT23[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT24[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT23, Mu2)
            #Mu2sIT24[i] = numpy.average(temp, axis=0)
            Mu2sIT24[i] = numpy.average([Mu2sIT23[i], Mu2])
        
        if j == 24:
            Znot =  (ZnotsIT24[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT25[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT24, Mu2)
            #Mu2sIT25[i] = numpy.average(temp, axis=0)
            Mu2sIT25[i] = numpy.average([Mu2sIT24[i], Mu2])
        
        if j == 25:
            Znot =  (ZnotsIT25[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT26[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT25, Mu2)
            #Mu2sIT26[i] = numpy.average(temp, axis=0)
            Mu2sIT26[i] = numpy.average([Mu2sIT25[i], Mu2])
        
        if j == 26:
            Znot =  (ZnotsIT26[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT27[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT26, Mu2)
            #Mu2sIT27[i] = numpy.average(temp, axis=0)
            Mu2sIT27[i] = numpy.average([Mu2sIT26[i], Mu2])
        
        if j == 27:
            Znot =  (ZnotsIT27[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT28[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT27, Mu2)
            #Mu2sIT28[i] = numpy.average(temp, axis=0)
            Mu2sIT28[i] = numpy.average([Mu2sIT27[i], Mu2])
        
        if j == 28:
            Znot =  (ZnotsIT28[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT29[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT28, Mu2)
            #Mu2sIT29[i] = numpy.average(temp, axis=0)
            Mu2sIT29[i] = numpy.average([Mu2sIT28[i], Mu2])
        
        if j == 29:
            Znot =  (ZnotsIT29[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT30[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT29, Mu2)
            #Mu2sIT30[i] = numpy.average(temp, axis=0)
            Mu2sIT30[i] = numpy.average([Mu2sIT29[i], Mu2])
        
        if j == 30:
            Znot =  (ZnotsIT30[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT31[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT30, Mu2)
            #Mu2sIT31[i] = numpy.average(temp, axis=0)
            Mu2sIT31[i] = numpy.average([Mu2sIT30[i], Mu2])
        
        if j == 31:
            Znot =  (ZnotsIT31[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT32[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT31, Mu2)
            #Mu2sIT32[i] = numpy.average(temp, axis=0)
            Mu2sIT32[i] = numpy.average([Mu2sIT31[i], Mu2])
        
        if j == 32:
            Znot =  (ZnotsIT32[i]);
            Mu2c = ((t10*MuEff10[i])-(2*Znot*MuEff4[i]))/(t10-(2*Znot));

            Mu2b = ((t6*MuEff6[i])-(2*Znot*MuEff4[i]))/(t6-(2*Znot));

            Mu2  = (Mu2b + Mu2c)/2;
            
            #if Mu2 < 0:
            #    Mu2sIT101[i] = 0;
            #else:
            #Mu2sIT33[i] = Mu2;

            #takes the average of previous iterations
            #temp = numpy.array(Mu2sIT32, Mu2)
            #Mu2sIT33[i] = numpy.average(temp, axis=0)
            Mu2sIT33[i] = numpy.average([Mu2sIT32[i], Mu2])
            
    for i in range(len(Waves)):

        if j == 0:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT1[i]))/(2*(MuEff4[i]-Mu2sIT1[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT1[i]))/(2*(MuEff4[i]-Mu2sIT1[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT1[i] = Znot;
            ZnotsIT1[i] = numpy.average([ZnotsIT0[i], Znot])
 
        if j == 1:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT2[i]))/(2*(MuEff4[i]-Mu2sIT2[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT2[i]))/(2*(MuEff4[i]-Mu2sIT2[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT2[i] = Znot;
            ZnotsIT2[i] = numpy.average([ZnotsIT1[i], Znot])

        if j == 2:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT3[i]))/(2*(MuEff4[i]-Mu2sIT3[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT3[i]))/(2*(MuEff4[i]-Mu2sIT3[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT3[i] = Znot;
            ZnotsIT3[i] = numpy.average([ZnotsIT2[i], Znot])

        if j == 3:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT4[i]))/(2*(MuEff4[i]-Mu2sIT4[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT4[i]))/(2*(MuEff4[i]-Mu2sIT4[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT4[i] = Znot;
            ZnotsIT4[i] = numpy.average([ZnotsIT3[i], Znot])

        if j == 4:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT5[i]))/(2*(MuEff4[i]-Mu2sIT5[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT5[i]))/(2*(MuEff4[i]-Mu2sIT5[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT5[i] = Znot;
            ZnotsIT5[i] = numpy.average([ZnotsIT4[i], Znot])
    

        if j == 5:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT6[i]))/(2*(MuEff4[i]-Mu2sIT6[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT6[i] = Znot;
            ZnotsIT6[i] = numpy.average([ZnotsIT5[i], Znot])

            
        if j == 6:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT7[i]))/(2*(MuEff4[i]-Mu2sIT7[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT7[i]))/(2*(MuEff4[i]-Mu2sIT7[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT7[i] = Znot;
            ZnotsIT7[i] = numpy.average([ZnotsIT6[i], Znot])

        if j == 7:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT8[i]))/(2*(MuEff4[i]-Mu2sIT8[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT8[i]))/(2*(MuEff4[i]-Mu2sIT8[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT8[i] = Znot;
            ZnotsIT8[i] = numpy.average([ZnotsIT7[i], Znot])

        if j == 8:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT9[i]))/(2*(MuEff4[i]-Mu2sIT9[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT9[i]))/(2*(MuEff4[i]-Mu2sIT9[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT9[i] = Znot;
            ZnotsIT9[i] = numpy.average([ZnotsIT8[i], Znot])

        if j == 9:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT10[i]))/(2*(MuEff4[i]-Mu2sIT10[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT10[i]))/(2*(MuEff4[i]-Mu2sIT10[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT10[i] = Znot;
            ZnotsIT10[i] = numpy.average([ZnotsIT9[i], Znot])

        if j == 10:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT11[i]))/(2*(MuEff4[i]-Mu2sIT11[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT11[i]))/(2*(MuEff4[i]-Mu2sIT11[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT11[i] = Znot;
            ZnotsIT11[i] = numpy.average([ZnotsIT10[i], Znot])

        if j == 11:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT12[i]))/(2*(MuEff4[i]-Mu2sIT12[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT12[i]))/(2*(MuEff4[i]-Mu2sIT12[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT12[i] = Znot;
            ZnotsIT12[i] = numpy.average([ZnotsIT11[i], Znot])

        if j == 12:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT13[i]))/(2*(MuEff4[i]-Mu2sIT13[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT13[i]))/(2*(MuEff4[i]-Mu2sIT13[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT13[i] = Znot;
            ZnotsIT13[i] = numpy.average([ZnotsIT12[i], Znot])

        if j == 13:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT14[i]))/(2*(MuEff4[i]-Mu2sIT14[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT14[i]))/(2*(MuEff4[i]-Mu2sIT14[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT14[i] = Znot;
            ZnotsIT14[i] = numpy.average([ZnotsIT13[i], Znot])

        if j == 14:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT15[i]))/(2*(MuEff4[i]-Mu2sIT15[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT15[i]))/(2*(MuEff4[i]-Mu2sIT15[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT15[i] = Znot;
            ZnotsIT15[i] = numpy.average([ZnotsIT14[i], Znot])

        if j == 15:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT16[i]))/(2*(MuEff4[i]-Mu2sIT16[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT16[i]))/(2*(MuEff4[i]-Mu2sIT16[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT16[i] = Znot;
            ZnotsIT16[i] = numpy.average([ZnotsIT15[i], Znot])
    

        if j == 16:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT17[i]))/(2*(MuEff4[i]-Mu2sIT17[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT17[i]))/(2*(MuEff4[i]-Mu2sIT17[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT17[i] = Znot;
            ZnotsIT17[i] = numpy.average([ZnotsIT16[i], Znot])

        if j == 17:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT18[i]))/(2*(MuEff4[i]-Mu2sIT18[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT18[i]))/(2*(MuEff4[i]-Mu2sIT18[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT18[i] = Znot;
            ZnotsIT18[i] = numpy.average([ZnotsIT17[i], Znot])

        if j == 18:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT19[i]))/(2*(MuEff4[i]-Mu2sIT19[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT19[i]))/(2*(MuEff4[i]-Mu2sIT19[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT19[i] = Znot;
            ZnotsIT19[i] = numpy.average([ZnotsIT8[i], Znot])

        if j == 19:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT20[i]))/(2*(MuEff4[i]-Mu2sIT20[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT20[i]))/(2*(MuEff4[i]-Mu2sIT20[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT20[i] = Znot;
            ZnotsIT20[i] = numpy.average([ZnotsIT19[i], Znot])

        if j == 20:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT21[i]))/(2*(MuEff4[i]-Mu2sIT21[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT21[i]))/(2*(MuEff4[i]-Mu2sIT21[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT21[i] = Znot;
            ZnotsIT21[i] = numpy.average([ZnotsIT20[i], Znot])

        if j == 21:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT22[i]))/(2*(MuEff4[i]-Mu2sIT22[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT22[i]))/(2*(MuEff4[i]-Mu2sIT22[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT22[i] = Znot;
            ZnotsIT22[i] = numpy.average([ZnotsIT21[i], Znot])
        if j == 22:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT23[i]))/(2*(MuEff4[i]-Mu2sIT23[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT23[i]))/(2*(MuEff4[i]-Mu2sIT23[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT23[i] = Znot;
            ZnotsIT23[i] = numpy.average([ZnotsIT22[i], Znot])

        if j == 23:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT24[i]))/(2*(MuEff4[i]-Mu2sIT24[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT24[i]))/(2*(MuEff4[i]-Mu2sIT24[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT24[i] = Znot;
            ZnotsIT24[i] = numpy.average([ZnotsIT23[i], Znot])

        if j == 24:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT25[i]))/(2*(MuEff4[i]-Mu2sIT25[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT25[i]))/(2*(MuEff4[i]-Mu2sIT25[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT25[i] = Znot;
            ZnotsIT25[i] = numpy.average([ZnotsIT24[i], Znot])

        if j == 25:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT26[i]))/(2*(MuEff4[i]-Mu2sIT26[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT26[i]))/(2*(MuEff4[i]-Mu2sIT26[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT26[i] = Znot;
            ZnotsIT26[i] = numpy.average([ZnotsIT25[i], Znot])

        if j == 26:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT27[i]))/(2*(MuEff4[i]-Mu2sIT27[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT27[i]))/(2*(MuEff4[i]-Mu2sIT27[i]));
                    
            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT27[i] = Znot;
            ZnotsIT27[i] = numpy.average([ZnotsIT26[i], Znot])
    

        if j == 27:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT28[i]))/(2*(MuEff4[i]-Mu2sIT28[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT28[i]))/(2*(MuEff4[i]-Mu2sIT28[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT28[i] = Znot;
            ZnotsIT28[i] = numpy.average([ZnotsIT27[i], Znot])
            
        if j == 28:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT29[i]))/(2*(MuEff4[i]-Mu2sIT29[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT29[i]))/(2*(MuEff4[i]-Mu2sIT29[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT29[i] = Znot;
            ZnotsIT29[i] = numpy.average([ZnotsIT28[i], Znot])

        if j == 29:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT30[i]))/(2*(MuEff4[i]-Mu2sIT30[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT30[i]))/(2*(MuEff4[i]-Mu2sIT30[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT30[i] = Znot;
            ZnotsIT30[i] = numpy.average([ZnotsIT29[i], Znot])

        if j == 30:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT31[i]))/(2*(MuEff4[i]-Mu2sIT31[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT31[i]))/(2*(MuEff4[i]-Mu2sIT31[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT31[i] = Znot;
            ZnotsIT31[i] = numpy.average([ZnotsIT30[i], Znot])

        if j == 31:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT32[i]))/(2*(MuEff4[i]-Mu2sIT32[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT32[i]))/(2*(MuEff4[i]-Mu2sIT32[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT32[i] = Znot;
            ZnotsIT32[i] = numpy.average([ZnotsIT31[i], Znot])

        if j == 32:
            ZnotB = (t6*(MuEff6[i]-Mu2sIT33[i]))/(2*(MuEff4[i]-Mu2sIT33[i]));
   
            ZnotC = (t10*(MuEff10[i]-Mu2sIT33[i]))/(2*(MuEff4[i]-Mu2sIT33[i]));

            Znot  = (ZnotB + ZnotC)/2;
            #ZnotsIT33[i] = Znot;
            ZnotsIT33[i] = numpy.average([ZnotsIT32[i], Znot])

#print parameter values
print 'Wavelength \t\tMu2sIT0 \t\tMu2sIT1 \t\tMu2sIT2 \t\tMu2sIT3 \t\tMu2sIT4 \t\tMu2sIT5 \t\tMu2sIT6 \t\tMu2sIT7 \t\tMu2sIT8 \t\tMu2sIT9 \t\tMu2sIT10 \t\tMu2sIT11 \t\tMu2sIT12 \t\tMu2sIT13 \t\tMu2sIT14 \t\tMu2sIT15 \t\tMu2sIT16 \t\tMu2sIT17 \t\tMu2sIT18 \t\tMu2sIT19 \t\tMu2sIT20 \t\tMu2sIT21 \t\tMu2sIT22 \t\tMu2sIT23 \t\tMu2sIT24 \t\tMu2sIT25 \t\tMu2sIT26 \t\tMu2sIT27 \t\tMu2sIT28 \t\tMu2sIT29 \t\tMu2sIT30 \t\tMu2sIT31 \t\tMu2sIT32 \t\tMu2sIT33 \t\tZnotsIT0 \t\tZnotsIT1 \t\tZnotsIT2 \t\tZnotsIT3 \t\tZnotsIT4 \t\tZnotsIT5 \t\tZnotsIT6 \t\tZnotsIT7 \t\tZnotsIT8 \t\tZnotsIT9 \t\tZnotsIT10 \t\tZnotsIT11 \t\tZnotsIT12 \t\tZnotsIT13 \t\tZnotsIT14 \t\tZnotsIT15 \t\tZnotsIT16 \t\tZnotsIT17 \t\tZnotsIT18 \t\tZnotsIT19 \t\tZnotsIT20 \t\tZnotsIT21 \t\tZnotsIT22 \t\tZnotsIT23 \t\tZnotsIT24 \t\tZnotsIT25 \t\tZnotsIT26 \t\tZnotsIT27 \t\tZnotsIT28 \t\tZnotsIT29 \t\tZnotsIT30 \t\tZnotsIT31 \t\tZnotsIT32 \t\tZnotsIT33'

for w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33 in zip(Waves,Mu2sIT0,Mu2sIT1,Mu2sIT2,Mu2sIT3,Mu2sIT4,Mu2sIT5,Mu2sIT6,Mu2sIT7,Mu2sIT8,Mu2sIT9,Mu2sIT10,Mu2sIT11,Mu2sIT12,Mu2sIT13,Mu2sIT14,Mu2sIT15,Mu2sIT16,Mu2sIT17,Mu2sIT18,Mu2sIT19,Mu2sIT20,Mu2sIT21,Mu2sIT22,Mu2sIT23,Mu2sIT24,Mu2sIT25,Mu2sIT26,Mu2sIT27,Mu2sIT28,Mu2sIT29,Mu2sIT30,Mu2sIT31,Mu2sIT32,Mu2sIT33,ZnotsIT0,ZnotsIT1,ZnotsIT2,ZnotsIT3,ZnotsIT4,ZnotsIT5,ZnotsIT6,ZnotsIT7,ZnotsIT8,ZnotsIT9,ZnotsIT10,ZnotsIT11,ZnotsIT12,ZnotsIT13,ZnotsIT14,ZnotsIT15,ZnotsIT16,ZnotsIT17,ZnotsIT18,ZnotsIT19,ZnotsIT20,ZnotsIT21,ZnotsIT22,ZnotsIT23,ZnotsIT24,ZnotsIT25,ZnotsIT26,ZnotsIT27,ZnotsIT28,ZnotsIT29,ZnotsIT30,ZnotsIT31,ZnotsIT32,ZnotsIT33):
    print "%.3f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f\t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f \t\t%.5f" % ( w,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30,z31,z32,z33)
