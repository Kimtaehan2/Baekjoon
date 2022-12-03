n=int(input())

def star(n):
    if n==1: return ['*']
    if n==2: return ['*****','*   *','* * *','*   *','*****']
    arr=star(n-1)
    star_copy=[]

    star_copy.append('*'+'****'*(n-1))
    star_copy.append('*'+'   '+'    '*(n-2)+'*')

    for i in arr:
        star_copy.append('*'+' '+i+' '+'*')
    
    star_copy.append('*'+'   '+'    '*(n-2)+'*')
    star_copy.append('*'+'****'*(n-1))
    return star_copy

print('\n'.join(star(n)))