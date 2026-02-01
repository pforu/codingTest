import sys
input = sys.stdin.readline

def deter(x, N):
    return x*x >= N

N = int(input())

l, r = 0, N
rst = 0
while l<=r:
    x = (l+r)//2
    if deter(x, N):
        rst = x
        r = x-1
    else:
        l = x+1

print(rst)