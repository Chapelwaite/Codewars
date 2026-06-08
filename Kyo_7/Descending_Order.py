def descending_order(num):
    num = str(num)
    digit = []
    
    for i in num:
        digit.append(i)
        
    digit.sort()
    digit.reverse()
    
    answer = "".join(digit)
    

    
    return int(answer)


# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python