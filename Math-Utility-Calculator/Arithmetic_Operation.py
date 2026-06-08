# PERFORM ARITHMETIC OPERATIONS: ADDITION / SUBTRACTION / MULTIPLICATION / DIVISION

a = int(input('Enter 1st Number: '))
b = int(input('Enter 2nd Number: '))

print('Choose any one operation:')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice = int(input('Enter your choice (1-4): '))

match choice:
    case 1:
        print(f'{a} + {b} = {a+b}')
    case 2:
        print(f'{a} - {b} = {a-b}')
    case 3:
        print(f'{a} x {b} = {a*b}')
    case 4:
        print(f'{a} / {b} = {a/b}')
    case _:
        print(f'Invalid Choice! Please select from 1-4')
    
