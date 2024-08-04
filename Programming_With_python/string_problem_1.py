str = input("Enter your text: ")

alpha_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_2 = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"

str1 = ""
str2 = ""
str3 = ""
str4 = ""

for c in str:
    if c in alpha_1:
        str1 = str1 + c
    elif c in alpha_2:
        str2 = str2 + c
    elif c in num:
        str3 = str3 + c
    else:
        str4 = str4 + c

print(str1)
print(str2)
print(str3)
print(str4)