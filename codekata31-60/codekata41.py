# 그리드 알고리즘
# 문제 1
# s = "02984"

# sum = 0
# for i in range(len(s)):
#     if sum == 0 or sum == 1 and s[i] == "0" or s[i] == "1":
#         sum += int(s[i])
#     else:
#         sum *= int(s[i])
    
# print(sum)


# data = "02984"
# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#     	result *= num
# print(result)

direct = {"R":(0,1),
        "L":(0,-1),
        "U":(-1,0),
        "D":(1,0)
        }

my = (1,1)

A = ["R","R","R","U","D","D"]
for i in A:
    dx = direct[i][0]
    dy = direct[i][1]
    myx = my[0]
    myy = my[1]

    print(dx, dy)
    print(myx, myy)
