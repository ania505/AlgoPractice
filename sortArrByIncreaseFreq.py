# leetcode # 1636

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        hashy = {}
        
        for n in nums:
            if n in hashy:
                hashy[n][1] += 1
                
            else:
                hashy[n] = [n, 1]
        
        res = []
        
        sortVals = sorted(hashy.values(), key=lambda x: (x[1], x[0]))
        print(sortVals)
        
        for val in sortVals:
            # print()
            for x in range(val[1]):
                res.append(val[0])
        return res
            
        
        