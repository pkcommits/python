initial_amt = 5000
balance = initial_amt

print('WELCOME TO MY ATM!')

print('Select an option below')
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

selection = int(input('Enter the option: '))

if selection == 1:
    print(f'Your balance is: {balance}')

elif selection == 2:
    deposit = int(input("Enter the amount to be deposited: "))
    balance += deposit
    print('Amount deposited successfully')
    print(f'Your balance is: {balance}')

elif selection == 3:
    withdraw = int(input("Enter the amount to be withdrawn: "))
    if withdraw > balance:
        print("Insufficient Balance")
    else:
        balance -= withdraw
        print('Amount withdrawn successfully')
        print(f'Your balance is: {balance}')

elif selection == 4:
    print('THANK YOU VISIT AGAIN!')

else:
    print('ERROR! Enter a correct option number')
