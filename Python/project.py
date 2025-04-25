# if the number is a multiple  of 3 and 5 then print fizzbuzz
for num in range(30):
    if '3' in str(num):
        print('lucky') 
    else:
        if num % 3 == 0 and num % 5 == 0:
            print(f'fizzbuzz')
        elif num % 3 == 0:
            print(f'fizz')
        elif num % 5 == 0:
            print(f'buzz')
        else:
            print(num)
 

 