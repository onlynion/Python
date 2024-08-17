# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-n>

class Car:
    name = "Premio"
    color = "White"

    def start():
        print("Starting the engine")

print("Name of the car is: ", Car.name)
print("Color of the car is: ", Car.color)

Car.start()