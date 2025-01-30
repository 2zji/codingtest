def solution(s):
    count = 0
    i = 0
    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            
            i += 1
            
            if x_count == other_count:
                break
        count += 1
    return count