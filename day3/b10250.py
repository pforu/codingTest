import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n%h!=0:
        print(f"{n%h}{n//h+1:02}")
    else:
        print(f"{h}{n//h:02}")