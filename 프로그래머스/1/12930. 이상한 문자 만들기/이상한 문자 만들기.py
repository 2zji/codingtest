def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        transformed = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                transformed += char.upper()
            else:
                transformed += char.lower()
        result.append(transformed)
    return " ".join(result)
