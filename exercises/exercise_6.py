# Exercise 6
a = int(input("Enter a number:  "))
b = int(input("Enter a number:  "))
divisible = "YES" * ((a%b) == 0) or "NO"
print(divisible)