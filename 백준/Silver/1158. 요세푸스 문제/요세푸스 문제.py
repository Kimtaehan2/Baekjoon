import sys

n,k=map(int,sys.stdin.readline().split())
#1부터 n까지 오름차순의 리스트
list=list(range(1,n+1))
result=[]
#num은 list에서 뽑을 인덱스 값과 같게 하였다
#num 초기화
num=0

for i in range(n):
    #num은 k번째에서 값이 하나 빠지므로 뒤의 인덱스가 전부 -1이 된다
    num+=k-1

    #num이 list의 크기보다 커지면 안되므로 list의 길이로 나누어 나머지 값을 취해 준다
    if num>=len(list): num=num%len(list)
    #join을 위해 문자열로 받아 준다
    result.append(str(list.pop(num)))

print('<'+', '.join(result)+'>')