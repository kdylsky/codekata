def solution(lottos, win_nums):
    win = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = []

    c = set(lottos).intersection(set(win_nums))
    min = win[len(c)]
    max = win[len(c) + lottos.count(0)]

    answer.append(max)
    answer.append(min)

    return answer


def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]


lottos = [44, 1, 3, 2, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

result = solution(lottos, win_nums)
print(result)