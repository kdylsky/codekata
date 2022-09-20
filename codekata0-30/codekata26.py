def solution(absolutes, signs):
    return sum([i if j == True else -i for i, j in zip(absolutes, signs)]) 

    
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer
    

absolutes = [4,7,12]	
signs = [True,False,True]

solution(absolutes, signs)