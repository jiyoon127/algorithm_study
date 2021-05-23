# O(N^2)으로 해결한 코드-----------------------------

# def solution(prices):
#     answer = [0] * len(prices)
    
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i + 1, len(prices)):
#             cnt += 1
#             if prices[i] > prices[j]: break
                
#         answer[i] = cnt
        
#     return answer

# 프로그래머스 코드 참고

def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        if prices[i] < prices[stack[-1]]:
            for j in reversed(stack):
                if prices[i] >= prices[j]: break
                answer[j] = i-j
                stack.pop()
        stack.append(i)
        
    for i in range(0, len(stack) - 1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    return answer
