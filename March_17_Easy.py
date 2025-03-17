class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = len(nums)
        d = {}
        for i in range(a):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for k in d:
            if d[k]%2!=0 :
                return False
        return True
                