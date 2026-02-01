# 스택의 개념만 차용하고 실제로 안 쓸 수도
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    inp = list(input().strip())
    par_open = 0
    vps = True

    for par in inp:
        if par=='(':
            par_open += 1
        else:
            if par_open:
                par_open -= 1
            else:
                vps = False
                break
            
    if par_open==0 and vps:
        print("YES")
    else:
        print("NO")