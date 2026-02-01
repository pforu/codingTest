import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
query = list(map(int, input().split()))

for q in query:
    print(1 if q in arr else 0)