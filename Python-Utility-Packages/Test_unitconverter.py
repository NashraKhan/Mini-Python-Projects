from unitconverter_2509399 import temp_convert, length_convert

# Celsius to Fahrenhiet
print('Convert Celsius to Fahrenhiet')
x = int(input('Enter temperature in Celsius: '))
print(f' Temperature in Fahrenhiet: {temp_convert.temp(x)}')

print()

# Convert cm to m
print('Convert cm to m')
y = int(input('Enter length in cm: '))
print(f' Length in Meters: {length_convert.length(y)}')
