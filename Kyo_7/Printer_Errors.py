def printer_error(s):
    allowed = "abcdefghijklm"
    error = 0
    
    for i in s:
        if i not in allowed:
            error += 1
        
    return f"{error}/{len(s)}"
        


# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python