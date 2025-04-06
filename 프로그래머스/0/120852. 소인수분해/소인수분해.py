def solution(n):
    answer = []
    l = prime_factorization(n,[])
    l = list(set(l))
    l.sort()
    return l

def prime_factorization(n,l):
    
    for i in range(2,n+1):
        if n % i == 0:
            l.append(i)
            return prime_factorization(n//i,l)
    return l