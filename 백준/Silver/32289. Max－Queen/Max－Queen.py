import sys
input = sys.stdin.readline

n,m = map(int,input().split())

row_num = m-2
column_num = 1+(4*(n-1))

base_num = 1+(5*(n-1))

print(base_num + (row_num*column_num))