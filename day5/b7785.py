import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for i in range(n): #안에서 O(1)만
    name, el = input().split()
    if el=='enter':
        dict[name] = 1
    else:
        dict[name] = 0

dict = sorted(dict.items(), reverse=True)

for name, el in dict:
    if el==1:
        print(name)

# set 사용 가능, 정렬을 일단 하고 있으면 빼고 없으면 추가 