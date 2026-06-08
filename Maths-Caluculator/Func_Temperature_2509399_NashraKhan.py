# Function - Temperature: Celsius -> Fahrenheit

def temp(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = int(input('Enter Temperatue in °C: '))

print(f'Celsius: {celsius} -> Fahrenheit: {temp(celsius)}')
    
