import sys
input = sys.stdin.readline

def roll(curcell, wheel, n):
    alphas = []
    for i in range(k):
        cell, alpha = input().split()
        cell = int(cell)
        cell %= n
        curcell = (curcell + cell) % n
        if wheel[curcell] != alpha:
            if wheel[curcell] != '?':
                print('!')
                exit()
            if alpha in alphas:
                print('!')
                exit()
            else:
                alphas.append(alpha)
        wheel[curcell] = alpha
    return curcell, wheel


n, k = map(int, input().split())
curcell = 0
wheel = ['?']*n

curcell, wheel = roll(curcell, wheel, n)

wheelrst = ['?']*n
for i in range(n):
    wheelrst[i] = wheel[curcell - i if curcell >= i else curcell - i + n]
print(''.join(wheelrst))