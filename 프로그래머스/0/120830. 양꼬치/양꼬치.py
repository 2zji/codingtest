def solution(n, k):
    a = 12000 * n
    b = 2000 * (k - n // 10)
    answer = a + b
    return answer