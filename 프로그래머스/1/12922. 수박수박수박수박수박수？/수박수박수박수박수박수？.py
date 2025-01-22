def solution(n):
    answer = ("수박" * (n // 2)) + ("수" if n % 2 == 1 else "")
    return answer