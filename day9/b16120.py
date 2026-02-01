import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())
dq = deque()
pa = list("PAPP")

for ch in string:
    dq.appendleft(ch)
    # print(dq)
    if len(dq)>=4:
        passed = True
        for i in range(4):
            if pa[i]!=dq[i]:
                passed = False
        if passed:
            for _ in range(4):
                dq.popleft()
            dq.appendleft("P")
        
if len(dq)==1 and dq[0]=='P':
    print("PPAP")    
else:
    print("NP")