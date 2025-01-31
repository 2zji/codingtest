def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    result = ""
    
    for char in s:
        pos = alphabet.index(char)
        new_char = alphabet[(pos + index) % len(alphabet)]
        result += new_char
    
    return result