import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [0] + list(map(int, input().split()))
sumlst = [0]*(n+1)
for i in range(1, n+1):
    if i==1:
        sumlst[i] = num[i] #어차피 첫번째 0이라서 if처리 필요없음 
    else:
        sumlst[i] = sumlst[i-1] + num[i]
for i in range(m):
    start, end = map(int, input().split())
    print(sumlst[end] - sumlst[start-1])