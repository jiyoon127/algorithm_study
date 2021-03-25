import sys
input = sys.stdin.readline

def curve(x, y, q, g):
    tmp = q.copy()
    for _ in range(g + 1):
        for now in q:
            x += dx[now]
            y += dy[now]
            board[x][y] = 1
        q = [(now + 1) % 4 for now in tmp]
        q.reverse()
        tmp += q

def find_square():
    square = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
                square += 1

    return square

n = int(input())
board = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1
    curve(x, y, [d], g)

print(find_square())
