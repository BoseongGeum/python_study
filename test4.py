def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    fourNumbers = sorted([[(number*4)[:4], len(number)] for number in numbers])[::-1]
    for number in fourNumbers:
        answer += number[0][:number[1]]

    if answer == '0' * len(numbers):
        answer = '0'
    
    return answer

numbers = [0, 0, 0, 0, 0]
print(solution(numbers))
