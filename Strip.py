with open("cleaned_10mm_for_fit.txt", "r") as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty                                                                                               
            print(cleanedLine)
