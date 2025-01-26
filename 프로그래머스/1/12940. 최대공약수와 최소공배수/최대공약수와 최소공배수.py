def solution(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    x = gcd(n, m)
    y = (n * m) // x
    answer = [x, y]
    return answer