import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())
dq = deque()
pa, ispa = "PPAP", 0

for ch in string:
    if ch==pa[ispa]:
        ispa+=1
    else:
        dq.append(ch)
        ispa = 0
    
    if ispa==4:
        ispa = len(dq)
    dq.append("P")
        
print("PPAP")    