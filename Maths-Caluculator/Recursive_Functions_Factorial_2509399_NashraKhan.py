# Recursive Function - Factorial of a Number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Enter a Number: '))
print(f'Factorial of {n} is {factorial(n)}')
    

