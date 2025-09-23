import re

def generate_slug(str):
    # lower string
    str = str.lower()

    # use of regex
    str = re.sub(r'[^a-z0-9 ]', '', str)

    # split the words
    words = str.split()

    # join the splitted words
    slug = "%20".join(words)
    
    return slug

print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))