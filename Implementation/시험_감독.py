import sys
input = sys.stdin.readline

n = int(input())
classes = list(map(int, input().split()))
_main, _sub = map(int, input().split())
teachers = 0

for _class in classes:
    rest = _class - _main
    teachers += 1 # _main
    if rest <= 0: continue
    if rest % _sub: teachers += 1

    teachers += rest // _sub

print(teachers)
