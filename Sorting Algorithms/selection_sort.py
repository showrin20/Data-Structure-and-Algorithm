def selectionSort(arr):
  for i in range(len(arr)):
    smallest=i
    for j in range(i+1,len(arr)):
      if arr[smallest]>arr[j]:
        smallest=j
    temp=arr[smallest]
    arr[smallest]=arr[i]
    arr[i]=temp
  print(arr)

arr=[8, 2, 9, 7, 99]

selectionSort(arr)
