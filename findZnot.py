import numpy
#program to calculate Znot given values for Mu Effective

##############################################################################################
########################## Without scaling factor: ###########################################
######################### Does NOT consider base mu ##########################################
##############################################################################################
                                                                                          ####
#array that contains the different MuE values based on each Measurement (4 mm)           ####
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
#array that contains the different MuE values based on each Measurement (4 mm)            ####
#the first value is from the average of transmission values from data                     ####
#the second and third values are for each of the individual transmission values from data ####
#MuE4
MuEffective4 = [0.0185106, 0.0185529, 0.0184707]                                                  ####   
                                                                                          ####
#array that contains the different MuE values based on each Measurement (6 mm)           ####
#MuE3
MuEffective3 = [0.016123, 0.0159874, 0.0162499]                                                   ####
                                                                                          ####
#array that contains the different MuE values based on each Measurement (8 mm)           ####
#MuE2 BAD DATA
#Arr6 = [0.016016, 0.0160196, 0.0160147]                                                  ####
#array that contains the different MuE values based on each Measurement (10 mm)           ####
#MuE1

MuEffective1 = [0.01234, 0.01215, 0.01254]                                                        ####
                                                                                          ####  
##############################################################################################
##############################################################################################

t1    = 10
t2    = 8
t3    = 6
t4    = 4
Znots = [None]*27;
Mu1s  = [None]*27;
Mu2s  = [None]*27;
MuE2s = [None]*27;
counter = 0;
for i in range(len(MuEffective4)):
    for j in range(len(MuEffective3)):
        for k in range(len(MuEffective1)):
            Mu1 = MuEffective4[i];
            Mu1s[counter] = Mu1;

            Mu2 = (MuEffective3[j]*t3-MuEffective1[k]*t1)/(t3-t1);
            Mu2s[counter] = Mu2;
            

            Znot = 0.5*t3*(MuEffective3[j]-Mu2)/(MuEffective4[i]-Mu2);
            Znots[counter] = Znot; 

            MuE2 = Mu2 + (2*Znot/t2*(Mu1-Mu2));
            MuE2s[counter] = MuE2;

            print MuE2, "\n";
            counter = counter + 1;


Znot = sum(Znots)/len(Znots);
Mu1  = sum(Mu1s)/len(Mu1s);
Mu2  = sum(Mu2s)/len(Mu2s);
MuE2 = sum(MuE2s)/len(MuE2s);
print ("\n\n");
print "Znot is ", Znot, " plus or minus ", numpy.std(Znots);
print "Mu1 is ", Mu1, " plus or minus ", numpy.std(Mu1s);
print "Mu2 is ", Mu2, " plus or minus ", numpy.std(Mu2s);
