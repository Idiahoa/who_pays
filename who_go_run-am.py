
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

A=(len(names))
random_name=random.randint(0,A)
print(names[random_name]+" is going to buy the meal today!")
