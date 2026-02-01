# import sys
# input = sys.stdin.readline

# T = int(input())
# rst = ["0"]*T
# for i in range(T):
#     string = list(input().strip())
#     front, rear = 0, len(string)-1
#     wfront, wrear = 0, 0
#     like = 0
#     while front < rear:
#         # print(f"{front} : {string[front]}, {rear} : {string[rear]}")
#         if string[front]!=string[rear]:
#             if like==0:
#                 wfront, wrear = front, rear
#                 like = 1
#                 front -= 1
#             elif like==1:
#                 front, rear = wfront, wrear
#                 like = 2
#                 rear += 1
#             else:
#                 rst[i] = "2"
#                 like = 0
#                 break
#         front += 1
#         rear -= 1
#     if like!=0:
#         rst[i] = "1"

# print('\n'.join(rst))

# 이건 진짜 개에바띠인 코드라 갈아엎어야 됨, 논리는 맞는데 이지랄사고하면
# 시간 개처오래걸리고 테스트케이스 실행하면서 조정해야 함 등신같음

# 다음의 코드 참고하기

def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
# return s[l:r] == s[r:l:-1]과 같음 

import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    s = input().strip()
    l, r = 0, len(s)-1

    # 기본적으로 0: 회문, 1: 유사 회문, 2: 둘 다 아님
    result = 0

    while l < r:
        if s[l] == s[r]: # 같으면 상관없음
            l += 1
            r -= 1
            continue

        # 다른 지점이 처음 나타났을 때
        # 1) 왼쪽 하나 제거해보기
        # 2) 오른쪽 하나 제거해보기
        if is_pal(s, l+1, r) or is_pal(s, l, r-1):
            result = 1
        else:
            result = 2
        break

    out.append(str(result))

print("\n".join(out))

# 부분들의 합으로 보기, 문제를 쪼개는 연습하기 


# 테스트케이스와 반례를 내가 만드는 연습 하기 
# 변화 추적을 위해 전체를 다 볼 필요는 없음, 바뀌는 순간의 특징 포착 
# 0>1 or 1>0일 때만 unique_cnt가 바뀌는 것, 리스트에서 x>0들을 다 셀 필요 없음 




# abcddadca 1>not
# XYXYAAYXY not>1
# abc 1>not
# ppbpppb 1>not
# aabab 1>not

# 5
# abcddadca
# XYXYAAYXY
# abc
# ppbpppb
# aabab