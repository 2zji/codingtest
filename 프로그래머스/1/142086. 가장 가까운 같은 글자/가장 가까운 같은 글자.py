def solution(s):
    char_index = {}
    result = []
    for i, char in enumerate(s):
        if char not in char_index:
            result.append(-1)
        else:
            result.append(i - char_index[char])
        char_index[char] = i
    
    return result
