import sys
from collections import deque
input = sys.stdin.readline

def check(graph):
    for row in graph:
        if row.count(0): return False
    return True

def spread(candid):
    q = deque(candid)
    _max = 0
    new_graph = [[0] * n for _ in range(n)]
    v = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]: new_graph[i][j] = graph[i][j]

    while q:
        x, y, cnt = q.popleft()
        v[x][y] = 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and new_graph[nx][ny] != 1:
                if not new_graph[nx][ny]:
                    v[nx][ny] = 1
                    new_graph[nx][ny] = 2
                    _max = cnt + 1
                q.append((nx, ny, cnt + 1))

    if check(new_graph): return _max
    else: return -1

def pickVirus():
    global _min
    if len(candid) == m:
        full_seconds = spread(candid)
        if full_seconds != -1:
            _min = min(_min, full_seconds)

    for i in range(len(virus)):
        if not visited[i]:
            visited[i] = 1
            candid.append(virus[i])
            pickVirus()
            candid.pop()
            for j in range(i + 1, len(virus)):
                visited[j] = 0

n, m = map(int, input().split())
graph = []
virus = []
candid = []
_min = int(1e9)

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 2:
            virus.append((i, j, 0))

visited = [0] * len(virus)
pickVirus()
print(_min if _min != int(1e9) else -1)
