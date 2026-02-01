import sys
from collections import deque
input = sys.stdin.readline

rst = []
N, K = map(int, input().split())
dq = deque(i for i in range(1, N+1))

while len(dq):
    for i in range(K-1):
        dq.append(dq.popleft())
    rst.append(dq.popleft())

print("<", ", ".join(map(str, rst)), ">", sep="")
