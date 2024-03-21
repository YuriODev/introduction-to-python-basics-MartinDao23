# Exercise 9
hours = int(input("How many hours have passed?  "))
minutes = int(input("How many minutes have passed?  "))
seconds = int(input("How many seconds have passed?  "))
angle = ((hours/12)*360) + ((minutes/60)*30) +((seconds/60)*6)
print(angle)