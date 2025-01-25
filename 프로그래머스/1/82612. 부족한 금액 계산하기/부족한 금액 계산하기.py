def solution(price, money, count):
    a = price * count * (count + 1) // 2
    answer = max(a - money, 0)

    return answer