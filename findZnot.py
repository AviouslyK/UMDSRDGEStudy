#program to calculate Znot given values for Mu Effective


#array that contains the different MuE1 values based on each Measurement (4 mm)
#the first value is from the average of transmission values from data
#the second and third values are for each of the individual transmission values from data
Arr1 = [0.019732, 0.0197657, 0.0196875]

#array that contains the different MuE2 values based on each Measurement (6 mm)
Arr2 = [0.0174, 0.0172835, 0.0175252]

#array that contains the different MuE3 values based on each Measurement (8 mm)
Arr3 = [0.015745, 0.0157487, 0.0157424]
 
counter = 1;
for i in range(len(Arr1)):
    for j in range(len(Arr2)):
        for k in range(len(Arr3)):
            Znot = (-2*Arr1[i]+12*Arr2[j]-12*Arr3[k])/(3*Arr2[j]-4*Arr3[k])
            print("\n\nFor MuE values of:")
            print Arr1[i], Arr2[j], Arr3[k];
            print ("\nZnot is %s" % str(Znot))
            counter = counter + 1;
