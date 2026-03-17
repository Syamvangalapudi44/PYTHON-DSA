# Attendence Tracker

std_name=""
std_status=""

def menu():
    print("\n -----------Attendence Tracker---------- \n 1. Add attendence \n 2. View Attendence \n 3. Exit")
    
def add_att():
    global std_name
    global std_status
    
    std_name=input("Enter the student name: ")
    std_status=input("Enter student status(present/absent): ")
    print("Attendence added succesfully")
    
def view_att():
    if std_name == "":
        print("No attendence record found ")
    else:
        print("\n---------Attendence record--------")
        print(std_name,"-",std_status)
    
def main():
    while True:
        menu()
        Ch=int(input("Enter option based upon the menu "))
        if Ch==1:
            add_att()
        elif Ch==2:
            view_att()
        elif Ch==3:
            break
        else:
            print("Invalid choice choose in the given range")

main()
