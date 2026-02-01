import sys
input = sys.stdin.readline

n = int(input())
sen = list(map(ord, input().strip()))
alpha = [0]*26
orda = ord('a')

maxlen = 0

sp = 0
N = len(sen)
l, r = 0, 0

while r<N:
    alpha[sen[r]-orda] += 1
    if alpha[sen[r]-orda] == 1:
        sp += 1
    
    while sp>n:
        alpha[sen[l]-orda] -= 1
        if alpha[sen[l]-orda] == 0:
            sp -= 1
        l += 1
    
    maxlen = max(maxlen, r-l+1) #실제길이
    #print(f"{l}~{r}, {r-l+1}")
    r += 1

print(maxlen)

# while l<N and r<N:
#     # 개수 올리고 rear 증가 
#     if alpha[sen[r]-orda]==0:
#         sp += 1 
#     alpha[sen[r]-orda] += 1
#     r += 1
    
#     if sp>n:
#         # rear 원복
#         r -= 1
#         alpha[sen[r]-orda] -= 1
#         # l 증가 
#         #print(l, r)
#         alpha[sen[l]-orda] -= 1
#         if alpha[sen[l]-orda] == 0:
#             sp -= 1
#             #print(f"{l}~{r}, {r-l}")
#             maxlen = max(maxlen, r-l) #sp 증가 직전 r이랑 현재 l 
#         l += 1
        