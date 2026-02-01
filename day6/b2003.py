import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

j, sum, rst = 0, 0, 0
for i in range(N):
    #j는 마지막값+1
    while sum < M and j < N:
        sum += arr[j] 
        j += 1 #because this
    if sum == M:
        rst += 1
    sum -= arr[i] #sum - 첫값 

print(rst)