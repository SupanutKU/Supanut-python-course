# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print(f"Now money you have : {balance}")
        elif choice == "2":
            withdraw = float(input("Enter money withdraw: "))
            if withdraw <= balance :
                balance -= withdraw
                print(f"withdraw money : {withdraw:.2f}")
                print(f"total money : {balance:.2f}")
            else:
                print("Error! Not enough money to withdraw.")
        elif choice == "3":
            deposit = float(input("Enter money deposit: "))
            if deposit > 0:
                balance += deposit
                print(f"deposit money : {deposit:.2f}")
                print(f"total money : {balance:.2f}")
            else :
                print("Error! please enter a positive integer.")
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Error!")
else:
    print("Invalid PIN")