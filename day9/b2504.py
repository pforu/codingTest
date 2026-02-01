import sys
input = sys.stdin.readline
from collections import deque

# 논리: 분배법칙으로 영향력=배수 계산, 배수는 여는 괄호의 종류와 수 
pars = list(input().strip())
rst = 0
mul = 1
past = None #첫 번째 원소일 때 이전 원소 참조 예외처리 
stack = deque()
is_vps = True

for par in pars: #O(n)
    if par=='(':
        mul *= 2
        stack.append(par)
    elif par=='[':
        mul *= 3
        stack.append(par)
    elif par==')':
        if past=='(':
            rst += mul
        mul //= 2
        if len(stack)==0 or stack.pop()!='(':
            is_vps = False
            break
    else:
        if past=='[':
            rst += mul
        mul //= 3
        if len(stack)==0 or stack.pop()!='[':
            is_vps = False
            break
    past = par
    
print(rst) if is_vps and len(stack)==0 else print(0)


#런타임에러(indexerror)
# deque.pop()을 쓸 때는 len>0인지 확인할 것 
# deque를 끝냈다면 len==0인지 확인할 것 

#(()[[]])([])
# ++2**332+*32 : 이진트리로 풀 수 있을지? 

# 입력: (()
# 루프가 다 돌았을 때 is_vps는 무엇인가요?
# 스택에는 무엇이 남아있나요?
# 출력값은 무엇이 나오나요? (정답은 0이어야 합니다.)