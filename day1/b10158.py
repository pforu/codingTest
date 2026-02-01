import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dirX = 1 if (t - (w-p))//w%2 else -1
posX = (t - (w-p))%w
dirY = 1 if (t - (h-q))//h%2 else -1
posY = (t - (h-q))%h

p = posX if dirX==1 else w-posX
q = posY if dirY==1 else h-posY

    
print(f"{p} {q}")

# for _ in range(t % (2*w)) : 모듈러 사용
# x = w - abs()