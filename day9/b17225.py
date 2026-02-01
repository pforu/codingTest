import sys
input = sys.stdin.readline
from collections import deque


A, B, N = map(int, input().split())
time = [A, B]
queue = [deque(), deque()]
rst = [list(), list()]

for _ in range(N):
    order, color, num = input().split()
    order, num = int(order), int(num)

    who = 0 if color=='B' else 1
    start = max(order, queue[who][-1]+time[who]) if queue[who] else order
    for i in range(num):
        queue[who].append(start + time[who]*i)

# print(queue[0])
# print(queue[1])

cnt = 1
while all(q for q in queue):
    who = 0 if queue[0][0]<=queue[1][0] else 1
    rst[who].append(cnt)
    queue[who].popleft()
    cnt += 1

who = 0 if queue[0] else 1
while queue[who]:
    rst[who].append(cnt)
    queue[who].popleft()
    cnt += 1

for r in rst:
    print(len(r))
    print(*r)


# 상민-"B"-A초(우선), 지수-"R"-B초
# 손님 수, 주문 시각, 선택한 포장지, 포장받을 선물 개수 
# > 각자 어떤 선물 포장?

# input : A, B, N
# N개의 줄에 걸쳐 1번부터 N번 손님의 주문 시각 ti(1 ≤ ti ≤ 86,400),
# 선택한 포장지의 색깔 ci(ci = "B"|"R"), 주문한 선물의 개수 mi(1 ≤ mi ≤ 100)가 주어진다
# 같은 시간에 주문한 손님은 없다

# output : 상민 포장한 선물의 개수, 선물들의 번호(오름차순), .., ..

# 시간 틱이 기준?
# 1 b 3 주문이 들어오고, 포장시간이 2라면, 상민 큐에는 1 3 5가 들어가 있을 것(시간)
# 근데 이게 지수 큐랑 겹친다면 상민이 우선순위
# 포장 중에 주문이 들어온다면,
# 해당 큐에 들어간 가장 마지막의 끝 시간 or 주문시각 중 큰 거에서 더해야 함
# 즉 큐에는 시작시각 말고 종료시각이 들어가 있어야 함
# 2 3 4
# 1 B 3
# 4 R 2
# 6 B 2
# 12 R 1
# 상민: 3 5 7
# 지수: 7 10
# 상민: + max(6, 7)= 7+2= 9 11
# 지수: + max(12, 10)= 12+3= 15
# 문제는 이러면 겹칠 때 우선순위 판단을 못함
# 그럼 시작시각을 넣고 주문이 들어오는 건 그때그때 계산