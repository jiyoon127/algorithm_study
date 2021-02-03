import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_val = -int(1e9)
n, m = map(int, input().split())
graph = []
new_graph = [[0] * m for _ in range(n)]
virus = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 2:
            virus.append((i, j))

def get_safe():
    safe_area = 0
    for i in range(n):
        safe_area += new_graph[i].count(0)
    return safe_area

def infect(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
            new_graph[nx][ny] = 2
            infect(nx, ny)

def dfs(start, count):
    global max_val
    if count == 3:
        for i in range(n):
            for j in range(m):
                new_graph[i][j] = graph[i][j]
        for i, j in virus:
            infect(i, j)
        max_val = max(max_val, get_safe())
        return
    for i in range(start, n*m):
        x = i // m
        y = i % m
        if graph[x][y] == 0:
            graph[x][y] = 1
            count += 1
            dfs(i+1, count)
            graph[x][y] = 0
            count -= 1

dfs(0, 0)
print(max_val)
