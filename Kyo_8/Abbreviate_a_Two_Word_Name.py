def abbrev_name(name):
    word = name.split()
    
    
    first_name = word[0]
    last_name = word[1]
    
    first_initial = first_name[0]
    last_initial = last_name[0]
    
    first_initial = first_initial.upper()
    last_initial = last_initial.upper()
    
    initial = first_initial + "." + last_initial
    
    return initial


# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python