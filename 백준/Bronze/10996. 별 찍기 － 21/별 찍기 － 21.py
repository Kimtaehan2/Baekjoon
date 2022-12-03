

def star(n):
    if n==1: return ['*']
    if n==2: return ['* ',' *']
    starlist=star(n-1)
    star2=[]
    
    if n%2==0:
        s=1
        for i in starlist:
        
            if s%2==0:
                star2.append(i+'*')
            else:
                star2.append(i+' ')
            s+=1
    else:
        s=1
        for i in starlist:
        
            if s%2==0:
                star2.append(i+' ')
            else:
                star2.append(i+'*')
            s+=1
    return star2

n=int(input())
print('\n'.join(n*star(n)))