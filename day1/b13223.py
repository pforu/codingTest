import sys
input = sys.stdin.readline

t1 = list(map(int, input().split(':')))
t2 = list(map(int, input().split(':')))

# 구분하지 않을 시, 가장 작은 단위로 통합 
t1 = t1[0]*3600 + t1[1]*60 + t1[2]
t2 = t2[0]*3600 + t2[1]*60 + t2[2]

# 같은 시각일 때 00:00:00 말고 24:00:00 필요 
rstT = t2 - t1 if t2 > t1 else 24*3600 - (t1 - t2)
# t = t2 - t1
# if t<=0: t += 24*3600
rstlst = []
for _ in range(3):
    rstlst.append(f"{rstT % 60:02d}") #파이썬 포맷 알아놓기 
    rstT //= 60

print(':'.join(rstlst[::-1]))