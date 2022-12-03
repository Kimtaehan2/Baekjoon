n=int(input())

def star(n):
    star=[]
    star.append('*'*n+' '*(2*(n-2)+1)+'*'*n)
    
    for i in range(1,n-1):
        star.append(' '*i+'*'+' '*(n-2)+'*'+' '*(n-2-i)+' '+' '*(n-2-i)+'*'+' '*(n-2)+'*')
    
    star.append(' '*(n-1)+'*'+' '*(n-2)+'*'+' '*(n-2)+'*')

    for i in range(1,n-1):
        star.append(' '*(n-1-i)+'*'+' '*(n-2)+'*'+' '*(i-1)+' '+' '*(i-1)+'*'+' '*(n-2)+'*')

    star.append('*'*n+' '*(2*(n-2)+1)+'*'*n)

    return star

print('\n'.join(star(n)))