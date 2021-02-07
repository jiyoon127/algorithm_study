import sys
import heapq
input = sys.stdin.readline

n = int(input())
shark = []
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 9:
            shark = [i, j, 2]
            graph[i][j] = 0

def moveShark():
    ate = 0
    seconds = 0
    visited = [[False] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, shark[0], shark[1]))

    while q:
        d, x, y = heapq.heappop(q)
        if 0 < graph[x][y] < shark[2]:
            ate += 1
            graph[x][y] = 0
            if ate == shark[2]:
                ate = 0
                shark[2] += 1
            seconds += d
            d = 0
            q = []
            visited = [[False] * n for _ in range(n)]
        for i in range(4):
            nd = d + 1
            nx = x + dx[i]
            ny = y + dy[i]
            if not 0 <= nx < n or not 0 <= ny < n: continue
            if graph[nx][ny] > shark[2] or visited[nx][ny]: continue
            visited[nx][ny] = True
            heapq.heappush(q, (nd, nx, ny))
    print(seconds)

moveShark()
