def solution(s):
    length = len(s)
    mid = length // 2
    return s[mid] if length % 2 == 1 else s[mid - 1:mid + 1]