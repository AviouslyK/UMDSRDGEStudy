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
sTag = "10mmDataCollection"
dirname = "jobs/%s_%s"%(sTag,fTag)
DetType = "1" #rod
logFile = "0629.log"

try:
    os.makedirs(dirname)
except:
    pass

ProdTag = "Run1_20170706"
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

try:
    os.makedirs(OutDir+"/"+ProdTag+"/logs")
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

#starting and ending wavelenght
#Initial = 2.1

#Final = 3.6

#waveNUM = 35
#array that contains the different wavelengths being tested                          
#Arr = np.linspace(Initial,Final,num=waveNUM)

#Arr = [2.9590, 2.9520, 2.9450, 2.9380, 2.9311, 2.9242, 2.9173, 2.8833, 2.8502, 2.8178, 2.7862, 
#       2.7552, 2.7249, 2.6953, 2.6663, 2.6380, 2.6102, 2.5830, 2.5564, 2.5303, 2.5047, 2.4797, 
#       2.4551, 2.4311, 2.4075, 2.3843, 2.3616, 2.3393, 2.3175, 2.2960, 2.2749, 2.2543] 


#3.5424, 3.4925, 3.4440, 3.3968, 3.3509, 3.3062, 3.2627, 3.2204, 3.2037, 3.1955, 3.1791, 
 #      3.1709, 3.1629, 3.1548, 3.1468, 3.1388, 3.1309, 3.1230, 3.1152, 3.1074, 3.0996, 3.0919, 
  #     3.0842, 3.0765, 3.0689, 3.0613, 3.0538, 3.0463, 3.0388, 3.0314, 3.0240, 3.0166, 3.0093, 
   #    3.0020, 2.9948, 2.9876, 2.9804, 2.9732, 2.9661



#for q in range(0,len(Arr)):

#initial absorption length
AbsIN = 4.0

#final absorption length
AbsFI = 6.0

#total number of jobs being submitted 
jobNUM = 175

#array that contains the different abs lengths being tested                          
Arr = np.linspace(AbsIN,AbsFI,num=jobNUM)

for q in range(len(Arr)):
    
    # Creating new file                                                              
    shutil.copy2('photontest.mac', 'photest' '%s' '.mac' % q)

    # Reading in the file                                                            
    with open('photest' '%s' '.mac' % q, 'r') as file :
        filedata = file.read()

    # Replacing the target string                                                    
    j = str(Arr[q])
    #i = str(Initial)
    i = str(AbsIN)
    filedata = filedata.replace(i, j)

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
    #print "Histos output dir: %s/%s"%(OutDir,ProdTag)
