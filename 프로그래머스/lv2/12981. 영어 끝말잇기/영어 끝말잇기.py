"""
문제풀이
1.첫번째 단어를 temp에 담는다. 첫번째 사람부터 시작하니까 x=1
2.단어는 두번째 부터 시작한다. 시작하기 전에 사람을 +1해준다.
3.단어가 temp안에 있다면 return x와 cnt
4.단어의 끝 문자와 첫문자가 다르다면 역시 return x와 cnt
5.마지막에 x가 n과 같다면 맨처음으로 돌아간다.그리고 cnt를 +1해준다.
"""
def solution(n, words):
    temp =[]
    temp.append(words[0])
    x=1
    cnt=1
    for i in words[1:]:
        x +=1
        if i in temp:
            return [x, cnt]
        elif i[0] != temp[-1][-1]:
            return [x, cnt]
        else:
            temp.append(i) 
        
        if x==n:
            x = 0
            cnt+=1
    return [0, 0]