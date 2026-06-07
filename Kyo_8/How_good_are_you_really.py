def better_than_average(class_points, your_points):
    total = 0
    
    for i in class_points:
        total = total + i
        
    average = total/len(class_points)
    if average < your_points:
        return True
    else:
        return False
    


# https://www.codewars.com/kata/5601409514fc93442500010b/train/python