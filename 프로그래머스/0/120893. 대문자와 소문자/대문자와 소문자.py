def solution(my_string):
    answer = ''.join([char.upper() if char.islower() else char.lower() for char in my_string])
    return answer