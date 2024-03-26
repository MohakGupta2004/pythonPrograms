arr=[1,4,3,7,8]
def sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min = j

        arr[i],arr[min]=arr[min],arr[i]


sort(arr)
print(arr)

