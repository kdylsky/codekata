"""
하샤드 수
x의 자릿수의 합으로 x를 나누었을때 나누어 떨어지면은 x는 하샤드 수이다.
나누어 떨어진다는 말은 나머지 연산을 했을 때 나머지가 0인 것을 의미한다.

양의 정수 x를 입력받으므로 먼저 문자열로 바꾸어 주고, 반복문을 돌면서 각 자리수의 합을 구한다.
그리고 x를 더한 값으로 나머지 연산시 0이라면 True 아니라면 False를 반환한다.

"""

def solution(x):
    str_x = str(x)
    a = sum(map(int, [i for i in str_x]))
    
    return True if x%a == 0 else False
    


"""
평균구하기
정수 배열 arr이 주어졌을 때 평균을 구하기

1. arr의 len()을 구한다.
2. sum()함수를 이용해서 전체 합을 구한다.
3. sum을 len으로 나눈다.
"""

def solution(arr):
    num_len = len(arr)
    num_sum= sum(arr)

    return num_sum / num_len


"""
콜라츠 추측
모든 수는 다음을 방법하면 1이 된다.
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

몇번을 반복하면 1이되는지 반환하라.(단, 1인 경우는 0을 500번 이상인 경우라면 -1을 반환하라)

몇번을 반복해야하는지 알수 없기 때문에 while문을 이용하도록 한다.
count변수를 두고서 while문 안에 분기 처리를 해준다.

"""
def solution(num):
    if num == 1:
        return 0
    count = 0
    while num != 1:
        num = num / 2 if num % 2 == 0 else num*3 +1
        
        count +=1

        if count >=500:
            return -1    
    
    return count

result = solution(1)
print(result)


