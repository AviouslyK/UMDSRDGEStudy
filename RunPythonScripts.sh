#!/bin/bash

#use this as the executable in singlesubmitjobs.py 
# setup CMSSW software environment at UMD
export VO_CMS_SW_DIR=/sharesoft/cmssw
. $VO_CMS_SW_DIR/cmsset_default.sh
cd /home/kahn/PhysHonr268n/CMSSW_5_3_30/Research/G4/honrgeant/UMDSRDGEStudy-build/
eval `scramv1 runtime -sh`


#python /home/kahn/PhysHonr268n/CMSSW_5_3_30/Research/G4/honrgeant/UMDSRDGEStudy-build/CalMuSpectrum.py
python CalMuSpectrum.py
