def find_outlier(integers):
    first_three = integers[:3]

    even_count = 0
    odd_count = 0

    for num in first_three:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1


    if even_count > odd_count:
        for num in integers:
            if num % 2 != 0:
                return num

    else:
        for num in integers:
            if num % 2 == 0:
                return num
            


# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python