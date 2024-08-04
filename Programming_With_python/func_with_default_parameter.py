def myfnc(y=10):
    print("y =", y)

x = 20
myfnc(x)
myfnc()

# এই program  এ আমরা দুইবার myfnc function call করলাম। প্রথমবার argument হিসেবে x পাঠাচ্ছি। দ্বিতীয়বার কিছুই পাঠাচ্ছি না। কিন্ত function এর parameter এ আবার বলে দিয়েছি y = 10। এর মানে হচ্ছে যদি কোন argument পাঠানো না হয় তাহলে y এর মান হবে 10, আর যদি কোন argument পাঠানো হয় তাহলে argument এ যেই variable টি পাঠানো হয়েছে, সেই variable এর মান y তে কপি হবে 