import sys
input = sys.stdin.readline

def deter(home, N, C, x):
    before, sum, total = 1, 0, 1
    for i in range(2, N+1):
        sum = home[i] - home[before]
        if sum>=x:
            total += 1
            before = i
    return total>=C

N, C = map(int, input().split())
home = [0]
for i in range(N):
    home.append(int(input()))

home.sort()

l, r = 0, home[-1] - home[1]
rst = 0
while l<=r:
    x = (l+r)//2
    if deter(home, N, C, x):
        rst = x
        l = x+1
    else:
        r = x-1

print(rst)