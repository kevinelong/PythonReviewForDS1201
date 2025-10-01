#code resue/code organization like functions - DRY (Don't Repeat Yourself)

#defines a named function but does not executer/run it
def double_number(n): #receiving values into the input n parameter
    return n * 2

# calling/invoking the function causes it to run/execute
print(double_number(5)) #passing in the value 5 as the input argument

print(double_number(12))

#OOP Object Oriented Programming - Nouns (People, Places or Things)

class Animal: #blueprint/template for a kind of object?
    def __init__(self, name, species): #receiving values into the input parameters
        #define attributes/properties
        self.name = name
        self.species = species

    def speak(self): #method for the animal to speak (function in a class is a "method")
        print(f"{self.name} says: Hello!")

    def get_species(self): #method to get the species of the animal
        return self.species
    
a = Animal("Leo", "Lion") #create an instance of the Animal class
a.speak()
print(a.get_species())
