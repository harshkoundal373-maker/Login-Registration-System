import json
import os

FILE = "users.json"

# File create if not exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE, "r") as f:
        users = json.load(f)

    if username in users:
        print("Username already exists!")
        return

    users[username] = password

    with open(FILE, "w") as f:
        json.dump(users, f)

    print("Registration Successful!")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE, "r") as f:
        users = json.load(f)

    if username in users and users[username] == password:
        print("Login Successful!")
    else:
        print("Invalid Username or Password!")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid Choice!")