def is_triangle(a, b, c):
    
    if (a+ b) > c and (a + c) > b and (c + b) > a:
        return True
    else:
        return False



# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python