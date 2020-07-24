def partition(arr, low, high):
    pivot = arr[low]
    i = low+1
    j = high
    while i<=j:
        while i<=j and arr[i]<=pivot:
            i+=1
        while j>=i and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        else:
            break
    arr[j],arr[low] = arr[low],arr[j]
    return j


def quickSort(arr, low, high):
    if low<high:
        par = partition(arr, low, high)
        quickSort(arr, 0,par-1)
        quickSort(arr, par+1, high)

a = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
quickSort(a, 0, len(a)-1)
print(a)


