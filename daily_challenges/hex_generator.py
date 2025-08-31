import random

def generate_hex(color):
    dominant_rand = random.randint(128, 225)
    non_dominant_1 = random.randint(0, 127)
    non_dominant_2 = random.randint(0, 127)
    if color == "red":
        r, g, b = dominant_rand, non_dominant_1, non_dominant_2
    elif color == "green":
        r, g, b = non_dominant_1, dominant_rand, non_dominant_2
    elif color == "blue":
        r, g, b = non_dominant_1, non_dominant_2, dominant_rand
    else:
        return "Invalid color"
    
    return "{:02X}{:02X}{:02X}".format(r, g, b)

print(generate_hex("red"))   