a,b,c=map(int,input().split())
sum=(c-b)//(a-b)
r=(c-b)%(a-b)
if r!=0:
    print((c-b)//(a-b)+1)
else: print((c-b)//(a-b))