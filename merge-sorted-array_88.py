from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(n):
            nums1[m + i] = nums2[i]
        
        nums1.sort()

        return nums1
        

demo = Solution()

print(demo.merge([1,2,3,0,0,0],3,[2,5,6],3))


