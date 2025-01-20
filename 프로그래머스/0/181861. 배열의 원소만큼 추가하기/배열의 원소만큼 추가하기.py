def solution(arr):
    X = []
    for a in arr:
        X.extend([a] * a)
    answer = X
    return answer