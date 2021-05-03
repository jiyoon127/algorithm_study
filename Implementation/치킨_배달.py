import sys
input = sys.stdin.readline

def choose_chicken(cnt):
    global _min
    if cnt == m:
        cur_city_dist = 0
        for hx, hy in houses:
            cur_min = int(1e9)
            for cx, cy in tmp_choice:
                cur_min = min(cur_min, abs(hx - cx) + abs(hy - cy))
            cur_city_dist += cur_min

        _min = min(_min, cur_city_dist)
        return

    for i, chicken in enumerate(chickens):
        if visited[i]: continue
        visited[i] = 1
        tmp_choice.append(chicken)
        choose_chicken(cnt + 1)
        tmp_choice.pop()
        for j in range(i + 1, len(chickens)):
            visited[j] = 0

n, m = map(int, input().split())
graph = []
chickens = []
houses = []
tmp_choice = []
_min = int(1e9)

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1: houses.append((i, j))
        elif row[j] == 2: chickens.append((i, j))

visited = [0] * len(chickens)

choose_chicken(0)

print(_min)
