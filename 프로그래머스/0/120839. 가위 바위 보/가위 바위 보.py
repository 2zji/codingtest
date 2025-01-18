def solution(rsp):
    a = {'2':'0', '0':'5', '5':'2'}
    answer = ''.join(a[char] for char in rsp)
    return answer