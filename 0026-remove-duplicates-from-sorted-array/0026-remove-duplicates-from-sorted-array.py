class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        b=set(nums)
        b=list(b)
        b.sort()
        for i in range(len(b)):
            nums[i]=b[i]
        return len(b)