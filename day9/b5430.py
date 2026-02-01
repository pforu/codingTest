import sys
from collections import deque
input = sys.stdin.readline

#루프 내에서 reverse() 쓰지 않기
#제거가 앞/뒤의 하나만 된다는 성질 이용 

T = int(input())

for _ in range(T):
    p = list(input().strip())
    n = int(input())
    if n==0:
        if 'D' in p:
            print("error")
        else:
            print("[]")
        input()
        continue

    arr = deque(map(int, input().strip()[1:-1].split(',')))
    is_rev = False
    is_error = False

    for inst in p:
        if inst=='R':
            is_rev = not is_rev
        elif inst=='D':
            if arr:
                arr.pop() if is_rev else arr.popleft()
            else:
                is_error = True
                break

    if is_error:
        print("error")
    else:
        if is_rev:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")


# 리스트 시간복잡도
#
# append()        O(1)  맨 뒤에 데이터 추가
# pop(0)          O(N)  맨 앞을 빼면 뒤의 모든 데이터가 앞으로 이동해야 함
# insert(0, val)  O(N)  맨 앞에 넣으면 뒤의 모든 데이터가 뒤로 이동해야 함
# l[n]            O(1)  인덱스를 통한 직접 접근은 매우 빠름