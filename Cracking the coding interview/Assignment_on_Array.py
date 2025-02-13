

# Task 1: Pascal's triangle

def pascal(rows):
  tri=[]
  for i in range(rows):
    row=[1]*(i+1) # as first and last always 1
    for j in range(1,i):
      row[j]=tri[i-1][j-1]+tri[i-1][j]  #each number is summation of previous row
      
    tri.append(row)
    
  return tri
  
  
rows=5
print(pascal(rows)) 



#Task 2: Maximum Gap


import math

def max_gap(nums):
    min_num = min(nums)
    max_num = max(nums)
    
    if min_num == max_num or len(nums) < 2:
        return 0
    
    n = len(nums)
    bucket_size = math.ceil((max_num - min_num) / (n - 1))
    bucket_count = (max_num - min_num) // bucket_size + 1
    
    buckets = [[float('inf'), float('-inf')] for i in range(bucket_count)]
    
    for num in nums:
        idx = (num - min_num) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)
    
    maxx = min_num
    max_gap = 0
    
    for bucket in buckets:
        if bucket[0] == float('inf'):
            continue
        max_gap = max(max_gap, bucket[0] - maxx)
        maxx = bucket[1]
    
    return max_gap

nums = [3, 6, 9, 1]
nums2 = [10]
print(max_gap(nums))
