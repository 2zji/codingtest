def solution(k, score):
    a = []
    answer = []
    
    for s in score:
        a.append(s)
        a.sort(reverse = True)
        if len(a) > k:
            a.pop()
        answer.append(a[-1])
    
    return answer