def binary_array_to_number(arr):
    binary_string = ""
    
    for i in arr:
        binary_string += str(i)
    
    return int(binary_string, 2)

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python