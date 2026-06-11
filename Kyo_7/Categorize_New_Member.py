def open_or_senior(data):
    data1 = []
    
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            data1.append("Senior")
        else:
            data1.append("Open")
            
    return data1



# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python