# Exercise 1
number = int(input("Enter a five-digit number: "))
first_part = (number // 10000) + ((number // 100) % 10) + (number % 10)
second_part = ((number // 1000) % 10) + ((number // 10) % 10)
print(str(first_part) + str(second_part))