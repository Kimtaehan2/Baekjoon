import sys
input = sys.stdin.readline

N = int(input())

def set_time(on_HOURGLASS):
    global time
    if on_HOURGLASS:
        if time == 1:
            time = 12
        else:
            time -= 1
    else:
        if time == 12:
            time = 1
        else:
            time += 1

on_HOURGLASS = False

time = 1


for _ in range(N):
    card, t = input().split()
    t = int(t)
    action = "NO"

    if card == "HOURGLASS":
        if time != t:
            if on_HOURGLASS:
                on_HOURGLASS = False
            else:
                on_HOURGLASS = True
    else:
        if time == t:
            action = "YES"
    
    print(time,action)
    set_time(on_HOURGLASS)