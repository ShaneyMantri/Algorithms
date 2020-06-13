def heapify(i,arr,n):
    lar = i
    left = 2*i+1
    right=2*i+2
    if left<n and arr[lar]<arr[left]:
        lar=left
    if right<n and arr[lar]<arr[right]:
        lar=right
    if lar!=i:
        arr[i],arr[lar]=arr[lar],arr[i]
        heapify(lar,arr,n)




def Heapsort(arr,n):
    for i in range(n//2, -1,-1):
        heapify(i,arr,n)

    for i in range(n-1, 0, -1):
        arr[0], arr[i]=arr[i],arr[0]
        print("One",arr)
        heapify(0,arr,i)
        print("Two",arr)



arr = [ 12, 11, 13, 5, 6, 7] 
n = len(arr) 
Heapsort(arr,n) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])