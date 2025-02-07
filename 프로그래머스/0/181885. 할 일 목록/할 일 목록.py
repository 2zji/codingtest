def solution(todo_list, finished):
    answer = [task for task, done in zip(todo_list, finished) if not done]
    return answer