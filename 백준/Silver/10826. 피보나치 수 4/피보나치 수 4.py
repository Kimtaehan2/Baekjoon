n=int(input())
def dp(n):
    if n==0: return 0
    if n==1: return 1
    fb=[0,1]
    for i in range(2,n+1):
        fb.append(fb[i-2]+fb[i-1])
    return fb[-1]
print(dp(n))
