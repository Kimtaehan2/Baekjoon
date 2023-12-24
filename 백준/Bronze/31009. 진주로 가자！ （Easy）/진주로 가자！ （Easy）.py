import sys
input = sys.stdin.readline

N = int(input())

price = [0]*1001
j = 0


for i in range(N):
  a,b = input().split()
  b = int(b)
  if a == "jinju":
    j = b
  price[b] += 1

print(j)
print(sum(price[j+1:]))