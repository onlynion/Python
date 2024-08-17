def fibo_list(n):

    fibo_li = []
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    
    fibo_x , fibo_next = 1,1
    fibo_li.extend([fibo_x, fibo_next]) 
    
    # The .extend() method is used to add [1, 1] to the fibo_li list. This method is similar to .append(), but it adds multiple elements to the list.

    for i in range(3, n+1):
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
        fibo_li.append(fibo_next)

    return fibo_li

fibonacci_list = fibo_list(10)
print(fibonacci_list)

