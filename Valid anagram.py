class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapwannabe1={}
        hashmapwannabe2={}
        if(len(t)!=len(s)):
            return False
        for ele,ele2 in zip(t,s):
            hashmapwannabe1[ele]= hashmapwannabe1.get(ele, 0)+1
            hashmapwannabe2[ele2]= hashmapwannabe2.get(ele2, 0)+1
        if(hashmapwannabe1 == hashmapwannabe2):
                return True
        else:
            return False
                
# from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count = defaultdict(int)
#         # Increment for s, decrement for t
#         for char_s, char_t in zip(s, t):
#             count[char_s] += 1
#             count[char_t] -= 1

#         # All zero counts means perfect anagram
#         return all(v == 0 for v in count.values())
