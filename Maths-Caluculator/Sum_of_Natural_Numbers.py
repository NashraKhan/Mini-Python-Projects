# Sum of All Natural Numbers

x = int(input('Enter a Number: '))
sum = 0

for i in range(1, x + 1):
    sum += i
    
print(f'Sum of Numbers upto {x} is {sum}')
