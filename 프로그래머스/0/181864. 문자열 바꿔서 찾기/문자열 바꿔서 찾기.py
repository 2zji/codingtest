def solution(myString, pat):
    a = ''.join('B' if char == 'A' else 'A' for char in myString)
    answer = 1 if pat in a else 0
    return answer