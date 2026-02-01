import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
inst = [input().split() for _ in range(N)]
dq = deque()

for op in inst:
    if op[0]=='push_front':
        dq.appendleft(op[1])
    elif op[0]=='push_back':
        dq.append(op[1])
    elif op[0]=='pop_front':
        print(dq.popleft() if dq else -1)
    elif op[0]=='pop_back':
        print(dq.pop() if dq else -1)
    elif op[0]=='size':
        print(len(dq))
    elif op[0]=='empty':
        print(0 if dq else 1)
    elif op[0]=='front':
        print(dq[0] if dq else -1)
    elif op[0]=='back':
        print(dq[-1] if dq else -1)