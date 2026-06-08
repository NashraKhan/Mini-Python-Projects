# Function Prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

x = int(input('Enter a Number: '))

if is_prime(x):
    print(f'{x} is Prime')
else:
    print(f'{x} is not Prime')


