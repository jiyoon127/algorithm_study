# without reduce

def solution(clothes):
    answer = 1
    closet = {}
    
    for cloth, type in clothes:
        if type in closet: closet[type].append(cloth)
        else: closet[type] = [cloth]
        
    for type in closet:
        answer *= len(closet[type]) + 1
    return answer - 1
 
# with reduce

from collections import Counter
from functools import reduce

def solution(clothes):
    
    counter = Counter([type for clothe, type in clothes])
    answer = reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1
    return answer
