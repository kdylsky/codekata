# 풀이1
def solution(sizes):
    sizes = [sorted(i) for i in sizes]
    max_height = max([(i[0]) for i in sizes])
    max_width = max([(i[1]) for i in sizes])
    
    return max_width * max_height
# 풀이2
def solution(sizes):
    max_height = 0
    max_width = 0
    for i in [sorted(i) for i in sizes]:
        if i[0] > max_height:
            max_height = i[0]

        if i[1] > max_width:
            max_width = i[1]    
    return max_height * max_width

# 풀이3
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)    

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
result = solution(sizes)
print(result)


sizes_temp = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
a = sum(sizes_temp, [])
print(a) #[14, 4, 19, 6, 6, 16, 18, 7, 7, 11]

print(sum((["hu"],["hello"]),[]))