import sys
input = sys.stdin.readline

N = int(input())
sol = list(map(int, input().split()))
sol.sort()

front, rear = 0, N-1
rstf, rstr, rst = sol[front], sol[rear], sol[front] + sol[rear]

while (front < rear):
    this = sol[front] + sol[rear]
    if abs(this) < abs(rst):
        rstf, rstr, rst = sol[front], sol[rear], this
    if this < 0:
        front += 1
    else:
        rear -= 1

print(rstf, rstr)