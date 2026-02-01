import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 이건 야매 풀이 
# arr = arr1 + arr2
# arr.sort()
# arr = [str(i) for i in arr]

# print(' '.join(arr))

arr = []

f1, f2 = 0, 0
while f1<N and f2<M:
    if arr1[f1] < arr2[f2]:
        arr.append(str(arr1[f1]))
        f1 += 1
    else:
        arr.append(str(arr2[f2]))
        f2 += 1
while f1<N:
    arr.append(str(arr1[f1]))
    f1 += 1
while f2<M:
    arr.append(str(arr2[f2]))
    f2 += 1

print(' '.join(arr))
# str 변환해서 넣지 말고, 그냥 그대로 넣고 마지막에 *arr로 unzip이 더 예쁨
