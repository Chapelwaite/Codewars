def fake_bin(x):
    result = ""

    for i in x:
        number = int(i)

        if number < 5:
            result += "0"
        else:
            result += "1"

    return result


# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python