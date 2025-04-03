def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    
    for i in range(denom):
        if denom % (denom - i) == 0 and numer % (denom - i) == 0:
            return [numer // (denom - i),denom // (denom - i)]
        
    return [numer,denom]