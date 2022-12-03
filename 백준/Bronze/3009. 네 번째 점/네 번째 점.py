arr : list = [list(map(int,input().split())) for i in range(3)]
result=[]
if arr[0][0]==arr[1][0]: result.append(arr[2][0])
elif arr[1][0]==arr[2][0]: result.append(arr[0][0])
elif arr[0][0]==arr[2][0]: result.append(arr[1][0])
if arr[0][1]==arr[1][1]: result.append(arr[2][1])
elif arr[1][1]==arr[2][1]: result.append(arr[0][1])
elif arr[0][1]==arr[2][1]: result.append(arr[1][1])
print(*result)