#  leetcode # 961

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # if there are 4 ints, there are 3 unique elements
        hashy = {}
        for n in A:
            if n in hashy:
                hashy[n] += 1
            else:
                hashy[n] = 1
            # if hashy[n] > 1:
            #     return n
        largest = 0
        kWithMost = 0
        for k in hashy.keys():
            if hashy[k] > largest:
                largest = hashy[k]
                kWithMost = k
        return kWithMost
        return 0