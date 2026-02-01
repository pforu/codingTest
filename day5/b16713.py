import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
lst = [0] + list(map(int, input().split()))

xorlst = [0]*(N+1)
xorlst[1] = lst[1]
for i in range(2, N+1):
    xorlst[i] = xorlst[i-1] ^ lst[i]

qlst = [0]*Q
for i in range(Q):
    q1, q2 = map(int, input().split())
    qlst[i] = xorlst[q1-1] ^ xorlst[q2]

rst = 0
for q in qlst:
    rst = rst ^ q

print(rst)

# 4 4 2 1 0
# 1 1 = 4 ^ 4 = 0
# 1 2 = 4 ^ 4 = 0
# 1 3 = 4 ^ 4 ^ 2 = 1
# 2 4 = 4 ^ 2 ^ 1 = 0
# rst = 0 ^ 0 ^ 1 ^ 0 = 0 ^ 1 ^ 0 = 1 ^ 0 = 1

# 1 = 1?????
# 1 2 = 0
# 1 2 3 = 1
# 1 2 3 4 = 1
# 1 2 3 4 5 = 1

# 1 ^ 2 3 4 = 1 2 3 4
# ? ^ 0 = 1 >> ?==1