"""Print a Fibonacci sequence up to n."""

def fib():
    a,b = 1,1
    num=eval(input("Enter Fib Nummber to be calculated: "))
    num_int=int(num-2)
    for i in range (num_int):
        a,b=b,a+b
    print(b)
