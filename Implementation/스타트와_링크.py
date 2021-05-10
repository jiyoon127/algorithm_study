import sys
from itertools import combinations
input = sys.stdin.readline
 
def pickPlayer(cnt):
    global min_diff, start, link
    if cnt == n // 2:
        l_link = list(player - start)
        l_start = list(start)

        cur_diff = 0

        for i, j in list(combinations(l_start, 2)):
            cur_diff += abilities[i][j] + abilities[j][i]
        for i, j in list(combinations(l_link, 2)):
            cur_diff -= abilities[i][j] + abilities[j][i]

        min_diff = min(min_diff, abs(cur_diff))
        return

    for i, p in enumerate(player):
        if visited[i]: continue
        start.add(p)
        visited[i] = 1
        pickPlayer(cnt + 1)
        start.remove(p)
        for j in range(i + 1, n):
            visited[j] = 0


n = int(input())
player = set([i for i in range(n)])
start, link = set(), set()
abilities = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
min_diff = int(1e9)

pickPlayer(0)
print(min_diff)
