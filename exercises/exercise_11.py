# Exercise 11
s = int(input("How much does your goods cost?  "))
five_hundreds = s//500
s = s%500
hundreds = s//100
s = s%100
tens = s//10
s = s%10
fives = s//5
s = s%5
twos = s//2
s = s%2
ones = s
print(f"{five_hundreds} (500), {hundreds} (100), {tens} (10), {fives} (5),{twos} (2), {ones} (1) ")