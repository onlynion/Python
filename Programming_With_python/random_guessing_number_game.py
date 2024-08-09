import random

number = random.randint(1, 1000)
attempt = 0
low = 1
high = 1000

while True:
    # input_number = input("Guess the number (between 1 to 10000): ")
    # input_number = int(input_number)
    
    print("Guess the number (between 1 to 1000): ")
    input_number = (low + high) // 2
    print("My guess is", input_number)

    attempt += 1

    if input_number == number:
        print("Yes! Yes!! Yes!!! you guess the correct number")
        break 
    if input_number > number:
        print("Incorrect, Please try to guess a smaller number")
        high = input_number - 1
    else:
        print("Incorrect, Please try to guess a larger number")
        low = input_number + 1

print("You tried", attempt, "times to find the correct number")
