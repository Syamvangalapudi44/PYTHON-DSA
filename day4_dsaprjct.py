#file handling expense tracker

expenses = []
def export_expenses(expenses):
    with open("expenses.txt" , "w") as file:
        for expense in expenses:
           file.write(expense["name"] + " " + str(expense["amount"]) + "\n")

def main():
    while True:
        print("\n1.ADD EXPENSES")
        print("2.VIEW EXPENSES")
        print("3.EXPORT TO FILE")
        print("4.EXIT")

        choice = input("enter choice:")

        if choice =="1":
            name = input("enter expense name:")
            amount = int(input("enter amount:"))

            expenses.append({"name":name,"amount":amount})
        
        elif choice == "2":
            for expense in expenses:
                print(expense["name"]," ",expense["amount"])


        elif choice == "3":
            export_expenses(expenses)


        elif choice == "4":
            print("exit the programm")
            break

        else:
            print("invalid choice, try again")

main()

       
                       
