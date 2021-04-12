import sys
input = sys.stdin.readline

def disappear():
    for i in range(n):
        for j in range(n):
            if stinks[i][j][1] > 0:
                stinks[i][j][1] -= 1
            if graph[i][j] != 0:
                stinks[i][j] = [graph[i][j], k]

def move():
    new_graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                direction = directions[graph[x][y]]
                is_moved = False
                for i in range(4):
                    nd = priorities[graph[x][y]][direction][i]
                    nx = x + dx[nd]
                    ny = y + dy[nd]

                    if 0 <= nx < n and 0 <= ny < n and not stinks[nx][ny][1]:
                        directions[graph[x][y]] = nd
                        if not new_graph[nx][ny]: new_graph[nx][ny] = graph[x][y]
                        else: new_graph[nx][ny] = min(new_graph[nx][ny], graph[x][y])
                        is_moved = True
                        break

                if is_moved: continue
                for i in range(4):
                    nd = priorities[graph[x][y]][direction][i]
                    nx = x + dx[nd]
                    ny = y + dy[nd]

                    if 0 <= nx < n and 0 <= ny < n and stinks[nx][ny][0] == graph[x][y]:
                        directions[graph[x][y]] = nd
                        new_graph[nx][ny] = graph[x][y]
                        break
    return new_graph


n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
stinks = [[[0,0]] * n for _ in range(n)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
directions = [0] + list(map(int, input().split()))
priorities = [[[0]] for _ in range(m + 1)]
for i in range(m):
    for j in range(4):
        priorities[i + 1].append(list(map(int, input().split())))
seconds = 0

while True:
    disappear()
    graph = move()
    seconds += 1

    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False

    if check:
        print(seconds)
        break

    if seconds >= 1000:
        print(-1)
        break
