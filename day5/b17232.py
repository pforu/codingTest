import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
K, A, B = map(int, input().split())

arr = [[0]*(M+1)] + [[0] + list(input().strip()) for _ in range(N)]

for i in range(N+1):
    for j in range(M+1):
        arr[i][j] = 1 if arr[i][j]=='*' else 0

for _ in range(T):
    acc = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            acc[i][j] = acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1] + arr[i][j]
    
    new = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            new[i][j] = arr[i][j]

    for i in range(1, N+1):
        for j in range(1, M+1):
            endI = min(N, i+K)
            endJ = min(M, j+K)
            srtI = max(1, i-K)
            srtJ = max(1, j-K)
            cir = acc[endI][endJ] + acc[srtI-1][srtJ-1] - acc[srtI-1][endJ] - acc[endI][srtJ-1] - arr[i][j]
            if arr[i][j]==0:
                if A<cir<=B:
                    new[i][j] = 1
            else:
                if cir<A or cir>B:
                    new[i][j] = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            arr[i][j] = new[i][j]

for i in range(1, N+1):
    for j in range(1, M+1):
        print('*' if arr[i][j]==1 else '.', end='')
    print()
