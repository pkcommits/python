# Recursive function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:  # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Case


# Recursive function to calculate sum of first N natural numbers
def sum_natural(n):
    if n < 0:
        return "Sum not defined for negative numbers"
    if n == 0:  # Base Case
        return 0
    return n + sum_natural(n - 1)  # Recursive Case


# Taking user input
num = int(input("Enter a number: "))

# Factorial Calculation
fact_result = factorial(num)

# Sum Calculation
sum_result = sum_natural(num)


print(f"Factorial of {num} is {fact_result}")
print(f"Sum of first {num} natural numbers is {sum_result}")
