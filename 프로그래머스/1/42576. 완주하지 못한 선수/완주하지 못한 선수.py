from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    for answer in participant_count:
        if participant_count[answer] != completion_count[answer]:
            return answer