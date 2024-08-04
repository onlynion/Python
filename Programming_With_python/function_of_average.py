def calculate_average(numbers):
    total = 0
    number_of_element = 0

    for number in numbers:
        total += number
        number_of_element += 1
    return total/number_of_element

list = [1, 2, 3, 4, 5]

average = calculate_average(list)
print(int(average))