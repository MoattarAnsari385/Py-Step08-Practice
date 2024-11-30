# Write a python function which converts inches to cm.

def inches_to_cm(inches):
    return inches * 2.54


inches = int(input("Enter a number: "))
centimeter = inches_to_cm(inches)
print(f"The value of {inches} converted into centimeter is: {centimeter}")