terminate = False

while not terminate:
    num_1 = input("Please a enter a number: ")
    num_1 = int(num_1)
    num_2 = input("Please enter another number: ")
    num_2 = int(num_2)

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown Operation, Try Again!")
            continue
        if operation == "add":
            print("Result is ", num_1+num_2)
            break
        if operation == "sub":
            print("Result is ", num_1-num_2)
            break
