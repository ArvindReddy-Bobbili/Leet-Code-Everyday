class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 1, min(max(candies),sum(candies) // k)
        
        while left<=right:
            mid = left + (right - left) 
            total_k = 0
            
            for i in candies:
                total_k += i // mid
            
            if total_k >= k:
                left = mid + 1

            else:
                right = mid - 1
        return right