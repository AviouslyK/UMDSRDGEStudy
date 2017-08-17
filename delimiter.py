#takes outputfile from submitjobs.py and formats it to work with maketree.py
import sys
import shutil
import fileinput
inFile = sys.argv[1]

#reading in messy data
#with open(inFile, 'r') as file :
#        filedata = file.read()

# Creating new file                                                              
#shutil.copy2(inFile, 'CleanSimData.txt')

# Reading in the file                                                            
#with open('CleanSimData.txt','r') as file :
#    filedata = file.read()

# Removing messy text                                                
#mess  = "#Mu_tile [cm^-1]Mu_fiber [cm^-1]Efficiency"
#filedata = filedata.replace(mess, "");

# Writing out the new file                                                       
#with open('CleanSimData.txt', 'w') as file:
#    file.write(filedata)


###############################################3


outfile = "cleaned_file.txt"

#cleans file
delete_list = ["#","Mu_tile", "[cm^-1]", "Efficiency", "Mu_fiber"]
fin = open(inFile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "") #erases words
        if not line.strip(): continue #doesn't write blank lines to output
    fout.write(line)
fin.close()
fout.close()
