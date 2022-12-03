n=int(input())

global count
count=0

def fib(n):
    global count
    if n == 1: 
        count+=1
        return 0
    elif n == 0: 
        return 1
    else :
        return (fib(n - 1) + fib(n - 2))

fib(n)
print(count,n-2)