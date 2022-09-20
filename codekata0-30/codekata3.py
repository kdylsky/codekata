str = "hellosdf"

def reverseString(str):
    result = ""
    result += str[-1]
    str = str[0:len(str)-1]
    if len(str) == 0:
        return result
    else:    
        return result + reverseString(str)  
print(reverseString(str))

# result = ""
# result += str[0]
# print(result)