import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = list(map(int, input().split()))
seq = {}
for num in lst:
    seq[num] = seq[num] + 1 if num in seq else 1

seq = sorted(seq.items(), key=lambda x: x[1], reverse=True)

rst = []
for num, cnt in seq:
    for _ in range(cnt):
        rst.append(str(num))

print(' '.join(rst))

# from collections import Counter
# 부분적 order 반대 : -fre[num]
# depackaging 연산자 : * 