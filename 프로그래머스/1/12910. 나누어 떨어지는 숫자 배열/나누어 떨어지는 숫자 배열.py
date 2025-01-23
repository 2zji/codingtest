def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    return sorted(answer) if answer else [-1]