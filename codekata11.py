def solution(N):
    N = list(map(int, [i for i in format(N, 'b')]))
   
    a_index = [i for i in range(len(N)) if N[i] == 1]
    max = 0

    for i in range(len(a_index)-1):
        if a_index[i+1] - a_index[i] -1 > max:
            max = a_index[i+1] - a_index[i] -1
    return max

N = 32
a = solution(N)
print(a)


