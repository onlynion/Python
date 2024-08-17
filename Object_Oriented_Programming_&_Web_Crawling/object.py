class Car:
    name = ""
    color = ""

    # def start():
    #     print("Starting the car")

    def start(self):
        print("Starting the car")

# Creating Object
my_car = Car()
my_car.name = "Mitsubishi"
name = my_car.name

print(name)
my_car.start()