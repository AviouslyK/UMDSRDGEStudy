#takes outputfile from submitjobs.py and formats it to work with maketree.py
import sys
import shutil
import fileinput
inFile = sys.argv[1]



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
