import sys
input = sys.stdin.readline

def storm(_len, dx, dy, direct):
    global start, ans
    for _ in range(_len + 1):
        start = (start[0] + dx, start[1] + dy)
        if start[0] < 0 or start[1] < 0: break

        spreads = 0
        for dx, dy, r in rate[direct]:
            nx = start[0] + dx
            ny = start[1] + dy

            if not r: sand = graph[start[0]][start[1]] - spreads
            else: sand = int(graph[start[0]][start[1]] * r)

            if 0 <= nx < n and 0 <= ny < n: graph[nx][ny] += sand
            else: ans += sand
            spreads += sand

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
mid = n // 2
start = (mid, mid)
ans = 0

left = [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02),
        (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05), (0, -1, False)]
right = [(x, -y, r) for x, y, r in left]
down = [(-y, x, r) for x, y, r in left]
up = [(y, -x, r) for x, y, r in left]
rate = {'left': left, 'right': right, 'up': up, 'down': down}

for i in range(n):
    if i % 2 == 0:
        storm(i, 0, -1, 'left')
        storm(i, 1, 0, 'down')
    else:
        storm(i, 0, 1, 'right')
        storm(i, -1, 0, 'up')

print(ans)
