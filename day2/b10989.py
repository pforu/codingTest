# import sys
# input = sys.stdin.readline

# n = int(input())
# rst = [0]*n

# for _ in range(n):
#     rst[_] = int(input())
# rst.sort()
# for _ in rst:
#     print(_)

# 숫자 천만 개
# int(4byte) * 천만 /1024 /1024 = 38MB
# 끊어서 해라? 결국은 출력해야 되는데?
# 10000 크기의 맵에 개수를 저장

# countingSort : 개수를 저장하는 배열

import sys
input = sys.stdin.readline

n = int(input())
cntlst = [0]*10000 # 1~10000을 담는 idx 0~9999

for _ in range(n):
    cntlst[int(input())-1] += 1

for i in range(10000): # 0~9999
    for j in range(cntlst[i]): # 1~10000
        print(i+1)

# 다른 조건을 확인하기
# 숫자가 특히 작은 게 있는지 확인하기 