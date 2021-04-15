# leetcode # 242

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sSort = sorted(s)
        # tSort = sorted(t)
        # return sSort == tSort
        
        if len(s) != len(t):
            return False
        
        hashyT = {}
        for charT in t:
            if charT in hashyT:
                hashyT[charT] += 1
            else:
                hashyT[charT] = 1
        
        hashyS = {}
        for charS in s:
            if charS in hashyS:
                hashyS[charS] += 1
            else:
                hashyS[charS] = 1
        
        # print(hashyT)
        # print(hashyS)
        
        for k in hashyT:
            if k not in hashyS:
                return False
            else:
                if hashyT[k] != hashyS[k]:
                    return False
        return True
                    
                
                
                