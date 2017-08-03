import numpy
#program to calculate Znot given values for Mu Effective

##############################################################################################
########################## Without scaling factor: ###########################################
######################### Does NOT consider base mu ##########################################
##############################################################################################
                                                                                          ####
#array that contains the different MuE1 values based on each Measurement (4 mm)           ####
#the first value is from the average of transmission values from data                     ####
#the second and third values are for each of the individual transmission values from data ####
Arr1 = [0.019732, 0.0197657, 0.0196875]                                                   ####   
                                                                                          ####
#array that contains the different MuE2 values based on each Measurement (6 mm)           ####
Arr2 = [0.0174, 0.0172835, 0.0175252]                                                     ####
                                                                                          ####
#array that contains the different MuE3 values based on each Measurement (8 mm)           ####
Arr3 = [0.015745, 0.0157487, 0.0157424]                                                   ####
                                                                                          ####  
##############################################################################################
##############################################################################################


##############################################################################################
########################## WITH scaling factor: ##############################################
##############################################################################################
                                                                                          ####
#array that contains the different MuE1 values based on each Measurement (4 mm)           ####
#the first value is from the average of transmission values from data                     ####
#the second and third values are for each of the individual transmission values from data ####
Arr4 = [0.0185106, 0.0185529, 0.0184707]                                                  ####   
                                                                                          ####
#array that contains the different MuE2 values based on each Measurement (6 mm)           ####
Arr5 = [0.016123, 0.0159874, 0.0162499]                                                   ####
                                                                                          ####
#array that contains the different MuE3 values based on each Measurement (8 mm)           ####
Arr6 = [0.016016, 0.0160196, 0.0160147]                                                   ####
                                                                                          ####  
##############################################################################################
##############################################################################################
Znots = [None]*27;
Mu1s  = [None]*27;
Mu2s  = [None]*27;
counter = 0;
for i in range(len(Arr4)):
    for j in range(len(Arr5)):
        for k in range(len(Arr6)):
            Znot = (-2*Arr4[i]+12*Arr5[j]-12*Arr6[k])/(3*Arr5[j]-4*Arr6[k]);
            Znots[counter] = Znot;
            Mu1 = 2*Arr4[i]/Znot;
            Mu1s[counter] = Mu1;
            Mu2 = (Arr5[j] - Znot*Mu1/3)/(1-(Znot/6));
            Mu2s[counter] = Mu2;
            #print("\n\nFor MuE values of:")
            #print Arr4[i], Arr5[j], Arr6[k];
            #print ("Znot is %s" % str(Znot))
            counter = counter + 1;


Znot = sum(Znots)/len(Znots);
Mu1  = sum(Mu1s)/len(Mu1s);
Mu2  = sum(Mu2s)/len(Mu2s);
print ("\n\n");
print "Znot is ", Znot, " plus or minus ", numpy.std(Znots);
print "Mu1 is ", Mu1, " plus or minus ", numpy.std(Mu1s);
print "Mu2 is ", Mu2, " plus or minus ", numpy.std(Mu2s);
