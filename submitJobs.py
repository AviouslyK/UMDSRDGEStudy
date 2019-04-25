#!/usr/bin/python
import os, sys
import shlex, subprocess
from datetime import datetime, date, time
from time import sleep
import shutil
import numpy as np   
#sys.path.append(os.path.abspath(os.path.curdir))

sTag_temp = "wave_update_test"

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

#starting and ending wavelength
Initial = 3.0996

Final = 2.0664

waveNUM = 10

#array that contains the different wavelengths being tested                          
#Arr = [3.5424, 3.4925, 3.4440, 3.3968, 3.3509, 3.3062, 3.2627, 3.2204, 3.1791, 3.1629, 3.1468, 3.1388, 
#       3.1309, 3.1230, 3.1152, 3.0996, 3.0842, 3.0689, 3.0538, 3.0388, 3.0240, 3.0093, 2.9948, 2.9876, 
#       2.9520, 2.8834, 2.8178, 2.7552, 2.6953, 2.6380, 2.5830, 2.5303, 2.4797, 2.4311, 2.3843, 2.3393, 
#       2.2960, 2.2543, 2.2140, 2.1752];

#Fill array with random numbers between 0 and 100,000 to be used as random seeds
ArrRand = np.random.randint(1000000, size=200)
#starting seed 
startingseed1 = 98110
startingseed2 = 72722


Arr = np.linspace(Initial,Final,num=waveNUM)
pauser = 1;
for q in range(0,len(Arr)):




################################################################
################## For Changing AbsLength ######################
################################################################

#initial absorption length
#AbsIN = 0.01

#final absorption length
#AbsFI = 100

#total number of jobs being submitted 
#jobNUM = 6000

#array that contains the different abs lengths being tested                          
#Arr = np.linspace(AbsIN,AbsFI,num=jobNUM)


#range to loop over
#myrange = 100



#pauser = 1;
#for q in range(myrange):
#for q in range(0,len(Arr)):
 
#Arr = np.linspace(Initial,Final,num=waveNUM)
#pauser = 1;
#for q in range(0,len(Arr)):

    #if (pauser % 1 == 0 and pauser !=1):
        #sleep(10);

    #if (pauser % 10 == 0 and pauser !=1):
        #sleep(20)
    #sleep(1)
    pauser = pauser + 1; 
    # Creating new file                                                              
    shutil.copy2('photontest.mac', 'photest' '%s' '.mac' % q)

    # Reading in the file                                                            
    with open('photest' '%s' '.mac' % q, 'r') as file :
        filedata = file.read()

    # Replacing the target string
        a = str(startingseed1)
        b = str(ArrRand[2*q])
        k = str(startingseed2)
        l = str(ArrRand[2*q+1])
        j = str(Arr[q])
        i = str(Initial) # use if scanning wavelength
        #i = str(AbsIN) # use if scanning abslength
    
        filedata = filedata.replace(i, j)
        filedata = filedata.replace(k,l)
        filedata = filedata.replace(a,b)

    # Writing out the new file                                                       
    with open('photest' '%s' '.mac' % q, 'w') as file:
        file.write(filedata)



    # Normally at the Beginning of Script:


    # Defining the infile                                                            
    InFile = 'photest' '%s' '.mac' % q 
    #sTag = '%s' '%s' % sTag,q
    sTag = '%s' '%s' % (sTag_temp, q)
    
    
    JobTime = datetime.now()
    fTag = JobTime.strftime("%Y%m%d_%H%M%S")
    dirname = "jobs/%s_%s"%(sTag,fTag)
    DetType = "1" #rod
    logFile = "0424.log"


    try:
        os.makedirs(dirname)
    except:
        pass

    ProdTag = "Run3_20190424"
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



    kw = {}

    kw["MYPREFIX"]  = ProdTag
    kw["WORKDIR"]   = WorkDir
    kw["OUTDIR"]    = OutDir
    kw["INPUT"]     = InFile
    kw["FILENAME"]  = sTag # add _q
    kw["DETTYPE"]   = DetType
    kw["LOGFILE"]   = logFile

    script_str = condor_script_template % kw
    f = open("%s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag_temp), 'w')
    f.write(script_str)
    f.close()

    condorcmd = "condor_submit %s/condor_jobs_%s_G4Sim.jdl"%(dirname,sTag_temp)
    #print 'condorcmd: ', condorcmd
    print ('Executing condorcmd %s' % str(q))

    p=subprocess.Popen(condorcmd, shell=True)
    p.wait()
   
    
    print "\n"
    #sleep(500);
    #print "Histos output dir: %s/%s"%(OutDir,ProdTag)

print(Arr)
