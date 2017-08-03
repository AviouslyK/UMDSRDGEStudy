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
sTag = "saved4mmDataCollection"
dirname = "jobs/%s_%s"%(sTag,fTag)
DetType = "1" #rod
logFile = "0731.log"

try:
    os.makedirs(dirname)
except:
    pass

ProdTag = "Run3_20170803"
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
#Initial = 3.542

#Final = 2.254

#waveNUM = 100

#array that contains the different wavelengths being tested                          
#Arr = np.linspace(Initial,Final,num=waveNUM)

#for q in range(0,len(Arr)):




################################################################
################## For Changing AbsLength ######################
################################################################

#initial absorption length
AbsIN = 0.5

#final absorption length
AbsFI = 50.0

#total number of jobs being submitted 
jobNUM = 1000

#array that contains the different abs lengths being tested                          
Arr = np.linspace(AbsIN,AbsFI,num=jobNUM)
# used to allow the submission of thousands of jobs, 20 at a time
pauser = 1;
for q in range(len(Arr)):
    
    if (pauser % 20 == 0):
        sleep(600);

    pauser = pauser + 1; 
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

#print(Arr)
