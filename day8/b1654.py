import sys
input = sys.stdin.readline

K, N = map(int, input().split())
line = []
for i in range(K):
    line.append(int(input()))
# line = [int(input()) for _ in range(K)]

l, r = 0, max(line)
rst = 0

#nlogn
while l<=r:
    x = max((l+r)//2, 1)
    maxl = 0
    for li in line:
        maxl += li//x
    if maxl>=N:
        rst = x
        l = x+1
    else:
        r = x-1
    
print(rst)