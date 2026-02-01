import sys
input = sys.stdin.readline

alpha = [0]*26
s = input().strip()
# s.upper()

asc_a = ord('a')
asc_A = ord('A')
for n in s:
    asc = ord(n)
    asc = asc - asc_A if asc < asc_a else asc - asc_a
    alpha[asc] += 1

maxal = max(alpha)
# 찾았을 시 그걸로 바꾸기, 한 번 더 찾았을 시 ?로 바꾸고 break
maxidx = [i for i, n in enumerate(alpha) if n==maxal]
print('?' if len(maxidx)>1 else chr(maxidx[0] + asc_A))
# extension 중에 boj testcase 다 돌리는 게 있음 