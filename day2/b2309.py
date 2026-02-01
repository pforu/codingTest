import sys
input = sys.stdin.readline

h = [0]*9
total = 0
for i in range(9):
    h[i] = int(input())
    total += h[i]

h.sort()
total -= 100

front = 0
rear = 8

while h[rear] > total:
    rear -= 1
    
while front < rear:
    if total - h[front] > h[rear]:
        front += 1
    elif total - h[front] < h[rear]:
        rear -= 1
    else:
        for i in range(9):
            if i==front or i==rear:
                continue
            print(h[i])
        break


# 제거할 2개를 찾는 것
# 이중 반복문 속에서 2개 더했을 때 sum - 100이면 찾은 것

# from itertools import combinations
# 7중 반복문을 돌아서 모든 조합을 찾아 줌
# for c in combinations(iterable, 7):
#     if sum(c) == 100: 찾음

# 파이썬을 정말 주 언어로 쓸 거면 라이브러리 잘 알자
