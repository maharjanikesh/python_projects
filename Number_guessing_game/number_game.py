import random

def number_guessing():

    lower_bound = 0 
    higher_bound = 100

    secret_number = random.randint(lower_bound, higher_bound)
    # print(secret_number)

    print(f'Guess the number between {lower_bound} and {higher_bound}')

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess < lower_bound or guess > higher_bound:
            print(f'Enter a number between {lower_bound} and {higher_bound}')
        elif guess < secret_number:
            print("Too low! Try again")
        elif guess > secret_number:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You have guessed the secret number {secret_number} in {attempts} attempts")
            break


    else:
        print(f"Sorry You have finished your {max_attempts} attempts")

number_guessing()