def pig_it(text):
    splited_text = text.split()
    new_text = []
    
    for i in splited_text:
        if i.isalpha():
            changed_word = i[1:] + i[0] + "ay"
            new_text.append(changed_word)
        else:
            new_text.append(i)
    
    return " ".join(new_text)



# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python