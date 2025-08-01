def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by 0"

print("SELECT OPERATION")
print("1. Add")    
print("2. Subtract")    
print("3. Multiply")    
print("4. Divide")    
choice = input("Enter a choice(1/2/3/4):\n")
# user data store

if choice in ["1", "2", "3", "4"]:
    userInput1 = int(input("Enter first number: \n"))
    userInput2 = int(input("Enter second number: \n"))

    if choice == "1":
        print("The sum of ",userInput1 ," and " ,userInput2 , " is ",add(userInput1, userInput2))

    if choice == "2":
        print("The difference of ",userInput1 ," and " ,userInput2 , " is ",sub(userInput1, userInput2))
        

    if choice == "3":
        print("The Multiplication of ",userInput1 ," and " ,userInput2 , " is ",mul(userInput1, userInput2))
        

    if choice == "4":
        print("The division of ",userInput1 ," and " ,userInput2 , " is ",div(userInput1, userInput2))
        

else:
    print("Invalid input")