def solution(num_list):
    odd_sum = sum(num_list[::2])
    even_sum = sum(num_list[1::2])
    return max(odd_sum, even_sum)