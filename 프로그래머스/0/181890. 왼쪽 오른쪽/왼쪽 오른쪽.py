def solution(str_list):
    answer = []
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return list(str_list[:i])
        elif str_list[i] == 'r':
            return list(str_list[i+1:])
    return answer