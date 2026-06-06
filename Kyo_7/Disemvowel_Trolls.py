def disemvowel(string_):
    result = ""
    vowels = "aeiouAEIOU"
    
    for char in string_:
        if char not in vowels:
            result += char
            
    return result


# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python