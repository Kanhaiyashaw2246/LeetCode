class Solution(object):
    def kthDistinct(self, arr= ["d","b","c","b","c","a"], k = 2):
        count = 0
        k = 0
        temp = []
        
        for ele in arr:
            i = 0
            while i < len(arr):
                if ele == arr[i]:
                    temp.append(i)
                    
                i+=1
            print(" ",temp)
            
           
           
s1 = Solution()
s1.kthDistinct()