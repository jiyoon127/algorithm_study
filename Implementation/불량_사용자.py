import re
from itertools import product

def solution(user_id, banned_id):
    answer = 1
    candid = []
    banned_id = [banned.replace('*', '.') for banned in banned_id]
    
    for banned in banned_id:
        pattern = '^' + banned + '$'
        candid.append(list(x for x in user_id if re.match(pattern, x)))

    return len(set([frozenset(a) for a in product(*candid) if len(set(a)) == len(banned_id)]))
