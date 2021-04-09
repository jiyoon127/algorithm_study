import sys
input = sys.stdin.readline

def disappear():
    for i in range(n):
        for j in range(n):
            if stinks[i][j][1] > 0: stinks[i][j][1] -= 1
            if graph[i][j]: stinks[i][j] = [graph[i][j], k]

def move():
    new_graph = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if graph[r][c]:
                direct = directs[graph[r][c] - 1]
                is_moved = False

                for i in range(4):
                    nd = priorities[graph[r][c] - 1][direct - 1][i]
                    nx = r + dx[nd - 1]
                    ny = c + dy[nd - 1]
                    if 0 <= nx <n and 0 <= ny < n and not stinks[nx][ny][1]:
                        directs[graph[r][c] - 1] = nd
                        if not new_graph[nx][ny]: new_graph[nx][ny] = graph[r][c]
                        else: new_graph[nx][ny] = min(new_graph[nx][ny], graph[r][c])
                        is_moved = True
                        break
                if is_moved: continue
                for i in range(4):
                    nd = priorities[graph[r][c] - 1][direct - 1][i]
                    nx = r + dx[nd - 1]
                    ny = c + dy[nd - 1]
                    if 0 <= nx <n and 0 <= ny < n and stinks[nx][ny][0] == graph[r][c]:
                        directs[graph[r][c] - 1] = nd
                        new_graph[nx][ny] = graph[r][c]
                        break
    return new_graph

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
directs = list(map(int, input().split()))
stinks = [[[0,0]] * n for _ in range(n)]
priorities = [[] for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
seconds = 0

for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

while True:
    disappear()
    graph = move()
    seconds += 1

    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1: check = False

    if check:
        print(seconds)
        break
    if seconds >= 1000:
        print(-1)
        break
