from collections import Counter

#same solution but instead of creating new substring, we just add and remove to existing one
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        string1 = Counter(s1)
        windowFreq = Counter()
        k = len(s1)

        for right in range(len(s2)):
            incoming = s2[right]
            windowFreq[incoming] += 1

            if right >= k:
                leftChar = s2[right-k]
                if windowFreq[leftChar] == 1:
                    del windowFreq[leftChar]
                else:
                    windowFreq[leftChar] -= 1
            if windowFreq == string1:
                return True
        return False

        

        