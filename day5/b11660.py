import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# arr = [[0]*n]*n 은 참조 그대로 먹힘
# arr = [[0] * (n+1)]
# for n: row = [0] + list(input()), arr.append(row)
# 웬만하면 맞춰주기 헷갈리니까

lst = [0]*n
for i in range(n):
    lst[i] = list(map(int, input().split()))

sumlst = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sumlst[i][j] = sumlst[i][j-1] + sumlst[i-1][j] - sumlst[i-1][j-1] + lst[i-1][j-1]


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumlst[x2][y2] - sumlst[x1-1][y2] - sumlst[x2][y1-1] + sumlst[x1-1][y1-1])


#모아서 출력하는 게 더 빠르긴 함 
#ans = []
#ans.append(str(num))
#sys.stdout.write('\n'.join(ans))