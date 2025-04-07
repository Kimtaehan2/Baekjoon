def solution(arr, k):
    answer = []
    check = [0]*100001
    for i in range(len(arr)):
        if len(answer) == k:
            return answer
        if check[arr[i]] == 0:
            check[arr[i]] = 1
            answer.append(arr[i])
            
    return answer + [-1]*(k-len(answer))