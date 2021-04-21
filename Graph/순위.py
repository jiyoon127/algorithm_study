from collections import defaultdict

def solution(n, results):
    winners, losers = defaultdict(set), defaultdict(set)
    cnt = 0

    for won, lose in results:
        winners[won].add(lose)
        losers[lose].add(won)

    for i in range(1, n + 1):
        for won in losers[i]: winners[won].update(winners[i])
        for lose in winners[i]: losers[lose].update(losers[i])

    for i in range(1, n + 1):
        if len(winners[i]) + len(losers[i]) == n - 1: cnt += 1

    return cnt
  
