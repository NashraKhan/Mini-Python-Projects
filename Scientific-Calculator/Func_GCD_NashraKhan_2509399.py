# Functions - Greatest Common Divisor (GCD)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(200, 50))

