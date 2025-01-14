def solution(my_string):
    vowels = "aeiou"
    return ''.join(char for char in my_string if char not in vowels)