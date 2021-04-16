import sys
from collections import deque
input = sys.stdin.readline

def turn(sep):
    new_graph = [[0] * n for _ in range(n)]
    for i in range(0, n, sep):
        for j in range(0, n, sep):
            for r in range(sep):
                for c in range(sep):
                    new_graph[i + c][j + sep - r - 1] = graph[i + r][j + c]
    return new_graph

def melt():
    new_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not graph[i][j]: continue

            cnt = 4
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni = i + dx
                nj = j + dy
                if not 0 <= ni < n or not 0 <= nj < n or not graph[ni][nj]: cnt -= 1
                if cnt < 3: break

            if cnt >= 3: new_graph[i][j] = graph[i][j]
            else: new_graph[i][j] = graph[i][j] - 1

    return new_graph

def bfs(x, y):
    cnt = 1
    q.append((x, y))
    graph[x][y] = 0
    while q:
        r, c = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dx
            nc = c + dy
            if 0 <= nr < n and 0 <= nc < n and graph[nr][nc]:
                graph[nr][nc] = 0
                q.append((nr, nc))
                cnt += 1

    return cnt

n, q = map(int, input().split())
n = 2 ** n
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
ans = 0

for step in list(map(int, input().split())):
    if step: graph = turn(2 ** step)
    graph = melt()

print(sum(map(sum, graph)))

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            ans = max(ans, bfs(i, j))

print(ans)
