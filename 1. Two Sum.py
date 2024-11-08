#Brute-force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n)
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
return []
#Efficient-HashMap
hash_map={}
for i,num in enumerate(nums):
  complement=target-num
  if complement in hash_map:
    return[hash_map[complement],i]
  hashmap[nums]=i
return[]

        
