import sys
input = sys.stdin.readline

class Number:
    def __init__(self, val, idx, coor):
        self.val, self.idx, self.coor = val, idx, coor

N = int(input())
lst = list(map(int, input().split()))

num = []
for i in range(N):
    num.append(Number(lst[i], i, -1))

num.sort(key=lambda x: x.val)

temp = None
cnt = -1
for i in range(N):
    if num[i].val!=temp:
        cnt+=1
    temp = num[i].val
    num[i].coor = cnt

num.sort(key=lambda x: x.idx)

rst = []
for n in num:
    rst.append(str(n.coor))

print(' '.join(rst))

# map 사용
# 최적화 소스코드 익혀두기
# 값이 크니까 인덱스로 줄이기 위해 


# dict = {}
# for i in range(N):
#     dict[i] = lst[i]
# dict = sorted(dict.items(), key=lambda x:x[1])
# cnt = -1
# temp = -1
# for i in range(N):
#     if dict[i][1]!=temp:
#         cnt+=1
#     temp = dict[i]
#     dict[i][1] = cnt
# for i in range(N):
#     print(dict[i], end=' ')

