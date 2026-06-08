def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    positive_count = 0
    negative_sum = 0
    new_arr = []
    
    for i in arr:
        if i > 0:
            positive_count += 1

        elif i < 0:
            negative_sum += i
            
    new_arr.append(positive_count)
    new_arr.append(negative_sum)
    
    return new_arr





# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python