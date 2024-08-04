def myfnc(y):
    print("y =", y)
    print("x =", x)

x = 20
myfnc(x)

# function এর বাইরে যদি কোন variable থাকে, তাহলে function এর ভেতর থেকে ওই variable পাওয়া যায়। একে বলে global variable। উপরের function থেকে আমরা যদি y এর মান myfnc এর বাইরে থেকে দেখতে চাই তাহলে সেটা সম্ভব না সেটা error দিবে
