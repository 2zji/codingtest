from itertools import combinations

def solution(number):
    comb = combinations(number, 3)
    answer = sum(1 for c in comb if sum(c) == 0)
    return answer