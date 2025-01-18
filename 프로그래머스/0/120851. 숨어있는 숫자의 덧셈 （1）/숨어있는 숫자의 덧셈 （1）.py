def solution(my_string):
    answer = sum(int(char) for char in my_string if char.isdigit())
    return answer