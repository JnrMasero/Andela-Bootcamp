"""Print a Fibonacci sequence up to n."""
    
def fib(n):
    x = []
    a, b = 0, 1
    for i in range(n):
        x.append(a)
        a, b = b, a+b

    x.append(b)
    return x    
