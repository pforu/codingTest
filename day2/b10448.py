import sys
input = sys.stdin.readline

# 삼각수가 몇 개 있는지 확인을 한다
i = 1
sams = []
while True:
    sam = i*(i+1)//2
    if sam > 1000:
        break
    sams.append(sam)
    i += 1

# O(n^3)은 삼각수 44개 안에서 가능함

def eureka(front, rear, num):
    while front <= rear:
        front = 0
        mid = rear
        total = num - sams[rear]
        while front <= mid:
            if total - sams[front] < sams[mid]:
                mid -= 1
            elif total - sams[front] > sams[mid]:
                front += 1
            else:
                return 1
        rear -= 1
    return 0


n = int(input())
for i in range(n):
    num = int(input())

    rear = len(sams) - 1
    while sams[rear] > num:
        rear -= 1

    print(eureka(0, rear, num))

# is_eureka (체크배열)
# 3개의 삼각수의 합이 되는 모든 수를 구하고 시작
# testcase의 수에 덜 제한받음
# 전처리를 통해서 시간을 줄일 수 있음 
# 가끔 전처리 시간을 따로 주는 문제가 있음, 이때 활용 가능
