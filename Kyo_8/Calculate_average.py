def find_average(numbers):
    if numbers == []:
        return 0

    total = 0

    for i in numbers:
        total += i

    average = total / len(numbers)

    return average


# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python