import sys
from collections import deque
input = sys.stdin.readline

def fireStorm(s_len):
    global graph

    new_graph = [[0] * n for _ in range(n)]

    for i in range(0, n, s_len):
        for j in range(0, n, s_len):
            for x in range(s_len):
                for y in range(s_len):
                    new_graph[i + y][j + s_len - x - 1] = graph[i + x][j + y]

    graph = new_graph

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

def findChunk(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    cur_chunk = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
                cur_chunk += 1
                graph[nx][ny] = 0
                q.append((nx, ny))

    return cur_chunk

n, q = map(int, input().split())
n = 2 ** n
graph = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
chunk = 0

for order in orders:
    graph = fireStorm(2 ** order)

print(sum(map(sum, graph)))

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            chunk = max(chunk, findChunk(i, j))

print(chunk)
