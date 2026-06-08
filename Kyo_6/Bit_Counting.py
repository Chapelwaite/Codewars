def count_bits(n):
    n_bin = bin(n)
    sum = 0
    
    for i in n_bin:
        sum += 1
    
    return sum


# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python