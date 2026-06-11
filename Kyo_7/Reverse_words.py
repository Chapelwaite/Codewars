def reverse_words(text):
    result = ""
    word = ""
    
    for char in text:
        if char != " ":
            word += char
        else:
            result += word[::-1]
            result += " "
            word = ""
    
    result += word[::-1]
    
    return result

# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python