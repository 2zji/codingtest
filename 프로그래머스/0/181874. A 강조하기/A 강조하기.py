def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            i = 'A'
        elif i.isupper() and i != 'A':
            i = i.lower()
        answer += i
    return answer