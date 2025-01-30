import re

def solution(babbling):
    possible_words = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        temp = word
        for p in possible_words:
            temp = temp.replace(p, f" {p} ")
        
        split_words = temp.split()
        
        if all(w in possible_words for w in split_words):
            if not re.search(r"(aya|ye|woo|ma)\1", word):
                count += 1

    return count