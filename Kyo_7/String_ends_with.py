def solution(text, ending):
    len_ending = len(ending)
    
    if text[-len_ending:] == ending:
        return True
    else:
        return False
    


# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python