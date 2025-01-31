from collections import Counter

def solution(X: str, Y: str) -> str:
    count_x = Counter(X)
    count_y = Counter(Y)
    
    common_digits = []
    
    for digit in range(9, -1, -1):
        digit_str = str(digit)
        if digit_str in count_x and digit_str in count_y:
            common_count = min(count_x[digit_str], count_y[digit_str])
            common_digits.append(digit_str * common_count)
    
    result = ''.join(common_digits)
    
    if not result:
        return "-1"
    if result[0] == "0":
        return "0"
    
    return result