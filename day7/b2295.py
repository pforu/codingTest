# 같아도 된대
# 정렬부터

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

def bisect_left(val):
    l, r = 0, len(arr)
    while l<r:
        mid = (l+r)//2
        if arr[mid]<val:
            l = mid+1
        else:
            r = mid
    return l

x, y, z = 0, 0, N-1
for k in range(N-1, -1, -1):
    for z in range(k, -1, -1):
        last = arr[k] - arr[z] # x+y = last, x랑 y는 상관x
        y = bisect_left(last)
        #print(last, y)
        while x<=y<=z: #x는 y까지만 돌게
            ifx = last - y
            print(arr[x], arr[y], arr[z], arr[k])
            if ifx in arr[:y]:
                print(arr[k])
                exit(0)
            y-=1