def solution(n):
    for a in range(2, n):
        if n % a == 1:
            return a