import sys
input = sys.stdin.readline

def leftright(row, col):
    if pan[row][col] =='|':
        pan[row][col] = '+'
    elif pan[row][col] =='.':
        pan[row][col] = '-'

def updown(row, col):
    if pan[row][col] =='-':
        pan[row][col] = '+'
    elif pan[row][col] =='.':
        pan[row][col] = '|'


n = int(input())
move = input()

pan = [['.']*n for _ in range(n)]

row = 0
col = 0

for i in range(len(move)):

    if move[i] =='U' and row>0:
        updown(row, col)
        row -= 1
        if row>=0:
            updown(row, col)
        else:
            row += 1

    elif move[i] =='D' and row<n-1:
        updown(row, col)
        row += 1
        if row<=n-1:
            updown(row, col)
        else:
            row -= 1

    elif move[i] =='L' and col>0:
        leftright(row, col)
        col -= 1
        if col>=0:
            leftright(row, col)
        else:
            col += 1

    elif move[i] =='R' and col<n-1:
        leftright(row, col)
        col += 1
        if col<=n-1:
            leftright(row, col)
        else:
            col -= 1


for i in range(n):
    print(''.join(pan[i]))