n=int(input())

def star(n):
    if n==1: return ['*']
    if n==2: return ['*****','*','* ***','* * *','* * *','*   *','*****']
    arr=star(n-1)
    star_copy=[]

    star_copy.append('*'+'****'*(n-1))
    star_copy.append('*')
    count=1
    for i in arr:
        if count==1: star_copy.append('*'+' '+'***'+'****'*(n-2))
        elif count==2: star_copy.append('*'+' '+i+' '+'    '*(n-2)+'*')
        else: star_copy.append('*'+' '+i+' '+'*')
        count+=1
    
    star_copy.append('*'+'   '+'    '*(n-2)+'*')
    star_copy.append('*'+'****'*(n-1))
    return star_copy

print('\n'.join(star(n)))