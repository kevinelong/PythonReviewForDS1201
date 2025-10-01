#demo for loop
for i in range(5): #five times? 0,1,2,3,4 but not 5
    print(i)


import random
r = random.randint(1, 100)
print(r)

def roll(sides=6):
    return random.randint(1, sides)

print(roll())
print(roll())
print(roll())

def roll_many(n): # n how many dice n for number
    #how can we repeat in python
    pass 
