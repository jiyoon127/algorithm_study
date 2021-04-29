def solution(citations):
    answer = 0
    
    mid = sum(citations) // len(citations)
    while mid > 0:
        cnt = 0
        for citation in citations:
            if citation >= mid:
                cnt += 1
        if cnt >= mid: return mid
        else: mid -= 1
    
    return mid
