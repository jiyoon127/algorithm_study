# topology sort

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def topologySort(target):
    dp = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] += time[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])
            if indegree[i] == 0:
                if target == i: break
                else: q.append(i)

    print(dp[w])

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    topologySort(w)
