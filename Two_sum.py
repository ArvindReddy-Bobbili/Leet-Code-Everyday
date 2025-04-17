class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i, num in enumerate(nums):
            complement = target- nums[i]
            if(complement in seen):
                return [seen[complement],i]
            else:
                seen[num]= i