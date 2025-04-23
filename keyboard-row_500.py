class Solution(object):
    def findWords(self, words):
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        row1Count , row2Count , row3Count = 0, 0, 0    
        row1index , row2index , row3index = [], [], []

        for ele in words:
            word = ele.lower()
            for wd in word:
                if wd in row1:
                    row1Count +=1
                elif wd in row2:
                    row2Count +=1
                elif wd in row3:
                    row3Count +=1
            if row1Count == len(ele):
                row1index.append(ele)
            
            if row2Count == len(ele):
                row2index.append(ele)
            
            if row3Count == len(ele):
                row3index.append(ele)
            
            row1Count , row2Count , row3Count = 0, 0, 0

        if row1index:
            return row1index
        elif row2index:
            return row2index
        elif row3index:
            return row3index
        
        
        
demo = Solution()

word1 = ["omk"]
word2 = ["Helo","Alaska","Dad","Peace"]
word3 = ["adsdf","sfd"]
print(demo.findWords(word2))
