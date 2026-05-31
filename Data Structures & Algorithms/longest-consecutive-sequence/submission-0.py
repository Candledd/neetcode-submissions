class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        finalCount = 0

        for num in hashSet:
            count = 1
            if (num-1) in hashSet:
                continue
            while (num+1) in hashSet:
                count += 1
                num += 1
            if count > finalCount:
                finalCount = count

        return finalCount