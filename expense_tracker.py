import os

file_name = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, etc): ")
    amount = float(input("Enter amount: "))

    with open(file_name, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(file_name):
        print("No expenses found!\n")
        return

    total = 0
    print("\n--- Expense List ---")
    with open(file_name, "r") as file:
        for line in file:
            date, category, amount = line.strip().split(",")
            print(f"Date: {date} | Category: {category} | Amount: ₹{amount}")
            total += float(amount)

    print(f"\nTotal Expense: ₹{total}\n")


def menu():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

menu()
