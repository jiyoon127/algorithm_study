function solution(N, number) {
    let answer = -1;
    const dp = [new Set([0]), new Set([N])]
    
    if (N === 1 || N === number) return N % number + 1
    
    for(let i = 2; i < 9; i++) {
        const _case = new Set()
        _case.add(parseInt(N.toString().repeat(i)))
        for(let j = 1; j < i / 2 + 1; j++) {
            dp[j].forEach((x) => {
                dp[i - j].forEach((y) => {
                    _case.add(x + y)
                    _case.add(Math.abs(x - y))
                    _case.add(x * y)
                    if(x !== 0) _case.add(parseInt(y / x))
                    if(y !== 0) _case.add(parseInt(x / y))
                })
            })
        }
        
        if(_case.has(number)) return i
        dp.push(_case)
    }
    
    return answer;
}
