class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:

            if n - 1 not in num_set:

                current = n
                lenght = 1

                while current + 1 in num_set:
                    current += 1
                    lenght += 1
                longest = max(longest, lenght)
                
        return longest