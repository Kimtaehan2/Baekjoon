
N=int(input())
new_str=[]


for i in range(N):
    _str=[]
    n,word=input().split()
    n=int(n)
    word=str(word)
    for i in word:
        _str.append(i*n)
    new_str.append("".join(_str))


print("\n".join(new_str))