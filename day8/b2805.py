import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [0] + list(map(int, input().split()))
tree.sort()

trees = [0]*(N+1)
for i in range(1, N+1):
    trees[i] = trees[i-1] + tree[i]


l, r = 0, tree[N]
rst = 0
while l<=r:
    mid = (l+r)//2
    idx = bisect.bisect_left(tree, mid)
    total = trees[N] - trees[idx-1] - mid*(N-(idx-1))
    if total>=M:
        rst = mid
        l = mid+1
    else:
        r = mid-1
        
print(rst)