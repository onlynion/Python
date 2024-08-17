class Car:
    name = ""
    color = ""

    def start():
        print("Starting the engine")

Car.name = "Axio"
Car.color = "Red"

print("Name of the car is: ", Car.name)
print("Color of the car is: ", Car.color)

# print(dir(Car))