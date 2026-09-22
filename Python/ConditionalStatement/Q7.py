#Q7 - Create a simple ATM menu:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
Amount = 100000
opertion = input("""Selet any Operation you want to Perform:
                 1- Check Balance
                 2- Deposit 
                 3- Withdraw 
                 4- Exit""")
if opertion == "1":
    print("Checking Balance")
    print("Current Amount: ",Amount)

elif opertion == "2":
    Deposit = int(input("Enter Deposit Amount: "))
    Amount = Amount + Deposit
    print("Depositing Amount")
    print("Current Amount: ",Amount)

elif opertion == "3":
    withdraw = int(input("Enter withdraw Amount: "))
    if withdraw <= Amount:
        Amount = Amount - withdraw
        print("Withdrawal successful")
        print("Current Amount:", Amount)
    else:
        print("Insufficient Balance")

elif opertion == "4":
    print("Exiting Program")

else:
    print("Invalid Operation")
