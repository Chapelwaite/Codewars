def accum(st):
    new_st = []

    for i, char in enumerate(st):
        new_word = char.upper() + char.lower() * i
        new_st.append(new_word)

    return "-".join(new_st)


# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python