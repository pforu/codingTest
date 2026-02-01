import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))


def colCheck(board, row, col): # col 고정, row의 i 반복 
    candy = 'A'
    length = 0
    candies = []
    for k in range(row):
        if k==0:
            candy = board[k][col]
            length += 1
        else:
            if candy != board[k][col]:
                candies.append(length)
                candy = board[k][col]
                length = 1
            else:
                length += 1
    candies.append(length)
    return max(candies)

def rowCheck(board, row, col): # row 고정, col의 j 반복 
    candy = 'A'
    length = 0
    candies = []
    for k in range(col):
        if k==0:
            candy = board[row][k]
            length += 1
        else:
            if candy != board[row][k]:
                candies.append(length)
                candy = board[row][k]
                length = 1
            else:
                length += 1
    candies.append(length)
    return max(candies)



maxCandy = []

for i in range(n):
    for j in range(n-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        maxCandy.append(max(rowCheck(board, i, n), colCheck(board, n, j), colCheck(board, n, j+1)))
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 돌려놔야지 
            

for i in range(n-1):
    for j in range(n):
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        maxCandy.append(max(rowCheck(board, i, n), rowCheck(board, i+1, n), colCheck(board, n, j)))
        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max(maxCandy))