import sys
input = sys.stdin.readline

def roll(front, rear, invert):
    front = 0
    rear = len(invert) - 1
    while front <= rear:
        if invert[front] != invert[rear]:
            return 0
        front += 1
        rear -= 1
    return 1

def baseroll(i):
    for base in range(2, 65):
        num = i
        invert = []
        while num > 0:
            invert.append(num%base)
            num//=base
        if roll(0, len(invert), invert) == 1:
            return 1
    return 0


n = int(input())
for _ in range(n):
    i = int(input())
    print(baseroll(i))