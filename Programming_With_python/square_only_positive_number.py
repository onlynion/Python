while True:
    n = input("Enter a positive number: ")
    n = int(n)

    if n < 0:
        print("We only allows positive number Please try with a positive number")
        continue
    if n == 0:
        break
    print("Square of ", n, " is", n*n)
