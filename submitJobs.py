#!/usr/bin/python
import os, sys
import shlex, subprocess
from datetime import datetime, date, time
from time import sleep
import shutil
#sys.path.append(os.path.abspath(os.path.curdir))

JobTime = datetime.now()
fTag = JobTime.strftime("%Y%m%d_%H%M%S")
sTag = "run10"
dirname = "jobs/%s_%s"%(sTag,fTag)
DetType = "1" #rod
logFile = "0606.log"

try:
    os.makedirs(dirname)
except:
    pass

ProdTag = "run10_20170606"
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
Arguments = %(WORKDIR)s %(INPUT)s %(FILENAME)s %(DETTYPE)s %(LOGFILE)s
Queue 1
 
"""
######################%(WORKDIR)s %(INPUT)s %(FILENAME)s %(DETTYPE)s###################
# %(OUTDIR)s/%(MYPREFIX)s/

Abs = 199
counter = 1  
for counter in range (1,10):
    #Abs = Abs + 1
    #counter = counter + 1
    #Copy photontet to a new dummy file
    shutil.copy2('photontest.mac', 'photest' '%s' '.mac' % counter)
    
    # Read in the file
    with open('photest' '%s' '.mac' % counter, 'r') as file :
        filedata = file.read()

        # Replace original abslength with abslength + counter 
    AbsPlusSome = Abs + counter
    j = str(AbsPlusSome)
    i = str(Abs)
    filedata = filedata.replace(i, j)

    # Write the file out again
    with open('photest' '%s' '.mac' % counter, 'w') as file:
        file.write(filedata)

    # Define new infile
    InFile = 'photest' '%s' '.mac' % counter
     
    
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
    print 'condorcmd: ', condorcmd
    print ('Executing condorcmd %s' % str(counter))

    p=subprocess.Popen(condorcmd, shell=True)
    p.wait()
   
        
    print "\n"
    print "Histos output dir: %s/%s"%(OutDir,ProdTag)

#########################
### in separate script###
#num = counter
#counter2 = 0
# Now delete the dummy files
#while (counter2 < num):
#    counter2 = counter2 + 1
#    os.remove('photest' '%s' '.mac' % counter2)
