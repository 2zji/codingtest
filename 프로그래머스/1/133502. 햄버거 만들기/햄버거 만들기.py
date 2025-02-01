def solution(ingredient):
    stack = []
    answer = 0
    
    for item in ingredient:
        stack.append(item)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            del stack[-4:]
    
    return answer