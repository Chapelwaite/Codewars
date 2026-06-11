def nb_year(p0, percent, aug, p):
    i = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent/100) + aug)
        i += 1
        
    return i

# https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python