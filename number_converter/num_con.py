def num_converter():
    number = input("Enter a number:\n")
    base_from = int(input("Enter the base of number:\n"))

    try:
        decimal_value = int(number, base_from)
    except ValueError:
        print(f"Invalid number for base {base_from}")

    base_to = int(input("Enter the base to convert the number into:\n"))

    if base_to == 2:
        converted_value = bin(decimal_value)[2:]
    elif base_to == 8:
        converted_value = oct(decimal_value)[2:]
    elif base_to == 10:
        converted_value = str(decimal_value)
    elif base_to == 16:
        converted_value = hex(decimal_value)[2:].upper()
    else:
        print(f"Invalid target base")

    print(f"The number {number} in base {base_from} is {converted_value} in base {base_to}.")

num_converter()
