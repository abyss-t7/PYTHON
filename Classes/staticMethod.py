class car:
    car = "Alto"
    model = "1998"

    def newcar(self):
        print(f"This is {self.car} car and its model is {self.model}.")

    @staticmethod # ===> static method
    def nah():
        print("Goog buy!")

buy = car()
buy.newcar() 
buy.nah()

