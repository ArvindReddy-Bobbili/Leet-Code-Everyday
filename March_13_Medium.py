class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def checkzeroarray(k):

            diffarray = [0]* (n+1)

            for i in range(k):
                left, right, val = queries[i]
                diffarray[left]+= val
                diffarray[right+1] -= val
            curr_sum =0
            for i in range(n):
                curr_sum += diffarray[i]
                if curr_sum < nums[i]:
                    return False
            return True

        if all(x == 0 for x in nums):
                return 0
            
    #binary search
        l,r = 1, len(queries)
        if not checkzeroarray(r):
            return -1
        
        while l<r:
            mid =l+ (r -l)//2

            if(checkzeroarray(mid)):
                r = mid
            else:
                l = mid + 1
        return l
