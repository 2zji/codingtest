def solution(keymap, targets):
    key_dict = {}

    for i, keys in enumerate(keymap):
        for j, key in enumerate(keys):
            if key in key_dict:
                key_dict[key] = min(key_dict[key], j + 1)
            else:
                key_dict[key] = j + 1
    
    answer = []
    
    for target in targets:
        press_count = 0
        for char in target:
            if char in key_dict:
                press_count += key_dict[char]
            else:
                press_count = -1
                break
        answer.append(press_count)
    
    return answer