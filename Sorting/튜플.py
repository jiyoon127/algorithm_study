# without regex

def solution(s):
    answer = []
    
    s = s[2 : -2].split("},{")
    if len(s) == 1: return [int(s[0])]
    
    s = sorted(list(partial.split(',') for partial in s), key = lambda x: len(x))
    
    for partial in s:
        if len(partial) == 1: answer.append(int(partial[0]))
        else:
            for num in partial:
                if int(num) not in answer: 
                    answer.append(int(num))
                    break
        
    return answer
  
  # with regex
  
# import re
from collections import Counter

def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: -x[1])]))
