
n = int(input())

def semo(n):
    if n <= 3:
        return ['  *  ',' * * ','*****']

    arr = semo(n//2)
    semo_copy = []

    for i in arr:
        semo_copy.append(' '*(n//2)+i+' '*(n//2))

    for i in arr:
        semo_copy.append(i+' '+i)

    return semo_copy

print("\n".join(semo(n)))