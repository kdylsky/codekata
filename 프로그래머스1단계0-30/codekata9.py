
def groupAnagrams(strs):
    result = []
    word_list =[]    

    for i in range(len(strs)):
        temp_result = []
        temp_result.append(strs[i])
        if strs[i] in word_list:
            continue
        word_list.append(strs[i])

        for j in range(i+1, len(strs)):
            if sorted(strs[i]) == sorted(strs[j]):
                temp_result.append(strs[j])
                word_list.append(strs[j])
        result.append(temp_result)
    return result


strs = ['apple','ppeal','star','arts','google','googel','tars','car']


groupAnagrams(strs)

