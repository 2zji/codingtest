def solution(arr1, arr2):
    answer = [[a+b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    return answer