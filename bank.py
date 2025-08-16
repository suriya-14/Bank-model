class Bank:
    def __init__(self):
        self.database = {}

    def create_account(self, name, details):
        if name in self.database:
            print("Account already exists!")
        else:
            self.database[name] = details
            print("Account created successfully.")

    def login(self, name, password):
        if name in self.database and self.database[name][1] == password:
            print(f"\nWelcome back, {name}!")
            print("_" * 50)
            while True:
                print("\n1. Check balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transaction History")
                print("5. Send Money")
                print("6. Exit")
                p = input("Select one option: ")

                if p == "1":
                    print(f"Your balance: ₹{self.database[name][3]}")

                elif p == "2":
                    amount = int(input("Enter the amount to withdraw: ₹"))
                    if amount <= self.database[name][3]:
                        self.database[name][3] -= amount
                        self.database[name][4].append(f"Withdrawn ₹{amount}")
                        print("Withdrawal successful.")
                    else:
                        print("Insufficient balance.")

                elif p == "3":
                    amount = int(input("Enter the amount to deposit: ₹"))
                    self.database[name][3] += amount
                    self.database[name][4].append(f"Deposited ₹{amount}")
                    print("Deposit successful.")

                elif p == "4":
                    print("Transaction History:")
                    for t in self.database[name][4]:
                        print("-", t)

                elif p == "5":
                    receiver = input("Enter receiver's name: ")
                    amount = int(input("Enter amount to send: ₹"))
                    if receiver in self.database:
                        if amount <= self.database[name][3]:
                            self.database[name][3] -= amount
                            self.database[receiver][3] += amount
                            self.database[name][4].append(f"Sent ₹{amount} to {receiver}")
                            self.database[receiver][4].append(f"Received ₹{amount} from {name}")
                            print("Money sent successfully.")
                        else:
                            print("Insufficient balance.")
                    else:
                        print("Receiver not found.")

                elif p == "6":
                    print("Logging out...")
                    break

                else:
                    print("Invalid option.")
        else:
            print("Invalid username or password.")


class Account:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        self.details = [self.name, self.password, self.email, 0, []]  # balance = 0, transaction list = []
        a.create_account(self.name, self.details)


a = Bank()

while True:
    print("\nWelcome to our Bank")
    print("_" * 50)
    print("1. Login")
    print("2. Signup")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        a.login(name, password)

    elif choice == "2":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        Account(name, password, email)

    elif choice == "3":
        print("Thank you for visiting our Bank.")
        break

    else:
        print("Invalid choice. Please try again.")