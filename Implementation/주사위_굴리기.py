import sys
input = sys.stdin.readline

def roll():
    global x, y, dice_row, dice_column

    for order in orders:
        nx = x + dx[order]
        ny = y + dy[order]
        if not 0 <= nx < n or not 0 <= ny < m: continue
        if order in (1, 2): # 가로 이동
            if order == 1: dice_row = dice_row[-1:] + dice_row[:-1]
            else: dice_row = dice_row[1:] + dice_row[:1]
            dice_column[1], dice_column[-1] = dice_row[1], dice_row[-1]
        else: # 세로 이동
            if order == 3: dice_column = dice_column[1:] + dice_column[:1]
            else: dice_column = dice_column[-1:] + dice_column[:-1]
            dice_row[1], dice_row[-1] = dice_column[1], dice_column[-1]

        if graph[nx][ny]:
            dice_row[-1], dice_column[-1] = graph[nx][ny], graph[nx][ny]
            graph[nx][ny] = 0
        else:
            graph[nx][ny] = dice_row[-1]

        print(dice_row[1])
        x, y = nx, ny

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice_row = [0] * 4
dice_column = [0] * 4
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

roll()
