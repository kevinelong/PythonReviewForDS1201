#Complex Data Types (multiple values)
# A list in python would called an array in other programming languages
# Like a row or column in SpreadSheet - Ordered
colors = ["red", "green", "blue"] # [] create a list "" creates a string

print(colors[2]) # Accessing the first element - index 0 is offset (distance from first is 0)
print(type(colors))

# defining a *dictionary* (dict) with three key-value pairs
# also called associateve-array or hash-map
lookup = {"A": "Apple", "B": "Banana", "C": "Cherry"} # {} creates a dictionary

print(lookup["B"]) # Accessing the value associated with key "B"

print(type(lookup))


readonly = (123,456,789)
print(readonly[1]) # one away from the first 456
print(type(readonly))

# game = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
game = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
# list of lists of values
print(game[1][1]) # second row, second column



