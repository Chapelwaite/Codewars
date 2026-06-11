def duplicate_count(text):
    text = text.lower()
    
    seen = set()
    duplicates = set()
    
    for i in text:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
            
    return len(duplicates)


# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python