import sys
input = sys.stdin.readline

def spreadVirus(x, y):
    for dx, dy in [(0, 1),(0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not new_graph[nx][ny]:
            new_graph[nx][ny] = 2
            spreadVirus(nx, ny)

def getSafeArea():
    safe_area = 0
    for i in range(n):
        safe_area += new_graph[i].count(0)
    return safe_area

def putWall(start, cnt):
    global max_val

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                new_graph[i][j] = graph[i][j]
        for x, y in virus:
            spreadVirus(x, y)
        max_val = max(max_val, getSafeArea())
        return

    for i in range(start, n * m):
        x = i // m
        y = i % m
        if not graph[x][y]:
            graph[x][y] = 1
            putWall(i + 1, cnt + 1)
            graph[x][y] = 0

n, m = map(int, input().split())
graph = []
new_graph = [[0] * m for _ in range(n)]
virus = []
max_val = 0

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 2: virus.append((i, j))

putWall(0, 0)
print(max_val)
