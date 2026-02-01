import sys
input = sys.stdin.readline

def exist(x, n):
    l, r = 0, n-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
        else:
            return True
    return False

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

arr.sort()

for q in query:
    print(1 if exist(q, N) else 0)