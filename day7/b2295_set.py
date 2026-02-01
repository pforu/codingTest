# x+y = k-z
# x+y는 미리 계산하고 exist 계산이니까 set

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

sumset = set()
for i in arr:
    for j in arr:
        sumset.add(i+j)

x, y, z = 0, 0, N-1
for k in range(N-1, -1, -1):
    for z in range(k, -1, -1):
        last = arr[k] - arr[z] # x+y = last, x랑 y는 상관x
        if last in sumset:
            print(arr[k])
            exit(0)