def are_you_playing_banjo(name):
    first_latter = name[0]
    lfirst_latter = first_latter.lower()
    
    if lfirst_latter == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    

# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python