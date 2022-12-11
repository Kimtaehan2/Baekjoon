import sys
input = sys.stdin.readline
N = int(input())
result = 0
for i in range(N):
  R = round(N/(N-i),10)
  result += R

print(result)