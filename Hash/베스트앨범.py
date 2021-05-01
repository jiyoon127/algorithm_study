from functools import reduce

def solution(genres, plays):
    answer = []
    
    by_genre = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in by_genre: by_genre[genre].append((i, play))
        else: by_genre[genre] = [(i, play)]
    
    for genre in by_genre:
        by_genre[genre].sort(key = lambda x: (-x[1], x[0]))
    
    # use reduce
    plays_per_genre = {key: reduce(lambda x, y: x + y[1], by_genre[key], 0) for key in by_genre}
    plays_per_genre = [key for key, value in sorted(plays_per_genre.items(), key = lambda x: -x[1])]
    
    # or sort by sum
    # plays_per_genre = sorted(list(by_genre.keys()), key = lambda x: sum(map(lambda y: y[1], by_genre[x])), reverse = True)
    
    for genre in plays_per_genre:
        answer += [i for i, play in by_genre[genre]][:2]
    
    return answer
