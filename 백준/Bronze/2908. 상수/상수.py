num=list(map(list,input().split()))
num[0].reverse()
num[1].reverse()
if num[0]>num[1]:
   print("".join(num[0]))
else: print("".join(num[1]))
