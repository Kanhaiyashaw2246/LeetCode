class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for _ in range(k):
            minval = min(nums)
            index = nums.index(minval)
            nums[index] = nums[index] * multiplier
        return nums
            
        





demo = Solution()
print(demo.getFinalState([2,1,3,5,6],5,2))
print(demo.getFinalState([1,2],3,4))