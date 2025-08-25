def to_camel_case(s):
    capitalize_str = []
    s = s.lower()
    s = s.replace("-", " ").replace("_", " ")
    lower_str = s.split(" ")
    for char in lower_str:
        capitalize_str.append(char.capitalize())
    return capitalize_str[0].lower() + ("").join(capitalize_str[1:])

    # return lower_str[0] + (" ").join(lower_str[-1:].capitalize())
        

print(to_camel_case("HELLo WORLD"))