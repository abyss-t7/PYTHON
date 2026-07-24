class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
     return f"{self.name} says woof!"

d = Dog("Radex", "Labrador")
print(d.bark())

"""1. __init__ = constructor (like Dog(string name, string breed)).
2. self = this, but explicit — every method takes it as the first parameter, always, by convention 
(not a keyword).
3. No destructor needed unless you're managing external resources (files, sockets) — Python's garbage 
collector handles memory (reference counting + cycle detector)."""