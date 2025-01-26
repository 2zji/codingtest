def solution(t, p):
    a = len(p)
    b = int(p)
    count = 0
    
    for i in range(len(t) - a + 1):
        substring = t[i:i+a]
        if int(substring) <= b:
            count += 1
    return count