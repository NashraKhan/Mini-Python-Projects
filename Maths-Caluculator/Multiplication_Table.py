# Multiplication Table

n = int(input('Enter a Number: '))
print(f'Multiplication Table of {n}: ')
table = 1

for i in range(1, n):
    table = n * i
    print(f'{n} x {i} = {table}')
