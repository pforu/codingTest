import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(int(input()) for _ in range(N))
acc = [0]*(N+1)
for i in range(1, N+1):
    acc[i] = acc[i-1] + arr[i]
sum = sum(arr)
# print(acc)
lens = []

rear = 1
for front in range(1, N+1):
    leng = 0
    while rear < N+1:
        if acc[rear] - acc[front-1] > sum/2:
            lens.append(leng)
            # print(leng)
            break
        leng = acc[rear] - acc[front-1]
        rear += 1
    
print(max(lens))