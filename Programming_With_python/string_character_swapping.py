str = input("Enter your text here: ")

str_list = list(str)

for i in range(0, len(str_list) - 1, 2):
    str_list[i], str_list[i+1] = str_list[i+1], str_list[i]

swapped_string = ''.join(str_list)

print(swapped_string)