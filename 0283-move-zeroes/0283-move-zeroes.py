class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in nums:
        #     if i == 0:
        #         nums.remove(0)
        #         nums.append(0)
        pos = 0
        
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
