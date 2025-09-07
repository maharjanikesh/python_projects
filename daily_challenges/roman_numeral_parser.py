def parse_roman_numeral(numeral):
    parsed_num = []
    sum = 0
    symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    };
    for char in numeral:
        parsed_num.append(symbols[char])
    for i in range(len(parsed_num)):
        if i+1 < len(parsed_num) and parsed_num[i+1] > parsed_num[i]:
            sum -= parsed_num[i]
        else:
            sum += parsed_num[i]

    return sum

print(parse_roman_numeral("III"))