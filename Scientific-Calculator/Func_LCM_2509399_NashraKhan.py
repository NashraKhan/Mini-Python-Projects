# Functions - Greatest Common Divisor (LCM)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input('Enter 1st Number: '))
b = int(input('Enter 2nd Number: '))

print(f'GCD of {a} & {b} is {gcd(a, b)}')
print(f'LCM of {a} & {b} is {lcm(a, b)}')

