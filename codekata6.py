record = ["Enter uid1234 Muzi",\
        "Enter uid4567 Prodo",\
        "Leave uid1234",\
        "Enter uid1234 Prodo",\
        "Change uid4567 Ryan"]

def solution(record):
    result = []
    user_id = {}

    for i in range(len(record)):
        temp_list = record[i].split()

        if temp_list[0] == "Enter" or temp_list[0] == "Change":
            user_id[temp_list[1]] = temp_list[2]


    for i in range(len(record)):
        temp_list = record[i].split()

        if temp_list[0] == "Enter":
            
            test = f"{user_id[temp_list[1]]}님이 들어왔습니다."    
            result.append(test)
    
        elif temp_list[0] =="Leave":
            test = f"{user_id[temp_list[1]]}님이 나갔습니다."    
            result.append(test)
        
        
    return result
a = solution(record)
print(a)





