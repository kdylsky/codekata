"""
1. n의 반에 해당하는 값으로 판단.
2. n이 짝수이면 cnt=0 , 홀수이면 cnt=1로 시작
3. v = 1 부터 시작한다.
4. v != n이 때까지 반복한다.
5. 반복문이 끝날때마다 1씩 더해준다.
6. v부터 시작하는 반복문으로 1씩 증가하면서 더할 때 더하고나서 판단 
   만약 n과 같으면 break cnt +=1 작으면 continue, 커지면 break
"""

def solution(n):
    if n==1:
        return 1
    
    new_n = n//2
    v = 1
    cnt = 0 if n%2==0 else 1
    while v != new_n:
        sum = 0
        for j in range(v,new_n+1):
            if sum < n:
                sum = sum+j
            elif sum == n:
                cnt+=1
                break
            elif sum>n:
                break
        v +=1
    return cnt + 1
