def is_isogram(string):
    arr = []
    cleaned_string = string.lower()
    
    for char in cleaned_string:
        arr.append(char)
        
    if len(set(arr)) == len(arr):
        return True
    else:
        return False
    

# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python