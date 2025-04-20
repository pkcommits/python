
#Input numbers from users


num1 = float(input(f'Enter the first value:'))
num2 = float(input(f'Enter the second value:'))

print(f'The numbers are {num1} and {num2}')


#Addition
addition = num1 + num2
print(f'sum of {num1} and {num2} is {addition}')

#subtraction
subtraction = num1 - num2
print(f'subtraction of {num1} and {num2} is {subtraction}')

#multiplication
multiplication = num1 * num2
print(f'multiplication of {num1} and {num2} is {multiplication}')

#division
if num2 == 0.0:
    print(f'division of {num1} and {num2} is not defined')
else:
    division = num1 * num2
    print(f'division of {num1} and {num2} is {division}')
