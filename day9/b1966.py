import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
rst = []
for _ in range(T):
    N, M = map(int, input().split())
    pri = deque((val, i) for i, val in enumerate(map(int, input().split())))
    cnt=0
    while True:
        if any(pri[0][0]<item[0] for item in pri):
            pri.append(pri.popleft())
        else:
            cnt+=1
            if M==pri.popleft()[1]:
                print(cnt)
                break

# any(iterable) : iterable 중 하나라도 True면 True
# all(iterable) : iterable 중 모두가 True면 True
# 둘 다 기본 라이브러리에 포함된 함수
# any(val<item for item in list) 형태로 사용 가능 
# all(visited)
# any(0 in row for row in board)


    # q.append(q.popleft()) == q.rotate(-1)

# for i in range(len(q)):
#     if q[i][1] > rank:
# deque로 인덱스 접근x, O(n^2)

# for elem in q:
#     if elem[1] > rank:
#         is_top = False
#         break
# O(n)
# 