def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(layer, total):
        global answer
        if layer == len(numbers)-1:
            if total == target:
                answer += 1
            return

        layer += 1
        print(layer)
        dfs(layer, total+numbers[layer])
        dfs(layer, total-numbers[layer])
    
    dfs(0, 0)
    
    return answer

