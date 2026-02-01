import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

arr.sort()

for q in query:
    idx = bisect.bisect_left(arr, q)
    print(1 if idx<N and arr[idx]==q else 0)