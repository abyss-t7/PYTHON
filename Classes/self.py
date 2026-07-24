class car:
    car = "Alto"
    model = "1998"

    def newcar(self):
        print(f"This is {self.car} car and its model is {self.model}.")

buy = car()
buy.newcar() 
    # or
car.newcar(buy)

# self: is a reference to the specific object that is calling the method. It is how an object 
# refers to itself from inside its own methods