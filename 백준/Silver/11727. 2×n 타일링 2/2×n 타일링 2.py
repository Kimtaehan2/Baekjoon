n=int(input())


#sq[i-1],sq[i-2]의 값이 필요하므로 n이 1과 2일때의 값을 미리 추가해줌
sq=[1,3]

def dp(n):
    #n이 1과 2일때 for 문에 정의되지 않아 런타임 에러가 나므로 미리 return 해서 에러 피하기
    if n==1: return 1
    elif n==2: return 3

    #for 문으로 구하고자 하는 n 값까지 그 전에 정의해둔 값을 이용하여 구함
    #n-2번만 반복하므로 시간 복잡도를 줄일 수 있다
    for i in range(2,n):
        sq.append(sq[i-1]+sq[i-2]*2)
    return sq[-1]

print(dp(n)%10007)