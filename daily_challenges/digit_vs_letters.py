import re
def digits_or_letters(s):
    alpha_count = 0
    digit_count = 0
    re_word = re.sub(r'[^A-Za-z0-9]',"", s)
    for char in re_word:
        if char.isalpha():
            alpha_count += 1
        else:
            digit_count += 1

    if alpha_count > digit_count:
        return "letters"
    elif digit_count > alpha_count:
        return "digits"
    else:
        return "tie"

print(digits_or_letters("abc123!@#DEF"))

