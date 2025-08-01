import random

def depoAmount():
    while True:
        amount = input("Enter the amount to bet.\n$")
        if amount.isdigit():
            # print(amount)
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Enter the amount greater than 0.")
        else:
            print("Enter the amount in digit.")

    return amount

depoAmount()



symbols =['bell', '7', 'cherry', 'Lemon', 'bar']

def randomChoice(): 
    reels =[random.choice(symbols),random.choice(symbols), random.choice(symbols)]
    return reels

def displayingOutput():
    print(randomChoice())

def comparingReels():
    reel = randomChoice()
    
    for single in reel:
        first = single
 

# comparingReels()


# displayingOutput()