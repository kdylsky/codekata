def dfs(numbers, target, sum):
    if len(numbers) == 0:
        if sum == target:
            return 1
        else:
            return 0
    else:
        total = 0
        total += dfs(numbers[1:], target, sum+numbers[0])
        total += dfs(numbers[1:], target, sum-numbers[0])
        return total   

def solution(numbers, target):
    return dfs(numbers, target, 0)