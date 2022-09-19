arr = [6,5,3,2,8]
# arr = [5,3,2,6,8]
def bubbleSort(arr):
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            print(arr)
        print("-----------------")
    return arr

print(bubbleSort(arr))
