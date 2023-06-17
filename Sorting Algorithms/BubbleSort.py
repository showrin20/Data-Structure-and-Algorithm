#Not optimised  
def bubble_sort(arr):
 for i in range(0,len(arr)):
   for j in range(0,len(arr)-i-1):
     if arr[j]>arr[j+1]:
       arr[j],arr[j+1]=arr[j+1],arr[j]
 return arr
arr = [12, 11, 13, 5, 6]
bubble_sort(arr)
print("Sorted array:", arr)

#optimised  
def bubble_sort(arr):
 for i in range(0,len(arr)):
   swapped = False
   for j in range(0,len(arr)-i-1):
     if arr[j]>arr[j+1]:
       arr[j],arr[j+1]=arr[j+1],arr[j]
       swapped = True
   if (swapped == False):
            break
 return arr
arr = [12, 11, 13, 5, 6]
bubble_sort(arr)
print("Sorted array:", arr
