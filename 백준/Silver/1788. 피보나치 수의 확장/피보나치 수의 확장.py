n=int(input())
def dp(n):
    if n==0: return 0
    if n==1: return 1
    fb=[0,1]
    for i in range(2,n+1):
        fb.append((fb[i-2]+fb[i-1])%1000000000)
    return fb[-1]

if n>=0: 
    if n==0: print(0)
    else: print(1)
    print(dp(n))
else: 
    if abs(n)%2==0: print(-1)
    else: print(1)
    print(dp(abs(n)))