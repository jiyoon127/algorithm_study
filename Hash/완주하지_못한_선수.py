# with sorting

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, complete in enumerate(completion):
        if participant[i] != complete: return participant[i]
            
    return participant[-1]
  
  
  # with hashing
  
from collections import Counter

def solution(participant, completion):
            
    return list((Counter(participant) - Counter(completion)).keys())[0]
