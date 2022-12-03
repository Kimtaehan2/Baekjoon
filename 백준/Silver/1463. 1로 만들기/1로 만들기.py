def dp(n):
    #append를 사용하지 않고 틀을 만들어 준 후 넣기만 하기
  if n==1: return 0
  else:
    arr=[0 for i in range(n)]
    arr[1]=1
    for i in range(2,n):
        
        arr[i]=arr[i-1]+1
        #min()이 두개 이상도 비교 가능
        if (i+1)%6==0: arr[i]=min(arr[i-1]+1,arr[((i+1)//3)-1]+1,arr[((i+1)//2)-1]+1)
        elif (i+1)%3==0: arr[i]=min(arr[i-1]+1,arr[((i+1)//3)-1]+1)
        elif (i+1)%2==0: arr[i]=min(arr[i-1]+1,arr[((i+1)//2)-1]+1)
        
    return arr[-1]
print(dp(int(input())))