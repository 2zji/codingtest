def solution(d, budget):
    d.sort()
    count = 0
    total = 0
    
    for amount in d:
        total += amount
        if total <= budget:
            count += 1
        else:
            break
    answer = count
    return answer