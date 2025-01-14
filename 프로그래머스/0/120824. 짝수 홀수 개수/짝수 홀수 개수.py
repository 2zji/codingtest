def solution(num_list):
    even_count = sum(1 for num in num_list if num % 2 == 0)
    odd_count = sum(1 for num in num_list if num % 2 != 0)
    answer = [even_count, odd_count]
    return answer