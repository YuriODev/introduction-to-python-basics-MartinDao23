# Exercise 4
four_digit = input("Give us a four digit number: ")
for i in range (4-(len(four_digit))):
    four_digit = "0" + four_digit
if four_digit[0] == four_digit[3] and four_digit[1] == four_digit[2]:
    print(1)
else:
    print(0)