numbers = [10,15,20,30,445,3,12,54,9,5]
max_num = 0
min_num = 9999

for i in range(10):
    if numbers[i] >= max_num:
        max_num = numbers[i]
    if (numbers[i] <= min_num):
        min_num = numbers[i]
print("Maximum number is: ",max_num)
print("Minimum number is: ",min_num)