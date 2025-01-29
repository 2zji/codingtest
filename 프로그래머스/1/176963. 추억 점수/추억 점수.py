def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    answer = [sum(score.get(p,0) for p in group) for group in photo]
    return answer