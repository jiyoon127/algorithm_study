import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]

def subSum(node, start, end, left, right):
    if left > end or right < start: return 0
    elif left <= start and right >= end: return tree[node]

    mid = (start + end) // 2
    return subSum(node * 2, start, mid, left, right) + subSum(node * 2 + 1, mid + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end: return

    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)

n, m, k = map(int, input().split())
data = [0]
tree = [0] * 4 * n

for _ in range(n):
    data.append(int(input()))

init(1, 1, n)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - data[b]
        data[b] = c
        update(1, 1, n, b, diff)
    else:
        print(subSum(1, 1, n, b, c))
