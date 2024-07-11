# example.py

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

class Animal:
    """A simple class to represent an animal"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        """Method to make the animal sound"""
        return f"{self.name} the {self.species} says {sound}!"

if __name__ == "__main__":
    # Example usage of the greet function
    print(greet("Alice"))

    # Example usage of the Animal class
    dog = Animal("Buddy", "dog")
    print(dog.make_sound("woof"))

    cat = Animal("Whiskers", "cat")
    print(cat.make_sound("meow"))
