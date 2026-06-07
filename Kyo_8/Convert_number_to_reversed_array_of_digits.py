def digitize(n):
    arr = []
    
    n = str(n)
    n = n[::-1]
    
    for i in n:
        i = int(i)
        arr.append(i)
        
    return arr


# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python