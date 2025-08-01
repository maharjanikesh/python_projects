def main():
    expenses = []
    while True:
        print("-----------Expense Tracker-----------\n")
        print("Choose from the options\n")
        print("1. Add all expenses\n2. List all expenses\n3. Show total expenses\n4. Filter expenses by Category\n5. Exit\n")
        choice = input("Enter the number from the options: ")
        if choice == '1':
            while True:  
                try:
                    amount = float(input("\nEnter the amount: "))
                    break
                except:
                    print("Enter the amount in digits")
            category = input("\nEnter the category: ")
            add_expense(expenses, amount, category)
        elif choice == '2':
            print("All expenses\n")
            display_expenses(expenses) 
        elif choice == '3':
            print("Total expenses: ",total_expenses(expenses))
        elif choice == '4':
            category = input("\nEnter the category to filter the expense: ")
            expense_by_filter = filter_expense(expenses, category)
            display_expenses(expense_by_filter)
        elif choice == '5':
            print("Exiting.....")
            break
        else:
            print("Enter the number from the options\n")


def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def display_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses)) 

def filter_expense(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

main()
        