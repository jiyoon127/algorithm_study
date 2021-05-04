import sys
input = sys.stdin.readline

def spreading():
    new_graph = [[0] * c for _ in range(r)]
    for row in cleaner: new_graph[row][0] = -1

    for x in range(r):
        for y in range(c):
            if graph[x][y] in (0, -1): continue

            spread = graph[x][y] // 5
            cnt = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                    cnt += 1
                    new_graph[nx][ny] += spread

            new_graph[x][y] += graph[x][y] - (spread * cnt)

    x, y = cleaner[0] - 1, 0
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        while 0 <= x + dx <= cleaner[0] and 0 <= y + dy < c and (x, y) != (cleaner[0], 1):
            nx = x + dx
            ny = y + dy
            new_graph[x][y] = new_graph[nx][ny]
            x, y = nx, ny
    new_graph[cleaner[0]][1] = 0

    x, y = cleaner[1] + 1, 0
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        while cleaner[1] <= x + dx < r and 0 <= y + dy < c and (x, y) != (cleaner[1], 1):
            nx = x + dx
            ny = y + dy
            new_graph[x][y] = new_graph[nx][ny]
            x, y = nx, ny
    new_graph[cleaner[1]][1] = 0

    return new_graph

r, c, t = map(int, input().split())
graph = []
cleaner = []

for i in range(r):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == -1: cleaner.append(i)

for _ in range(t):
    graph = spreading()

print(sum(map(sum, graph)) + 2)
