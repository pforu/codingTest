import sys
input = sys.stdin.readline

total = int(input())
staff = int(input())
chip = {}
for _ in range(staff):
    name, vote = input().split()
    vote = int(vote)
    if vote/total < 0.05:
        continue
    for i in range(1, 15):
        chip[vote/i] = name

chip = sorted(chip.items(), reverse=True)

rst = {}
for per in chip:
    rst[per[1]] = 0

for i in range(14):
    per = chip[i][1]
    rst[chip[i][1]] += 1

rst = sorted(rst.items())

for name, vote in rst:
    print(name, vote)