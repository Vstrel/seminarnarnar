def fib(a):
    if a==1 or a==0:
        return(1)
    return(fib(a-1)+fib(a-2))
a=int(input())
print(fib(a))