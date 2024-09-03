class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output will be "Car Information: 2020 Toyota Corolla"