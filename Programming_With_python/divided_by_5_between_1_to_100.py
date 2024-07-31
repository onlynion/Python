result = 0
for i in range(1,101):
    if i%5 == 0:
        print(i)
        result += i
print("sum is: ", result)