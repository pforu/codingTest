import sys
input = sys.stdin.readline

# acgt
# pos alt, another

S, P = map(int, input().split())
DNA = list(input().strip())
A, C, G, T = map(int, input().split())

front, rear = 0, 0
kind = 0
Ak, Ck, Gk, Tk = 0, 0, 0, 0

while rear - front < P:
    if DNA[rear]=='A':
        Ak += 1
    elif DNA[rear]=='C':
        Ck += 1
    elif DNA[rear]=='G':
        Gk += 1
    elif DNA[rear]=='T':
        Tk += 1
    rear += 1
rear -= 1

if A<=Ak and C<=Ck and G<=Gk and T<=Tk:
    kind += 1

while rear < S-1:

    if DNA[front]=='A':
        Ak -= 1
    elif DNA[front]=='C':
        Ck -= 1
    elif DNA[front]=='G':
        Gk -= 1
    elif DNA[front]=='T':
        Tk -= 1

    front += 1
    rear += 1

    if DNA[rear]=='A':
        Ak += 1
    elif DNA[rear]=='C':
        Ck += 1
    elif DNA[rear]=='G':
        Gk += 1
    elif DNA[rear]=='T':
        Tk += 1
    
    if A<=Ak and C<=Ck and G<=Gk and T<=Tk:
        kind += 1

print(kind)


# 0 8
# acgt
# 1001
# 1. ga f
# 2. at t
# 3. ta t
# rear  = 3, ret
# rear = 1 while, s-1 = 3, 1, 2ok, 3 ret

# 딕셔너리 사용, cnt[s[i-1]] -= 1과 같이 바로 사용 가능
# order = ['A', 'C', 'G', 'T']
# cnt_list = [cnt[c] for c in order]
# 이런 식으로 매핑하는 거 
# 딕셔너리라서 cnt.values() 쓰는 게 더 예쁘긴 함
# 이 코드는 좀 갈아엎기, 매핑 예쁘게 하기


