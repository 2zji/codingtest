def solution(x):
    answer = sum(int(digit) for digit in str(x))
    return x % answer == 0