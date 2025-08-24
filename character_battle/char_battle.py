def battle(my_army, opposing_army):
    my_army_power = []
    opposing_army_power = []
    my_army_win_count = 0
    opposing_army_win_count = 0
    power_for_small_char = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    power_for_capital_char = {
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52
    }
    
    power_for_digits = {
        '0': 0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
    }

    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(opposing_army) > len(my_army):
        return "We retreated"
    else:

        # Converting my_army into power and storing it into list

        for i in range(len(my_army)):
            if my_army[i] in power_for_capital_char:
                my_army_power.append(power_for_capital_char[my_army[i]])
            elif my_army[i] in power_for_small_char:
                my_army_power.append(power_for_small_char[my_army[i]])
            elif my_army[i] in power_for_digits:
                my_army_power.append(power_for_digits[my_army[i]])
            else:
                my_army_power.append(0)

        # Converting opposing_army into power and storing it into list
        for j in range(len(opposing_army)):
            if opposing_army[j] in power_for_capital_char:
                opposing_army_power.append(power_for_capital_char[opposing_army[j]])
            elif opposing_army[j] in power_for_small_char:
                opposing_army_power.append(power_for_small_char[opposing_army[j]])
            elif opposing_army[j] in power_for_digits:
                opposing_army_power.append(power_for_digits[opposing_army[j]])
            else:
                opposing_army_power.append(0)

        # Comparing the power of my_army and opposing_army
        for i, j in zip(my_army_power, opposing_army_power):
        
            if i > j:
                my_army_win_count += 1
            elif j > i:
                opposing_army_win_count += 1

        # Comparing the win count
        if my_army_win_count > opposing_army_win_count:
            return "We won"
        elif opposing_army_win_count > my_army_win_count:
            return "We lost"
        else:
            return "It was a tie"



print(battle("C@T5", "D0G$"))