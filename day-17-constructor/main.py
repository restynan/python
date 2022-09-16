# use keyword pass  if you don't want to write any thing in class
# pascal case for class names
# constructor  use __init__(self) , its called every time you create a new object for the class
# self is the actual object that is being initialized

class Car:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats
        self.miles = 100  # we can also provide default value

    def compare_car_miles(self, car):
        if self.miles > car.miles:
            print(f"{self.name}'s car has more mileage than {car.name}'s car")


resty_car = Car("Resty", 5)
resty_car.miles = 26000
print(f"car seats: {resty_car.seats} car miles: {resty_car.miles}")

## car2
aisha_car = Car("Aisha", 4)
print(f"car seats: {aisha_car.seats} car miles: {aisha_car.miles}")


resty_car.compare_car_miles(aisha_car)

