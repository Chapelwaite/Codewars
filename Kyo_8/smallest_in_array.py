def find_smallest_int(arr):
    min = arr[0]
    
    for i in arr:
        if min >= i:
            min = i
            
    return min


# www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python