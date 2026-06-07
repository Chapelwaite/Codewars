def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True

    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True

    else:
        return False
    

# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python