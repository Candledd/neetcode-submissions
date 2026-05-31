class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        finalCount = 0

        for num in nums:
            if num not in hashSet:
                continue
                
            count = 1
            hashSet.remove(num)
            
            forward = num + 1
            while forward in hashSet:
                hashSet.remove(forward)
                count += 1
                forward += 1
                
            backward = num - 1
            while backward in hashSet:
                hashSet.remove(backward)
                count += 1
                backward -= 1
                
            if count > finalCount:
                finalCount = count

        return finalCount