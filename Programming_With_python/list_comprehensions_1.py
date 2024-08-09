li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# for x in li:
#     if x%2 == 0:
#         even_numbers.append(x)

even_numbers = [x for x in li if x%2 == 0]

print(even_numbers)