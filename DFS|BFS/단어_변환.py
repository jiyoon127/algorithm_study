answer = int(1e9)

def dfs(begin, target, words, cnt):
    global answer
    
    if ''.join(begin) == target: 
        answer = min(answer, cnt)    
        return
    
    for word in words:
        diff = 0
        for b, w in zip(begin, word):
            if b != w: diff += 1
            if diff > 1: break
                
        if diff != 1: continue
            
        words.remove(word)
        dfs(word, target, words, cnt + 1)
        words.append(word)
        

def solution(begin, target, words):
    
    if target not in words: return 0
    
    begin = list(begin.rstrip())
    words = list(list(word.rstrip()) for word in words)
    print(begin)
    
    dfs(begin, target, words, 0)
    return answer
