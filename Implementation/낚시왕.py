import sys
input = sys.stdin.readline

r, c, m = map(int, input().split())
sharks = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
caught = 0

for _ in range(m):
    sr, sc, s, d, z = map(int, input().split())
    sr -= 1
    sc -= 1
    d -= 1
    if d in (0, 1): s = s % ((r - 1) * 2)
    else: s = s % ((c - 1) * 2)
    if sc in sharks: sharks[sc][sr] = (s, d, z)
    else: sharks[sc] = {sr: (s, d, z)}

for fisher in range(c):
    new_sharks = {}
    target = ()
    if fisher in sharks:
        row = sorted(sharks[fisher].keys())[0]
        caught += sharks[fisher][row][2]
        target = (fisher, row)

    if fisher == c - 1: break
    for sc in sharks:
        for sr in sharks[sc]:
            if (sc, sr) == target: continue
            s, d, z = sharks[sc][sr]
            if d in (0, 1):
                nr = sr + dx[d] * s
                for _ in range(2):
                    if nr < 0:
                        nr = -nr
                        if d == 0: d = 1
                        else: d = 0
                    elif nr >= r:
                        nr = (r - 1) * 2 - nr
                        if d == 0: d = 1
                        else: d = 0
                nc = sc
            else:
                nc = sc + dy[d] * s
                for _ in range(2):
                    if nc < 0:
                        nc = -nc
                        if d == 2: d = 3
                        else: d = 2
                    elif nc >= c:
                        nc = (c - 1) * 2 - nc
                        if d == 3: d = 2
                        else: d = 3
                nr = sr

            if nc in new_sharks:
                if nr in new_sharks[nc]:
                    if new_sharks[nc][nr][2] < z: new_sharks[nc][nr] = (s, d, z)
                else: new_sharks[nc][nr] = (s, d, z)
            else: new_sharks[nc] = {nr: (s, d, z)}

    sharks = new_sharks

print(caught)
