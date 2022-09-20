# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

# id_list= ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

'''
각 사람이 몇번 신고당했는지를 나타내는 것을 만든다.
{"muzi":1, "frodo":1, "apeach":2, "neo":3}

신고 당한 횟수가 k 보다 크면은 해당 사람을 신고한 사람의 count+1


'''
# def solution(id_list, report, k):
#     report = set(report)
    
#     result = {}
#     for i in report:
#         if i.split()[1] in result.keys():
#             result[i.split()[1]] += 1
#         else:
#             result[i.split()[1]] = 1

#     temp_list = []
#     for i in result:
#         if result[i] >= k:
#             temp_list.append(i)
    
#     result = {}
#     for i in report:
#         if i.split()[1] in temp_list:
#             if i.split()[0] in result:
#                 result[i.split()[0]] += 1
#             else:
#                 result[i.split()[0]] = 1
  
#     answer = []
#     for i in id_list:
#         if i in result.keys():
#             answer.append(result[i])
#         else:
#             answer.append(0) 

#     return answer

# a = solution(id_list,report,k)
# print(a)

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    print(answer)
    print(reports)
    
    # 신고 당한 횟수
    for r in set(report):
        reports[r.split()[1]] += 1

    print(reports)
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            print(r.split()[0])
            answer[id_list.index(r.split()[0])] += 1
    print(answer)
    return answer

solution(id_list, report, k)