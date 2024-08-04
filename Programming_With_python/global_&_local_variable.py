def myfnc(x):
    print("inside myfnc", x)
    x=10
    print("inside myfnc", x)

x = 20
myfnc(x)
print(x)

# myfnc যখন call হয়, তখন সে argument হিসেবে যেসব variable পায়, সেগুলোর একটি copy তৈরি হয়। তাই myfnc এর x আর তার বাইরের x দুটি আলাদা variable। একটি function এর ভেতর যেসব variable তৈরি করা হয়, সেগুলো হচ্ছে ওই ফাংশনের local variable। function এর বাইরে তার কোন অস্তিত্ব থাকে না 