def is_balanced(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    first_half_count = 0
    second_half_count = 0
    mid = len(s) // 2
    s = s.lower()

    first_half_char = s[:mid]
    second_half_char = s[mid if len(s) % 2 == 0 else mid+1:]

    for char in first_half_char:
        if char in vowels:
            first_half_count += 1


    for char in second_half_char:
        if char in vowels:
            second_half_count += 1

    return first_half_count == second_half_count
        

print(is_balanced("String"))