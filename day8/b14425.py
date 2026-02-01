import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
arr, query = [], []
for i in range(N):
    arr.append(input())
for i in range(M):
    query.append(input())

arr.sort()
rst = 0

for q in query:
    ub = bisect.bisect_right(arr, q)
    lb = bisect.bisect_left(arr, q)
    rst += ub - lb

# print(' '.join(rst))
print(rst)

# base 사용 cnt_array