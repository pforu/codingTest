import sys
input = sys.stdin.readline

# 끝나는시간기준인거임..

N = int(input())
conf = []
for _ in range(N):
    srt, end = map(int, input().split())
    conf.append((srt, end))

conf.sort(key=lambda x: (x[1], x[0]))
# x[1]만 했을 때 반례
# 4 / 1 2 / 4 4 / 4 4 / 2 4

cnt = 0
last = 0
for c in conf:
    if c[0] >= last:
        last = c[1]
        cnt += 1

print(cnt)
