def solution(money):
    price_per_cup = 5500 
    max_cups = money // price_per_cup 
    change = money % price_per_cup
    return [max_cups, change]