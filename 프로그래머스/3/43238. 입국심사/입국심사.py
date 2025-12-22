def getImmigration(n, times, time):
    res = 0
    for i in times:
        res += time // i
    return res


def solution(n, times):
    answer = 0
    left = 0
    right = 1024

    while getImmigration(n, times, right) < n:
        right *= 2

    while left <= right:
        mid = (left + right) // 2
        person = getImmigration(n, times, mid)

        if person >= n:
            right = mid - 1
            if mid == 0 or getImmigration(n, times, mid - 1) < n:
                answer = mid
                break
        else:
            left = mid + 1

    return answer