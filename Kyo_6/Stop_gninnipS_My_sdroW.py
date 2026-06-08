def spin_words(sentence):
    sentence = sentence.split()
    new_sentence = []
    
    for i in sentence:
        if len(i) >= 5:
            i = i[::-1]
            
        new_sentence.append(i)
        
    return " ".join(new_sentence)


# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python