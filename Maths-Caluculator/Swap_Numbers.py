# Swap 2 Numbers

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print(f"Numbers before Swapping: 1st Number: {a} 2nd Number: {b}")

a, b = b, a

print(f"Numbers after Swapping: 1st Number: {a} 2nd Number: {b}")
