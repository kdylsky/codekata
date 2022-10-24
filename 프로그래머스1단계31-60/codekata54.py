"""
보물지도

"""
def solution(n, arr1, arr2):
    test = []
    temp = []
    for i,j in zip(arr1, arr2):
        test.append(format(i, "b"))
        temp.append(format(j, "b"))
    
    arr_1 = [i if len(i) == n else i.zfill(n) for i in test ]
    arr_2 = [i if len(i) == n else i.zfill(n) for i in temp ]
    
    result = []
    for i, j in zip(arr_1, arr_2):
        new_temp = ""
        for k in range(n):
            if i[k] == j[k] == "1":
                new_temp+="#"
            elif i[k] == j[k] == "0":
                new_temp+=" "
            else:
                new_temp+="#"
        result.append(new_temp)    
    return result
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
