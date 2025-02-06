def solution(myString, pat):
    answer = 1 if pat.lower() in myString.lower() else 0
    return answer