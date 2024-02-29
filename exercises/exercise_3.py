# Exercise 3
time = int(input("How many seconds have passed since the beginning of the day: "))
minutes = time // 60
spare_seconds = time - (minutes*60)
hours = minutes // 60
spare_minutes = minutes - (hours*60)
print(str(hours) + ":" +  str(spare_minutes) + ":" + str(spare_seconds))