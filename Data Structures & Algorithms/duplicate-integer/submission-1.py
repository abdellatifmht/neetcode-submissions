class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dup = []
        for n in nums:
            if n in check_dup:
                return True
            else:
                check_dup.append(n)
        return False
        