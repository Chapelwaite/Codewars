def digital_root(n):
    while n >= 10:
        total = 0

        n_str = str(n)

        for i in n_str:
            i = int(i)
            total += i

        n = total

    return n


# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python