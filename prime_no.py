"""A function to generate Fibonacci sequence from 0 to n with asymptotic"""

analysis

primeList = []
for num in range(2,10000):
    if all(num%i!=0 for i in range(2,num)):
        primeList.append(num)
x = int(raw_input("Enter n: "))
for i in range(x):
    print primeList[i]
