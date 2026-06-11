def xo(s):
    cleaned_s = s.lower()
    
    new_string = ""
    
    for i in cleaned_s:
        if i == "x" or i == "o":
            new_string += i
    
    return new_string.count("x") == new_string.count("o")



# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python