
#countdown from 10
stage = 10

while stage > 0: #repeat while true
    print(stage)
    stage = stage - 1

print("Blast Off!!!")

colors = ["red", "green", "blue"]

# loop through list of colors
for c in colors:
    print(c)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# loop through each row in the grid
for row in grid:
    output = ""
    for col_value in row:
        output += str(col_value) + " " #concatenate chain together like train
    print(output)

# list of dicts
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# loop through each person in the list
for person in people: #do we have another in the list
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("---")
print("Done no more people")