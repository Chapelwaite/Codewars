def get_sum(a,b):
    sum = 0
    start = min(a, b)
    stop = max(a, b)
    
    if a == b:
        return a
    else:
        for i in range(start, stop + 1):
            sum += i
            
        return sum
    
    
        
        
    


# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python