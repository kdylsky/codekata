survey = ["TR", "RT", "TR"]
choice = [7, 1, 3]

def check_answer(a, b, result_list):
    if a in result_list.keys() and b in result_list.keys():
        if result_list[a] >= result_list[b]:
            return a
        else:
            return b
    elif a in result_list.keys():
        return a
    
    elif b in result_list.keys():
        return b
    
    else:
        return a

def solution(survey, choices):
    choice_list ={
        1   :"매우비동의",
        2   :"비동의",
        3   :"약간 비동의",
        4   :"모르겠음",
        5   :"약간 동의",
        6   :"동의",
        7   :"완전동의"
    }

    score_choice_list = {
        "매우비동의"    : 3,
        "비동의"       : 2,
        "약간 비동의"   : 1,
        "모르겠음"     : 0,
        "약간 동의"     : 1,
        "동의"         : 2,
        "완전동의"      : 3 
    }

    result_list = {}

    for i in range(len(survey)):
        if choices[i] < 4:
            if survey[i][0] in result_list:    
                result_list[survey[i][0]] += score_choice_list[choice_list[choices[i]]]
            else:
                result_list[survey[i][0]] = score_choice_list[choice_list[choices[i]]]
        
        elif 4 < choices[i]:
            if survey[i][1] in result_list:    
                result_list[survey[i][1]] += score_choice_list[choice_list[choices[i]]]
            else:
                result_list[survey[i][1]] = score_choice_list[choice_list[choices[i]]]
    answer = ""
    
    answer += check_answer("R","T", result_list)
    answer += check_answer("C","F", result_list)
    answer += check_answer("J","M", result_list)
    answer += check_answer("A","N", result_list)

    return answer  

a = solution(survey,choice)
print(a)


