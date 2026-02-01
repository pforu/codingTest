import sys
input = sys.stdin.readline

n = int(input())
dict = {}
words = []
for i in range(1, 51):
    dict[i] = []
for i in range(n):
    word = input().strip()
    if word not in words:
        words.append(word)
        dict[len(word)].append(word)
for i in range(1, 51):
    dict[i].sort()
for i in range(1, 51):
    for item in dict[i]:
        print(item)



word = [input().rstrip() for _ in range(n)]
word.sort(key=lambda x: (len(x), x)) #lambda 알기
print(word[0])
for i in range(1, n):
    if word[i - 1] != word[i]:
        print(word[i])

# set() : nlogn or nloglogn