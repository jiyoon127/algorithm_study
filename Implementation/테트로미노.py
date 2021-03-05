# bruth force------------------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
max_val = -int(1e9)
tetrominoes = [
    [(2, 0), (1, 0), (0, 0), (0, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(2, 0), (1, 0), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(2, 0), (1, 0), (1, 1), (0, 0)],
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 1), (1, 1), (1, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)]
]

def check_range(tetromino, i, j):
    cur_val = 0
    for dx, dy in tetromino:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < n and 0 <= ny < m:
            cur_val += graph[nx][ny]
        else: return False
    return cur_val

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        for tetromino in tetrominoes:
            cur = check_range(tetromino, i, j)
            if cur: max_val = max(max_val, cur)
            else: continue

print(max_val)

# back tracking----------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
max_map = max(map(max, graph))
max_val = -int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

def dfs(x, y, dep, _sum):
    global max_val
    if dep == 4:
        max_val = max(max_val, _sum)
        return
    if max_val > _sum + max_map * (4 - dep): return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if dep == 2:
                dfs(x, y, dep + 1, _sum + graph[nx][ny])
            dfs(nx, ny, dep + 1, _sum + graph[nx][ny])
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

print(max_val)
