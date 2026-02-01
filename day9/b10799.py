import sys
from collections import deque
input = sys.stdin.readline

arr = list(input().strip())
pos = deque()
rst = 0

bef = 0
for par in arr:
    if par=='(':
        pos.append('(')
        bef = '('
    else:
        pos.pop()
        if bef=='(':
            rst+=len(pos)
        else:
            rst+=1
        bef=')'

print(rst)