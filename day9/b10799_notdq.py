import sys
input = sys.stdin.readline

arr = list(input().strip())
rst, st, bef = 0, 0, 0

for par in arr:
    if par=='(':
        st+=1
        bef = -1
    else:
        st-=1
        if bef==-1:
            rst+=st
        else:
            rst+=1
        bef=1

print(rst)