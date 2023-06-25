"""""
M03 Case Study: List, functions, and classes

Author: Tanner Cole 

Creating a program using various lists, functions, and classes to define
the class vehicle to determine a car's type, year, model, make, number of doors
and type of roof"""""

#Creating a super class called Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
#Autmobile class. This class will inherit the attributes from the Vehicle class
class Autmobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#Inputs for the create_car function
def create_car():
        vehicle_type = "car"
        year = input("Enter the year of the car: ")
        make = input("Enter the make of the car: ")
        model = input("Enter the model of the car: ")
        doors = input("Enter the number of car doors: ")
        roof = input("Enter the type of roof(solid or sun roof): ")

        car = Autmobile(vehicle_type, year, make, model, doors, roof)
        return car
# the output for displaying all car information 
def display_car_info(car):
        print("Vehicle Type: ", car.vehicle_type)
        print("Car Year: ", car.year)
        print("Make of car: ", car.make)
        print("Model of car: ", car.model)
        print("Number of doors: ", car.doors)
        print("Type of roof: ", car.roof)
# Main Program module
car = create_car()
print("\nCar Information: ")
display_car_info(car)