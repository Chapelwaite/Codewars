def to_jaden_case(string):
    splitted_string = string.split()
    new_string = []
    
    for i in splitted_string:
        new_string.append(i.capitalize())
        
        
    return " ".join(new_string)



# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python