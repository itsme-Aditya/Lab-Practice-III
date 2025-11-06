def fibonacci(n):
    a, b = 0, 1 
    for _ in range (n):
        a, b = b, a + b
    return a


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

while(True):
    inp = str(input("Enter a or b: "))
    if inp == "a":
        print("Iterative: ")
        series = [fibonacci(i) for i in range (40)]
        print(series)
    elif inp == "b":
        print("Recursive: ")
        fib_series = [fib(j) for j in range (40)]
        print(fib_series)
    elif inp == "q":
        quit()
    else:
        print("Try Again!")
