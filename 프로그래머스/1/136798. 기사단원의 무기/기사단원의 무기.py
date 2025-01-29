def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count

def solution(number, limit, power):
    a = 0
    for i in range(1, number + 1):
        x = count_divisors(i)
        if x > limit:
            x = power
        a += x
    answer = a
    return answer