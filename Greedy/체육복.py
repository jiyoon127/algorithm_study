def solution(n, lost, reserve):
    
    _lost = set(set(lost) - set(reserve))
    _reserve = set(set(reserve) - set(lost))
    
    for l in _lost:
        if l - 1 in _reserve: _reserve -= set([l - 1])
        elif l + 1 in _reserve: _reserve -= set([l + 1])
        else: n -= 1
            
    return n
