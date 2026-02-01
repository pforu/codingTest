import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

stack = deque()
rst = [-1]*N

for i, val in enumerate(arr):
    while stack and arr[stack[-1]]<val:
            rst[stack.pop()] = val
    stack.append(i)

print(*rst)

# 4
# 3 5 2 7

# 5 7 7 -1

# 3(0): 0
# 5(1): 0이빠짐(1), 1
# 2(2): 2 >> 이때 1 2순서, 그리고 1을 봐야 함 
# 7(3): 나보다 작은 거 pop, 1이빠짐(3), 2가빠짐(3)
# 스택에 남은 3이빠짐(-1) -> 초기값 -1로 채워놓기 

# 0 3: st 0(3)
# 1 5: st _ / rst 5 + st 1(5)
# 2 2: st 1(5) '2(2)' / rst 5
# 3 7: st _ / rst 5 '7' 7 +..

# 작은 게 들어오면 들어오고, 큰 게 들어오면 더 큰 걸 만날 때까지
# = 그게 스택의 가장 작은 수일 때까지 쫓아냄, 오큰수는 이번 수
# 스택은 무조건 내림차순으로 유지
# 스택에는 인덱스 저장, 결과리스트에는 값 저장