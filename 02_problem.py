# Write a program using function to convert Celcius to Fahrenheit 

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
    
celsius = int(input("Enter a temperature: "))
fahrenheit =convert_celsius_to_fahrenheit(celsius)
print(f"The value of {celsius}°C is converted into Fahrenheit: {fahrenheit}°F")