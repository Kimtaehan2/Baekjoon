n=int(input())

def dp(n):
  if n==1: return [0,1]
  A=[0]
  B=[1]
  for i in range(1,n):
    A.append(B[i-1])
    B.append(A[i-1]+B[i-1])
  return [A[-1],B[-1]]

print(*dp(n))