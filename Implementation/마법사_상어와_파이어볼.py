import sys
input = sys.stdin.readline

def move(prev):
    _next = {}
    for key in prev:
        r, c = key
        for m, s, d in prev[key]:
            nr = (r + dx[d] * s) % n
            nc = (c + dy[d] * s) % n
            if (nr, nc) in _next: _next[(nr, nc)].append((m, s, d))
            else: _next[(nr, nc)] = [(m, s, d)]

    _remove = []
    for key in _next:
        if len(_next[key]) == 1: continue
        new_m = sum(map(lambda x: x[0], _next[key])) // 5
        if not new_m:
            _remove.append(key)
            continue
        new_s = sum(map(lambda x: x[1], _next[key])) // len(_next[key])
        all_even, all_odd = True, True
        for i in _next[key]:
            if i[2] % 2 == 0: all_odd = False
            else: all_even = False
        _next[key] = []
        if all_even or all_odd:
            for d in [0, 2, 4, 6]:
                _next[key].append((new_m, new_s, d))
        else:
            for d in [1, 3, 5, 7]:
                _next[key].append((new_m, new_s, d))

    for key in _remove:
        del _next[key]
    return _next

n, m, k = map(int, input().split())
fireballs = {}
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
ans = 0

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r, c)] = [(m, s, d)]

for _ in range(k):
    fireballs = move(fireballs)

for key in fireballs:
        ans += sum(map(lambda x: x[0], fireballs[key]))

print(ans)
