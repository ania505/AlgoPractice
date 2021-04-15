# leetcode #1002

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # charCount = {}
        
        prevHash = {}
        for charFirst in A[0]:
            if charFirst in prevHash:
                prevHash[charFirst] += 1
            else:
                prevHash[charFirst] = 1
                    
        for string in A:
            currHash = {}
            for char in string:
                if char in currHash:
                    currHash[char] += 1
                else:
                    currHash[char] = 1
            # prevHash = currHash
            for charKey in currHash.keys():
                if charKey in prevHash:
                    if currHash[charKey] < prevHash[charKey]:
                        prevHash[charKey] = currHash[charKey]
            
            for prevChar in prevHash.keys():
                if prevChar not in currHash:
                    prevHash[prevChar] = 0
                    
        res = []
        for finalKey in prevHash.keys():
            i = 0
            while i < prevHash[finalKey]:
                res.append(finalKey)
                i += 1
        return res
                
                        
                    
            
        