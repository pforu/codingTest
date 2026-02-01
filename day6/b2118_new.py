# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = [0] + list(int(input()) for _ in range(N))
# acc = [0]*(N+1)
# for i in range(1, N+1):
#     acc[i] = acc[i-1] + arr[i]
# sumlen = sum(arr)
# lens = []

# for i in range(N+1):
#     max_loop = 0
#     for j in range(i+1, N):
#         length = acc[j]-acc[i]
#         length = min(length, sumlen-length)
#         print(f"{length}: {i+1}~{j+1}")
#         max_loop = length if length > max_loop else max_loop
#     lens.append(max_loop)
#     print()

# print(max(lens))

import sys
input = sys.stdin.readline

N = int(input())
arr = list(int(input()) for _ in range(N))
half = sum(arr)/2
rst = 0

l, r, length = 0, 0, 0
while l<N:
    length += arr[r%N]
    if length > half:
        length -= arr[r%N]
        r -= 1
        if rst < length:
            rst = length
        length -= arr[l]
        l += 1
    r += 1

print(rst) #원형을 존나 처리를 못하네