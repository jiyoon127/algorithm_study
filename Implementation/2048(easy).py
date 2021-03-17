import sys
input = sys.stdin.readline

def rotate(board):
    new_board = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]: new_board[j][n - i - 1] = board[i][j]

    return new_board

def addingUp(row):
    new_row = [i for i in row if i]
    for i in range(1, len(new_row)):
        if new_row[i - 1] == new_row[i]:
            new_row[i -1] *= 2
            new_row[i] = 0
    new_row = [i for i in new_row if i]
    return new_row + [0] * (n - len(new_row))

def solution(cnt, board):
    global _max
    if cnt == 5:
        for row in board: _max = max(_max, max(row))
        return

    for _ in range(4):
        new_board = [addingUp(row) for row in board]
        solution(cnt + 1, new_board)
        board = rotate(board)

n = int(input())
_max = -int(1e9)
board = [list(map(int, input().split())) for _ in range(n)]

solution(0, board)

print(_max)
