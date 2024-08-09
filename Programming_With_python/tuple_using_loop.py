items = (1, 2, 5.5, ["a", "b", "c"], ("apple", "mango"))
for item in items:
    print(item, type(item))

print(items[3])
print(items[3][0])
print(items[4][1])
print(items[4])

# tuple এর ভেতর আমরা বিভিন্ন জিনিস রাখতে পারি, এবং এগুলোর উপর loop ও চালানো যায় 