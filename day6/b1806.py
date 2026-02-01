# 아니무슨 시간제한이 0.5초임

import sys
input = sys.stdin.readline

# prefix sum over, len low
# not -> 0

N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
acc = [0]*(N+1)
for i in range(1, N+1):
    acc[i] = acc[i-1] + arr[i]

front, rear, minlen = 1, 1, N+1
while front <= rear <= N:
    sum = acc[rear] - acc[front - 1]
    # print(sum)
    if sum < S:
        # print("*", front, rear)
        rear += 1
    else:
        leng = rear - front + 1
        minlen = min(minlen, leng)
        # print("**", front, rear)
        front += 1

print(minlen if minlen!= N+1 else 0)


# 계속 부분합을 약간 다르게 (i는 그냥 for 돌리심) 구현하는데
# 그거 한번 물어보고 체크하기