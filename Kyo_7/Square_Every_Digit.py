def square_digits(num):
    result = ""

    for i in str(num):
        square = int(i) ** 2
        result += str(square)

    return int(result)


# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python