function solution(genres, plays) {
    var answer = [];
    const map = new Map();
    const list = new Map();
    
    genres.forEach((_, i) => {
        if (!map.get(genres[i])) {
            map.set(genres[i], plays[i]);
            list.set(genres[i], [{num:plays[i], index:i}]);
        } else {
            map.set(genres[i], map.get(genres[i]) + plays[i]);
            list.set(genres[i], list.get(genres[i])
                     .concat([{num:plays[i], index:i}]));
        }
    });
    
    let arr = [...map.entries()];
    arr = arr.sort((a,b) => b[1] - a[1])
    arr.forEach((item) => {
        let top2 = list.get(item[0]).sort((a,b) => b.num - a.num).slice(0, 2);
        top2.forEach((t) => {
            answer = answer.concat(t.index);
        });
    });
    
    return answer;
}
