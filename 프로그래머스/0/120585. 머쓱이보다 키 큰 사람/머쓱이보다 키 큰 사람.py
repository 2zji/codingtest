def solution(array, height):
    answer = sum(1 for h in array if h > height)
    return answer