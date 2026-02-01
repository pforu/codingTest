import sys
input = sys.stdin.readline

# black <= B
# white >= W
# not -> return
# length: longer <<

N, B, W = map(int, input().split())
arr = list(input().strip())

front, rear = 0, 0
maxlen = 0

b, w = 0, 0

while rear < N:
    if arr[rear] == 'B':
        b+=1
    else:
        w+=1
    # print(front, rear, b, w)
    if b>B:
        if arr[front] == 'B':
            b-=1
        else:
            w-=1
        front+=1
    if w>=W:
        maxlen = max(maxlen, rear-front+1)
    rear+=1

print(maxlen)

# 길이가 자율적으로 조정되는 게 투포인터 특징
# 이건 너무 읽기가 불편함, 왜 구현이 계속 미묘하게 다르지
# for i는 기본적으로 존재, j의 조건에 따라 while이 돌고있음
# 대체로 조건 + j<M 두 조건으로 돌아감
# 뭐가 더 좋은지 지피띠니한테 물어보고 패들렛에도 여쭤보기 
"""
따로 문제는 없습니다. 처음 할 때 이해를 돕기 위해 front를 고정한 형태를 사용한것이고(저도 이 편이 편해서) 실제적으로 코드를 보시면 둘이 똑같이 작동하고있을거예요
혜서님이 주신 코드는 굳이 따지자면 j를 고정한 형태로 보시면 됩니당
"""




import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
arr = list(input().strip())

front, rear = 0, 0
maxlen = 0

b, w = 0, 0

while rear < N:
    if arr[rear] == 'B':
        b+=1
    else:
        w+=1
    if b>B:
        if arr[front] == 'B':
            b-=1
        else:
            w-=1
        front+=1
    if w>=W:
        maxlen = max(maxlen, rear-front+1)
    rear+=1

print(maxlen)