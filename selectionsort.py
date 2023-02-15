#sorts a sequence in ascending order using the selection sort
def selectionSort(arr):
    n= len(arr)
    for i in range(n-1):
        #assume the ith element is the smallest
        smallNdx= i
        #Determine if any other element contains a smaller value.
        for j in range(i+ 1, n):
            if arr[j]< arr[smallNdx]:
                smallNdx= j
    if smallNdx != i:
        tmp= arr[i]
        arr[i]= arr[smallNdx]
        arr[smallNdx]= tmp
arr=[]
p= int(input("Enter number of elements:"))
for i  in range(0,p):
    ele= int(input())
    arr.append(ele)
print(arr)
selectionSort(arr)
print("Sorted array is: ")
for i in range(len(arr)):
    print("%d" % arr[i], end= " ")
