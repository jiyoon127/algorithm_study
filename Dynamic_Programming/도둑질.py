def solution(money):
    _len = len(money)
    dp_f = [0] * _len
    dp_l = [0] * _len
    dp_f[0], dp_f[1], dp_l[1] = money[0], money[0], money[1]

    for i in range(2, _len - 1): dp_f[i] = max(dp_f[i - 2] + money[i], dp_f[i - 1])
    for i in range(2, _len): dp_l[i] = max(dp_l[i - 2] + money[i], dp_l[i - 1])

    return max(dp_f[-2], dp_l[-1])
