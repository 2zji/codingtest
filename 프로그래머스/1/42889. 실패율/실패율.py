def solution(N, stages):
    fail_rates = []
    total_players = len(stages)
    for stage in range(1, N + 1):
        count = stages.count(stage)
        if total_players > 0:
            fail_rate = count / total_players
        else:
            fail_rate = 0
        fail_rates.append((fail_rate, stage))
        total_players -= count
    fail_rates.sort(key=lambda x: (-x[0], x[1]))

    return [stage for _, stage in fail_rates]