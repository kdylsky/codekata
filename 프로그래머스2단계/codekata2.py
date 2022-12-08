"""
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
"""

"""
문제풀이
1.split()함수를 이용해서 빈칸을 기준으로 나누어 주기 -> list반환
2.map()함수를 이용해서 해당 문자로 구성된 리스트를 인트로 변경
3.min()과 max()를 이용한 최댓값과 최소값 출력
"""

def solution(s):
    new_str = s.split(" ")
    num_lst = list(map(int, list(new_str)))
    return f"{min(num_lst)} {max(num_lst)}"

s = "1 2 3 4"
result = solution(s)
print(result)