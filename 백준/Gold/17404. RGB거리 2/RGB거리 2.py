import sys
input = sys.stdin.readline

N = int(input())

color_cost = []
for _ in range(N):
    color_cost.append(list(map(int,input().split())))

INF = 1e9

result = []

def bottom_up(r,g,b,color):

    for i in range(1,N):
        # 0 : red / 1 : green / 2 : blue
        r.append(min(g[i-1],b[i-1])+color_cost[i][0])
        g.append(min(r[i-1],b[i-1])+color_cost[i][1])
        b.append(min(r[i-1],g[i-1])+color_cost[i][2])
    if color == 0:
        result.append(min(g[-1],b[-1]))
    if color == 1:
        result.append(min(r[-1],b[-1]))
    if color == 2:
        result.append(min(r[-1],g[-1]))

bottom_up([color_cost[0][0]],[INF],[INF],0)
bottom_up([INF],[color_cost[0][1]],[INF],1)
bottom_up([INF],[INF],[color_cost[0][2]],2)

print(min(result))