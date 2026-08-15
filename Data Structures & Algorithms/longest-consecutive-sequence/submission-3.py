class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in seen:
            if n - 1 not in seen:
                length = 1
                current = n
                
                while current + 1 in seen:
                    current += 1
                    length += 1
                longest = max(longest,length)
        
        return longest