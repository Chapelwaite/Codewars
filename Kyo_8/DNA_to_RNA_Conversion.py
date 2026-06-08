def dna_to_rna(dna):
    RNA = ""
    
    for i in dna:
        if i == "T":
            RNA += "U"
        else:
            RNA += i
    return RNA
            

# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python