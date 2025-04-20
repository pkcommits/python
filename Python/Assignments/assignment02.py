# Program to check if a number is prime

#Input the number from the user
num = int(input("Enter a number: "))

# Prime check function
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, n):
        if n % i == 0:  # If divisible by any number other than 1 and itself
            return False
    return True

# Calling the function and printing result
if is_prime(num):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")
