import sys
input = sys.stdin.readline
from collections import deque

#알파벳 대문자, 소문자, 숫자, 백스페이스(-), 화살표(<>)
#중간에 입력 가능(커서와 그 오른쪽 문자는 다 오른쪽으로 한칸씩 이동)
#비밀번호의 길이는 항상 0보다 크다

# 실제로 움직이면서 삽입할 수는 없음(뭘로 접근하든 불가)
# 현재 커서의 위치에 따라 뭘 출력할지 저장해 둬야 함
# 근데 그것도 위치가 이동함, 인덱스랑 매핑이 가능한가?
# 일정한 단위로 인덱스 매핑 불가능
# 매핑이 불가능하다면 커서를 기준으로 둘로 쪼개서, 커서가 이동하는 게 아니도록 


T = int(input())
for _ in range(T):
    inp = list(input().strip())
    stackl = deque()
    stackr = deque()
    for ins in inp:
        match ins:
            case '<':
                if stackl: stackr.appendleft(stackl.pop())
            case '>':
                if stackr: stackl.append(stackr.popleft())
            case '-':
                if stackl: stackl.pop()
            case _:
                stackl.append(ins)
                
    print(''.join(stackl)+''.join(stackr))


#인덱스 매핑을 쓰는 경우
#고정된 데이터에서 특정 조건으로 찾을 때
#값의 범위를 인덱스로 변환할 때(통계)
#좌표 압축 (Coordinate Compression)
# - 값의 범위는 매우 큰데(예: 0~10억), 실제로 등장하는 숫자의 개수는 적을 때

#중복된 데이터가 반복적으로 들어올 때
# - 문자열 압축, 같은 연산이 반복되는 수식 계산 (그림 압축, 징검다리문제)
#아무튼 동적인 거 없이
#리스트(스택)에 값이 아니라 인덱스만 넣고 그때그때 조회해서 처리 

#야 파이썬에 switch case 있대
# status = 404

# match status:
#     case 200:
#         print("Success")
#     case 400 | 404:  # 여러 조건을 하나로 묶을 수도 있음 (| 기호)
#         print("Not Found / Bad Request")
#     case 500:
#         print("Server Error")
#     case _:  # 타 언어의 'default' 역할
#         print("Unknown Status")

# join이나 unpack(*)이나 상관없음 