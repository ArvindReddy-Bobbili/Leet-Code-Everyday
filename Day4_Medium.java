class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, right + 1, i):
                    sieve[j] = False
        prime_num = [i for i in range(left, right + 1) if sieve[i]]
        
        if len(prime_num) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(prime_num)):
            diff = prime_num[i] - prime_num[i-1]
            if diff < min_gap:
                min_gap = diff
                result = [prime_num[i-1], prime_num[i]]
        
        return result