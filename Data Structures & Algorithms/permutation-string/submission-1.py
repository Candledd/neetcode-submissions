from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        string1 = Counter(s1)
        right = len(s1)

        for left in range(len(s2)-right + 1):
            substring = s2[left:left + right]
            string2 = Counter(substring)

            if string1 == string2:
                return True
        return False

        