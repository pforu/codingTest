import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))

ins = [0]*N
for i in range(M):
    x, y, lvl = map(int, input().split())
    ins[x-1] += lvl
    if y!=N:
        ins[y] -= lvl

cal = 0
rst = []
for i in range(N):
    cal += ins[i]
    rst.append(str(height[i] + cal))

print(' '.join(rst))