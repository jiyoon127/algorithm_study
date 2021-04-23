def solution(N, number):
    answer = -1
    dp = []
    dp.append(set([0]))
    dp.append(set([N]))

    if N == 1 or N == number: return N % number + 1

    for i in range(2, 9):
        case = set()
        case.add(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            for x in dp[j]:
                for y in dp[i - j]:
                    case.add(x + y)
                    case.add(x - y)
                    case.add(y - x)
                    case.add(x * y)
                    if x: case.add(y // x)
                    if y: case.add(x // y)
        if number in case:
            answer = i
            break
        dp.append(case)
        
    return answer
