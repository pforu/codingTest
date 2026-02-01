import sys
input = sys.stdin.readline

n, m = map(int, input().split())

curN = [0]*n
curM = [0]*m

# castle = [input().rstrip() for _ in range(N)]
# for i in range(N):
#     if 'X' not in castle[i]:
#         row += 1
# for i in range(M):
#     if 'X' not in [castle[i][j] for i in range(N)]:
#         col += 1

for i in range(n):
    cur = input().strip()
    for j in range(m):
        if cur[j]=='X':
            curN[i] += 1 # 필요없는 거 없애기, 몇 개 있는지는 필요없음 
            curM[j] += 1 # 있는지 없는지만 중요하지

cur0 = [0]*2

for i in range(n):
    if curN[i] == 0:
        cur0[0] +=1

for i in range(m):
    if curM[i] == 0:
        cur0[1] += 1

print(max(cur0))