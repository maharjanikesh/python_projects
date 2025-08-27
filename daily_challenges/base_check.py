# def is_valid_number(n, base):
#     n = n.upper()
#     value = 0
#     for char in n:
#         if char.isdigit():
#             value = int(char)
#         elif not char.isdigit():
#             value = ord(char) - ord('A') + 10
#         if value >= base:
#             return False
#     return True

# print(is_valid_number("9876543210", 8))


def is_valid_number(n, base):
    n = n.upper()
    values = []
    for char in n:
        if char.isdigit():
            values.append(int(char))
        elif not char.isdigit():
            values.append(ord(char) - ord('A') + 10)
    
    if values >= base:
            return False
    return True

print(is_valid_number("9876543210", 8))