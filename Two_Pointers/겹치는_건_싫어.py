import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0
cnt = {}
_max = 0
while end < n:
    if a[end] in cnt: cnt[a[end]] += 1
    else: cnt[a[end]] = 1
    if cnt[a[end]] > k:
        _max = max(_max, end - start)
        while cnt[a[end]] > k:
            cnt[a[start]] -= 1
            start += 1
    end += 1
    
_max = max(_max, end - start)

print(_max)
