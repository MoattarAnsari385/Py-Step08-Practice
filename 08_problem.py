# Write a function to print multiplication table of given number.

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

print_multiplication_table(5)