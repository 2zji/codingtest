def solution(n):
    ternary = ''
    while n > 0:
        ternary += str(n % 3)
        n //= 3
    answer = int(ternary, 3)
    return answer