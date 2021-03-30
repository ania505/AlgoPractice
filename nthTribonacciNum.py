# leetcode # 1137

class Solution:
    def tribonacci(self, n: int) -> int:
        # nth # == prev 3 #s summed
        
        hashy = {}
        
        def helper(k, hashy):
            if k == 0:
                return 0
            if k == 1:
                return 1
            if k == 2:
                return 1
            else:
                if k in hashy:
                    return hashy[k]
                ans = helper(k-3, hashy) + helper(k-2, hashy) + helper(k-1, hashy)
                hashy[k] = ans
                return ans
            
        return helper(n, hashy)