#!/usr/bin/python
import os, sys
import shlex, subprocess
from datetime import datetime, date, time
from time import sleep
import shutil
import numpy as np   
#sys.path.append(os.path.abspath(os.path.curdir))

JobTime = datetime.now()
fTag = JobTime.strftime("%Y%m%d_%H%M%S")
sTag = "8mm_Fit"
dirname = "jobs/%s_%s"%(sTag,fTag)
DetType = "1" #rod
logFile = "0705.log"

try:
    os.makedirs(dirname)
except:
    pass

ProdTag = "Run1_20180705"
OutDir  = "/home/kahn/PhysHonr268n/CMSSW_5_3_30/Research/G4/honrgeant/UMDSRDGEStudy-build/Absdata"
WorkDir = "/home/kahn/PhysHonr268n/CMSSW_5_3_30/Research/G4/honrgeant/UMDSRDGEStudy-build/"

try:
    os.makedirs(OutDir)
except:
    pass

try:
    os.makedirs(OutDir+"/"+ProdTag)
except:
    pass

try:    os.makedirs(OutDir+"/"+ProdTag+"/logs")
except:
    pass



#########################################
#make sure OutDir is the same in main.cc
#########################################
condor_script_template = """
universe = vanilla
Executable = ./CMS.sh
+IsLocalJob = true
Should_transfer_files = NO
Requirements = TARGET.FileSystemDomain == "privnet"
Output = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).stdout
Error  = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).stderr
Log    = %(OUTDIR)s/%(MYPREFIX)s/logs/%(FILENAME)s_sce_$(cluster)_$(process).condor
Arguments = %(WORKDIR)s %(INPUT)s %(FILENAME)s %(DETTYPE)s 
Queue 1
 
"""
######################    %(LOGFILE)s  ###################
# %(OUTDIR)s/%(MYPREFIX)s/


#################################################################
################## For Changing Wavelength ######################
#################################################################

#starting and ending wavelenght
#Initial = 3.0240

#Final = 2.5564

#waveNUM = 50

#array that contains the different wavelengths being tested                          
#Arr = [3.0240, 3.0166, 3.0093, 3.0020, 2.9948, 2.9876, 2.9804, 2.9732, 2.9661, 2.9591, 
#       2.9520, 2.9450, 2.9380, 2.9311, 2.9242, 2.9173, 2.9104, 2.9036, 2.8968, 2.8901, 
#       2.8834, 2.8767, 2.8700, 2.8634, 2.8568, 2.8502, 2.8437, 2.8372, 2.8307, 2.8242, 
#       2.8178, 2.8114, 2.8051, 2.7987, 2.7924, 2.7862, 2.7799, 2.7737, 2.7675, 2.7613, 
#       2.7552, 2.7491, 2.7430, 2.7370, 2.7309, 2.7249, 2.7190, 2.7130, 2.7071, 2.7012, 
#       2.6953, 2.6895, 2.6836, 2.6778, 2.6721, 2.6663, 2.6606, 2.6549, 2.6492, 2.6436, 
#       2.6380, 2.6324, 2.6268, 2.6212, 2.6157, 2.6102, 2.6047, 2.5992, 2.5938, 2.5884, 
#       2.5830, 2.5776, 2.5723, 2.5670, 2.5617, 2.5564];


#Arr = [3.542, 3.493, 3.444, 3.397, 3.351, 3.306, 3.263, 3.22, 3.179, 3.139, 
#       3.1, 3.061, 3.024, 2.988, 2.952, 2.917, 2.883, 2.85, 2.818, 2.786, 2.755, 
#       2.725, 2.695, 2.666, 2.638];

#Arr = [3.542, 3.493, 3.444, 3.397, 3.351, 3.306, 3.263, 3.220, 3.179, 3.163, 3.155, 3.147, 
#       3.139, 3.131, 3.123, 3.115, 3.107, 3.100, 3.092, 3.084, 3.077, 3.069, 3.061, 3.054, 
#       3.046, 3.039, 3.031, 3.024, 3.017, 3.009, 3.002, 2.995, 2.988, 2.952, 2.883, 2.818, 
#       2.755, 2.695, 2.638, 2.583, 2.530, 2.480, 2.431, 2.384, 2.339, 2.296, 2.254, 2.214, 
#       2.175, 2.138];

#Arr = [3.5424, 3.4925, 3.4440, 3.3968, 3.3509, 3.3062, 3.2627, 3.2204, 3.1791, 3.1629, 3.1468, 3.1388, 
#       3.1309, 3.1230, 3.1152, 3.0996, 3.0842, 3.0689, 3.0538, 3.0388, 3.0240, 3.0093, 2.9948, 2.9876, 
#       2.9520, 2.8834, 2.8178, 2.7552, 2.6953, 2.6380, 2.5830, 2.5303, 2.4797, 2.4311, 2.3843, 2.3393, 
#       2.2960, 2.2543, 2.2140, 2.1752];

#Arr = np.linspace(Initial,Final,num=waveNUM)
#pauser = 1;
#for q in range(0,len(Arr)):




################################################################
################## For Changing AbsLength ######################
################################################################

#initial absorption length
AbsIN = 0.1

#final absorption length
AbsFI = 20

#total number of jobs being submitted 
jobNUM = 1000

#array that contains the different abs lengths being tested                          
Arr = np.linspace(AbsIN,AbsFI,num=jobNUM)

#Fill array with random numbers between 0 and 100,000 to be used as random seeds
#ArrRand = np.random.randint(1000000, size=200)

#range to loop over
#myrange = 100

#starting seed 
#startingseed1 = 98110
#startingseed2 = 72722


pauser = 1;
#for q in range(myrange):
for q in range(0,len(Arr)):
    
    if (pauser % 1 == 0 and pauser !=1):
        sleep(15);

    if (pauser % 15 == 0 and pauser !=1):
        sleep(60);

    pauser = pauser + 1; 
    # Creating new file                                                              
    shutil.copy2('photontest.mac', 'photest' '%s' '.mac' % q)

    # Reading in the file                                                            
    with open('photest' '%s' '.mac' % q, 'r') as file :
        filedata = file.read()

    # Replacing the target string
        #a = str(startingseed1)
        #b = str(ArrRand[2*q])
        #k = str(startingseed2)
        #l = str(ArrRand[2*q+1])
        j = str(Arr[q])
        #i = str(Initial)
        i = str(AbsIN)
    
        filedata = filedata.replace(i, j)
        #filedata = filedata.replace(k,l)
        #filedata = filedata.replace(a,b)

    # Writing out the new file                                                       
    with open('photest' '%s' '.mac' % q, 'w') as file:
        file.write(filedata)

    # Defining the infile                                                            
    InFile = 'photest' '%s' '.mac' % q 
    
    kw = {}

    kw["MYPREFIX"]  = ProdTag
    kw["WORKDIR"]   = WorkDir
    kw["OUTDIR"]    = OutDir
    kw["INPUT"]     = InFile
    kw["FILENAME"]  = sTag
    kw["DETTYPE"]   = DetType
    kw["LOGFILE"]   = logFile

    script_str = condor_script_template % kw
    f = open("%s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag), 'w')
    f.write(script_str)
    f.close()

    condorcmd = "condor_submit %s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag)
    #print 'condorcmd: ', condorcmd
    print ('Executing condorcmd %s' % str(q))

    p=subprocess.Popen(condorcmd, shell=True)
    p.wait()
   
    
    print "\n"
    #sleep(500);
    #print "Histos output dir: %s/%s"%(OutDir,ProdTag)

print(Arr)
