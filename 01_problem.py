# Write a program using function to find greatest of three numbers

def find_greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
result1 = find_greatest(1, 2, 4)
result2 = find_greatest(3, 23, 45)
print(result1)
print(result2)