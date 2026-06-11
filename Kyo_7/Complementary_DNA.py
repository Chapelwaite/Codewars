def DNA_strand(dna):
    new_dna = ""
    
    
    for i in dna:
        if i == "A":
            new_dna += "T"
        elif i == "T":
            new_dna += "A"
        elif i == "C":
            new_dna += "G"
        elif i == "G":
            new_dna += "C"
            
    return new_dna


# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python