class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left to right pointers contains substring, increment right to increase
        #if right is already seen in subset -> increment left until not seen
        left = 0
        seen = set()
        result = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            result = max(result, right - left + 1)
        return result
