#makes a tree from a delimited text file with columns of data (generated from delimiter.py)
from ROOT import TFile, TTree, TH2F, TGraph, TCanvas
import sys

dirname = sys.argv[1]
fname   = sys.argv[2]


ifname = dirname.rstrip("/") + "/" + fname 
outdir = dirname.rstrip("/") 

try:
    os.makedirs(outdir)
except:
    pass

ofname = outdir + "/" + fname.rstrip(".txt") + ".root"

#output file and tree
outfile = TFile(ofname,"RECREATE")
tree = TTree("tree","tree of "+fname)
outfile.cd()

#create tree from text file
desc = "MUEFFECTIVE:EFFICIENCY" #this gives names and types of variables
tree.ReadFile(ifname,desc) # delimiter = space
#tree.ReadFile(ifname,desc,",") # delimiter = comma



c1 = TCanvas("c1","c1",500,500);
tree.Draw("EFFICIENCY:MUEFFECTIVE>>MvsE") # draws MuE vs Eff and saves to histogram 
c1.SaveAs("MvsE.root")

#save output tree
tree.Write()
outfile.Close()

#print message
print "Created tree in root file: %s"%ofname
