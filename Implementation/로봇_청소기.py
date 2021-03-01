import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

vacuum = tuple(map(int, input().split()))
cleaned = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

def cleaning(x, y, d):
    global cleaned
    if graph[x][y] == 0:
        graph[x][y] = 2
        cleaned += 1
    for _ in range(4):
        nd = (d - 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if graph[nx][ny] == 0:
            cleaning(nx, ny, nd)
            return
        d = nd
    nd = (d - 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if graph[nx][ny] == 1:
        return
    cleaning(nx, ny, d)

cleaning(vacuum[0], vacuum[1], vacuum[2])
print(cleaned)
