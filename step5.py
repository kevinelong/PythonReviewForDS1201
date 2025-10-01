#demo for loop
# for i in range(5): #five times? 0,1,2,3,4 but not 5
#     print(i)


import random
# r = random.randint(1, 100)
# print(r)

def roll(sides=6):
    return random.randint(1, sides)

# print(roll())
# print(roll())
# print(roll())

def roll_many(n): # n how many dice n for number
    total = 0
    #how can we repeat in python
    for _ in range(n): # _ is just a var name like x or i but indicates its not used
        r = roll()
        print(r)
        total += r
    return total

grand_total = roll_many(5) # roll five dice
print(grand_total)
