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

def put(x, y, cnt, _sum):
    global ans
    if cnt == 4:
        ans = max(ans, _sum)
        return

    if ans > max_map * (4 - cnt) + _sum: return
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            if cnt == 2: put(x, y, cnt + 1, _sum + graph[nx][ny])
            put(nx, ny, cnt + 1, _sum + graph[nx][ny])
            visited[nx][ny] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_map = max(map(max, graph))
ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        put(i, j, 1, graph[i][j])
        visited[i][j] = 0

print(ans)
