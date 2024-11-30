# How do you prevent a python print() function to print a new line at the end.
# To prevent the newline and continue printing on the same line, use the `end` parameter.

print("a")
print("b")
# Use `end=""` to avoid a new line after printing "c" and print "d" on the same line
print("c", end = "")
print("d", end = "")