import sys
input = sys.stdin.readline
from collections import deque

# 결정할 것: 언제 push/pop할지
# 4 3 6 8 7 5 2 1
# 이라면 처음에 4까지는 push, 6까지는 push, 8까지는 push
# push한 최대 수를 저장하고 그 이하라면 pop
# 거기까지 push하고 일치하는 만큼 pop해야 함
# 근데 안된다면 불가능

N = int(input())
stack = deque()
maxnum = 0
stacknum = 1
rstlst = []
for _ in range(N):
    num = int(input())
    if num > maxnum:
        while stacknum <= num:
            stack.append(stacknum)
            rstlst.append("+")
            stacknum+=1
        maxnum = num
    if num!= stack.pop():
        print("NO")
        exit()
    rstlst.append("-")

print(*rstlst, sep='\n')

    

# home, end : 줄 처음, 끝
# shift + end : 그 부분부터 줄 끝까지 선택
# ctrl + > : 단어 단위로 움직임 

# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# + 1
# + 2 1
# + 3 2 1
# + 4 3 2 1
# - 3 2 1 : 4
# - 2 1 : 4 3
# + 5 2 1
# + 6 5 2 1
# - 5 2 1 : 4 3 6
# + 7 5 2 1
# + 8 7 5 2 1
# - 7 5 2 1 : 4 3 6 8
# - 5 2 1 : 4 3 6 8 7
# - 2 1 : 4 3 6 8 7 5
# - 1 : 4 3 6 8 7 5 2
# - 4 3 6 8 7 5 2 1