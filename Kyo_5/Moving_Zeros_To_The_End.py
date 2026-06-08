def move_zeros(lst):
    new_lst = []
    zero = []
    
    
    for i in lst:
        if i == 0:
            zero.append(i)
        else:
            new_lst.append(i)
            
    return new_lst + zero


#  https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python