import sys
import heapq
input = sys.stdin.readline

def move():
    seconds = 0
    ate = 0
    visited = [[0] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, shark[1], shark[2]))

    while q:
        d, x, y = heapq.heappop(q)
        if 0 < graph[x][y] < shark[0]:
            ate += 1
            graph[x][y] = 0
            if ate == shark[0]:
                shark[0] += 1
                ate = 0
            seconds += d
            d = 0
            q = []
            visited = [[0] * n for _ in range(n)]

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nd = d + 1
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= shark[0] and not visited[nx][ny]:
                visited[nx][ny] = 1
                heapq.heappush(q, (nd, nx, ny))

    return seconds

n = int(input())
graph = []
shark = tuple()

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(len(row)):
        if row[j] == 9:
            shark = [2, i, j]
            graph[i][j] = 0

print(move())
