import sys
input = sys.stdin.readline

def move():
    turn = 1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while turn <= 1000:
        for i, (x, y, d) in enumerate(pieces):
            nx = x + dx[d]
            ny = y + dy[d]

            if not 0 <= nx < n or not 0 <= ny < n or graph[nx][ny] == 2:
                if d == 0: d = 1
                elif d == 1: d = 0
                elif d == 2: d = 3
                else: d = 2

                nx = x + dx[d]
                ny = y + dy[d]

            if not 0 <= nx < n or not 0 <= ny < n or graph[nx][ny] == 2: 
                pieces[i][2] = d
                continue
            else:
                index = chess_map[x][y].index(i)
                cur = chess_map[x][y][index:]
                chess_map[x][y] = chess_map[x][y][:index]

                if graph[nx][ny]: cur = cur[::-1]
                chess_map[nx][ny] += cur

                for piece in cur:
                    if i == piece: pieces[piece][2] = d
                    pieces[piece][0], pieces[piece][1] = nx, ny

                if len(chess_map[nx][ny]) > 3: return turn

        turn += 1
    return -1

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[list() for _ in range(n)] for _ in range(n)]
pieces = []
for i in range(k):
    x, y, d = map(int, input().split())
    pieces.append([x - 1, y - 1, d - 1])
    chess_map[x - 1][y - 1] = [i]

print(move())
