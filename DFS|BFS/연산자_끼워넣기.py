# 백준 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

def solution(i, result):
    global _max, _min, add, sub, mul, div
    if i == n:
        _max = max(_max, result)
        _min = min(_min, result)
        return

    if add > 0:
        add -= 1
        solution(i + 1, result + nums[i])
        add += 1
    if sub > 0:
        sub -= 1
        solution(i + 1, result - nums[i])
        sub += 1
    if mul > 0:
        mul -= 1
        solution(i + 1, result * nums[i])
        mul += 1
    if div > 0:
        div -= 1
        solution(i + 1, int(result / nums[i]))
        div += 1

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
data = []
INF = int(1e9)
_max = -INF
_min = INF

solution(1, nums[0])

print(_max, _min, sep = "\n")
