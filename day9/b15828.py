import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque()
while True:
    info = int(input())
    if info==-1:
        break
    elif info==0:
        dq.popleft()
    else:
        if len(dq)<N:
            dq.append(info)
print(*dq) if dq else print("empty")