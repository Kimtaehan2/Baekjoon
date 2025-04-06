def solution(my_str, n):
    answer = []
    while 1:
        if len(my_str) <= n:
            answer.append(my_str)
            return answer
        temp = my_str[:n]
        my_str = my_str[n:]
        answer.append(temp)
    return answer