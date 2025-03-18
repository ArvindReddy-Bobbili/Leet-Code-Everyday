class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bitmask=0
        left=0
        maxlength=1
        for right in range(len(nums)):
            while(bitmask & nums[right])!=0:
                bitmask^=nums[left]
                left+=1
            
            bitmask|= nums[right]
            maxlength = max(maxlength, right-left+1)
        return maxlength


            