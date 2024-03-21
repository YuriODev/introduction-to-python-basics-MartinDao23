# Exercise 1
number = int(input("Enter a five-digit number: "))
first_part = (number // 10000)
third_part = (number // 100) % 10
fifth_part = (number % 10)
second_part = (number // 1000) % 10
fourth_part = (number // 10) % 10
number_one = first_part + third_part + fifth_part
number_two = second_part + fourth_part
print(str(number_one) + str(number_two))