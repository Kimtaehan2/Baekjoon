n=int(input())
if n<10: n*=10
m=n
m=((m//10+m%10)%10)+(m%10)*10
count=1
while m!=n:
    count+=1
    m=((m//10+m%10)%10)+(m%10)*10
print(count)