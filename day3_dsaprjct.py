expenses=[]
def add_expenses():
    name=input("Enter name: ")
    amount=input("Enter value of expense: ")
    expense={
        "name":name,
        "amount":amount
    }
    expenses.append(expense)
    print("Expense is added.")
    
def view_expenses():
    print('\n')
    for expense in expenses:
        print(expense["name"],"-",expense["amount"])
        
def show_menu():
    print("\n Expense Tracker\n 1. Add Expense \n 2. View Expense\n 3. Find Total Expenses\n 4. Exit")

def main():
    while True:
        show_menu()
        ch=int(input("Enter a Number from 1 to 4 : "))
        if ch==1:
            add_expenses()
        elif ch==2:
            view_expenses()
        elif ch==3:
            total=0
            for expense in expenses:
                total+=int(expense["amount"])
            print(f"Total amount is {total}")
        elif ch==4:
            print(f"Thanks for using the Expense Tracker")
            break
        else:
            print("Please choose the valid range between 1 to 4 ")
            
main()