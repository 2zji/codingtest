def solution(a, b, n):
    answer = 0
    while n >= a:
        exchanged = (n // a) * b
        n = (n % a) + exchanged
        answer += exchanged
    return answer