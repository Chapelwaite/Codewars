def century(year):
    if year % 100 == 0:
        return year//100
    else:
        return year//100 + 1
    

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python