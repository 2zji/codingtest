def solution(sizes):
    rotated_sizes = [(max(w, h), min(w, h)) for w, h in sizes]
    max_width = max(w for w, h in rotated_sizes)
    max_height = max(h for w, h in rotated_sizes)
    return max_width * max_height
    return answer