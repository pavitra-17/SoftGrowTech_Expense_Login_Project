import os

file_name = "users.txt"

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(file_name, "a") as file:
        file.write(f"{username},{password}\n")

    print("Signup successful!\n")


def login():
    if not os.path.exists(file_name):
        print("No users found! Please signup first.\n")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(file_name, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if username == stored_user and password == stored_pass:
                print("Login successful!\n")
                return

    print("Invalid credentials!\n")


def menu():
    while True:
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

menu()
