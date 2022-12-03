x,y,w,h=map(int,input().split())
resultx=min(w-x,x)
resulty=min(h-y,y)
print(min(resultx,resulty))
