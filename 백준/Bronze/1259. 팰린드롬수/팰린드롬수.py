while (1):
    check=str(input())
    reversed_check=list(reversed(check))
    if check=='0': break
    if check==''.join(reversed_check):
        print('yes')
    else : print('no')
