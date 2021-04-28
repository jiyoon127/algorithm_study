candid = set()

def makeNum(numbers, visited, num):
    global candid
    
    if num:
        cur_num = int(''.join(num))
        if cur_num not in [*candid, 0 , 1]: candid.add(cur_num)
            
    for i in range(len(numbers)):
        if visited[i]: continue
        visited[i] = 1
        num.append(numbers[i])
        makeNum(numbers, visited, num)
        num.pop()
        visited[i] = 0

def solution(numbers):
    global candid
    
    answer = 0
    visited = [0] * len(numbers)
    
    makeNum(numbers, visited, [])
    
    for i in range(2, int(max(candid) ** 0.5) + 1):
        candid -= set(range(i * 2, max(candid) + 1, i))
        
    return len(candid)
