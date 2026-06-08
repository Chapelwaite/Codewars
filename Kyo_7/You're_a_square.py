def is_square(n):
    if n < 0:
        return False

    i = 0

    while i * i <= n:
        if i * i == n:
            return True
        i += 1

    return False


# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python