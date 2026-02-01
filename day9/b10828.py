import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
inst = [input().split() for _ in range(N)]
dq = deque()

for op in inst:
    if op[0]=='push':
        dq.appendleft(op[1])
    elif op[0]=='pop':
        print(dq.popleft() if dq else -1)
    elif op[0]=='size':
        print(len(dq))
    elif op[0]=='empty':
        print(0 if dq else 1)
    elif op[0]=='top':
        print(dq[0] if dq else -1)