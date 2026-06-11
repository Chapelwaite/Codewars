# P.s. ვარჯიშობ მაგიტო ვწერ გრძლად

# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    
    
    Last_four = cc[-4:]
    Without_four = cc[:-4]
    new_list = ""
    
    new_list += "#" * len(Without_four)
    
    return new_list + Last_four
        
#  https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python