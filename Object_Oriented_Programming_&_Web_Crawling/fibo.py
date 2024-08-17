def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next

    return fib_next

def list_fib(n):
    fib_list = [1,1]
    if n <= 2:
        return fib_list[:n]
    
    # The :n is a slicing operation in Python, which is used to return a specific portion of a list.
    # fib_list[:n] means "give me the first n elements of fib_list".
    # This is particularly useful in the case where n <= 2 because the initial list fib_list = [1, 1] already has 2 elements, so fib_list[:n] ensures that only the required number of elements (either 1 or 2) is returned.
    
    fib_x, fib_next = 1, 1

    i = 3

    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        fib_list.append(fib_next)

    return fib_list

if __name__ == "__main__":
    for x in range(1, 11):
        print(find_fib(x))

        print(list_fib(1))
        print(list_fib(2))
        print(list_fib(10))