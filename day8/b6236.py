import sys
input = sys.stdin.readline

N, M = map(int, input().split())
amount = [int(input()) for _ in range(N)]

# 최소금액 K 계산, N일동안 M번 인출
# 원하는 날에 남은 금액을 집어넣고 K원 인출 가능
# but K가 최소이기 때문에 정확히 M번 인출 가능하도록 K를 잡기
# 최소~ 문제이므로 이분탐색
# M번 부족하도록 설계 

Kl = max(amount)
Kr = sum(amount)

while Kl <= Kr: #O(nlogn)
    x = (Kl + Kr)//2
    money = 0
    cnt = 0
    for i in range(N):
        if money<amount[i]: #이게 전체 M번 
            money = x
            cnt += 1
        money -= amount[i]
    if cnt>M: # 더 많이 인출: K가 부족했던 거
        Kl = x+1
    else: # 더 적게 인출: K가 너무 컸던 거 
        Kr = x-1

print(Kl)

# cnt must be M
# M<=N이기 때문에 K는 최소 amount의 max

# >> 다 해봤을 때 1씩 올릴 수는 없음
# 최대를 정하고 그 안에서 찾든가 
# 최대는 인출 1번으로 해결 가능 = amount sum




# 7 5
# 100 500인출, 400남음
# 400          0남음
# 300 500인출, 200남음 
# 100          100남음 
# 500 500인출, 0남음 
# 101 500인출, 399남음 
# 400 500인출, 100남음 

# >> 500인출이 5번
# if 499인출

# 7 5
# 100 499인출, 399남음 
# 400 499인출, 99남음 
# 300 499인출, 199남음 
# 100          99남음
# 500 499인출, 불가능(애초에)
# 101 499인출, 398남음 
# 400 499인출, 99남음

# >>499인출이 6번(애초에 불가능)