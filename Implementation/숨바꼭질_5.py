import sys
input = sys.stdin.readline

def bfs(n, k):
    q = [n]
    visited = [[False] * 500001 for _ in range(2)]
    visited[0][n] = True
    flag = 0
    seconds = 0

    while q:
        if k > 500000: break
        if visited[flag][k]: return seconds

        new_q = []
        flag = 1 - seconds % 2
        for x in q:
            for i in (x - 1, x + 1, x * 2):
                if 0 <= i <= 500000 and not visited[flag][i]:
                    visited[flag][i] = True
                    new_q.append(i)
        seconds += 1
        k += seconds
        q = new_q

    return -1

n, k = map(int, input().split())

print(bfs(n, k))
