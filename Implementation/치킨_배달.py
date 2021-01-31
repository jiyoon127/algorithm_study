import sys

input = sys.stdin.readline

graph = []
chickens = []
houses = []
n, m = map(int, input().split())
ans = int(1e9)

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 2: chickens.append((i, j))
        if row[j] == 1: houses.append((i, j))

visited = [False] * len(chickens)
data = []

def chick_dist(candidates):
    dist = 0
    for hx, hy in houses:
        temp = int(1e9)
        for cx, cy in candidates:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        dist += temp
    return dist

def simulate():
    global ans
    if len(data) == m:
        ans = min(ans, chick_dist(data))
        return

    for i in range(len(chickens)):
        if visited[i]: continue
        visited[i] = True
        data.append(chickens[i])
        simulate()
        data.pop()
        for j in range(i+1, len(chickens)):
            visited[j] = False

simulate()
print(ans)
