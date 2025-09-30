# ATM Simulation Project

# Initial account details
account_pin = "1234"
balance = 5000.0
transaction_history = []
WITHDRAW_LIMIT = 20000  # per transaction

print("===== Welcome to ATM Cash =====")

# PIN verification
entered_pin = input("Enter PIN: ")
if entered_pin != account_pin:
    print("Invalid PIN. Access denied.")
else:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit & Print Receipt")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print(f"Your balance is ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                transaction_history.append(f"Deposited ₹{amount:.2f}")
                print(f"₹{amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            elif amount > WITHDRAW_LIMIT:
                print(f"Withdrawal limit per transaction is ₹{WITHDRAW_LIMIT}")
            else:
                balance -= amount
                transaction_history.append(f"Withdrew ₹{amount:.2f}")
                print(f"₹{amount:.2f} withdrawn successfully.")

        elif choice == "4":
            print("===== Transaction History =====")
            if transaction_history:
                for t in transaction_history:
                    print(t)
            else:
                print("No transactions yet.")

        elif choice == "5":
            old_pin = input("Enter old PIN: ")
            if old_pin != account_pin:
                print("Incorrect old PIN.")
            else:
                new_pin = input("Enter new PIN: ")
                account_pin = new_pin
                print("PIN changed successfully.")

        elif choice == "6":
            print("\n===== RECEIPT =====")
            if transaction_history:
                for t in transaction_history:
                    print(t)
            else:
                print("No transactions this session.")
            print(f"Final Balance: ₹{balance:.2f}")
            print("Thank you for using ATM Cash. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
