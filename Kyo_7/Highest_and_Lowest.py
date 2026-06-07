def high_and_low(numbers):
    nums = numbers.split()
    nums = [int(i) for i in nums]

    highest = max(nums)
    lowest = min(nums)

    return str(highest) + " " + str(lowest)


# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python