# Recursive Function - Sum of Digits

def sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum(n // 10)

x = int(input('Enter Number: '))
print(f'Sum of Digits of {x} is {sum(x)}')
