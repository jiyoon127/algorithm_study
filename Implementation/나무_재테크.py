import sys
input = sys.stdin.readline

a = [[]]
n, m, k = map(int, input().split())
graph = [[{} for _ in range(n+1)] for _ in range(n+1)]
nutrition = [[5] * (n + 1) for _ in range(n + 1)]
dead = []
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(n):
    a.append([0] + list(map(int, input().split())))

for _ in range(m):
    r, c, age = map(int, input().split())
    graph[r][c][age] = 1

def springSummerWinter():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]:
                temp = {}
                dead = 0
                for age in sorted(graph[i][j].keys()):
                    num = graph[i][j][age]
                    if nutrition[i][j] - (age * num) >= 0:
                        nutrition[i][j] -= (age * num)
                        temp[age+1] = num
                    else:
                        survived = nutrition[i][j] // age
                        if not survived:
                            dead += age // 2 * num
                            continue
                        nutrition[i][j] -= age * survived
                        dead += age // 2 * (num - survived)
                        temp[age+1] = survived
                graph[i][j] = temp
                nutrition[i][j] += dead
            nutrition[i][j] += a[i][j]

def fall():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]:
                num = 0
                for age in graph[i][j].keys():
                    if age % 5 == 0:
                        num += graph[i][j][age]
                if num:
                    for idx in range(8):
                        ni = i + di[idx]
                        nj = j + dj[idx]
                        if 0 < ni <= n and 0 < nj <= n:
                            if 1 not in graph[ni][nj].keys():
                                graph[ni][nj][1] = num
                            else: graph[ni][nj][1] += num

def count():
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            cnt += sum(graph[i][j].values())
    return cnt

for year in range(k):
    springSummerWinter()
    fall()

print(count())
