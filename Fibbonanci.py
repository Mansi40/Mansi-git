def Fibonacci(n):
    if n<0:
        print("invalid input")
    if n==1 or n==2:
       return 1
    elif n>2:
       return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))