def solution(s):
    word = {
            0:"zero", 
            1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine"
            }
    
    for i in word.items():
        s = s.replace(i[1], str(i[0]))
    return int(s)

def solution(s):
    answer = ""
    number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    num = ""
    for c in s:
        if c.isdigit():
            answer += c
        else:
            num += c
            if num in number.keys():
                answer += number[num]
                num = ""
    return int(answer)


s = "23four5six7"
result = solution(s)
print(result)

