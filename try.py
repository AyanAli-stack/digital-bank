import bcrypt

# Store user data
users = {}

# Function to hash the password using bcrypt
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check the password
def check_password(stored_password, password_to_check):
    return bcrypt.checkpw(password_to_check.encode('utf-8'), stored_password)

# Function to sign up a new user
def sign_up():
    print("Create a new account")
    username = input("Enter your username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    users[username] = {"password": hashed_password, "balance": 0}
    print(f"Account created successfully for {username}!")

# Function to log in
def login():
    username = input("Enter your username: ")
    if username not in users:
        print("Username does not exist!")
        return None
    password = input("Enter your password: ")
    if check_password(users[username]["password"], password):
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Incorrect password!")
        return None

# Function to deposit money
def deposit(username):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        users[username]["balance"] += amount
        print(f"${amount} has been deposited. New balance: ${users[username]['balance']}")
    else:
        print("Deposit amount must be positive.")

# Function to withdraw money
def withdraw(username):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > 0 and amount <= users[username]["balance"]:
        users[username]["balance"] -= amount
        print(f"${amount} has been withdrawn. New balance: ${users[username]['balance']}")
    elif amount > users[username]["balance"]:
        print("Insufficient funds!")
    else:
        print("Withdraw amount must be positive.")

# Function to view balance
def view_balance(username):
    print(f"Your current balance is: ${users[username]['balance']}")

# Main program loop
def main():
    print("Welcome to the Digital Bank!")
    
    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\n1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. View Balance")
                    print("4. Log Out")
                    action = input("Choose an action: ")
                    
                    if action == '1':
                        deposit(username)
                    elif action == '2':
                        withdraw(username)
                    elif action == '3':
                        view_balance(username)
                    elif action == '4':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Try again.")
        elif choice == '3':
            print("Thank you for using the Digital Bank!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()





