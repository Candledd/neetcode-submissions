class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #this time jump directly to where left should be
        #hashtable with index location
        hashMap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                left = max(hashMap[s[right]] + 1, left)
            hashMap[s[right]] = right
            result = max(result, right - left + 1)
        return result

        