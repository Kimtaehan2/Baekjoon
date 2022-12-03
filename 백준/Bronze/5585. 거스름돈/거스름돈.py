import sys
n = 1000-int(sys.stdin.readline())


count=n//500
n%=500
count+=n//100
n%=100
count+=n//50
n%=50
count+=n//10
n%=10
count+=n//5
n%=5
count+=n//1

print(count)