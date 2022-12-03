n=int(input())

def star(n):
    if n==1: return ['*']
    if n==2: return ['*****',' *** ','  *  ']
    arr=star(n-1)
    star_copy=[]

    if n%2==1:
        star_copy.append(' '*(2**(n-1))+' '*((2**(n-1))-2)+'*'+' '*(2**(n-1))+' '*((2**(n-1))-2))
        for i in range(3,(2**(n-1))+1):
            star_copy.append(' '*(2**(n-1))+' '*((2**(n-1))-i)+'*'+' '*(i-3)+' '+' '*(i-3)+'*'+' '*(2**(n-1))+' '*((2**(n-1))-i))

        k=(2**(n-1))-1
        j=0

        for i in arr:
            star_copy.append(' '*k+'*'+' '*j+i+' '*j+'*'+' '*k)
            j+=1
            k-=1
        star_copy.append("*"*((2**(n+1))-3))

    if n%2==0:
        star_copy.append("*"*((2**(n+1))-3))

        k=(2**(n-1))-2
        j=1

        for i in arr:
            star_copy.append(' '*j+'*'+' '*k+i+' '*k+'*'+' '*j)
            j+=1
            k-=1

        for i in range((2**(n-1))-2):
            star_copy.append(' '*(2**(n-1))+' '*i+'*'+' '*(((2**(n-1))-3)-i)+' '+' '*(((2**(n-1))-3)-i)+'*'+' '*(2**(n-1))+' '*i)
            
        star_copy.append(' '*(2**(n-1))+' '*((2**(n-1))-2)+'*'+' '*(2**(n-1))+' '*((2**(n-1))-2))
    return star_copy

strip_list=star(n)
result=[]
for i in strip_list:
    result.append(i.rstrip())
print('\n'.join(result))