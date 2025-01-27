def solution(numbers):
    sums = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.add(numbers[i] + numbers[j])
    return sorted(sums)
