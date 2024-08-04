fruits = ['apple', 'mango', 'coconut', 'banana', 'orange']
item = 'coconut'

if item in fruits:
    fruits.remove(item)
    print(fruits)
else:
    print(item, "is not in list")