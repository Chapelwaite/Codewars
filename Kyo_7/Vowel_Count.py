def get_count(sentence):
    count = 0
    vowels = "aeiou"

    for char in sentence:
        if char in vowels:
            count += 1

    return count

# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python