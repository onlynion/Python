def myfnc(x, y=10, z=0):
    print("x =", x, "y =", y, "z =", z)

x = 5
y = 6
z = 7

myfnc(x, y, z)
myfnc(x, y)
myfnc(x)

# আমরা যদি কোন argument  এ default value দি তাহলে তার পরের সবগুলো argument এ default value দিতে হবে যেমন আমরা যদি def myfnc(x, y=10, z) লিখতাম তাহলে error আসতো 
